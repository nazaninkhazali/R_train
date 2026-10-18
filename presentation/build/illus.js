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

// ---------- TALK (clean scientific) ----------
function hookCrowd() {
  const W = 800, H = 700, r = rng(7);
  let bg = "";
  for (let i = 0; i < 70; i++) bg += bacterium(40 + r() * 720, 40 + r() * 620, 30 + r() * 30, r() * 180, "mist", "line");
  for (let i = 0; i < 90; i++) bg += `<circle cx="${r() * W}" cy="${r() * H}" r="${3 + r() * 9}" fill="${c("brownL")}" opacity="${0.35 + r() * 0.4}"/>`;
  let lens = "";
  const r2 = rng(3);
  for (let i = 0; i < 24; i++) lens += bacterium(250 + r2() * 300, 200 + r2() * 300, 40 + r2() * 25, r2() * 180, "tealXL", "tealL");
  for (let i = 0; i < 40; i++) lens += `<circle cx="${230 + r2() * 340}" cy="${180 + r2() * 340}" r="${4 + r2() * 9}" fill="${c("brownL")}"/>`;
  lens += virus(345, 300, 22) + virus(470, 400, 18) + virus(380, 450, 15);
  return wrap(W, H, `<defs><clipPath id="cl"><circle cx="400" cy="350" r="190"/></clipPath></defs>${bg}
  <circle cx="400" cy="350" r="190" fill="#fff"/><g clip-path="url(#cl)">${lens}</g>
  <circle cx="400" cy="350" r="190" fill="none" stroke="${c("navy")}" stroke-width="18"/>
  <line x1="535" y1="485" x2="660" y2="610" stroke="${c("navy")}" stroke-width="34" stroke-linecap="round"/>`);
}

function recapTimeline() {
  const W = 1220, H = 420;
  const row = (y, label, steps, total, col, sub) => {
    let s = txt(20, y - 50, 30, label, col, "start", "bold");
    s += `<rect x="20" y="${y - 12}" width="1000" height="24" rx="12" fill="${c("mist")}"/>`;
    let x = 20;
    steps.forEach(([w, name, fill]) => {
      s += `<rect x="${x}" y="${y - 12}" width="${w}" height="24" rx="12" fill="${c(fill)}"/>`;
      s += txt(x + w / 2, y + 48, 22, name, "slate");
      x += w;
    });
    s += txt(1040, y + 12, 36, total, col, "start", "bold");
    if (sub) s += txt(20, y + 85, 20, sub, "slate", "start", "normal", `font-style="italic"`);
    return s;
  };
  return wrap(W, H, row(110, "Today: central-lab PCR panel", [[160, "sample", "slate"], [520, "transport + lab + report", "coralL"], [180, "release", "slate"]], "days", "coral", "a snapshot: the result describes the sample, not the next donation") +
    row(310, "Goal: rapid test at donation", [[160, "sample", "teal"], [70, "", "tealL"]], "~15 min", "teal", ""));
}

function antibodyVsAptamer() {
  const W = 900, H = 420;
  const card = (x, title, fig, lines, col) => {
    let s = `<rect x="${x}" y="10" width="420" height="400" rx="24" fill="${c(col === "violet" ? "mist" : "tealXL")}"/>`;
    s += txt(x + 210, 62, 34, title, col, "middle", "bold") + fig;
    lines.forEach((l, i) => (s += txt(x + 40, 290 + i * 34, 23, l, "navy", "start")));
    return s;
  };
  return wrap(W, H, card(10, "Antibody", antibody(220, 175, 120), ["• protein, made in animals/cells", "• batch-to-batch variation", "• heat-sensitive"], "violet") +
    card(470, "Aptamer", aptamer(680, 185, 110, "teal", 0), ["• short DNA/RNA, made chemically", "• identical every batch, cheap", "• stable, easy to label & tune"], "teal"));
}

function wp1Calendar() {
  const W = 1000, H = 520, donors = ["Donor A", "Donor B", "Donor C", "Donor D"], tp = 6;
  let s = "";
  for (let j = 0; j < tp; j++) s += txt(240 + j * 125, 40, 24, `t${j + 1}`, "slate", "middle", "bold");
  s += arrow(180, 490, 960, 490, "slate", 4) + txt(960, 480, 22, "time (weeks / months)", "slate", "end");
  donors.forEach((d, i) => {
    const y = 110 + i * 95;
    s += `<circle cx="40" cy="${y}" r="24" fill="${c("teal")}"/><circle cx="40" cy="${y - 8}" r="8" fill="#fff"/><path d="M26 ${y + 14} q 14 -18 28 0" fill="#fff"/>`;
    s += txt(75, y + 8, 24, d, "navy", "start");
    for (let j = 0; j < tp; j++) s += tube(240 + j * 125, y - 5, 70, "brownL");
  });
  return wrap(W, H, s);
}

function wp1Hypothesis() {
  const W = 1000, H = 420;
  const states = [0, 1, 1, 0, 0, 1, 0, 0];
  let s = txt(20, 40, 26, "Hypothetical example — one donor, repeated sampling", "slate", "start", "normal", `font-style="italic"`);
  s += `<line x1="60" y1="250" x2="960" y2="250" stroke="${c("line")}" stroke-width="6" stroke-dasharray="14 10"/>`;
  states.forEach((v, i) => {
    const x = 90 + i * 118;
    s += `<circle cx="${x}" cy="250" r="44" fill="${v ? c("coralL") : c("tealXL")}" stroke="${v ? c("coral") : c("teal")}" stroke-width="4"/>`;
    s += v ? virus(x, 250, 18) : `<path d="M${x - 16} 252 l 11 12 l 22 -26" stroke="${c("teal")}" stroke-width="7" fill="none" stroke-linecap="round"/>`;
    s += txt(x, 330, 22, `wk ${i * 2}`, "slate");
    s += txt(x, 180, 20, v ? "virus +" : "negative", v ? "coral" : "teal", "middle", "bold");
  });
  s += `<rect x="60" y="370" width="22" height="22" rx="4" fill="${c("tealXL")}" stroke="${c("teal")}" stroke-width="3"/>` + txt(95, 389, 20, "screening negative", "slate", "start");
  s += `<rect x="330" y="370" width="22" height="22" rx="4" fill="${c("coralL")}" stroke="${c("coral")}" stroke-width="3"/>` + txt(365, 389, 20, "enteric virus detected", "slate", "start");
  return wrap(W, H, s);
}

function aptamerLineup() {
  const W = 1000, H = 440;
  let s = "";
  ["A", "B", "C", "D"].forEach((n, i) => {
    const x = 90 + i * 150;
    s += `<rect x="${x - 65}" y="20" width="130" height="300" rx="20" fill="${c("mist")}"/>`;
    s += aptamer(x, 175, 115, ["teal", "navy", "violet", "coral"][i], i);
    s += txt(x, 300, 26, `Apt-${n}`, "navy", "middle", "bold");
  });
  s += txt(330, 390, 24, "same target · different sequences, folds and origins", "slate", "middle", "normal", `font-style="italic"`);
  // buffer vs stool
  s += tube(760, 170, 150, "tealXL") + txt(760, 300, 26, "buffer", "teal", "middle", "bold");
  s += tube(910, 170, 150, "brown") + txt(910, 300, 26, "stool", "brown", "middle", "bold");
  s += txt(835, 160, 34, "vs", "slate", "middle", "bold");
  return wrap(W, H, s);
}

// Microplate well cross-section with an aptamer-based sandwich.
function elisaWell(problems = false) {
  const W = 900, H = 560;
  let s = `<path d="M80 60 L80 430 Q80 500 150 500 L750 500 Q820 500 820 430 L820 60" fill="${c("mist")}" stroke="${c("slate")}" stroke-width="10"/>`;
  s += `<rect x="90" y="420" width="720" height="70" fill="${c("tealXL")}" opacity="0.5"/>`;
  s += `<line x1="90" y1="490" x2="810" y2="490" stroke="${c("navy")}" stroke-width="8"/>`;
  // coated target protein blobs
  for (let i = 0; i < 6; i++) {
    const x = 160 + i * 115;
    s += `<ellipse cx="${x}" cy="462" rx="42" ry="26" fill="${c("coral")}" stroke="${c("navy")}" stroke-width="3"/>`;
    if (i % 2 === 0 || !problems) {
      s += aptamer(x, 362, 70, "teal", 0, { rot: 180 });
      s += `<circle cx="${x}" cy="300" r="10" fill="${c("navy")}"/>`; // biotin
      s += `<rect x="${x - 24}" y="248" width="48" height="40" rx="10" fill="${c("sun")}" stroke="${c("navy")}" stroke-width="3"/>`;
      s += txt(x, 275, 18, "HRP", "navy", "middle", "bold");
      s += `<path d="M${x} 240 q -10 -30 0 -60 q 10 -30 0 -60" stroke="${c("teal")}" stroke-width="4" fill="none" stroke-dasharray="6 6"/>`;
    }
  }
  s += `<rect x="90" y="60" width="720" height="70" fill="${c("teal")}" opacity="${problems ? 0.15 : 0.35}"/>`;
  s += txt(450, 108, 26, problems ? "weak / patchy colour" : "TMB → blue colour", "navy", "middle", "bold");
  return wrap(W, H, s);
}

function fpPrinciple() {
  const W = 1150, H = 540;
  const panel = (x, bound) => {
    let s = `<rect x="${x}" y="20" width="540" height="500" rx="26" fill="${c(bound ? "tealXL" : "mist")}"/>`;
    s += txt(x + 270, 70, 30, bound ? "Bound to virus → slow tumbling" : "Free aptamer → fast tumbling", "navy", "middle", "bold");
    // polarized light in
    s += `<path d="M${x + 30} 270 ${[...Array(8)].map((_, i) => `q 9 ${i % 2 ? 26 : -26} 18 0`).join(" ")}" stroke="${c("sun")}" stroke-width="6" fill="none"/>`;
    s += arrow(x + 175, 270, x + 200, 270, "sun", 6);
    s += txt(x + 100, 220, 20, "polarized light", "slate");
    const cx = x + 300;
    if (bound) {
      s += virus(cx, 270, 62, "coralL", "navy");
      s += aptamer(cx + 32, 172, 55, "teal", 0, { dye: true, rot: 200 });
      s += `<path d="M${cx - 95} 330 a 110 110 0 0 0 30 40" stroke="${c("slate")}" stroke-width="4" fill="none"/>` + arrow(cx - 70, 362, cx - 58, 372, "slate", 4);
    } else {
      s += aptamer(cx, 270, 80, "teal", 0, { dye: true });
      [0, 1, 2].forEach((i) => (s += `<path d="M${cx - 70 - i * 18} ${300 - i * 8} a ${80 + i * 18} ${80 + i * 18} 0 0 1 ${60} ${-140}" stroke="${c("slate")}" stroke-width="4" fill="none" opacity="${1 - i * 0.3}"/>`));
      s += arrow(cx + 40, 172, cx + 70, 182, "slate", 4);
    }
    // emitted light
    const ex = x + 420;
    if (bound) s += `<path d="M${ex} 270 ${[...Array(5)].map((_, i) => `q 9 ${i % 2 ? 22 : -22} 18 0`).join(" ")}" stroke="${c("coral")}" stroke-width="6" fill="none"/>`;
    else ["-25", "0", "25"].forEach((d, i) => (s += `<g transform="rotate(${d} ${ex} 270)"><path d="M${ex} 270 ${[...Array(5)].map((_, j) => `q 9 ${(j + i) % 2 ? 14 : -14} 18 0`).join(" ")}" stroke="${c("coral")}" stroke-width="4" fill="none" opacity="0.8"/></g>`));
    s += txt(x + 270, 460, 28, bound ? "light stays polarized → HIGH mP" : "light scrambled → LOW mP", bound ? "teal" : "coral", "middle", "bold");
    return s;
  };
  return wrap(W, H, panel(10, false) + panel(600, true));
}

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
  s += arrow(80, 360, 1120, 360, "teal", 6) + txt(600, 405, 22, "capillary flow · ~15 min · read by eye", "teal", "middle", "bold");
  s += txt(305, y + h + 45, 20, "gold–aptamer", "slate") + txt(305, y + h + 70, 20, "conjugate", "slate");
  return wrap(W, H, s);
}

// ---------- POSTER (cartoon) ----------
function posterBanner() {
  const W = 1600, H = 520;
  let s = "";
  // podium
  const pod = [[620, 230, "1", "sun"], [330, 320, "2", "tealL"], [910, 370, "3", "coralL"]];
  pod.forEach(([x, top, n, col]) => {
    s += `<rect x="${x}" y="${top}" width="260" height="${520 - top}" rx="12" fill="${c(col)}" stroke="${c("navy")}" stroke-width="6"/>`;
    s += txt(x + 130, top + 95, 90, n, "navy", "middle", "bold");
  });
  s += aptamer(750, 140, 150, "teal", 0, { face: "grin" });
  s += aptamer(460, 235, 140, "navy", 1, { face: "worried" });
  s += aptamer(1040, 280, 140, "violet", 2, { face: "smile" });
  s += aptamer(1330, 400, 140, "coral", 3, { face: "sleep" }) + txt(1330, 500, 34, "zzz… wrong buffer", "slate", "middle", "bold", `font-style="italic"`);
  // question marks
  s += txt(750, 40, 70, "?", "coral", "middle", "bold") + txt(160, 200, 120, "?", "sun", "middle", "bold");
  // salt shaker
  s += `<g transform="translate(160 330)"><rect x="-55" y="-40" width="110" height="160" rx="30" fill="#fff" stroke="${c("navy")}" stroke-width="6"/><path d="M-45 -40 q 45 -70 90 0 z" fill="${c("slate")}"/>${txt(0, 60, 40, "NaCl", "navy", "middle", "bold")}<circle cx="-20" cy="-80" r="5" fill="${c("slate")}"/><circle cx="5" cy="-110" r="5" fill="${c("slate")}"/><circle cx="25" cy="-90" r="5" fill="${c("slate")}"/></g>`;
  return wrap(W, H, s);
}

function shapeShifter() {
  const W = 1000, H = 560;
  let s = "";
  s += `<rect x="20" y="20" width="440" height="480" rx="30" fill="${c("tealXL")}"/><rect x="540" y="20" width="440" height="480" rx="30" fill="${c("mist")}"/>`;
  s += aptamer(240, 290, 210, "teal", 0, { face: "grin" });
  const ions = [[90, 120, "Mg²⁺", "violet"], [380, 140, "K⁺", "coral"], [100, 400, "Na⁺", "sun"], [390, 420, "Mg²⁺", "violet"]];
  ions.forEach(([x, y, l, col]) => (s += `<circle cx="${x}" cy="${y}" r="38" fill="${c(col)}" stroke="${c("navy")}" stroke-width="4"/>${faceAt(x, y + 8, 22, "smile")}${txt(x, y - 46, 26, l, "navy", "middle", "bold")}`));
  s += txt(240, 540, 30, "right ions → folded & ready", "teal", "middle", "bold");
  // unfolded floppy strand
  s += `<path d="M640 430 C 600 330, 760 360, 700 260 S 860 200, 780 120 S 900 90, 900 70" stroke="${c("teal")}" stroke-width="16" fill="none" stroke-linecap="round"/>`;
  s += `<circle cx="900" cy="70" r="32" fill="${c("teal")}"/>` + faceAt(900, 74, 26, "sleep");
  s += txt(840, 260, 40, "z", "slate", "middle", "bold") + txt(870, 220, 52, "z", "slate", "middle", "bold");
  s += txt(760, 540, 30, "no Mg²⁺ / wrong pH → floppy", "coral", "middle", "bold");
  return wrap(W, H, s);
}

function applesOranges() {
  const W = 1000, H = 520;
  let s = `<polygon points="500,470 450,510 550,510" fill="${c("navy")}"/><rect x="490" y="160" width="20" height="320" fill="${c("navy")}"/>`;
  s += `<g transform="rotate(-8 500 170)"><rect x="110" y="160" width="780" height="16" rx="8" fill="${c("navy")}"/>`;
  s += `<path d="M130 176 L 200 300 L 360 300 L 430 176" fill="none" stroke="${c("slate")}" stroke-width="5"/><path d="M570 176 L 640 300 L 800 300 L 870 176" fill="none" stroke="${c("slate")}" stroke-width="5"/>`;
  s += `<ellipse cx="280" cy="300" rx="110" ry="18" fill="${c("slate")}"/><ellipse cx="720" cy="300" rx="110" ry="18" fill="${c("slate")}"/>`;
  s += aptamer(280, 210, 110, "navy", 1, { face: "smile" }) + aptamer(720, 210, 110, "violet", 2, { face: "worried" }) + `</g>`;
  const tag = (x, y, lines, col) => `<rect x="${x}" y="${y}" width="330" height="${lines.length * 38 + 20}" rx="16" fill="#fff" stroke="${c(col)}" stroke-width="4"/>` + lines.map((l, i) => txt(x + 20, y + 44 + i * 38, 26, l, "navy", "start")).join("");
  s += tag(40, 340, ["SELEX buffer: K⁺ / 37 °C", "label: 5′-FAM", "Kd by SPR"], "navy");
  s += tag(630, 300, ["SELEX buffer: PBS, Mg²⁺", "label: 3′-biotin", "Kd by ELISA"], "violet");
  return wrap(W, H, s);
}

function villains() {
  const W = 1500, H = 560;
  const cards = [
    ["Salt Swing", "sun", (x, y) => `<rect x="${x - 50}" y="${y - 50}" width="100" height="100" rx="14" fill="${c("sunL")}" stroke="${c("navy")}" stroke-width="5" transform="rotate(12 ${x} ${y})"/>${faceAt(x, y + 5, 40, "angry")}`],
    ["Bile Bubbles", "green", (x, y) => `<circle cx="${x - 25}" cy="${y + 15}" r="45" fill="#BFE0A8" stroke="${c("navy")}" stroke-width="5"/><circle cx="${x + 35}" cy="${y - 25}" r="30" fill="#BFE0A8" stroke="${c("navy")}" stroke-width="5"/>${faceAt(x - 25, y + 20, 32, "angry")}`],
    ["Nuclease Scissors", "coral", (x, y) => `<g stroke="${c("navy")}" stroke-width="5"><circle cx="${x - 30}" cy="${y + 40}" r="22" fill="${c("coralL")}"/><circle cx="${x + 30}" cy="${y + 40}" r="22" fill="${c("coralL")}"/><path d="M${x - 15} ${y + 22} L ${x + 35} ${y - 60} M${x + 15} ${y + 22} L ${x - 35} ${y - 60}" stroke-width="12" stroke-linecap="round" stroke="${c("slate")}"/></g>${faceAt(x, y - 5, 22, "angry")}`],
    ["Sticky Proteins", "violet", (x, y) => `<path d="M${x - 55} ${y} q 0 -60 55 -55 q 60 -10 55 50 q 10 60 -55 55 q -60 5 -55 -50z" fill="#D7CBEA" stroke="${c("navy")}" stroke-width="5"/><path d="M${x - 40} ${y + 50} q -5 25 5 35 M${x + 20} ${y + 55} q 0 25 -8 35" stroke="#D7CBEA" stroke-width="10" stroke-linecap="round"/>${faceAt(x, y, 38, "grin")}`],
    ["Brown Quenchers", "brown", (x, y) => `<path d="M${x - 60} ${y + 45} q -10 -60 30 -70 q 10 -40 50 -20 q 50 0 40 50 q 15 40 -20 40 z" fill="${c("brown")}" stroke="${c("navy")}" stroke-width="5"/>${faceAt(x, y + 5, 36, "angry")}`],
    ["Bacteria Crowd", "teal", (x, y) => bacterium(x - 30, y - 30, 70, 30, "tealXL", "teal") + bacterium(x + 30, y + 10, 80, -20, "tealXL", "teal") + faceAt(x + 30, y + 12, 18, "grin")],
  ];
  const desc = [
    ["shifts ionic strength", "& Mg²⁺ → changes fold"],
    ["detergent-like bile", "salts disturb binding"],
    ["DNases chew up", "DNA aptamers"],
    ["non-specific binding,", "raise background"],
    ["humic / pigment", "colour quench & scatter"],
    ["particles, turbidity", "& competing surfaces"],
  ];
  let s = "";
  cards.forEach(([n, col, f], i) => {
    const x = 125 + i * 250;
    s += `<rect x="${x - 115}" y="20" width="230" height="520" rx="26" fill="#fff" stroke="${c(col)}" stroke-width="6"/>`;
    s += f(x, 170);
    s += txt(x, 330, 27, n, col === "sun" ? "navy" : col, "middle", "bold");
    s += txt(x, 395, 23, desc[i][0], "navy") + txt(x, 428, 23, desc[i][1], "navy");
  });
  return wrap(W, H, s);
}

function fpCartoon() {
  const W = 1300, H = 600;
  let s = "";
  // dizzy free aptamer
  s += `<rect x="20" y="20" width="600" height="560" rx="30" fill="${c("mist")}"/>`;
  s += aptamer(320, 300, 170, "teal", 0, { face: "worried", dye: true, rot: 25 });
  [0, 1].forEach((i) => (s += `<ellipse cx="320" cy="290" rx="${190 + i * 40}" ry="${150 + i * 30}" fill="none" stroke="${c("slate")}" stroke-width="5" stroke-dasharray="20 18" opacity="${0.8 - i * 0.3}"/>`));
  s += txt(320, 70, 40, "Wheee! (fast spin)", "coral", "middle", "bold");
  s += txt(320, 545, 30, "light scrambled → LOW polarization", "navy", "middle", "bold");
  // bound, calm
  s += `<rect x="680" y="20" width="600" height="560" rx="30" fill="${c("tealXL")}"/>`;
  s += virus(980, 330, 110, "coralL", "navy", true);
  s += aptamer(1010, 160, 110, "teal", 0, { face: "grin", dye: true, rot: 195 });
  s += txt(980, 70, 40, "Got it! (slow spin)", "teal", "middle", "bold");
  s += txt(980, 545, 30, "light stays aligned → HIGH polarization", "navy", "middle", "bold");
  return wrap(W, H, s);
}

function lfaCartoon() {
  const W = 900, H = 360;
  let s = `<rect x="40" y="110" width="820" height="130" rx="40" fill="#fff" stroke="${c("navy")}" stroke-width="7"/>`;
  s += `<ellipse cx="170" cy="175" rx="55" ry="35" fill="${c("mist")}" stroke="${c("navy")}" stroke-width="5"/>${txt(170, 185, 26, "S", "navy", "middle", "bold")}`;
  s += `<rect x="380" y="140" width="300" height="70" rx="10" fill="${c("mist")}" stroke="${c("navy")}" stroke-width="5"/>`;
  s += `<rect x="470" y="140" width="16" height="70" fill="#B03A2E"/><rect x="580" y="140" width="16" height="70" fill="#B03A2E"/>`;
  s += txt(478, 270, 28, "T", "navy", "middle", "bold") + txt(588, 270, 28, "C", "navy", "middle", "bold");
  s += faceAt(770, 180, 40, "grin");
  s += txt(450, 60, 34, "Next (WP3): the winner goes onto a strip", "tealL", "middle", "bold");
  return wrap(W, H, s);
}

module.exports = {
  P, toPng, hookCrowd, recapTimeline, antibodyVsAptamer, wp1Calendar, wp1Hypothesis, aptamerLineup,
  elisaWell, fpPrinciple, lfaStrip, posterBanner, shapeShifter, applesOranges, villains, fpCartoon, lfaCartoon,
  _prim: { virus, aptamer, tube, bacterium, faceAt },
};
