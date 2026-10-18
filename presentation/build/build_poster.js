// Builds ../aptamer_poster.pptx (DIN A0 portrait, cartoon style). Export to PDF with LibreOffice.
// Placeholders the presenter must fill are written in [square brackets].
const pptxgen = require("pptxgenjs");
const path = require("path");
const I = require("./illus");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const THEME = {
  name: "Aptamer Poster",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2A41", lt1: "FFFFFF", dk2: "5C6B7D", lt2: "E3F2F1",
    accent1: "138A8A", accent2: "E85D4A", accent3: "F2C14E", accent4: "7A5BA6",
    accent5: "7CC6C2", accent6: "8A6A4F", hlink: "138A8A", folHlink: "7A5BA6",
  },
};
const OUT = path.join(__dirname, "..", "aptamer_poster.pptx");
const W = 33.11, H = 46.81, M = 1.0; // A0 portrait, inches

(async () => {
  const pres = new pptxgen();
  pres.defineLayout({ name: "A0", width: W, height: H });
  pres.layout = "A0";
  pres.title = "Which aptamer wins? It depends on the salt.";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;
  const K = { navy: C.text1, slate: C.text2, white: C.background1, bg: C.background2, teal: C.accent1, coral: C.accent2, sun: C.accent3, violet: C.accent4, tealL: C.accent5, brown: C.accent6 };
  pres.defineSlideMaster({ title: "Poster", background: { color: K.bg } });
  const s = pres.addSlide({ masterName: "Poster" });

  const T = (text, o) => s.addText(text, { isTextBox: true, fontSize: 28, color: K.navy, margin: 0, valign: "top", ...o });
  const img = async (ill, x, y, w, name) => {
    const h = (w * ill.h) / ill.w;
    s.addImage({ data: "image/png;base64," + (await I.toPng(ill, 3000)).toString("base64"), x, y, w, h, altText: name, objectName: name });
    return h;
  };
  // Cartoon panel: white card, thick coloured outline, numbered badge + heading.
  const panel = (n, title, x, y, w, h, col) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.5, fill: { color: K.white }, line: { color: col, width: 6 }, objectName: `panel-${n}` });
    s.addShape(pres.shapes.OVAL, { x: x + 0.45, y: y + 0.35, w: 1.15, h: 1.15, fill: { color: col }, line: { color: K.navy, width: 3 } });
    T(String(n), { x: x + 0.45, y: y + 0.35, w: 1.15, h: 1.15, fontSize: 48, bold: true, color: K.white, align: "center", valign: "middle" });
    T(title, { x: x + 1.85, y: y + 0.35, w: w - 2.3, h: 1.15, fontSize: 50, bold: true, color: col, valign: "middle" });
  };
  const bullets = (items, o) => T(items.map((t, i) => ({ text: t, options: { bullet: { indent: 30 }, breakLine: i < items.length - 1 } })), { paraSpaceAfter: 10, ...o });

  // ---------- Title ----------
  T([{ text: "Which aptamer wins?", options: { color: K.navy, breakLine: true } }, { text: "It depends on the salt.", options: { color: K.coral } }], { x: M, y: 0.7, w: W - 2 * M - 4.5, h: 2.7, fontSize: 92, bold: true, lineSpacingMultiple: 0.9 });
  T("Why comparing aptamers for rapid virus detection in stool is hard — and how fluorescence polarization helps", { x: M, y: 3.5, w: W - 2 * M - 4.5, h: 0.7, fontSize: 36, color: K.teal, bold: true });
  T("[Your name]  ·  [Lab, Institute]  ·  [email]  ·  PhD Retreat 2026", { x: M, y: 4.25, w: W - 2 * M - 4.5, h: 0.5, fontSize: 28, color: K.slate });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: W - M - 3.8, y: 0.9, w: 3.8, h: 3.8, rectRadius: 0.3, fill: { color: K.white }, line: { color: K.navy, width: 4, dashType: "dash" } });
  T("[QR code: talk slides / contact]", { x: W - M - 3.6, y: 0.9, w: 3.4, h: 3.8, fontSize: 24, color: K.slate, align: "center", valign: "middle" });

  // ---------- Banner row ----------
  const bannerH = await img(I.posterBanner(), M + 0.6, 5.0, 16, "Aptamer characters on a podium with a salt shaker");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 18.4, y: 5.0, w: W - M - 18.4, h: bannerH, rectRadius: 0.5, fill: { color: K.navy }, line: { color: K.navy } });
  T([
    { text: "The question", options: { bold: true, color: K.sun, fontSize: 36, breakLine: true } },
    { text: "Several published aptamers bind my target virus [name]. Which one should go on the rapid strip test?", options: { color: K.white, fontSize: 28, breakLine: true } },
    { text: " ", options: { fontSize: 14, breakLine: true } },
    { text: "The catch", options: { bold: true, color: K.sun, fontSize: 36, breakLine: true } },
    { text: "Their ranking changes with salt, method and matrix — so a fair comparison needs a fair method.", options: { color: K.white, fontSize: 28 } },
  ], { x: 18.9, y: 5.35, w: W - M - 19.4, h: bannerH - 0.6, paraSpaceAfter: 6 });

  // ---------- Row B: panels 1 & 2 ----------
  const G = 0.45, rB = 5.0 + bannerH + G, colW = (W - 2 * M - 0.6) / 2, x2 = M + colW + 0.6, hB = 10.0, iw = 10.4;
  panel(1, "Aptamers are shape-shifters", M, rB, colW, hB, K.teal);
  await img(I.shapeShifter(), M + (colW - iw) / 2, rB + 1.7, iw, "Folded aptamer with ions versus floppy unfolded aptamer");
  bullets([
    "Mg²⁺ & Na⁺ shield the negative backbone so the strand can fold",
    "K⁺ specifically stabilises G-quadruplexes; pH & temperature matter too",
    "No fold → no binding pocket → no binding",
  ], { x: M + 0.9, y: rB + 7.6, w: colW - 1.8, h: 2.3, fontSize: 26 });

  panel(2, "Apples vs oranges", x2, rB, colW, hB, K.violet);
  await img(I.applesOranges(), x2 + (colW - iw) / 2, rB + 1.8, iw, "Scale comparing two aptamers with different buffers, labels and Kd methods");
  bullets([
    "Each aptamer was selected (SELEX) in its own buffer",
    "Labels & linkers differ (FAM, biotin, spacers) and can change binding",
    "Published Kd values come from different methods → not directly comparable",
  ], { x: x2 + 0.9, y: rB + 7.6, w: colW - 1.8, h: 2.3, fontSize: 26 });

  // ---------- Row C: panel 3 (matrix villains) ----------
  const rC = rB + hB + G, hC = 9.5;
  panel(3, "Meet the stool matrix gang", M, rC, W - 2 * M, hC, K.coral);
  const vh = await img(I.villains(), M + 0.6, rC + 1.65, 20.5, "Six cartoon villains: salt, bile, nucleases, proteins, quenchers, bacteria");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M + 21.6, y: rC + 1.65, w: W - 2 * M - 22.2, h: vh, rectRadius: 0.4, fill: { color: K.bg }, line: { color: K.bg } });
  T([
    { text: "Why it hits every assay", options: { bold: true, color: K.coral, fontSize: 32, breakLine: true } },
    { text: "Stool composition varies between donors and days, so salt and Mg²⁺ — and with them the aptamer fold — are never fixed.", options: { fontSize: 26, breakLine: true } },
    { text: " ", options: { fontSize: 10, breakLine: true } },
    { text: "Watch-out for optics", options: { bold: true, color: K.coral, fontSize: 32, breakLine: true } },
    { text: "Pigments & particles absorb and scatter light — they can fake a signal in colour and fluorescence assays alike.", options: { fontSize: 26 } },
  ], { x: M + 22.0, y: rC + 2.0, w: W - 2 * M - 23.0, h: vh - 0.6, paraSpaceAfter: 6 });

  // ---------- Row D: panels 4 & 5 ----------
  const rD = rC + hC + G, hD = 11.3, w4 = 11.2, x5 = M + w4 + 0.6, w5 = W - M - x5;
  panel(4, "ELISA: lessons learned", M, rD, w4, hD, K.brown);
  const hdr = (t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: "8A6A4F" } } });
  s.addTable([
    [hdr("What we saw"), hdr("Why it happens")],
    ["[Weak / patchy signal]", "Washes strip aptamers that unbind fast"],
    ["[Ranking ≠ literature]", "Surface tethering changes folding & access"],
    ["[Result shifts with wash buffer]", "One buffer is unfair to aptamers selected in other salts"],
    ["[High background in stool]", "Matrix & blockers stick to plate and DNA"],
  ], { x: M + 0.6, y: rD + 1.9, w: w4 - 1.2, colW: [4.4, w4 - 1.2 - 4.4], fontSize: 25, color: "1B2A41", fontFace: "Calibri", border: { type: "solid", pt: 2, color: "D9C3A5" }, rowH: 1.35, valign: "middle", margin: 0.12 });
  T("Bottom line: ELISA scored the assay, not the aptamer.", { x: M + 0.6, y: rD + hD - 1.75, w: w4 - 1.2, h: 1.2, fontSize: 30, bold: true, color: K.brown });

  panel(5, "Fluorescence polarization to the rescue", x5, rD, w5, hD, K.teal);
  const fh = await img(I.fpCartoon(), x5 + 0.6, rD + 1.8, 9.8, "Cartoon: free aptamer spins fast, bound aptamer spins slowly");
  bullets([
    "Homogeneous: no surface, no washes",
    "True equilibrium Kd, minutes per plate",
    "Same plate, many buffers → fair comparison",
    "Ratiometric → less sensitive to intensity loss",
  ], { x: x5 + 0.7, y: rD + 2.0 + fh, w: 10.0, h: hD - fh - 2.3, fontSize: 26, paraSpaceAfter: 6 });
  // planned experiment matrix
  const mx = x5 + 11.2, mw = w5 - 11.8;
  T("Planned experiment matrix", { x: mx, y: rD + 1.85, w: mw, h: 0.7, fontSize: 32, bold: true, color: K.teal });
  const conds = ["Own SELEX buffer", "Shared\nbuffer", "NaCl series", "Mg²⁺ series", "K⁺ (G4)", "Stool 1:[x]"];
  const dot = (on) => ({ text: on ? "●" : "○", options: { align: "center", color: on ? "138A8A" : "C9D3DC", fontSize: 28 } });
  s.addTable([
    [{ text: "", options: { fill: { color: "FFFFFF" } } }, ...conds.map((c) => ({ text: c, options: { bold: true, fontSize: 18, align: "center", color: "FFFFFF", fill: { color: "138A8A" } } }))],
    ...["A", "B", "C", "D"].map((n) => [{ text: `Apt-${n}`, options: { bold: true } }, ...conds.map((c) => dot(!(c === "K⁺ (G4)" && n !== "B")))]),
  ], { x: mx, y: rD + 2.65, w: mw, colW: [1.6, ...Array(6).fill((mw - 1.6) / 6)], fontSize: 24, color: "1B2A41", fontFace: "Calibri", border: { type: "solid", pt: 1.5, color: "C9D3DC" }, rowH: [1.0, 0.68, 0.68, 0.68, 0.68], valign: "middle", margin: 0.05 });
  T([
    { text: "Readout → Kd", options: { bold: true, color: K.teal, fontSize: 28, breakLine: true } },
    { text: "titrate target, fit mP to a 1:1 binding model", options: { fontSize: 24, breakLine: true } },
    { text: "Controls", options: { bold: true, color: K.teal, fontSize: 28, breakLine: true } },
    { text: "scrambled sequence · dye only · stool-only blank · unlabelled competitor", options: { fontSize: 24, breakLine: true } },
    { text: "Watch-outs", options: { bold: true, color: K.coral, fontSize: 28, breakLine: true } },
    { text: "stool scatter/autofluorescence → red dye + blanks · dye/linker can alter binding", options: { fontSize: 24 } },
  ], { x: mx, y: rD + 6.5, w: mw, h: hD - 6.8, paraSpaceAfter: 3 });

  // ---------- Row E: discussion + next step ----------
  const rE = rD + hD + G, hE = H - rE - 0.6;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y: rE, w: W - 2 * M, h: hE, rectRadius: 0.5, fill: { color: K.navy }, line: { color: K.navy } });
  T("Let's discuss!", { x: M + 0.7, y: rE + 0.35, w: 8, h: 0.9, fontSize: 44, bold: true, color: K.sun });
  const qs = ["Which buffer is ‘fair’ — each aptamer's own, or one common buffer?", "How much stool dilution is acceptable for a rapid test?", "Your experience with FP in complex matrices?"];
  qs.forEach((q, i) => {
    const qx = M + 0.7 + i * 7.0;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: qx, y: rE + 1.3, w: 6.7, h: hE - 1.6, rectRadius: 0.35, fill: { color: K.white }, line: { color: K.sun, width: 4 } });
    T(q, { x: qx + 0.3, y: rE + 1.3, w: 6.1, h: hE - 1.6, fontSize: 25, valign: "middle", bold: true });
  });
  await img(I.lfaCartoon(), M + 22.0, rE + 0.25, Math.min(W - 2 * M - 22.4, (hE - 0.5) * 900 / 360), "Lateral flow strip with a smiling face: the next step");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT, "rowE", rE.toFixed(2), "hE", hE.toFixed(2));
})();
