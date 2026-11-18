#!/usr/bin/env Rscript
# K_d from the Tecan Spark FP plate "Method_buf-2_full_series" (16 Nov 2026)
#
# Usage (from a terminal or RStudio's Terminal):
#   Rscript kd_fit_full_series.R  <result.xlsx>  [output_folder]
# or open it in RStudio, edit the SETTINGS block below, and press Source.
#
# Needs: readxl, ggplot2   (install.packages(c("readxl", "ggplot2")))
#
# What it does
#   1. reads the raw parallel / perpendicular tables from the Spark export
#   2. subtracts the blank PER CHANNEL (median of all VLP-only wells), applies G to the
#      parallel channel and computes mP for every well
#   3. flags outlier wells (total intensity > 25 % from the median of their replicates)
#   4. fits mP = free + (bound - free) * c / (Kd + c)  (1:1)  and a Hill version
#   5. bootstraps the wells for an uncertainty range, and draws the line chart

suppressPackageStartupMessages({
  library(readxl)
  library(ggplot2)
})

## ------------------------------ SETTINGS -------------------------------------
args      <- commandArgs(trailingOnly = TRUE)
xlsx_file <- if (length(args) >= 1) args[1] else "Method_buf-2_full_series_20261116_205301.xlsx"
out_dir   <- if (length(args) >= 2) args[2] else "."

G_FACTOR      <- 1.05    # G multiplies the PARALLEL channel (Spark convention). Your calibrations
                         # ranged 1.03-1.09; K_d does not depend on it, only the absolute mP does.
UG_TO_NM_VP1  <- 17.14   # 1 ug/mL VLP = 17.14 nM VP1 (VP1 = 58 kDa)
exclude_wells <- c("B7") # wells to drop by hand (B7 read ~2x brighter than its replicates)
flag_tol      <- 0.25    # automatic flag: total intensity > 25 % from the replicate median
n_boot        <- 2000    # bootstrap resamples

# Plate map: VLP concentration (ug/mL), aptamer + VLP wells, and the matching VLP-only (blank) wells.
# 2.3 is the planned concentration (the "2.1" in your description looked like a typo).
layout <- data.frame(
  conc  = c(28, 14, 7, 5.5, 4.5, 3.5, 3, 2.3, 1.7, 0.8, 0.4, 0.2),
  wells = c("A1-A3", "A4-A6", "A7-A9", "A10-A12", "B1-B3", "B4-B6",
            "B7-B9", "B10-B12", "C1-C3", "C4-C6", "C7-C9", "C10-C12"),
  blank = c("D1-D2", "D3-D4", "D5-D6", "D7-D8", "D9-D10", "D11-D12",
            "E1-E2", "E3-E4", "E5-E6", "E7-E8", "E9-E10", "E11-E12"),
  stringsAsFactors = FALSE
)
free_wells         <- "F10-F12"  # aptamer alone (5 nM), used as the free baseline (conc 0)
fluor_wells        <- "F1-F3"    # fluorescein 1 nM (instrument / G check)
fluor_buffer_wells <- "F4-F6"    # fluorescein buffer

## ------------------------------ READ THE FILE --------------------------------
raw <- as.matrix(read_excel(xlsx_file, sheet = 1, col_names = FALSE,
                            col_types = "text", .name_repair = "minimal"))

# 8 x 12 table (rows A-H, columns 1-12) that follows a given title in the export
read_table <- function(title) {
  hit <- which(raw == title, arr.ind = TRUE)
  if (nrow(hit) == 0) stop("Table '", title, "' not found in ", xlsx_file)
  start <- hit[1, "row"]
  tab <- matrix(NA_real_, 8, 12, dimnames = list(LETTERS[1:8], 1:12))
  rows_read <- 0
  for (r in (start + 1):min(start + 14, nrow(raw))) {
    filled <- which(!is.na(raw[r, ]))
    if (length(filled) && raw[r, filled[1]] %in% LETTERS[1:8]) {
      tab[raw[r, filled[1]], ] <- suppressWarnings(as.numeric(raw[r, filled[1] + 1:12]))
      rows_read <- rows_read + 1
      if (rows_read == 8) break          # stop: the next table starts right after row H
    }
  }
  tab
}
par_raw  <- read_table("Rawdata (parallel)")
perp_raw <- read_table("Rawdata (perpendicular)")

# value that follows a label in the header block, e.g. "Gain Optimal" -> 178
header_value <- function(label) {
  hit <- which(matrix(grepl(label, raw, fixed = FALSE), nrow(raw)), arr.ind = TRUE)
  if (nrow(hit) == 0) return(NA_real_)
  row <- raw[hit[1, "row"], ]
  after <- which(!is.na(row) & seq_along(row) > hit[1, "col"])
  suppressWarnings(as.numeric(row[after[1]]))
}
cat("File:", basename(xlsx_file), "\n")
cat(sprintf("Header: gain %s, Z %s um, G calibrated in file %s; G used here = %.3f\n",
            header_value("^Gain "), header_value("^Z-Position"),
            header_value("^G Factor "), G_FACTOR))

## ------------------------------ HELPERS --------------------------------------
well_names <- function(spec) {                      # "A1-A3" -> "A1","A2","A3"
  p <- trimws(strsplit(spec, "-")[[1]]); a <- p[1]; b <- if (length(p) > 1) p[2] else p[1]
  r1 <- match(substr(a, 1, 1), LETTERS); c1 <- as.integer(substring(a, 2))
  if (grepl("^[0-9]+$", b)) { r2 <- r1; c2 <- as.integer(b)
  } else { r2 <- match(substr(b, 1, 1), LETTERS); c2 <- as.integer(substring(b, 2)) }
  as.vector(outer(LETTERS[r1:r2], c1:c2, paste0))
}
val <- function(tab, w) tab[cbind(match(substr(w, 1, 1), LETTERS[1:8]), as.integer(substring(w, 2)))]
mp_fun <- function(p, s) 1000 * (G_FACTOR * p - s) / (G_FACTOR * p + s)   # mP, G on the parallel channel

## ------------------------------ BLANK + mP PER WELL --------------------------
# VLP-only wells showed no trend with concentration, so one pooled blank (median of all of them,
# per channel) is used: it is not disturbed by a single contaminated blank well.
blank_wells <- unlist(lapply(layout$blank, well_names))
blank_p <- median(val(par_raw, blank_wells)); blank_s <- median(val(perp_raw, blank_wells))
blank_total <- G_FACTOR * blank_p + 2 * blank_s
cat(sprintf("Pooled blank (%d VLP-only wells): parallel %.0f, perpendicular %.0f, total %.0f\n",
            length(blank_wells), blank_p, blank_s, blank_total))

well_table <- function(conc, spec) {
  w <- well_names(spec); p <- val(par_raw, w); s <- val(perp_raw, w)
  data.frame(conc = conc, well = w,
             gross_total = G_FACTOR * p + 2 * s,
             mP = mp_fun(p - blank_p, s - blank_s),
             net_total = G_FACTOR * (p - blank_p) + 2 * (s - blank_s),
             stringsAsFactors = FALSE)
}
wells_df <- rbind(
  do.call(rbind, Map(well_table, layout$conc, layout$wells)),
  well_table(0, free_wells)                                          # aptamer alone = conc 0
)
wells_df$flagged <- wells_df$well %in% exclude_wells
for (cc in unique(wells_df$conc)) {                                  # automatic outlier rule
  i <- which(wells_df$conc == cc & !wells_df$flagged)
  if (length(i) >= 3) {
    med <- median(wells_df$gross_total[i])
    wells_df$flagged[i[abs(wells_df$gross_total[i] - med) > flag_tol * med]] <- TRUE
  }
}
cat("Flagged / excluded wells:", paste(wells_df$well[wells_df$flagged], collapse = ", "), "\n")

use <- wells_df[!wells_df$flagged, ]
stats <- do.call(rbind, lapply(split(use, use$conc), function(g)
  data.frame(conc = g$conc[1], n = nrow(g), mP = mean(g$mP),
             sd = if (nrow(g) > 1) sd(g$mP) else NA_real_, net_total = mean(g$net_total))))
stats <- stats[order(-stats$conc), ]; rownames(stats) <- NULL
print(transform(stats, nM_VP1 = round(conc * UG_TO_NM_VP1), mP = round(mP, 1), sd = round(sd, 1),
                net_total = round(net_total)), row.names = FALSE)
free_mP <- stats$mP[stats$conc == 0]

## ------------------------------ FITS -----------------------------------------
fit_model <- function(d, hill = FALSE) {
  start <- list(f = max(min(d$mP), 1), b = min(max(d$mP) * 1.1, 700), K = median(d$conc[d$conc > 0]))
  if (hill) {
    start$n <- 1
    nls(mP ~ f + (b - f) * conc^n / (K^n + conc^n), data = d, start = start, algorithm = "port",
        lower = c(0, 0, 0.01, 0.5), upper = c(300, 800, 500, 8),
        control = nls.control(maxiter = 500, warnOnly = TRUE))
  } else {
    nls(mP ~ f + (b - f) * conc / (K + conc), data = d, start = start, algorithm = "port",
        lower = c(0, 0, 0.01), upper = c(300, 800, 500),
        control = nls.control(maxiter = 500, warnOnly = TRUE))
  }
}
summarise_fit <- function(fit, label) {
  s <- summary(fit); co <- s$coefficients; tcrit <- qt(0.975, s$df[2])
  k <- co["K", "Estimate"]; se <- co["K", "Std. Error"]
  data.frame(model = label, Kd_ug_mL = k, CI_low = max(k - tcrit * se, 0), CI_high = k + tcrit * se,
             Kd_nM_VP1 = k * UG_TO_NM_VP1, free_mP = co["f", "Estimate"], bound_mP = co["b", "Estimate"],
             hill_n = if ("n" %in% rownames(co)) co["n", "Estimate"] else NA_real_,
             residual_SD_mP = s$sigma)
}
fit1 <- fit_model(use)                  # 1:1 hyperbola
fit2 <- tryCatch(fit_model(use, TRUE), error = function(e) NULL)
res  <- summarise_fit(fit1, "1:1 hyperbola")
if (!is.null(fit2)) res <- rbind(res, summarise_fit(fit2, "Hill"))

# bootstrap: resample wells within each concentration, refit the 1:1 model
set.seed(1)
boot_K <- replicate(n_boot, {
  dd <- do.call(rbind, lapply(split(use, use$conc), function(g) g[sample(nrow(g), replace = TRUE), ]))
  f <- tryCatch(suppressWarnings(fit_model(dd)), error = function(e) NULL)
  if (is.null(f)) NA_real_ else unname(coef(f)["K"])
})
bq <- quantile(boot_K, c(0.025, 0.5, 0.975), na.rm = TRUE)

## ------------------------------ QUALITY CHECKS -------------------------------
top <- stats$conc[1]; second <- stats$conc[2]
dbl <- (stats$mP[1] - stats$mP[2]) / stats$mP[1] * 100
f_p <- val(par_raw, well_names(fluor_wells)) - mean(val(par_raw, well_names(fluor_buffer_wells)))
f_s <- val(perp_raw, well_names(fluor_wells)) - mean(val(perp_raw, well_names(fluor_buffer_wells)))
cat("\n================ RESULT ================\n")
res_print <- res; num <- sapply(res_print, is.numeric)
res_print[num] <- lapply(res_print[num], round, 2)
print(res_print, row.names = FALSE)
cat(sprintf("\nBootstrap over wells (%d resamples): K_d median %.2f ug/mL, 95%% range %.2f - %.2f ug/mL (%.0f - %.0f nM VP1)\n",
            n_boot, bq[2], bq[1], bq[3], bq[1] * UG_TO_NM_VP1, bq[3] * UG_TO_NM_VP1))
cat(sprintf("\n>>> K_d (1:1 fit) = %.2f ug/mL = %.0f nM VP1   (95%% CI %.2f - %.2f ug/mL)\n",
            res$Kd_ug_mL[1], res$Kd_nM_VP1[1], res$CI_low[1], res$CI_high[1]))
cat("\nChecks:\n")
cat(sprintf(" - plateau: going from %g to %g ug/mL changes mP by %.1f %% (want < 5 %%)\n", second, top, dbl))
cat(sprintf(" - saturation at the top concentration: %.0f %% of the fitted curve\n", 100 * top / (res$Kd_ug_mL[1] + top)))
cat(sprintf(" - signal over blank: mean net total / blank total = %.1f (low = noisy, expect larger without the lid)\n",
            mean(use$net_total[use$conc > 0]) / blank_total))
cat(sprintf(" - fluorescein reference: %s mP at G = %.3f (expect ~20); G that would give 20 mP: %.3f\n",
            paste(round(mp_fun(f_p, f_s), 1), collapse = "/"), G_FACTOR, mean(1.0408 * f_s / f_p)))
cat(sprintf(" - net total drops from %.0f (aptamer alone) to %.0f (top VLP): bound/free brightness ratio Q = %.2f;\n",
            stats$net_total[stats$conc == 0], stats$net_total[1], stats$net_total[1] / stats$net_total[stats$conc == 0]))
cat("   if Q is well below 1 the plain fit overestimates K_d (a Q-corrected fit gave ~35-55 nM VP1 in the Python analysis)\n")

## ------------------------------ LINE CHART -----------------------------------
curve <- data.frame(conc = 10^seq(log10(min(use$conc[use$conc > 0]) * 0.7), log10(top * 1.3), length.out = 300))
curve$mP <- predict(fit1, newdata = curve)
kd <- res$Kd_ug_mL[1]
p <- ggplot() +
  geom_hline(yintercept = free_mP, linetype = "dotted", colour = "grey30") +
  annotate("text", x = max(curve$conc), y = free_mP, label = "aptamer alone (no VLP)", vjust = -0.6, hjust = 1, size = 3, colour = "grey30") +
  geom_vline(xintercept = kd, linetype = "dashed", colour = "#B22222", linewidth = 0.4) +
  geom_point(data = subset(wells_df, !flagged & conc > 0), aes(conc, mP), colour = "grey55", size = 1.8, alpha = 0.7) +
  geom_point(data = subset(wells_df, flagged & conc > 0), aes(conc, mP), colour = "#B22222", shape = 4, size = 2.5) +
  geom_errorbar(data = subset(stats, conc > 0 & !is.na(sd)), aes(conc, ymin = mP - sd, ymax = mP + sd),
                width = 0.06, colour = "#1F4E79") +
  geom_line(data = subset(stats, conc > 0), aes(conc, mP), colour = "#1F4E79", linewidth = 0.9) +
  geom_point(data = subset(stats, conc > 0), aes(conc, mP), colour = "#1F4E79", size = 2.6) +
  geom_line(data = curve, aes(conc, mP), colour = "#B22222", linetype = "longdash", linewidth = 0.8) +
  annotate("label", x = kd, y = max(stats$mP) * 0.35,
           label = sprintf("K[d] == %.1f~mu*g/mL~(%.0f~nM~VP1)", kd, res$Kd_nM_VP1[1]), parse = TRUE,
           size = 3.6, fill = "white", label.size = 0, hjust = -0.05) +
  scale_x_log10(breaks = c(0.2, 0.5, 1, 2, 5, 10, 20),
                sec.axis = sec_axis(~ . * UG_TO_NM_VP1, name = "VLP (nM VP1)", breaks = c(5, 10, 20, 50, 100, 200, 500))) +
  labs(x = expression(paste("VLP (", mu, "g/mL)")), y = sprintf("Polarization (mP), G = %.2f", G_FACTOR),
       title = "Buf-2 aptamer (5 nM) binding norovirus VLPs",
       subtitle = "grey = single wells, blue line = mean +/- SD, red dashed = 1:1 fit, x = flagged well") +
  theme_bw(base_size = 12) + theme(panel.grid.minor = element_blank())

dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)
ggsave(file.path(out_dir, "kd_fit_buf2_full_series.png"), p, width = 8, height = 5, dpi = 300)
ggsave(file.path(out_dir, "kd_fit_buf2_full_series.pdf"), p, width = 8, height = 5)
write.csv(wells_df, file.path(out_dir, "kd_wells_mP.csv"), row.names = FALSE)
write.csv(res, file.path(out_dir, "kd_fit_results.csv"), row.names = FALSE)
if (interactive()) print(p)   # show in RStudio; under Rscript this would create a stray Rplots.pdf
cat("\nSaved in", normalizePath(out_dir), ": kd_fit_buf2_full_series.png / .pdf, kd_wells_mP.csv, kd_fit_results.csv\n")
