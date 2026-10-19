// Corrected fluorescence-polarization schematic, white background (#FFFFFF).
//
// Fixes applied vs. the draft figure:
//  1. Geometry is now physically possible. Excitation propagates along x and is
//     polarised along z (vertical). Emission is collected along y — at 90° to
//     BOTH the beam and its polarisation — so every polariser glyph shows a
//     direction the light can actually have.
//  2. The nanosecond window is shown: a strobe track comparing how far the
//     transition dipole rotates during the ~4 ns excited-state lifetime.
//  3. Photoselection is stated, so polarised emission has a cause.
//  4. Bound-state emission stays vertical; only the free state is scrambled.
//  5. Rotation indicators differ visibly between the two states.
//  6. Transmitted excitation is labelled as discarded.
//  7. The cuvette shows the real equilibrium: free and bound together.
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const W = 2400, H = 1900;
const C = {
  bg: "#FFFFFF",
  ink: "#14263F",
  slate: "#5C6B7D",
  hair: "#D7DEE5",
  teal: "#138A8A",      // excitation path
  tealL: "#A8DAD6",
  coral: "#E85D4A",     // emission path
  coralL: "#F7C5BC",
  gold: "#E9B23C",      // the fluorophore
  violet: "#7A5BA6",    // the target (virus)
  violetL: "#D3C6E4",
  panel: "#F6F9FA",
};
const FONT = "Inter, Liberation Sans, Helvetica, sans-serif";
const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;");
let uid = 0;

const txt = (x, y, size, t, o = {}) =>
  `<text x="${x}" y="${y}" font-size="${size}" fill="${o.fill || C.ink}"
     text-anchor="${o.anchor || "middle"}" font-family="${FONT}"
     font-weight="${o.weight || 400}" letter-spacing="${o.ls || 0}"
     ${o.style ? `font-style="${o.style}"` : ""} ${o.op ? `opacity="${o.op}"` : ""}>${esc(t)}</text>`;

// --- primitives --------------------------------------------------------------
function arrow(x1, y1, x2, y2, col, w = 5, head = 16, op = 1) {
  const a = Math.atan2(y2 - y1, x2 - x1);
  const bx = x2 - Math.cos(a) * head * 0.85, by = y2 - Math.sin(a) * head * 0.85;
  return `<g opacity="${op}"><line x1="${x1}" y1="${y1}" x2="${bx}" y2="${by}"
      stroke="${col}" stroke-width="${w}" stroke-linecap="round"/>
    <polygon points="${x2},${y2} ${x2 - Math.cos(a - 0.42) * head},${y2 - Math.sin(a - 0.42) * head}
      ${x2 - Math.cos(a + 0.42) * head},${y2 - Math.sin(a + 0.42) * head}" fill="${col}"/></g>`;
}
// Double-headed arrow = an oscillation direction (a polarisation or a dipole).
// angleDeg is measured from +x, so 90 = vertical on screen.
function dbl(cx, cy, len, angleDeg, col, w = 5, head = 13, op = 1) {
  const a = (angleDeg * Math.PI) / 180, hx = (Math.cos(a) * len) / 2, hy = (Math.sin(a) * len) / 2;
  return arrow(cx, cy, cx + hx, cy + hy, col, w, head, op) +
         arrow(cx, cy, cx - hx, cy - hy, col, w, head, op);
}
// A polariser disc. `tilt` turns the disc itself (it sits square to its beam);
// `stripe` is the transmission axis AS SEEN ON SCREEN, which is what matters —
// the projection of a vertical axis stays vertical however the disc is tilted.
function polariser(cx, cy, rx, ry, tilt, stripe, col) {
  const id = `pc${uid++}`;
  let g = `<g transform="rotate(${tilt} ${cx} ${cy})">
      <ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="#EDF3F6" stroke="${C.ink}" stroke-width="5"/></g>`;
  g += `<clipPath id="${id}"><ellipse cx="${cx}" cy="${cy}" rx="${rx - 4}" ry="${ry - 4}"
      transform="rotate(${tilt} ${cx} ${cy})"/></clipPath>`;
  g += `<g clip-path="url(#${id})" transform="rotate(${stripe} ${cx} ${cy})">`;
  for (let i = -6; i <= 6; i++)
    g += `<line x1="${cx + i * 15}" y1="${cy - ry - 30}" x2="${cx + i * 15}" y2="${cy + ry + 30}" stroke="${col}" stroke-width="6" opacity="0.85"/>`;
  g += `</g>`;
  return g;
}
function lamp(x, y) {
  return `<g><rect x="${x - 78}" y="${y - 46}" width="120" height="92" rx="14" fill="#64798F" stroke="${C.ink}" stroke-width="5"/>
    <ellipse cx="${x + 46}" cy="${y}" rx="16" ry="34" fill="#9FB2C4" stroke="${C.ink}" stroke-width="5"/></g>`;
}
function detector(x, y, rot = 0) {
  return `<g transform="rotate(${rot} ${x} ${y})"><rect x="${x - 54}" y="${y - 42}" width="108" height="84" rx="14"
      fill="#64798F" stroke="${C.ink}" stroke-width="5"/>
    <ellipse cx="${x - 54}" cy="${y}" rx="15" ry="31" fill="#D8E2EA" stroke="${C.ink}" stroke-width="5"/></g>`;
}
function unpolarised(cx, cy, r, col) {
  let g = "";
  for (let i = 0; i < 6; i++) g += dbl(cx, cy, r * 2, (i * 180) / 6, col, 4, 11, 0.95);
  return g;
}
function aptamer(cx, cy, s, col = C.teal, opts = {}) {
  const k = s / 100, w = 8 * k;
  let g = `<path d="M${-13 * k} ${64 * k} L${-13 * k} ${-6 * k}
      C ${-13 * k} ${-42 * k}, ${-40 * k} ${-48 * k}, ${-31 * k} ${-66 * k}
      C ${-21 * k} ${-90 * k}, ${21 * k} ${-90 * k}, ${31 * k} ${-66 * k}
      C ${40 * k} ${-48 * k}, ${13 * k} ${-42 * k}, ${13 * k} ${-6 * k} L ${13 * k} ${64 * k}"
      fill="none" stroke="${col}" stroke-width="${w}" stroke-linecap="round"/>`;
  for (let i = 0; i < 5; i++)
    g += `<line x1="${-13 * k}" x2="${13 * k}" y1="${(52 - i * 13) * k}" y2="${(52 - i * 13) * k}" stroke="${col}" stroke-width="${3.4 * k}" opacity="0.55"/>`;
  g += `<circle cx="${-13 * k}" cy="${70 * k}" r="${13 * k}" fill="${C.gold}" stroke="${C.ink}" stroke-width="${3 * k}"/>`;
  return `<g transform="translate(${cx} ${cy})${opts.rot ? ` rotate(${opts.rot})` : ""}">${g}</g>`;
}
function virus(cx, cy, r, fill = C.violetL) {
  let g = "";
  for (let i = 0; i < 12; i++) {
    const a = (i * Math.PI * 2) / 12;
    const x1 = cx + Math.cos(a) * r * 0.94, y1 = cy + Math.sin(a) * r * 0.94;
    const x2 = cx + Math.cos(a) * r * 1.26, y2 = cy + Math.sin(a) * r * 1.26;
    g += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${C.violet}" stroke-width="${r * 0.07}" stroke-linecap="round"/>`;
    g += `<circle cx="${x2}" cy="${y2}" r="${r * 0.11}" fill="${fill}" stroke="${C.violet}" stroke-width="${r * 0.045}"/>`;
  }
  g += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${C.violet}" stroke-width="${r * 0.075}"/>`;
  return g;
}

// =============================================================================
// TOP — the instrument, in a geometry that is actually possible
// =============================================================================
function instrument() {
  let s = "";
  const beamY = 372;

  // --- axis key ---
  const KX = 1880, KY = 70, KW = 440, KH = 330;
  s += `<rect x="${KX}" y="${KY}" width="${KW}" height="${KH}" rx="18" fill="${C.panel}" stroke="${C.hair}" stroke-width="3"/>`;
  s += txt(KX + KW / 2, KY + 46, 27, "all three at 90°", { weight: 700 });
  const ox = KX + 110, oy = KY + 262;
  s += arrow(ox, oy, ox + 196, oy, C.ink, 4, 14);
  s += txt(ox + 206, oy + 9, 25, "x — beam", { anchor: "start", fill: C.slate });
  s += arrow(ox, oy, ox, oy - 160, C.ink, 4, 14);
  s += txt(ox + 14, oy - 164, 25, "z — polarisation", { anchor: "start", fill: C.slate });
  s += arrow(ox, oy, ox - 72, oy + 56, C.ink, 4, 14);
  s += txt(ox - 60, oy + 82, 25, "y — detection", { anchor: "start", fill: C.slate });

  // --- excitation arm ---
  s += lamp(170, beamY);
  s += txt(170, beamY + 92, 26, "light source", { fill: C.slate });
  s += `<line x1="228" y1="${beamY}" x2="560" y2="${beamY}" stroke="${C.tealL}" stroke-width="7"/>`;
  s += unpolarised(330, beamY, 46, C.teal);
  s += txt(330, beamY + 92, 26, "unpolarised", { fill: C.slate, style: "italic" });
  s += txt(430, beamY - 186, 34, "EXCITATION", { fill: C.teal, weight: 700, ls: 4 });
  s += arrow(330, beamY - 152, 560, beamY - 152, C.teal, 5, 15);

  s += polariser(600, beamY, 42, 88, 0, 0, C.teal);
  s += txt(600, beamY + 136, 27, "excitation polariser", { weight: 700 });
  s += txt(600, beamY + 168, 25, "passes vertical (z)", { fill: C.slate });

  // vertically polarised, travelling along x — a valid combination
  s += `<line x1="642" y1="${beamY}" x2="950" y2="${beamY}" stroke="${C.tealL}" stroke-width="7"/>`;
  for (let i = 0; i < 5; i++) s += dbl(690 + i * 62, beamY, 104, 90, C.teal, 5, 13);

  // --- sample ---
  const bx = 980, by = beamY - 96, bw = 168, bh = 192, dx = 30, dy = -26;
  s += `<polygon points="${bx},${by} ${bx + bw},${by} ${bx + bw + dx},${by + dy} ${bx + dx},${by + dy}" fill="#E6EFF2" stroke="${C.ink}" stroke-width="4"/>`;
  s += `<polygon points="${bx + bw},${by} ${bx + bw + dx},${by + dy} ${bx + bw + dx},${by + bh + dy} ${bx + bw},${by + bh}" fill="#DCE8EC" stroke="${C.ink}" stroke-width="4"/>`;
  s += `<rect x="${bx}" y="${by}" width="${bw}" height="${bh}" fill="#F4FAFB" stroke="${C.ink}" stroke-width="4"/>`;
  s += aptamer(bx + 46, by + 86, 54, C.teal);
  s += virus(bx + 116, by + 132, 34);
  s += aptamer(bx + 116, by + 78, 34, C.teal, { rot: 20 });

  // photoselection — the reason emission is polarised at all
  s += `<rect x="716" y="104" width="760" height="124" rx="16" fill="${C.panel}" stroke="${C.teal}" stroke-width="3"/>`;
  s += txt(1096, 146, 27, "Photoselection: the vertical field excites only molecules", { weight: 700 });
  s += txt(1096, 180, 27, "whose dipole happens to lie along z —", { weight: 700 });
  s += txt(1096, 212, 25, "that is why the emission starts out polarised", { fill: C.slate, style: "italic" });
  s += `<path d="M1096 228 L1096 256 L1064 256" fill="none" stroke="${C.teal}" stroke-width="3" stroke-dasharray="8 7"/>`;

  // --- transmitted beam is waste, not signal ---
  s += `<line x1="${bx + bw + dx}" y1="${beamY}" x2="1452" y2="${beamY}" stroke="${C.tealL}" stroke-width="7" opacity="0.55"/>`;
  for (let i = 0; i < 2; i++) s += dbl(1286 + i * 66, beamY, 84, 90, C.teal, 4, 11, 0.4);
  s += `<path d="M1462 ${beamY - 56} L1516 ${beamY - 56} L1462 ${beamY + 56} L1516 ${beamY + 56} Z" fill="#8296A8" stroke="${C.ink}" stroke-width="4"/>`;
  s += txt(1489, beamY - 92, 25, "transmitted excitation", { fill: C.slate });
  s += txt(1489, beamY - 62, 25, "(discarded)", { fill: C.slate, style: "italic" });

  // --- emission arm: along y, 90° to the beam AND to its polarisation ---
  const ex = bx + 60, ey = by + bh;
  const ux = -0.526, uy = 0.851;                      // unit vector along +y
  const P = (t) => [ex + ux * t, ey + uy * t];
  const [pxA, pyA] = P(250), [pxB, pyB] = P(410);
  s += `<line x1="${ex}" y1="${ey}" x2="${pxB}" y2="${pyB}" stroke="${C.coralL}" stroke-width="7"/>`;
  s += arrow(ex, ey, ...P(150), C.coral, 6, 18);
  const ang = (Math.atan2(uy, ux) * 180) / Math.PI;   // 121.7°
  s += polariser(pxA, pyA, 38, 80, ang - 90, 0, C.coral);   // disc tilted, stripes vertical on screen
  s += detector(pxB - 6, pyB + 16, -32);

  // sample caption, placed clear of the emission arm
  s += txt(1186, ey + 54, 27, "sample: free + bound aptamer", { anchor: "start", weight: 700 });
  s += txt(1186, ey + 86, 25, "at equilibrium", { anchor: "start", fill: C.slate });

  s += txt(872, 606, 32, "EMISSION", { fill: C.coral, weight: 700, ls: 4, anchor: "end" });
  s += txt(872, 642, 25, "collected along y, toward the viewer", { fill: C.slate, style: "italic", anchor: "end" });
  s += `<path d="M${ex + 50} ${ey} A 50 50 0 0 1 ${P(50)[0]} ${P(50)[1]}" fill="none" stroke="${C.slate}" stroke-width="3"/>`;
  s += txt(ex + 62, ey + 46, 25, "90°", { fill: C.slate, anchor: "start" });
  s += txt(628, 790, 26, "emission polariser → detector", { anchor: "end", weight: 700 });
  s += txt(628, 822, 25, "one polariser, turned between the readings", { anchor: "end", fill: C.slate, style: "italic" });

  // the two readings — each glyph is a direction this beam can actually have
  const rx0 = 1186, ry0 = 584;
  s += `<rect x="${rx0}" y="${ry0}" width="446" height="122" rx="16" fill="${C.panel}" stroke="${C.hair}" stroke-width="3"/>`;
  s += dbl(rx0 + 64, ry0 + 61, 74, 90, C.coral, 6, 14);
  s += txt(rx0 + 132, ry0 + 52, 34, "I∥", { anchor: "start", weight: 700 });
  s += txt(rx0 + 132, ry0 + 88, 25, "polariser vertical (z)", { anchor: "start", fill: C.slate });
  s += `<rect x="${rx0}" y="${ry0 + 142}" width="446" height="122" rx="16" fill="${C.panel}" stroke="${C.hair}" stroke-width="3"/>`;
  s += dbl(rx0 + 64, ry0 + 203, 74, 0, C.coral, 6, 14);
  s += txt(rx0 + 132, ry0 + 194, 34, "I⊥", { anchor: "start", weight: 700 });
  s += txt(rx0 + 132, ry0 + 230, 25, "polariser horizontal (x)", { anchor: "start", fill: C.slate });
  return s;
}

// =============================================================================
// BOTTOM — why binding changes the answer: the nanosecond window
// =============================================================================
function statePanel(x0, y0, w, bound) {
  let s = "";
  s += txt(x0 + 40, y0 + 46, 44, bound ? "BOUND" : "UNBOUND",
           { anchor: "start", weight: 700, fill: bound ? C.violet : C.teal, ls: 3 });
  s += txt(x0 + 40, y0 + 88, 27, bound ? "aptamer on the virus — one big, slow object"
                                       : "free aptamer — small and quick",
           { anchor: "start", fill: C.slate, style: "italic" });

  // --- the molecule, with a rotation indicator that differs between states ---
  const mx = x0 + 210, my = y0 + 250;
  if (bound) {
    s += virus(mx, my + 8, 88);
    s += aptamer(mx + 50, my - 88, 50, C.teal, { rot: 24 });
    s += `<path d="M${mx - 146} ${my + 38} a 150 150 0 0 1 20 -44" fill="none" stroke="${C.ink}" stroke-width="7" stroke-linecap="round"/>`;
    s += arrow(mx - 128, my - 4, mx - 123, my - 16, C.ink, 7, 16);
  } else {
    for (let i = 0; i < 3; i++)
      s += `<ellipse cx="${mx}" cy="${my}" rx="${104 + i * 25}" ry="${92 + i * 21}" fill="none" stroke="${C.teal}" stroke-width="${5 - i}" stroke-dasharray="20 16" opacity="${0.6 - i * 0.16}"/>`;
    s += aptamer(mx, my + 18, 82, C.teal, { rot: -14 });
    s += arrow(mx + 98, my - 66, mx + 126, my - 28, C.ink, 7, 17);
    s += arrow(mx - 98, my + 66, mx - 126, my + 28, C.ink, 7, 17);
  }
  s += txt(mx, my + 160, 28, bound ? "τc ≈ 1 µs" : "τc ≈ 1 ns", { weight: 700 });
  s += txt(mx, my + 190, 24, "rotational correlation time", { fill: C.slate });

  // --- excitation in, emission out ---
  s += dbl(x0 + 398, my - 34, 84, 90, C.teal, 5, 13);
  s += arrow(x0 + 378, my + 26, x0 + 420, my + 26, C.teal, 5, 14);
  const eo = x0 + 580;
  if (bound) {
    for (let i = 0; i < 4; i++) s += dbl(eo + i * 56, my, 112, 90 + (i - 1.5) * 4, C.coral, 6, 14);
    s += txt(eo + 84, my + 124, 27, "emission keeps its direction", { weight: 700, fill: C.coral });
  } else {
    for (let i = 0; i < 7; i++) s += dbl(eo + 84, my, 148, (i * 180) / 7, C.coral, 5, 13, 0.95);
    s += txt(eo + 84, my + 124, 27, "emission direction scrambled", { weight: 700, fill: C.coral });
  }

  // --- the strobe: how far the dipole turns inside the 4 ns window ---
  const bt = y0 + 462, sy = bt + 120, sx = x0 + 78, sw = w - 168;
  s += `<rect x="${sx - 30}" y="${bt}" width="${sw + 60}" height="206" rx="18" fill="${C.panel}" stroke="${C.hair}" stroke-width="3"/>`;
  s += txt(sx + sw / 2, bt + 34, 26, "direction of the emission dipole during the ~4 ns excited state",
           { weight: 700 });
  s += `<line x1="${sx}" y1="${sy}" x2="${sx + sw}" y2="${sy}" stroke="${C.slate}" stroke-width="4"/>`;
  const angles = bound ? [0, 5, 11, 16, 21] : [0, 72, 158, 236, 311];
  angles.forEach((a, i) => {
    const px = sx + (i * sw) / 4;
    s += `<line x1="${px}" y1="${sy - 8}" x2="${px}" y2="${sy + 8}" stroke="${C.slate}" stroke-width="4"/>`;
    s += txt(px, sy + 36, 23, `${i} ns`, { fill: C.slate });
    s += dbl(px, sy - 52, 66, 90 - a, i === 0 ? C.ink : C.coral, 5, 12);
  });
  s += txt(sx + sw / 2, bt + 188, 26,
           bound ? "slower than the lifetime → it barely turns before emitting"
                 : "faster than the lifetime → it turns several times before emitting",
           { fill: C.slate, style: "italic" });

  // --- intensities and the verdict ---
  const byy = y0 + 860, bw2 = 94, gap = 60, bx0 = x0 + 118, maxh = 150;
  const Ipar = bound ? 1.30 : 1.05, Iperp = bound ? 0.70 : 0.95;
  [[Ipar, "I∥", C.coral], [Iperp, "I⊥", C.coralL]].forEach(([v, lab, col], i) => {
    const h = (v / 1.45) * maxh, bxx = bx0 + i * (bw2 + gap);
    s += `<rect x="${bxx}" y="${byy - maxh}" width="${bw2}" height="${maxh}" rx="6" fill="#EDF2F5"/>`;
    s += `<rect x="${bxx}" y="${byy - h}" width="${bw2}" height="${h}" rx="6" fill="${col}" stroke="${C.coral}" stroke-width="3"/>`;
    s += txt(bxx + bw2 / 2, byy + 36, 30, lab, { weight: 700 });
  });
  s += `<line x1="${bx0 - 24}" y1="${byy}" x2="${bx0 + 2 * bw2 + gap + 24}" y2="${byy}" stroke="${C.ink}" stroke-width="4"/>`;
  const Pm = Math.round(((Ipar - Iperp) / (Ipar + Iperp)) * 1000 / 10) * 10;
  s += txt(x0 + 450, byy - 108, 40, bound ? "HIGH polarisation" : "LOW polarisation",
           { anchor: "start", weight: 700, fill: bound ? C.violet : C.teal });
  s += txt(x0 + 450, byy - 56, 34, `P ≈ ${Pm} mP`, { anchor: "start", weight: 700 });
  s += txt(x0 + 450, byy - 14, 26, bound ? "I∥ clearly exceeds I⊥" : "I∥ and I⊥ almost equal",
           { anchor: "start", fill: C.slate, style: "italic" });
  return s;
}

// =============================================================================
function build() {
  let s = `<rect width="${W}" height="${H}" fill="${C.bg}"/>`;
  s += txt(60, 62, 40, "Fluorescence polarisation: how binding is read out",
           { anchor: "start", weight: 700 });
  s += instrument();
  s += `<line x1="60" y1="896" x2="${W - 60}" y2="896" stroke="${C.hair}" stroke-width="4"/>`;
  s += statePanel(60, 926, 1120, false);
  s += `<line x1="1200" y1="956" x2="1200" y2="1830" stroke="${C.hair}" stroke-width="4"/>`;
  s += statePanel(1240, 926, 1120, true);
  s += txt(300, H - 26, 26, "P = (I∥ − G·I⊥) / (I∥ + G·I⊥)", { fill: C.slate });
  s += txt(840, H - 26, 26, "mP = 1000 × P", { fill: C.slate });
  s += txt(1560, H - 26, 26, "G corrects the detector's own polarisation bias", { fill: C.slate });
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">${s}</svg>`;
}

(async () => {
  const svg = build();
  const out = path.join(__dirname, "..", "fp_principle_figure");
  fs.writeFileSync(out + ".svg", svg);
  await sharp(Buffer.from(svg), { density: 110 }).png().toFile(out + ".png");
  console.log("wrote", out + ".png");
})();
