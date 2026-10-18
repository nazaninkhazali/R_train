// Standalone artwork: "THE POLARISATION SHOW" — a vintage-theatre poster about
// fluorescence polarization and the salt effect. Outputs PNG + print-ready PDF.
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const W = 2400, H = 3400;
const P = {
  ink: "#101E36", inkL: "#1C3253", cream: "#F7EDD9", creamD: "#E8D9BC",
  gold: "#E9B23C", goldL: "#F6D98A", coral: "#E2574C", coralL: "#F2A398",
  teal: "#1E948F", tealL: "#7ECFC9", violet: "#8E6FA8", paper: "#FBF5E9",
};
const DISPLAY = "Inter Display, Inter, Liberation Sans, sans-serif";
const SERIF = "Bitstream Charter, Liberation Serif, serif";
const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;");

const txt = (x, y, size, t, o = {}) =>
  `<text x="${x}" y="${y}" font-size="${size}" fill="${o.fill || P.cream}" text-anchor="${o.anchor || "middle"}"
     font-family="${o.font || DISPLAY}" font-weight="${o.weight || 700}" letter-spacing="${o.ls || 0}"
     ${o.style ? `font-style="${o.style}"` : ""} ${o.op ? `opacity="${o.op}"` : ""}>${esc(t)}</text>`;

function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }

// ---------- ornaments ----------
function starburst(cx, cy, rIn, rOut, n, col, op = 0.14) {
  let s = "";
  for (let i = 0; i < n; i++) {
    const a0 = (i / n) * Math.PI * 2, w = (Math.PI / n) * 0.52;
    s += `<path d="M${cx + Math.cos(a0 - w) * rIn} ${cy + Math.sin(a0 - w) * rIn}
      L${cx + Math.cos(a0) * rOut} ${cy + Math.sin(a0) * rOut}
      L${cx + Math.cos(a0 + w) * rIn} ${cy + Math.sin(a0 + w) * rIn} Z" fill="${col}" opacity="${op}"/>`;
  }
  return s;
}
// Banner ribbon with folded tails.
function ribbon(cx, y, w, h, col = P.coral, shade = "#B8413A") {
  const x = cx - w / 2, t = h * 0.55;
  return `<path d="M${x - t} ${y + h * 0.1} L${x} ${y} L${x} ${y + h} L${x - t} ${y + h * 0.9} L${x - t * 0.45} ${y + h / 2} Z" fill="${shade}"/>
    <path d="M${x + w + t} ${y + h * 0.1} L${x + w} ${y} L${x + w} ${y + h} L${x + w + t} ${y + h * 0.9} L${x + w + t * 0.45} ${y + h / 2} Z" fill="${shade}"/>
    <rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${col}"/>
    <rect x="${x}" y="${y}" width="${w}" height="${h * 0.14}" fill="#fff" opacity="0.18"/>`;
}
function flourish(x, y, s, rot = 0, col = P.gold) {
  return `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${s})" fill="none" stroke="${col}" stroke-width="5" stroke-linecap="round">
    <path d="M0 0 C 40 -10, 70 -40, 72 -78 C 74 -40, 104 -10, 144 0 C 104 10, 74 40, 72 78 C 70 40, 40 10, 0 0 Z" fill="${col}" stroke="none" opacity="0.9"/>
    <path d="M-70 0 q 35 -26 68 -2 M214 0 q -35 -26 -68 -2"/>
    <circle cx="-82" cy="0" r="9" fill="${col}" stroke="none"/><circle cx="226" cy="0" r="9" fill="${col}" stroke="none"/>
  </g>`;
}
const sparkle = (x, y, r, col = P.goldL, op = 1) =>
  `<path d="M${x} ${y - r} Q${x + r * 0.2} ${y - r * 0.2} ${x + r} ${y} Q${x + r * 0.2} ${y + r * 0.2} ${x} ${y + r}
     Q${x - r * 0.2} ${y + r * 0.2} ${x - r} ${y} Q${x - r * 0.2} ${y - r * 0.2} ${x} ${y - r} Z" fill="${col}" opacity="${op}"/>`;

// A polarized light ribbon: a sine wave travelling along a direction.
function waveRay(x, y, len, angle, amp, cycles, col, w = 7, op = 1) {
  const step = len / (cycles * 2);
  let d = `M0 0`;
  for (let i = 0; i < cycles * 2; i++) d += ` q ${step / 2} ${i % 2 ? amp : -amp} ${step} 0`;
  return `<path transform="translate(${x} ${y}) rotate(${angle})" d="${d}" fill="none" stroke="${col}"
    stroke-width="${w}" stroke-linecap="round" opacity="${op}"/>`;
}

// ---------- characters ----------
function aptamerChar(x, y, s, col, opts = {}) {
  const k = s / 100, st = col, w = 9 * k;
  let g = "";
  if (opts.limp) {
    g += `<path d="M${-60 * k} ${70 * k} C ${-20 * k} ${20 * k}, ${-70 * k} ${0}, ${-20 * k} ${-40 * k}
      S ${30 * k} ${-70 * k}, ${70 * k} ${-62 * k}" fill="none" stroke="${st}" stroke-width="${w}" stroke-linecap="round"/>`;
    g += `<circle cx="${70 * k}" cy="${-62 * k}" r="${20 * k}" fill="${st}"/>`;
    g += face(70 * k, -58 * k, 15 * k, "sleep");
  } else {
    // folded hairpin body
    g += `<path d="M${-14 * k} ${72 * k} L${-14 * k} ${-6 * k} C ${-14 * k} ${-44 * k}, ${-44 * k} ${-50 * k}, ${-34 * k} ${-70 * k}
      C ${-23 * k} ${-96 * k}, ${23 * k} ${-96 * k}, ${34 * k} ${-70 * k}
      C ${44 * k} ${-50 * k}, ${14 * k} ${-44 * k}, ${14 * k} ${-6 * k} L ${14 * k} ${72 * k}"
      fill="none" stroke="${st}" stroke-width="${w}" stroke-linecap="round"/>`;
    for (let i = 0; i < 5; i++)
      g += `<line x1="${-14 * k}" x2="${14 * k}" y1="${(58 - i * 14) * k}" y2="${(58 - i * 14) * k}" stroke="${st}" stroke-width="${4 * k}" opacity="0.55"/>`;
    g += face(0, -66 * k, 19 * k, opts.mood || "grin");
  }
  // the lantern (fluorophore) on a little arm
  if (opts.lantern) {
    const lx = opts.lanternX !== undefined ? opts.lanternX * k : 46 * k, ly = opts.lanternY !== undefined ? opts.lanternY * k : 34 * k;
    g += `<path d="M${14 * k} ${10 * k} Q ${lx * 0.7} ${ly - 30 * k} ${lx} ${ly}" fill="none" stroke="${st}" stroke-width="${6 * k}" stroke-linecap="round"/>`;
    g += `<circle cx="${lx}" cy="${ly}" r="${26 * k}" fill="${P.gold}" opacity="0.28"/>`;
    g += `<circle cx="${lx}" cy="${ly}" r="${15 * k}" fill="${P.goldL}" stroke="${P.ink}" stroke-width="${3 * k}"/>`;
  }
  return `<g transform="translate(${x} ${y})${opts.rot ? ` rotate(${opts.rot})` : ""}">${g}</g>`;
}
function face(x, y, r, mood = "grin") {
  const ex = r * 0.42, e = r * 0.3;
  let s = "";
  if (mood === "dizzy") {
    s += `<g stroke="${P.ink}" stroke-width="${r * 0.13}" fill="none" stroke-linecap="round">
      <path d="M${x - ex - e} ${y - e} L${x - ex + e} ${y + e} M${x - ex + e} ${y - e} L${x - ex - e} ${y + e}"/>
      <path d="M${x + ex - e} ${y - e} L${x + ex + e} ${y + e} M${x + ex + e} ${y - e} L${x + ex - e} ${y + e}"/></g>`;
    s += `<ellipse cx="${x}" cy="${y + r * 0.6}" rx="${r * 0.3}" ry="${r * 0.22}" fill="${P.ink}"/>`;
  } else if (mood === "sleep") {
    s += `<g stroke="${P.ink}" stroke-width="${r * 0.14}" fill="none" stroke-linecap="round">
      <path d="M${x - ex - e} ${y} q ${e} ${e * 1.1} ${2 * e} 0"/><path d="M${x + ex - e} ${y} q ${e} ${e * 1.1} ${2 * e} 0"/></g>`;
  } else {
    s += `<circle cx="${x - ex}" cy="${y}" r="${e * 0.72}" fill="${P.ink}"/><circle cx="${x + ex}" cy="${y}" r="${e * 0.72}" fill="${P.ink}"/>`;
    s += `<circle cx="${x - ex + e * 0.26}" cy="${y - e * 0.28}" r="${e * 0.24}" fill="#fff"/><circle cx="${x + ex + e * 0.26}" cy="${y - e * 0.28}" r="${e * 0.24}" fill="#fff"/>`;
    s += mood === "grin"
      ? `<path d="M${x - r * 0.42} ${y + r * 0.42} q ${r * 0.42} ${r * 0.55} ${r * 0.84} 0 Z" fill="${P.ink}"/>`
      : `<path d="M${x - r * 0.36} ${y + r * 0.45} q ${r * 0.36} ${r * 0.36} ${r * 0.72} 0" stroke="${P.ink}" stroke-width="${r * 0.13}" fill="none" stroke-linecap="round"/>`;
  }
  return s;
}
// Virus particle, drawn big and friendly.
function virusChar(x, y, r, opts = {}) {
  let s = "";
  for (let i = 0; i < 14; i++) {
    const a = (i * Math.PI * 2) / 14;
    const x1 = x + Math.cos(a) * r * 0.92, y1 = y + Math.sin(a) * r * 0.92;
    const x2 = x + Math.cos(a) * r * 1.3, y2 = y + Math.sin(a) * r * 1.3;
    s += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${P.ink}" stroke-width="${r * 0.075}" stroke-linecap="round"/>`;
    s += `<circle cx="${x2}" cy="${y2}" r="${r * 0.13}" fill="${opts.fill || P.coralL}" stroke="${P.ink}" stroke-width="${r * 0.05}"/>`;
  }
  const hex = [...Array(6)].map((_, i) => {
    const a = (i * Math.PI) / 3 + Math.PI / 6;
    return `${x + Math.cos(a) * r},${y + Math.sin(a) * r}`;
  }).join(" ");
  s += `<polygon points="${hex}" fill="${opts.fill || P.coralL}" stroke="${P.ink}" stroke-width="${r * 0.08}" stroke-linejoin="round"/>`;
  s += `<polygon points="${[...Array(3)].map((_, i) => { const a = (i * 2 * Math.PI) / 3 - Math.PI / 2; return `${x + Math.cos(a) * r * 0.46},${y + Math.sin(a) * r * 0.46}`; }).join(" ")}"
    fill="none" stroke="${P.ink}" stroke-width="${r * 0.05}" opacity="0.4"/>`;
  if (opts.face) s += face(x, y + r * 0.08, r * 0.3, opts.face);
  return s;
}
const ionPlus = (x, y, s, col = P.goldL, op = 1) =>
  `<g opacity="${op}"><line x1="${x - s}" y1="${y}" x2="${x + s}" y2="${y}" stroke="${col}" stroke-width="${s * 0.62}" stroke-linecap="round"/>
   <line x1="${x}" y1="${y - s}" x2="${x}" y2="${y + s}" stroke="${col}" stroke-width="${s * 0.62}" stroke-linecap="round"/></g>`;

// ---------- the poster ----------
function build() {
  let s = "";
  // background
  s += `<rect width="${W}" height="${H}" fill="${P.ink}"/>`;
  s += `<radialGradient id="glow" cx="50%" cy="34%" r="62%">
      <stop offset="0" stop-color="${P.inkL}"/><stop offset="1" stop-color="${P.ink}"/></radialGradient>`;
  s += `<rect width="${W}" height="${H}" fill="url(#glow)"/>`;
  s += starburst(1200, 1180, 180, 2600, 36, P.cream, 0.05);
  // paper grain speckles
  const r = rng(13);
  for (let i = 0; i < 900; i++) s += `<circle cx="${r() * W}" cy="${r() * H}" r="${r() * 2.2}" fill="${P.cream}" opacity="${r() * 0.07}"/>`;
  // double border
  s += `<rect x="34" y="34" width="${W - 68}" height="${H - 68}" fill="none" stroke="${P.gold}" stroke-width="9"/>`;
  s += `<rect x="60" y="60" width="${W - 120}" height="${H - 120}" fill="none" stroke="${P.gold}" stroke-width="3" opacity="0.65"/>`;
  [[60, 60, 0], [W - 60, 60, 90], [W - 60, H - 60, 180], [60, H - 60, 270]].forEach(([x, y, rot]) => {
    s += `<g transform="translate(${x} ${y}) rotate(${rot})"><path d="M0 110 L0 0 L110 0" fill="none" stroke="${P.gold}" stroke-width="10"/>
      <circle cx="30" cy="30" r="11" fill="${P.gold}"/></g>`;
  });

  // ===== TITLE =====
  s += txt(1200, 206, 44, "ONE MOLECULE · TWO TEMPOS · AND THE TIDE OF SALT", { fill: P.gold, ls: 10, weight: 600 });
  s += txt(1200, 300, 54, "the", { fill: P.cream, font: SERIF, style: "italic", weight: 400, op: 0.85 });
  s += txt(1200, 436, 168, "POLARISATION", { fill: P.cream, ls: 8 });
  s += txt(1200, 572, 168, "SHOW", { fill: P.gold, ls: 46 });
  s += sparkle(556, 512, 30) + sparkle(1844, 512, 30) + sparkle(640, 574, 16, P.cream, 0.8) + sparkle(1760, 574, 16, P.cream, 0.8);

  // ===== THE LAMP: polarized light source =====
  const lampY = 742;
  s += txt(1200, 672, 34, "POLARISED LIGHT", { fill: P.gold, ls: 8 });
  s += `<rect x="1148" y="${lampY - 48}" width="104" height="52" rx="14" fill="${P.creamD}" stroke="${P.ink}" stroke-width="6"/>`;
  s += `<path d="M1200 ${lampY} L1118 ${lampY + 96} L1282 ${lampY + 96} Z" fill="${P.gold}"/>`;
  s += `<circle cx="1200" cy="${lampY + 96}" r="26" fill="${P.goldL}"/>`;
  s += waveRay(1150, lampY + 128, 400, 118, 26, 5, P.goldL, 9, 0.95);
  s += waveRay(1250, lampY + 128, 400, 62, 26, 5, P.goldL, 9, 0.95);

  // ===== THE TWO ACTS =====
  const archTop = 1060, archBot = 2190, archW = 1030, lx = 110, rx = 1260;
  const arch = (x, title, kicker, accent, shade) => {
    const dome = `M${x} ${archBot} L${x} ${archTop + 330}
      A ${archW / 2} ${archW / 2 * 0.86} 0 0 1 ${x + archW} ${archTop + 330} L${x + archW} ${archBot} Z`;
    let g = `<path d="${dome}" fill="${P.paper}"/><path d="${dome}" fill="none" stroke="${accent}" stroke-width="12"/>`;
    g += `<path d="M${x + 22} ${archBot - 22} L${x + 22} ${archTop + 334}
      A ${archW / 2 - 22} ${archW / 2 * 0.86 - 22} 0 0 1 ${x + archW - 22} ${archTop + 334}
      L${x + archW - 22} ${archBot - 22} Z" fill="none" stroke="${accent}" stroke-width="3" opacity="0.5"/>`;
    g += ribbon(x + archW / 2, archTop + 108, 640, 96, accent, shade);
    g += txt(x + archW / 2, archTop + 176, 58, title, { fill: P.cream, ls: 6 });
    g += txt(x + archW / 2, archTop + 258, 36, kicker, { fill: P.ink, font: SERIF, style: "italic", weight: 400, op: 0.75 });
    return g;
  };
  s += arch(lx, "THE SPINNER", "free · small · fast", P.coral, "#B8413A");
  s += arch(rx, "THE ANCHOR", "bound · huge · slow", P.teal, "#15706C");

  // --- LEFT: the spinner, light thrown everywhere ---
  const lcx = lx + archW / 2, lcy = 1626;
  [0, 1, 2].forEach((i) => {
    s += `<ellipse cx="${lcx}" cy="${lcy}" rx="${250 + i * 52}" ry="${196 + i * 38}" fill="none"
      stroke="${P.coral}" stroke-width="${8 - i * 1.6}" stroke-dasharray="28 24" opacity="${0.6 - i * 0.16}"/>`;
  });
  const r2 = rng(5);
  s += `<clipPath id="archL"><path d="M${lx} ${archBot} L${lx} ${archTop + 330}
    A ${archW / 2} ${archW / 2 * 0.86} 0 0 1 ${lx + archW} ${archTop + 330} L${lx + archW} ${archBot} Z"/></clipPath>`;
  s += `<g clip-path="url(#archL)">`;
  for (let i = 0; i < 18; i++) {
    const a = (i / 18) * 360 + r2() * 10;
    const rad = 300 + r2() * 40;
    const px = lcx + Math.cos((a * Math.PI) / 180) * rad, py = lcy + Math.sin((a * Math.PI) / 180) * rad * 0.76;
    s += waveRay(px, py, 96 + r2() * 38, a, 14, 2, P.gold, 7, 0.8);
  }
  s += `</g>`;
  s += aptamerChar(lcx - 10, lcy + 40, 188, P.coral, { mood: "dizzy", lantern: true, rot: -18 });
  s += `<path d="M${lcx - 232} ${lcy - 150} a 262 206 0 0 1 150 -128" fill="none" stroke="${P.ink}" stroke-width="11" stroke-linecap="round"/>`;
  s += `<path d="M${lcx - 90} ${lcy - 306} l 48 22 l -46 30 z" fill="${P.ink}"/>`;
  s += sparkle(lcx + 236, lcy - 244, 26, P.gold) + sparkle(lcx - 296, lcy + 188, 20, P.gold, 0.8);
  s += txt(lcx, archTop + 258, 36, "free · small · fast", { fill: P.ink, font: SERIF, style: "italic", weight: 400, op: 0.75 });
  s += `<rect x="${lx + 60}" y="1884" width="${archW - 120}" height="244" rx="22" fill="${P.ink}" opacity="0.94"/>`;
  s += txt(lcx, 1950, 40, "light thrown every which way", { fill: P.cream, font: SERIF, weight: 400, style: "italic" });
  s += txt(lcx, 2062, 104, "LOW mP", { fill: P.coralL, ls: 4 });

  // --- RIGHT: the anchor, the beam holds its line ---
  const rcx = rx + archW / 2, rcy = 1618;
  s += `<ellipse cx="${rcx}" cy="${rcy + 168}" rx="282" ry="48" fill="${P.ink}" opacity="0.12"/>`;
  s += virusChar(rcx + 24, rcy + 62, 190, { fill: P.tealL, face: "grin" });
  s += aptamerChar(rcx - 150, rcy - 140, 142, P.teal, { mood: "grin", lantern: true, lanternX: -52, lanternY: 26, rot: 16 });
  s += waveRay(rcx + 150, rcy - 236, 250, 24, 20, 4, P.goldL, 10, 1);
  s += `<path d="M${rcx + 384} ${rcy - 128} l 50 22 l -48 30 z" fill="${P.goldL}"/>`;
  s += `<path d="M${rcx - 282} ${rcy + 188} a 290 216 0 0 0 74 84" fill="none" stroke="${P.ink}" stroke-width="11" stroke-linecap="round"/>`;
  s += `<path d="M${rcx - 206} ${rcy + 250} l -6 48 l -40 -30 z" fill="${P.ink}"/>`;
  s += sparkle(rcx - 300, rcy - 232, 24, P.gold) + sparkle(rcx + 300, rcy + 184, 20, P.gold, 0.8);
  s += `<rect x="${rx + 60}" y="1884" width="${archW - 120}" height="244" rx="22" fill="${P.ink}" opacity="0.94"/>`;
  s += txt(rcx, 1950, 40, "light holds its line", { fill: P.cream, font: SERIF, weight: 400, style: "italic" });
  s += txt(rcx, 2062, 104, "HIGH mP", { fill: P.tealL, ls: 4 });

  // ===== THE SALT TIDE =====
  const tideTop = 2256;
  s += ribbon(1200, tideTop, 820, 100, P.gold, "#BE8C26");
  s += txt(1200, tideTop + 70, 58, "THE SALT TIDE", { fill: P.ink, ls: 10 });
  s += txt(1200, tideTop + 162, 38, "every act has its price", { fill: P.cream, font: SERIF, style: "italic", weight: 400, op: 0.9 });

  const cy0 = 2748, x0 = 250, x1 = 2150, peak = 2512;
  const hill = (t) => cy0 - Math.exp(-Math.pow((t - 0.5) * 3.1, 2)) * (cy0 - peak);
  const pts = [];
  for (let i = 0; i <= 60; i++) { const t = i / 60; pts.push(`${x0 + t * (x1 - x0)},${hill(t)}`); }
  const bx = x0 + 0.37 * (x1 - x0), bw = 0.26 * (x1 - x0);
  s += `<path d="M${x0},${cy0} ${pts.join(" ")} L${x1},${cy0} Z" fill="${P.coral}" opacity="0.18"/>`;
  // the sweet spot reads as a lit panel on a dark stage — a pale slab, not a tint
  s += `<rect x="${bx}" y="${peak - 34}" width="${bw}" height="${cy0 - peak + 34}" rx="16" fill="${P.goldL}" opacity="0.92"/>`;
  s += `<rect x="${bx}" y="${peak - 34}" width="${bw}" height="${cy0 - peak + 34}" rx="16" fill="none" stroke="${P.gold}" stroke-width="5"/>`;
  s += txt(1200, cy0 - 26, 30, "THE SWEET SPOT", { fill: P.ink, ls: 7 });
  s += `<polyline points="${pts.join(" ")}" fill="none" stroke="${P.coral}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>`;
  s += `<line x1="${x0 - 40}" y1="${cy0}" x2="${x1 + 40}" y2="${cy0}" stroke="${P.cream}" stroke-width="5" opacity="0.45"/>`;
  s += txt(x1 + 40, cy0 + 54, 30, "IONIC STRENGTH  →", { fill: P.cream, anchor: "end", ls: 6, op: 0.72 });
  s += `<g transform="rotate(-90 160 2640)">${txt(160, 2640, 30, "AFFINITY", { fill: P.cream, ls: 6, op: 0.72 })}</g>`;

  // three medallions hanging from the curve
  const acts = [
    [x0 + 0.075 * (x1 - x0), "TOO LITTLE", "the fold won't hold", P.violet, 0, "#6B5182"],
    [1200, "JUST RIGHT", "folded — and gripping", P.gold, 1, "#BE8C26"],
    [x0 + 0.925 * (x1 - x0), "TOO MUCH", "the grip washes away", P.teal, 2, "#15706C"],
  ];
  const my = 2972, R = 148;
  acts.forEach(([x, label, cap, col, kind, shade]) => {
    s += `<line x1="${x}" y1="${hill((x - x0) / (x1 - x0))}" x2="${x}" y2="${my - R}" stroke="${col}" stroke-width="5" stroke-dasharray="14 12" opacity="0.75"/>`;
    s += `<circle cx="${x}" cy="${my}" r="${R}" fill="${P.paper}" stroke="${col}" stroke-width="11"/>`;
    s += `<circle cx="${x}" cy="${my}" r="${R - 17}" fill="none" stroke="${col}" stroke-width="3" opacity="0.45"/>`;
    if (kind === 0) {
      s += aptamerChar(x - 6, my + 4, 84, P.violet, { limp: true });
      s += ionPlus(x - 96, my - 76, 12, P.violet, 0.65) + ionPlus(x + 92, my + 44, 10, P.violet, 0.5);
    } else if (kind === 1) {
      s += `<circle cx="${x}" cy="${my - 16}" r="${R - 44}" fill="${P.gold}" opacity="0.16"/>`;
      s += virusChar(x + 44, my - 4, 60, { fill: P.coralL });
      s += aptamerChar(x - 58, my - 44, 64, P.teal, { mood: "grin" });
      for (let i = 0; i < 6; i++) s += ionPlus(x - 96 + i * 38, my + 62 - (i % 2) * 18, 10, P.gold, 0.85);
    } else {
      s += virusChar(x + 62, my - 10, 56, { fill: P.coralL });
      s += aptamerChar(x - 84, my - 34, 62, P.teal, { mood: "sleep", rot: -24 });
      s += `<path d="M${x - 10} ${my - 120} q 32 44 0 88 q -32 44 0 88" fill="none" stroke="${P.tealL}" stroke-width="11" stroke-linecap="round"/>`;
      for (let i = 0; i < 6; i++) s += ionPlus(x - 104 + (i % 3) * 104, my - 96 + Math.floor(i / 3) * 150, 12, P.tealL, 0.7);
    }
    s += ribbon(x, my + R + 28, 320, 66, col, shade);
    s += txt(x, my + R + 76, 38, label, { fill: kind === 1 ? P.ink : P.cream, ls: 4 });
    s += txt(x, my + R + 140, 30, cap, { fill: P.cream, font: SERIF, style: "italic", weight: 400, op: 0.9 });
  });

  // ===== BOTTOM ROLL =====
  s += txt(1200, 3318, 52, "SALT PREPARES THE HAND — AND WEAKENS THE HANDSHAKE", { fill: P.gold, ls: 3 });

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">${s}</svg>`;
}

(async () => {
  const svg = build();
  const out = path.join(__dirname, "..", "art_fp_salt");
  fs.writeFileSync(out + ".svg", svg);
  await sharp(Buffer.from(svg), { density: 90 }).png().toFile(out + ".png");
  console.log("wrote", out + ".png");
})();
