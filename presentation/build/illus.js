// Vector illustrations (SVG) shared by the talk and the poster.
// Each export returns { svg, w, h } in SVG user units; render with toPng().
const sharp = require("sharp");

const P = {
  navy: "1B2A41", teal: "138A8A", tealL: "7CC6C2", tealXL: "D5EEEC",
  coral: "E85D4A", coralL: "F6B7AC", sun: "F2C14E", sunL: "FBE6A8",
  slate: "5C6B7D", mist: "EEF3F6", line: "C9D3DC", white: "FFFFFF",
  brown: "8A6A4F", brownL: "D9C3A5", violet: "7A5BA6", green: "5E9E50",
};
const c = (k) => "#" + (P[k] || k);

async function toPng(ill, widthPx = 1600) {
  const density = Math.max(72, (72 * widthPx) / ill.w);
  return sharp(Buffer.from(ill.svg), { density }).png().toBuffer();
}
const wrap = (w, h, body) => ({
  w, h,
  svg: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" font-family="Calibri, Arial, sans-serif">${body}</svg>`,
});

// ---------- primitives ----------
function virus(x, y, r, fill = "coral", stroke = "navy", face = false) {
  let s = "";
  for (let i = 0; i < 12; i++) {
    const a = (i * Math.PI) / 6;
    const x1 = x + Math.cos(a) * r * 0.9, y1 = y + Math.sin(a) * r * 0.9;
    const x2 = x + Math.cos(a) * r * 1.35, y2 = y + Math.sin(a) * r * 1.35;
    s += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${c(stroke)}" stroke-width="${r * 0.09}"/>`;
    s += `<circle cx="${x2}" cy="${y2}" r="${r * 0.14}" fill="${c(fill)}" stroke="${c(stroke)}" stroke-width="${r * 0.06}"/>`;
  }
  const hex = [...Array(6)].map((_, i) => {
    const a = (i * Math.PI) / 3 + Math.PI / 6;
    return `${x + Math.cos(a) * r},${y + Math.sin(a) * r}`;
  }).join(" ");
  s += `<polygon points="${hex}" fill="${c(fill)}" stroke="${c(stroke)}" stroke-width="${r * 0.08}" stroke-linejoin="round"/>`;
  s += `<polygon points="${[...Array(3)].map((_, i) => { const a = (i * 2 * Math.PI) / 3 - Math.PI / 2; return `${x + Math.cos(a) * r * 0.5},${y + Math.sin(a) * r * 0.5}`; }).join(" ")}" fill="none" stroke="${c(stroke)}" stroke-opacity="0.35" stroke-width="${r * 0.05}"/>`;
  if (face) s += faceAt(x, y + r * 0.1, r * 0.55, "grin");
  return s;
}
function bacterium(x, y, len, rot, fill = "tealXL", stroke = "tealL") {
  const h = len * 0.38;
  return `<g transform="translate(${x} ${y}) rotate(${rot})"><rect x="${-len / 2}" y="${-h / 2}" width="${len}" height="${h}" rx="${h / 2}" fill="${c(fill)}" stroke="${c(stroke)}" stroke-width="${len * 0.05}"/><path d="M${len / 2} 0 q ${len * 0.2} ${-h * 0.4} ${len * 0.4} 0 t ${len * 0.4} 0" fill="none" stroke="${c(stroke)}" stroke-width="${len * 0.03}"/></g>`;
}
// Stem-loop aptamer drawn as a strand with base-pair rungs.
function aptamer(x, y, s, col = "teal", variant = 0, opts = {}) {
  const k = s / 100;
  const st = c(col), w = 7 * k;
  let g = "";
  if (variant === 0) { // hairpin
    g += `<path d="M${-12 * k} ${60 * k} L${-12 * k} ${-5 * k} C ${-12 * k} ${-40 * k}, ${-38 * k} ${-45 * k}, ${-30 * k} ${-62 * k} C ${-20 * k} ${-85 * k}, ${20 * k} ${-85 * k}, ${30 * k} ${-62 * k} C ${38 * k} ${-45 * k}, ${12 * k} ${-40 * k}, ${12 * k} ${-5 * k} L ${12 * k} ${60 * k}" fill="none" stroke="${st}" stroke-width="${w}" stroke-linecap="round"/>`;
    for (let i = 0; i < 5; i++) g += `<line x1="${-12 * k}" x2="${12 * k}" y1="${(50 - i * 12) * k}" y2="${(50 - i * 12) * k}" stroke="${st}" stroke-width="${3 * k}" opacity="0.6"/>`;
  } else if (variant === 1) { // G-quadruplex stack
    for (let i = 0; i < 3; i++) g += `<rect x="${-26 * k}" y="${(-60 + i * 24) * k}" width="${52 * k}" height="${14 * k}" rx="${3 * k}" fill="none" stroke="${st}" stroke-width="${w * 0.8}" transform="skewX(-15)"/>`;
    g += `<path d="M${-30 * k} ${-40 * k} q ${-20 * k} ${20 * k} 0 ${40 * k} M${30 * k} ${-50 * k} q ${20 * k} ${25 * k} 0 ${48 * k} M0 ${10 * k} L0 ${60 * k}" fill="none" stroke="${st}" stroke-width="${w}" stroke-linecap="round"/>`;
  } else if (variant === 2) { // three-way junction
    g += `<path d="M${-10 * k} ${60 * k} L${-10 * k} ${10 * k} L${-45 * k} ${-25 * k} q ${-15 * k} ${-20 * k} ${5 * k} ${-28 * k} L ${-2 * k} ${-12 * k} L ${-2 * k} ${-50 * k} q 0 ${-22 * k} ${18 * k} ${-12 * k} L ${14 * k} ${-6 * k} L ${45 * k} ${-30 * k} q ${18 * k} ${5 * k} ${5 * k} ${22 * k} L ${10 * k} ${12 * k} L ${10 * k} ${60 * k}" fill="none" stroke="${st}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`;
  } else { // bulged hairpin
    g += `<path d="M${-12 * k} ${60 * k} L${-12 * k} ${20 * k} q ${-22 * k} ${-12 * k} 0 ${-24 * k} L ${-12 * k} ${-30 * k} C ${-40 * k} ${-60 * k}, ${40 * k} ${-90 * k}, ${12 * k} ${-30 * k} L ${12 * k} ${60 * k}" fill="none" stroke="${st}" stroke-width="${w}" stroke-linecap="round"/>`;
    for (let i = 0; i < 4; i++) g += `<line x1="${-12 * k}" x2="${12 * k}" y1="${(50 - i * 10) * k - (i > 1 ? 30 * k : 0)}" y2="${(50 - i * 10) * k - (i > 1 ? 30 * k : 0)}" stroke="${st}" stroke-width="${3 * k}" opacity="0.6"/>`;
  }
  if (opts.face) g += faceAt(0, -55 * k, 15 * k, opts.face);
  if (opts.dye) g += `<circle cx="0" cy="${64 * k}" r="${9 * k}" fill="${c("sun")}" stroke="${c("navy")}" stroke-width="${2 * k}"/>`;
  return `<g transform="translate(${x} ${y})${opts.rot ? ` rotate(${opts.rot})` : ""}">${g}</g>`;
}
function faceAt(x, y, r, mood = "smile") {
  const e = r * 0.28, ex = r * 0.38;
  let eyes = mood === "sleep"
    ? `<path d="M${x - ex - e} ${y - r * 0.15} q ${e} ${e} ${2 * e} 0 M${x + ex - e} ${y - r * 0.15} q ${e} ${e} ${2 * e} 0" stroke="#1B2A41" stroke-width="${r * 0.1}" fill="none" stroke-linecap="round"/>`
    : `<circle cx="${x - ex}" cy="${y - r * 0.15}" r="${e * 0.7}" fill="#1B2A41"/><circle cx="${x + ex}" cy="${y - r * 0.15}" r="${e * 0.7}" fill="#1B2A41"/><circle cx="${x - ex + e * 0.25}" cy="${y - r * 0.22}" r="${e * 0.22}" fill="#fff"/><circle cx="${x + ex + e * 0.25}" cy="${y - r * 0.22}" r="${e * 0.22}" fill="#fff"/>`;
  if (mood === "angry") eyes += `<path d="M${x - ex - e} ${y - r * 0.55} L${x - ex + e} ${y - r * 0.35} M${x + ex + e} ${y - r * 0.55} L${x + ex - e} ${y - r * 0.35}" stroke="#1B2A41" stroke-width="${r * 0.1}" stroke-linecap="round"/>`;
  const mouth = {
    smile: `<path d="M${x - r * 0.3} ${y + r * 0.2} q ${r * 0.3} ${r * 0.3} ${r * 0.6} 0" stroke="#1B2A41" stroke-width="${r * 0.1}" fill="none" stroke-linecap="round"/>`,
    grin: `<path d="M${x - r * 0.35} ${y + r * 0.15} q ${r * 0.35} ${r * 0.45} ${r * 0.7} 0 z" fill="#1B2A41"/>`,
    sleep: `<ellipse cx="${x}" cy="${y + r * 0.3}" rx="${r * 0.12}" ry="${r * 0.08}" fill="#1B2A41"/>`,
    angry: `<path d="M${x - r * 0.3} ${y + r * 0.35} q ${r * 0.3} ${-r * 0.25} ${r * 0.6} 0" stroke="#1B2A41" stroke-width="${r * 0.1}" fill="none" stroke-linecap="round"/>`,
    worried: `<path d="M${x - r * 0.3} ${y + r * 0.35} q ${r * 0.15} ${-r * 0.15} ${r * 0.3} 0 t ${r * 0.3} 0" stroke="#1B2A41" stroke-width="${r * 0.09}" fill="none" stroke-linecap="round"/>`,
  }[mood] || "";
  return eyes + mouth;
}
function tube(x, y, s, fill = "brownL", label = "") {
  const k = s / 100;
  return `<g transform="translate(${x} ${y})"><rect x="${-18 * k}" y="${-50 * k}" width="${36 * k}" height="${14 * k}" rx="${3 * k}" fill="${c("slate")}"/><path d="M${-15 * k} ${-36 * k} L${-15 * k} ${35 * k} q 0 ${15 * k} ${15 * k} ${15 * k} q ${15 * k} 0 ${15 * k} ${-15 * k} L ${15 * k} ${-36 * k} z" fill="#fff" stroke="${c("slate")}" stroke-width="${3 * k}"/><path d="M${-13 * k} ${0} L${-13 * k} ${35 * k} q 0 ${13 * k} ${13 * k} ${13 * k} q ${13 * k} 0 ${13 * k} ${-13 * k} L ${13 * k} 0 z" fill="${c(fill)}"/>${label ? `<text x="0" y="${72 * k}" font-size="${16 * k}" text-anchor="middle" fill="${c("slate")}">${label}</text>` : ""}</g>`;
}
function antibody(x, y, s, col = "violet") {
  const k = s / 100, w = 13 * k, st = c(col);
  return `<g transform="translate(${x} ${y})" stroke="${st}" stroke-width="${w}" stroke-linecap="round" fill="none"><path d="M0 ${55 * k} L0 0 L${-38 * k} ${-45 * k} M0 0 L${38 * k} ${-45 * k}"/><path d="M${-16 * k} ${-6 * k} L${-50 * k} ${-46 * k} M${16 * k} ${-6 * k} L${50 * k} ${-46 * k}" stroke-opacity="0.45"/></g>`;
}
const arrow = (x1, y1, x2, y2, col = "slate", w = 3) => {
  const a = Math.atan2(y2 - y1, x2 - x1), L = w * 4;
  return `<line x1="${x1}" y1="${y1}" x2="${x2 - Math.cos(a) * L * 0.8}" y2="${y2 - Math.sin(a) * L * 0.8}" stroke="${c(col)}" stroke-width="${w}" stroke-linecap="round"/><polygon points="${x2},${y2} ${x2 - Math.cos(a - 0.45) * L},${y2 - Math.sin(a - 0.45) * L} ${x2 - Math.cos(a + 0.45) * L},${y2 - Math.sin(a + 0.45) * L}" fill="${c(col)}"/>`;
};
const txt = (x, y, s, t, col = "navy", anchor = "middle", weight = "normal", extra = "") =>
  `<text x="${x}" y="${y}" font-size="${s}" fill="${c(col)}" text-anchor="${anchor}" font-weight="${weight}" ${extra}>${String(t).replace(/&(?!amp;)/g, "&amp;")}</text>`;
function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }


// ---------- shared small parts ----------
// Diffuse counterion atmosphere: a cloud of small "+" marks, denser near the strand.
function ionCloud(cx, cy, rx, ry, n, seed, col = "coral", size = 9) {
  const r = rng(seed); let s = "";
  for (let i = 0; i < n; i++) {
    const a = r() * Math.PI * 2, u = Math.sqrt(r());
    const x = cx + Math.cos(a) * rx * u, y = cy + Math.sin(a) * ry * u;
    const o = 0.85 - u * 0.5;
    s += `<g opacity="${o.toFixed(2)}"><line x1="${x - size / 2}" y1="${y}" x2="${x + size / 2}" y2="${y}" stroke="${c(col)}" stroke-width="${size * 0.3}" stroke-linecap="round"/><line x1="${x}" y1="${y - size / 2}" x2="${x}" y2="${y + size / 2}" stroke="${c(col)}" stroke-width="${size * 0.3}" stroke-linecap="round"/></g>`;
  }
  return s;
}
const minus = (x, y, size = 9, col = "teal") =>
  `<line x1="${x - size / 2}" y1="${y}" x2="${x + size / 2}" y2="${y}" stroke="${c(col)}" stroke-width="${size * 0.32}" stroke-linecap="round"/>`;
// Norovirus-like particle with a positively charged patch.
function noro(x, y, r, opts = {}) {
  let s = virus(x, y, r, opts.fill || "coralL", "navy", opts.face);
  if (opts.patch) {
    s += `<path d="M${x + r * 0.15} ${y - r * 0.95} a ${r} ${r} 0 0 1 ${r * 0.82} ${r * 0.62} z" fill="${c("violet")}" opacity="0.85"/>`;
    for (let i = 0; i < 3; i++) s += `<g><line x1="${x + r * 0.3 + i * r * 0.22}" y1="${y - r * 0.6 + i * r * 0.1}" x2="${x + r * 0.46 + i * r * 0.22}" y2="${y - r * 0.6 + i * r * 0.1}" stroke="#fff" stroke-width="${r * 0.07}"/><line x1="${x + r * 0.38 + i * r * 0.22}" y1="${y - r * 0.68 + i * r * 0.1}" x2="${x + r * 0.38 + i * r * 0.22}" y2="${y - r * 0.52 + i * r * 0.1}" stroke="#fff" stroke-width="${r * 0.07}"/></g>`;
  }
  return s;
}
const person = (x, y, s, col = "teal") => {
  const k = s / 100;
  return `<g transform="translate(${x} ${y})"><circle cx="0" cy="${-28 * k}" r="${18 * k}" fill="${c(col)}"/><path d="M${-26 * k} ${22 * k} q 0 ${-32 * k} ${26 * k} ${-32 * k} q ${26 * k} 0 ${26 * k} ${32 * k} z" fill="${c(col)}"/></g>`;
};

// ---------- TALK ----------
// Slide 1 + 14: donor -> donations -> patient, with today's donation unlabelled.
function donationChain() {
  const W = 1150, H = 460;
  let s = person(90, 230, 150, "teal") + txt(90, 340, 26, "donor", "slate");
  for (let i = 0; i < 4; i++) {
    const x = 330 + i * 150, today = i === 2;
    s += tube(x, 215, 110, today ? "brownL" : "brownL");
    if (today) {
      s += `<circle cx="${x}" cy="215" r="88" fill="none" stroke="${c("coral")}" stroke-width="7" stroke-dasharray="16 12"/>`;
      s += txt(x, 355, 26, "today", "coral", "middle", "bold");
      s += txt(x, 100, 60, "?", "coral", "middle", "bold");
    }
  }
  s += arrow(200, 215, 270, 215, "slate", 5) + arrow(950, 215, 1020, 215, "slate", 5);
  s += person(1085, 230, 150, "violet") + txt(1085, 340, 26, "patient", "slate");
  return wrap(W, H, s);
}

// Slide 2: the donation cannot be sterilised.
function activeIngredient() {
  const W = 900, H = 420, r = rng(11);
  let s = `<rect x="40" y="60" width="380" height="300" rx="30" fill="${c("tealXL")}" stroke="${c("teal")}" stroke-width="6"/>`;
  for (let i = 0; i < 26; i++) s += bacterium(80 + r() * 300, 100 + r() * 220, 40 + r() * 26, r() * 180, "white", "teal");
  s += txt(230, 395, 26, "living microbial community", "teal", "middle", "bold");
  s += arrow(450, 210, 530, 210, "slate", 6);
  s += `<rect x="560" y="60" width="300" height="300" rx="30" fill="${c("mist")}" stroke="${c("line")}" stroke-width="6"/>`;
  s += `<g opacity="0.3">`;
  for (let i = 0; i < 18; i++) s += bacterium(590 + r() * 240, 100 + r() * 220, 40, r() * 180, "line", "slate");
  s += `</g>`;
  s += `<line x1="600" y1="100" x2="820" y2="320" stroke="${c("coral")}" stroke-width="14" stroke-linecap="round"/><line x1="820" y1="100" x2="600" y2="320" stroke="${c("coral")}" stroke-width="14" stroke-linecap="round"/>`;
  s += txt(710, 395, 26, "cannot be sterilised", "coral", "middle", "bold");
  return wrap(W, H, s);
}

// Slide 3: the screening interval, with a shedding episode inside it.
function screeningGap() {
  const W = 1250, H = 600;
  const y0 = 300, x0 = 110, x1 = 1140;
  let s = "";
  // shedding curve rising and falling inside the interval
  s += `<path d="M${x0} ${y0} L 430 ${y0} C 520 ${y0}, 540 120, 650 120 C 760 120, 790 ${y0}, 880 ${y0} L ${x1} ${y0}" fill="${c("coralL")}" fill-opacity="0.55" stroke="${c("coral")}" stroke-width="6"/>`;
  s += `<line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y0}" stroke="${c("navy")}" stroke-width="6"/>`;
  // screening bookends
  [[x0, "screened"], [x1, "re-assessed"]].forEach(([x, l]) => {
    s += `<line x1="${x}" y1="100" x2="${x}" y2="${y0 + 40}" stroke="${c("teal")}" stroke-width="7"/>`;
    s += `<circle cx="${x}" cy="90" r="26" fill="${c("teal")}"/><path d="M${x - 12} 90 l 8 10 l 17 -20" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
    s += txt(x, 58, 26, l, "teal", "middle", "bold");
  });
  // donations
  for (let i = 0; i < 7; i++) {
    const x = 190 + i * 140, hot = x > 470 && x < 850;
    s += tube(x, y0 + 105, 82, "brownL");
    if (hot) s += `<circle cx="${x}" cy="${y0 + 105}" r="62" fill="none" stroke="${c("coral")}" stroke-width="6" stroke-dasharray="12 9"/>`;
  }
  s += txt(625, 500, 26, "donations made between the two tests", "slate");
  s += txt(650, 95, 28, "acquires virus → sheds → recovers", "coral", "middle", "bold");
  s += txt(625, 556, 28, "possibly without symptoms", "coral", "middle", "bold", `font-style="italic"`);
  return wrap(W, H, s);
}

// Slide 5: triage funnel - flags for confirmation, never clears a donation.
function triageFunnel() {
  const W = 1000, H = 620;
  let s = "";
  for (let i = 0; i < 8; i++) s += tube(95 + (i % 4) * 70, 90 + Math.floor(i / 4) * 115, 72, "brownL");
  s += txt(200, 290, 26, "every donation", "slate", "middle", "bold");
  s += arrow(330, 140, 420, 140, "slate", 5);
  s += `<rect x="440" y="60" width="300" height="160" rx="24" fill="${c("teal")}"/>`;
  s += txt(590, 125, 32, "rapid test", "white", "middle", "bold");
  s += txt(590, 170, 24, "minutes, at the bank", "tealXL");
  s += arrow(760, 110, 840, 85, "coral", 5) + arrow(760, 175, 840, 215, "teal", 5);
  s += `<rect x="845" y="38" width="150" height="96" rx="18" fill="${c("coralL")}" stroke="${c("coral")}" stroke-width="5"/>`;
  s += txt(920, 78, 24, "flagged", "coral", "middle", "bold") + txt(920, 110, 22, "→ RT-qPCR", "navy");
  s += `<rect x="845" y="170" width="150" height="96" rx="18" fill="${c("mist")}" stroke="${c("line")}" stroke-width="5"/>`;
  s += txt(920, 208, 24, "not flagged", "slate", "middle", "bold") + txt(920, 240, 22, "→ usual route", "slate");
  // the honest caveat
  s += `<rect x="60" y="400" width="880" height="170" rx="26" fill="${c("navy")}"/>`;
  s += txt(500, 462, 34, "Triage, not a verdict", "sun", "middle", "bold");
  s += txt(500, 512, 27, "it narrows the window where an infected donation goes unnoticed —", "white");
  s += txt(500, 548, 27, "it never declares a donation safe on its own", "white");
  return wrap(W, H, s);
}

// Slide 6: why norovirus.
function norovirusFacts() {
  const W = 1180, H = 470;
  const items = [
    ["very low", "infectious dose", "coral"],
    ["huge", "shedding titres", "violet"],
    ["silent", "shedding without symptoms", "sun"],
    ["prolonged", "in immuno- compromised hosts", "teal"],
  ];
  let s = noro(145, 215, 95, { patch: false, fill: "coralL" });
  s += txt(145, 390, 30, "norovirus", "navy", "middle", "bold");
  items.forEach(([big, small, col], i) => {
    const x = 310 + i * 218;
    s += `<rect x="${x}" y="70" width="196" height="320" rx="24" fill="${c("mist")}"/>`;
    s += txt(x + 98, 185, 42, big, col, "middle", "bold");
    const words = small.split(" "); let line = "", lines = [];
    words.forEach((w) => { if ((line + w).length > 14) { lines.push(line); line = w + " "; } else line += w + " "; });
    lines.push(line);
    lines.forEach((l, j) => (s += txt(x + 98, 245 + j * 34, 24, l.trim(), "navy")));
  });
  return wrap(W, H, s);
}

// Slide 8: WP1 sampling across one interval.
function wp1Sampling() {
  const W = 1050, H = 470;
  let s = person(80, 180, 140, "teal") + txt(80, 285, 24, "same donor", "slate");
  s += `<line x1="200" y1="180" x2="1010" y2="180" stroke="${c("navy")}" stroke-width="6"/>`;
  for (let i = 0; i < 6; i++) {
    const x = 270 + i * 145;
    s += tube(x, 180, 92, "brownL");
    s += `<line x1="${x}" y1="245" x2="${x}" y2="300" stroke="${c("line")}" stroke-width="4"/>`;
    s += `<rect x="${x - 46}" y="305" width="92" height="${30 + (i % 3) * 22}" rx="6" fill="${c(["teal", "coral", "violet"][i % 3])}" opacity="0.8"/>`;
  }
  s += txt(605, 420, 26, "viral diversity measured at each point", "slate");
  s += txt(605, 100, 28, "one screening interval", "teal", "middle", "bold");
  s += `<path d="M270 138 L 270 118 L 995 118 L 995 138" fill="none" stroke="${c("teal")}" stroke-width="5"/>`;
  return wrap(W, H, s);
}

// Slide 9: six candidate aptamers.
function sixAptamers() {
  const W = 1250, H = 330;
  let s = "";
  const cols = ["teal", "navy", "violet", "coral", "teal", "violet"];
  for (let i = 0; i < 6; i++) {
    const x = 105 + i * 208;
    s += `<rect x="${x - 88}" y="20" width="176" height="230" rx="22" fill="${c("mist")}"/>`;
    s += aptamer(x, 150, 100, cols[i], i % 4);
    s += txt(x, 290, 28, `Apt-${i + 1}`, "navy", "middle", "bold");
  }
  return wrap(W, H, s);
}

// Slide 10: three target models.
function targetModels() {
  const W = 1150, H = 420;
  const panels = [
    ["Virus-like particle", "capsid, no genome", (x) => noro(x, 175, 92, { fill: "coralL" })],
    ["Recombinant capsid protein", "the binding domain alone", (x) => `<path d="M${x - 70} 175 q 0 -80 70 -72 q 78 -12 72 66 q 12 78 -72 72 q -78 6 -70 -66z" fill="${c("violet")}" opacity="0.35" stroke="${c("violet")}" stroke-width="6"/>`],
    ["Murine norovirus", "a real, infectious virus", (x) => noro(x, 175, 92, { fill: "tealXL" }) + `<g transform="translate(${x + 70} 248)"><ellipse cx="0" cy="0" rx="34" ry="20" fill="${c("slate")}"/><circle cx="-22" cy="-12" r="13" fill="${c("slate")}"/><path d="M26 -6 q 22 -14 30 2" stroke="${c("slate")}" stroke-width="6" fill="none"/></g>`],
  ];
  let s = "";
  panels.forEach(([t, sub, f], i) => {
    const x = 200 + i * 375;
    s += `<rect x="${x - 175}" y="20" width="350" height="300" rx="26" fill="${c("mist")}"/>`;
    s += f(x);
    s += txt(x, 362, 27, t, "navy", "middle", "bold") + txt(x, 396, 23, sub, "slate");
  });
  return wrap(W, H, s);
}

// Slide 11: signal drops in stool - degraded or interfered with?
function degradeVsInterfere() {
  const W = 1150, H = 560;
  let s = `<rect x="330" y="20" width="490" height="120" rx="26" fill="${c("navy")}"/>`;
  s += txt(575, 78, 32, "signal drops in stool", "white", "middle", "bold");
  s += txt(575, 118, 26, "why?", "sun", "middle", "bold");
  s += arrow(470, 150, 300, 215, "slate", 5) + arrow(680, 150, 850, 215, "slate", 5);
  // left: degradation
  s += `<rect x="40" y="225" width="500" height="315" rx="26" fill="${c("coralL")}" fill-opacity="0.35" stroke="${c("coral")}" stroke-width="5"/>`;
  s += txt(290, 275, 30, "Degraded", "coral", "middle", "bold");
  s += `<path d="M110 370 q 30 -40 60 0 q 30 40 60 0" stroke="${c("teal")}" stroke-width="10" fill="none" stroke-linecap="round"/>`;
  s += `<g stroke="${c("navy")}" stroke-width="5"><circle cx="300" cy="400" r="18" fill="${c("coralL")}"/><circle cx="350" cy="400" r="18" fill="${c("coralL")}"/><path d="M312 385 L 355 330 M338 385 L 295 330" stroke-width="11" stroke="${c("slate")}" stroke-linecap="round"/></g>`;
  s += `<path d="M390 370 q 20 -30 45 0" stroke="${c("teal")}" stroke-width="10" fill="none" stroke-linecap="round" stroke-dasharray="14 12"/>`;
  s += txt(290, 475, 25, "nucleases cut the aptamer", "navy") + txt(290, 510, 24, "test: integrity over time", "slate", "middle", "normal", `font-style="italic"`);
  // right: interference
  s += `<rect x="610" y="225" width="500" height="315" rx="26" fill="${c("tealXL")}" fill-opacity="0.5" stroke="${c("teal")}" stroke-width="5"/>`;
  s += txt(860, 275, 30, "Interfered with", "teal", "middle", "bold");
  s += aptamer(790, 395, 95, "teal", 0);
  s += `<ellipse cx="880" cy="380" rx="50" ry="38" fill="${c("brownL")}" stroke="${c("brown")}" stroke-width="5"/>`;
  s += `<ellipse cx="930" cy="425" rx="34" ry="26" fill="${c("sunL")}" stroke="${c("sun")}" stroke-width="5"/>`;
  s += txt(860, 475, 25, "matrix blocks or competes", "navy") + txt(860, 510, 24, "test: spike-in & dilution", "slate", "middle", "normal", `font-style="italic"`);
  return wrap(W, H, s);
}

// Slide 12 / poster: fluorescence polarization principle.
function fpPrinciple() {
  const W = 1150, H = 540;
  const panel = (x, bound) => {
    let s = `<rect x="${x}" y="20" width="540" height="500" rx="26" fill="${c(bound ? "tealXL" : "mist")}"/>`;
    s += txt(x + 270, 70, 30, bound ? "Bound → slow tumbling" : "Free aptamer → fast tumbling", "navy", "middle", "bold");
    s += `<path d="M${x + 30} 270 ${[...Array(8)].map((_, i) => `q 9 ${i % 2 ? 26 : -26} 18 0`).join(" ")}" stroke="${c("sun")}" stroke-width="6" fill="none"/>`;
    s += arrow(x + 175, 270, x + 200, 270, "sun", 6);
    s += txt(x + 100, 220, 20, "polarized light", "slate");
    const cx = x + 300;
    if (bound) {
      s += noro(cx, 280, 62, { fill: "coralL" });
      s += aptamer(cx + 32, 182, 55, "teal", 0, { dye: true, rot: 200 });
      s += `<path d="M${cx - 95} 340 a 110 110 0 0 0 30 40" stroke="${c("slate")}" stroke-width="4" fill="none"/>` + arrow(cx - 70, 372, cx - 58, 382, "slate", 4);
    } else {
      s += aptamer(cx, 270, 80, "teal", 0, { dye: true });
      [0, 1, 2].forEach((i) => (s += `<path d="M${cx - 70 - i * 18} ${300 - i * 8} a ${80 + i * 18} ${80 + i * 18} 0 0 1 ${60} ${-140}" stroke="${c("slate")}" stroke-width="4" fill="none" opacity="${1 - i * 0.3}"/>`));
      s += arrow(cx + 40, 172, cx + 70, 182, "slate", 4);
    }
    const ex = x + 420;
    if (bound) s += `<path d="M${ex} 270 ${[...Array(5)].map((_, i) => `q 9 ${i % 2 ? 22 : -22} 18 0`).join(" ")}" stroke="${c("coral")}" stroke-width="6" fill="none"/>`;
    else ["-25", "0", "25"].forEach((d, i) => (s += `<g transform="rotate(${d} ${ex} 270)"><path d="M${ex} 270 ${[...Array(5)].map((_, j) => `q 9 ${(j + i) % 2 ? 14 : -14} 18 0`).join(" ")}" stroke="${c("coral")}" stroke-width="4" fill="none" opacity="0.8"/></g>`));
    s += txt(x + 270, 465, 28, bound ? "polarization HIGH" : "polarization LOW", bound ? "teal" : "coral", "middle", "bold");
    return s;
  };
  return wrap(W, H, panel(10, false) + panel(600, true));
}

// Slide 13: lateral flow strip.
function lfaStrip() {
  const W = 1200, H = 420;
  let s = "";
  const y = 170, h = 90;
  s += `<rect x="40" y="${y}" width="200" height="${h}" rx="10" fill="${c("brownL")}"/>` + txt(140, y - 25, 24, "sample pad", "navy", "middle", "bold");
  s += `<rect x="220" y="${y + 5}" width="170" height="${h - 10}" rx="6" fill="${c("coralL")}"/>` + txt(305, y - 25, 24, "conjugate pad", "navy", "middle", "bold");
  for (let i = 0; i < 9; i++) s += `<circle cx="${245 + (i % 5) * 30}" cy="${y + 25 + Math.floor(i / 5) * 40}" r="10" fill="#B03A2E"/>`;
  s += `<rect x="370" y="${y + 10}" width="580" height="${h - 20}" fill="#fff" stroke="${c("line")}" stroke-width="4"/>` + txt(660, y - 25, 24, "nitrocellulose membrane", "navy", "middle", "bold");
  s += `<rect x="600" y="${y + 10}" width="22" height="${h - 20}" fill="#B03A2E"/>` + txt(611, y + h + 45, 22, "test line", "coral", "middle", "bold");
  s += `<rect x="780" y="${y + 10}" width="22" height="${h - 20}" fill="#B03A2E"/>` + txt(791, y + h + 45, 22, "control line", "slate", "middle", "bold");
  s += `<rect x="930" y="${y}" width="230" height="${h}" rx="10" fill="${c("slate")}" opacity="0.8"/>` + txt(1045, y - 25, 24, "absorbent pad", "navy", "middle", "bold");
  s += arrow(80, 360, 1120, 360, "teal", 6) + txt(600, 405, 22, "capillary flow · read by eye", "teal", "middle", "bold");
  s += txt(305, y + h + 45, 20, "gold–aptamer", "slate") + txt(305, y + h + 70, 20, "conjugate", "slate");
  return wrap(W, H, s);
}

// ---------- POSTER (cartoon) ----------
// Banner: six aptamers from six labs, each holding an incomparable number.
function posterBanner() {
  const W = 1800, H = 420;
  const cols = ["teal", "navy", "violet", "coral", "teal", "violet"];
  const labs = ["lab A", "lab B", "lab C", "lab D", "lab E", "lab F"];
  const moods = ["grin", "smile", "worried", "sleep", "smile", "grin"];
  let s = "";
  for (let i = 0; i < 6; i++) {
    const x = 160 + i * 296, y = 175;
    s += aptamer(x, y, 118, cols[i], i % 4, { face: moods[i] });
    s += `<rect x="${x - 72}" y="${y + 66}" width="144" height="52" rx="15" fill="#fff" stroke="${c(cols[i])}" stroke-width="5"/>`;
    s += txt(x, y + 101, 28, "Kd = ?", cols[i], "middle", "bold");
    s += txt(x, y + 150, 25, labs[i], "slate");
    s += txt(x, y - 108, 40, "?", "sun", "middle", "bold");
  }
  return wrap(W, H, s);
}

// Panel 2: folding pulls like charges together; the ion atmosphere screens them.
function ionAtmosphere() {
  const W = 1150, H = 620;
  let s = "";
  // unfolded
  s += `<rect x="20" y="20" width="520" height="580" rx="30" fill="${c("mist")}"/>`;
  s += txt(280, 78, 34, "Unfolded: charges far apart", "navy", "middle", "bold");
  s += ionCloud(280, 330, 215, 190, 42, 5, "coral", 20);
  const path = "M90 520 C 150 420, 230 470, 250 370 S 360 300, 340 200 S 430 150, 470 120";
  s += `<path d="${path}" stroke="${c("teal")}" stroke-width="18" fill="none" stroke-linecap="round"/>`;
  [[110, 495], [205, 420], [262, 320], [333, 240], [410, 160]].forEach(([x, y]) => (s += minus(x, y, 30, "teal")));
  s += txt(280, 580, 28, "thin ion atmosphere", "slate");
  // folded
  s += `<rect x="610" y="20" width="520" height="580" rx="30" fill="${c("tealXL")}"/>`;
  s += txt(870, 78, 34, "Folded: charges crowded", "navy", "middle", "bold");
  s += ionCloud(870, 330, 190, 175, 95, 9, "coral", 20);
  s += aptamer(870, 350, 185, "teal", 0);
  [[812, 430], [928, 430], [870, 220], [820, 300], [920, 300]].forEach(([x, y]) => (s += minus(x, y, 30, "teal")));
  s += txt(870, 580, 28, "denser ion atmosphere", "teal", "middle", "bold");
  // the key caption between
  s += txt(575, 330, 46, "→", "navy", "middle", "bold");
  return wrap(W, H, s);
}

// Panel 3 centrepiece: non-monotonic affinity vs salt, with the two effects beneath.
function saltCurve() {
  const W = 1250, H = 760;
  const x0 = 150, x1 = 1180, yTop = 90, yBot = 430;
  const X = (t) => x0 + t * (x1 - x0);
  const pt = (t, v) => `${X(t)},${yBot - v * (yBot - yTop)}`;
  let s = "";
  // axes
  s += `<line x1="${x0}" y1="${yBot}" x2="${x1}" y2="${yBot}" stroke="${c("navy")}" stroke-width="6"/>`;
  s += `<line x1="${x0}" y1="${yBot}" x2="${x0}" y2="${yTop - 20}" stroke="${c("navy")}" stroke-width="6"/>`;
  s += txt(665, 495, 30, "ionic strength  →", "navy", "middle", "bold");
  s += `<g transform="rotate(-90 58 ${(yTop + yBot) / 2})">${txt(58, (yTop + yBot) / 2, 30, "affinity (1/Kd)", "navy", "middle", "bold")}</g>`;
  // the non-monotonic curve
  const pts = [[0, 0.18], [0.1, 0.4], [0.2, 0.63], [0.3, 0.8], [0.4, 0.9], [0.5, 0.93], [0.6, 0.88], [0.7, 0.74], [0.8, 0.55], [0.9, 0.36], [1, 0.2]];
  s += `<polyline points="${pts.map(([t, v]) => pt(t, v)).join(" ")}" fill="none" stroke="${c("coral")}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>`;
  // the window
  s += `<rect x="${X(0.38)}" y="${yTop - 20}" width="${X(0.62) - X(0.38)}" height="${yBot - yTop + 20}" fill="${c("sunL")}" opacity="0.55"/>`;
  s += txt(X(0.5), yTop + 10, 30, "usable window", "navy", "middle", "bold");
  s += txt(X(0.5), yTop - 42, 26, "folded enough, interface still strong", "slate");
  // end annotations
  s += txt(X(0.06), yBot - 60, 25, "too little", "slate", "start") + txt(X(0.06), yBot - 30, 25, "folding", "slate", "start");
  s += txt(X(0.94), yBot - 60, 25, "interface", "slate", "end") + txt(X(0.94), yBot - 30, 25, "screened out", "slate", "end");
  // two opposing effects as bars beneath
  const bar = (y, label, col, dir, sub) => {
    let g = `<rect x="${x0}" y="${y}" width="${x1 - x0}" height="54" rx="27" fill="${c("mist")}"/>`;
    const grad = dir > 0
      ? `<linearGradient id="g${y}" x1="0" x2="1"><stop offset="0" stop-color="${c(col)}" stop-opacity="0.15"/><stop offset="1" stop-color="${c(col)}" stop-opacity="1"/></linearGradient>`
      : `<linearGradient id="g${y}" x1="0" x2="1"><stop offset="0" stop-color="${c(col)}" stop-opacity="1"/><stop offset="1" stop-color="${c(col)}" stop-opacity="0.15"/></linearGradient>`;
    g = `<defs>${grad}</defs>` + g + `<rect x="${x0}" y="${y}" width="${x1 - x0}" height="54" rx="27" fill="url(#g${y})"/>`;
    g += txt(x0 + 24, y + 36, 28, label, "navy", "start", "bold");
    g += txt(x1 - 24, y + 36, 26, sub, "navy", "end");
    return g;
  };
  s += bar(560, "Folding: ions screen the repulsion", "teal", 1, "better with more salt →");
  s += bar(650, "Interface: ions screen the attraction", "violet", -1, "← worse with more salt");
  return wrap(W, H, s);
}

// Panel 4: counterion release on binding.
function counterionRelease() {
  const W = 1150, H = 520;
  let s = "";
  // before
  s += `<rect x="20" y="20" width="480" height="480" rx="30" fill="${c("mist")}"/>`;
  s += txt(260, 72, 32, "Before binding", "navy", "middle", "bold");
  s += ionCloud(170, 300, 90, 120, 34, 3, "coral", 18);
  s += aptamer(170, 310, 120, "teal", 0);
  s += noro(380, 300, 78, { fill: "coralL", patch: true });
  s += ionCloud(392, 268, 56, 48, 16, 17, "teal", 18);
  s += txt(260, 470, 25, "ions crowd each partner", "slate");
  // arrow
  s += arrow(520, 260, 620, 260, "navy", 7);
  // after
  s += `<rect x="650" y="20" width="480" height="480" rx="30" fill="${c("tealXL")}"/>`;
  s += txt(890, 72, 32, "After binding", "navy", "middle", "bold");
  s += noro(900, 300, 82, { fill: "coralL", patch: true });
  s += aptamer(905, 180, 95, "teal", 0, { rot: 190 });
  // released ions flying outward
  const r = rng(23);
  for (let i = 0; i < 16; i++) {
    const a = r() * Math.PI * 2, d = 150 + r() * 90;
    const x = 900 + Math.cos(a) * d, y = 300 + Math.sin(a) * d * 0.72;
    s += `<g opacity="0.9"><line x1="${x - 11}" y1="${y}" x2="${x + 11}" y2="${y}" stroke="${c("coral")}" stroke-width="6" stroke-linecap="round"/><line x1="${x}" y1="${y - 11}" x2="${x}" y2="${y + 11}" stroke="${c("coral")}" stroke-width="6" stroke-linecap="round"/></g>`;
    s += arrow(900 + Math.cos(a) * (d - 60), 300 + Math.sin(a) * (d - 60) * 0.72, x - Math.cos(a) * 20, y - Math.sin(a) * 0.72 * 20, "coralL", 3);
  }
  s += txt(890, 470, 25, "released ions gain freedom → entropy", "teal", "middle", "bold");
  return wrap(W, H, s);
}

// Panel 5: ion identity matters, not just concentration.
function ionIdentity() {
  const W = 1250, H = 450;
  const cards = [
    ["K⁺", "violet", "sits in the G-quadruplex channel — a structural role, not just screening", (x, y) => {
      let g = "";
      for (let i = 0; i < 3; i++) g += `<rect x="${x - 60}" y="${y - 60 + i * 44}" width="120" height="30" rx="6" fill="none" stroke="${c("violet")}" stroke-width="7" transform="skewX(-14)"/>`;
      g += `<circle cx="${x}" cy="${y - 22}" r="17" fill="${c("sun")}" stroke="${c("navy")}" stroke-width="4"/><circle cx="${x}" cy="${y + 22}" r="17" fill="${c("sun")}" stroke="${c("navy")}" stroke-width="4"/>`;
      return g;
    }],
    ["Mg²⁺", "coral", "strongly shapes nucleic-acid structure and competes with monovalent ions", (x, y) => {
      let g = `<circle cx="${x}" cy="${y}" r="42" fill="${c("coral")}" stroke="${c("navy")}" stroke-width="5"/>${txt(x, y + 12, 30, "2+", "white", "middle", "bold")}`;
      g += `<circle cx="${x - 78}" cy="${y + 18}" r="25" fill="${c("sunL")}" stroke="${c("navy")}" stroke-width="4"/>${txt(x - 78, y + 27, 22, "+", "navy", "middle", "bold")}`;
      g += `<circle cx="${x + 78}" cy="${y + 18}" r="25" fill="${c("sunL")}" stroke="${c("navy")}" stroke-width="4"/>${txt(x + 78, y + 27, 22, "+", "navy", "middle", "bold")}`;
      g += arrow(x - 50, y + 10, x - 78 + 30, y + 14, "slate", 4) + arrow(x + 50, y + 10, x + 78 - 30, y + 14, "slate", 4);
      return g;
    }],
    ["Cl⁻ vs glutamate⁻", "teal", "anions are not interchangeable either — swapping them shifts affinity", (x, y) => {
      let g = `<circle cx="${x - 55}" cy="${y}" r="34" fill="${c("tealXL")}" stroke="${c("teal")}" stroke-width="5"/>${minus(x - 55, y, 30, "teal")}`;
      g += txt(x, y + 10, 30, "vs", "slate", "middle", "bold");
      g += `<path d="M${x + 30} ${y - 26} l 22 16 l -10 22 l 26 10" stroke="${c("teal")}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>${minus(x + 95, y - 20, 26, "teal")}`;
      return g;
    }],
  ];
  let s = "";
  cards.forEach(([t, col, d, f], i) => {
    const x = 210 + i * 415;
    s += `<rect x="${x - 190}" y="20" width="380" height="410" rx="28" fill="#fff" stroke="${c(col)}" stroke-width="6"/>`;
    s += txt(x, 78, 38, t, col, "middle", "bold");
    s += f(x, 195);
    const words = d.split(" "); let line = "", lines = [];
    words.forEach((w) => { if ((line + w).length > 30) { lines.push(line); line = w + " "; } else line += w + " "; });
    lines.push(line);
    lines.forEach((l, j) => (s += txt(x, 320 + j * 33, 24, l.trim(), "navy")));
  });
  return wrap(W, H, s);
}

// Panel 6: specificity - background at low salt, lost recognition at high salt.
function specificityWindow() {
  const W = 1150, H = 520;
  const col = (x, w, title, body, fill, stroke, fig) => {
    let g = `<rect x="${x}" y="20" width="${w}" height="480" rx="26" fill="${c(fill)}" fill-opacity="0.4" stroke="${c(stroke)}" stroke-width="6"/>`;
    g += txt(x + w / 2, 76, 32, title, stroke === "sun" ? "navy" : stroke, "middle", "bold");
    g += fig(x + w / 2);
    body.forEach((l, i) => (g += txt(x + w / 2, 390 + i * 34, 24, l, "navy")));
    return g;
  };
  let s = col(20, 350, "Low salt", ["random DNA sticks to", "positive patches —", "background mimics binding"], "coralL", "coral",
    (cx) => noro(cx, 230, 62, { fill: "coralL", patch: true }) + aptamer(cx - 108, 220, 70, "slate", 2) + aptamer(cx + 108, 220, 70, "slate", 3));
  s += col(400, 350, "Right window", ["real recognition stands", "out above background"], "sunL", "sun",
    (cx) => noro(cx, 255, 66, { fill: "coralL", patch: true }) + aptamer(cx + 28, 155, 64, "teal", 0, { rot: 190 }));
  s += col(780, 350, "High salt", ["background is suppressed —", "but real binding may be", "weakened too"], "tealXL", "teal",
    (cx) => noro(cx, 240, 64, { fill: "coralL", patch: true }) + aptamer(cx - 92, 170, 60, "teal", 0, { rot: -28 }) + arrow(cx - 60, 210, cx - 100, 240, "slate", 4));
  return wrap(W, H, s);
}

// Poster closing: FP + CD together.
function fpPlusCd() {
  const W = 1000, H = 420;
  let s = `<rect x="20" y="20" width="460" height="380" rx="28" fill="${c("tealXL")}"/>`;
  s += txt(250, 80, 34, "Fluorescence polarization", "teal", "middle", "bold");
  s += aptamer(160, 240, 110, "teal", 0, { dye: true });
  s += arrow(255, 230, 310, 230, "slate", 5);
  s += noro(395, 240, 68, { fill: "coralL" });
  s += txt(250, 370, 26, "did binding change?", "navy", "middle", "bold");
  s += `<rect x="520" y="20" width="460" height="380" rx="28" fill="${c("mist")}"/>`;
  s += txt(750, 80, 34, "Circular dichroism", "violet", "middle", "bold");
  s += `<path d="M600 300 C 640 180, 700 180, 730 240 C 760 300, 820 300, 880 200" stroke="${c("violet")}" stroke-width="9" fill="none"/>`;
  s += `<line x1="590" y1="250" x2="900" y2="250" stroke="${c("line")}" stroke-width="4"/>`;
  s += txt(750, 370, 26, "did the fold change?", "navy", "middle", "bold");
  return wrap(W, H, s);
}

module.exports = {
  P, toPng,
  donationChain, activeIngredient, screeningGap, triageFunnel, norovirusFacts,
  wp1Sampling, sixAptamers, targetModels, degradeVsInterfere, fpPrinciple, lfaStrip,
  posterBanner, ionAtmosphere, saltCurve, counterionRelease, ionIdentity, specificityWindow, fpPlusCd,
  _prim: { virus, noro, aptamer, tube, bacterium, faceAt, person, ionCloud },
};
