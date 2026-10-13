# 3D molecule generation and visualisation in R (benzene by default).
# Requires the 'rgl' package:  install.packages("rgl")

library(rgl)

# ---- Element properties (CPK colours, covalent radii in Angstrom) ----------
elements <- data.frame(
  symbol = c("H", "C", "N", "O"),
  color  = c("white", "grey30", "blue", "red"),
  radius = c(0.31, 0.76, 0.71, 0.66),
  stringsAsFactors = FALSE
)

# ---- Build a molecule: atoms (element + xyz) and bonds (index pairs) -------
make_benzene <- function(cc = 1.39, ch = 1.09) {
  theta <- seq(0, 2 * pi, length.out = 7)[1:6]
  carbon   <- cbind(cc * cos(theta), cc * sin(theta), 0)
  hydrogen <- cbind((cc + ch) * cos(theta), (cc + ch) * sin(theta), 0)

  atoms <- data.frame(
    element = c(rep("C", 6), rep("H", 6)),
    x = c(carbon[, 1], hydrogen[, 1]),
    y = c(carbon[, 2], hydrogen[, 2]),
    z = c(carbon[, 3], hydrogen[, 3]),
    stringsAsFactors = FALSE
  )

  ring <- cbind(1:6, c(2:6, 1))   # C-C bonds
  ch_b <- cbind(1:6, 7:12)        # C-H bonds
  list(atoms = atoms, bonds = rbind(ring, ch_b))
}

# Water as a second example (O-H 0.96 A, H-O-H 104.5 degrees)
make_water <- function() {
  half <- 104.5 / 2 * pi / 180
  atoms <- data.frame(
    element = c("O", "H", "H"),
    x = c(0, 0.96 * sin(half), -0.96 * sin(half)),
    y = c(0, 0.96 * cos(half),  0.96 * cos(half)),
    z = 0,
    stringsAsFactors = FALSE
  )
  list(atoms = atoms, bonds = rbind(c(1, 2), c(1, 3)))
}

# ---- Drawing helpers -------------------------------------------------------
# Cylinder between two points (used for bonds)
draw_bond <- function(p1, p2, radius = 0.09, col = "grey60") {
  d <- p2 - p1
  len <- sqrt(sum(d^2))
  cyl <- cylinder3d(
    center = rbind(p1, p2),
    radius = radius, sides = 20, closed = -2
  )
  shade3d(cyl, color = col)
}

draw_molecule <- function(mol, scale_atoms = 0.5) {
  atoms <- mol$atoms
  xyz <- as.matrix(atoms[, c("x", "y", "z")])

  # Bonds first, then atoms on top
  for (i in seq_len(nrow(mol$bonds))) {
    a <- mol$bonds[i, 1]; b <- mol$bonds[i, 2]
    draw_bond(xyz[a, ], xyz[b, ])
  }
  for (i in seq_len(nrow(atoms))) {
    el <- elements[elements$symbol == atoms$element[i], ]
    spheres3d(xyz[i, 1], xyz[i, 2], xyz[i, 3],
              radius = el$radius * scale_atoms * 2,
              color = el$color)
  }
}

# ---- Run -------------------------------------------------------------------
mol <- make_benzene()      # or make_water()

open3d()
bg3d("black")
draw_molecule(mol)
title3d(main = "Benzene (C6H6)", color = "white")
view3d(theta = 0, phi = -60, zoom = 0.8)

# Drag with the mouse to rotate. Uncomment to save a snapshot:
# rgl.snapshot("molecule.png")
