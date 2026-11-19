# Overlay of two plates read with the same layout (outputs of kd_fit_full_series.R).
# Usage: OUT16=<folder of plate 1 results> OUT19=<folder of plate 2 results> Rscript plot_two_plates.R
# Writes kd_two_plates_overlay.png into the OUT19 folder.
suppressPackageStartupMessages({library(ggplot2)})
a <- read.csv(file.path(Sys.getenv("OUT16"), "kd_wells_mP.csv")); a$plate <- "16 Nov"
b <- read.csv(file.path(Sys.getenv("OUT19"), "kd_wells_mP.csv")); b$plate <- "19 Nov"
d <- rbind(a, b); d <- d[!d$flagged, ]
m <- aggregate(mP ~ conc + plate, d, function(x) c(mean = mean(x), sd = sd(x))); m <- do.call(data.frame, m); names(m)[3:4] <- c("mean", "sd")
p <- ggplot(m[m$conc > 0, ], aes(conc, mean, colour = plate)) +
  geom_errorbar(aes(ymin = mean - sd, ymax = mean + sd), width = 0.06, alpha = 0.7) +
  geom_line(linewidth = 0.9) + geom_point(size = 2.4) +
  geom_hline(data = m[m$conc == 0, ], aes(yintercept = mean, colour = plate), linetype = "dotted") +
  scale_x_log10(breaks = c(0.2, 0.5, 1, 2, 5, 10, 20)) + scale_colour_manual(values = c("16 Nov" = "#8A8A8A", "19 Nov" = "#1F4E79")) +
  labs(x = expression(paste("VLP (", mu, "g/mL)")), y = "Polarization (mP), G = 1.05, pooled VLP-only blank",
       title = "Buf-2 (5 nM) + VLP: two plates", subtitle = "mean +/- SD of wells, dotted = aptamer alone") + theme_bw(base_size = 12) + theme(panel.grid.minor = element_blank())
ggsave(file.path(Sys.getenv("OUT19"), "kd_two_plates_overlay.png"), p, width = 8, height = 5, dpi = 300)
