// Builds ../aptamer_poster.pptx (DIN A0 portrait, cartoon style). Export to PDF with LibreOffice.
// Content follows the user's source document; [square brackets] = still to fill in.
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
const W = 33.11, H = 46.81, M = 1.0, G = 0.5; // A0 portrait, inches

(async () => {
  const pres = new pptxgen();
  pres.defineLayout({ name: "A0", width: W, height: H });
  pres.layout = "A0";
  pres.title = "Salt prepares the hand and weakens the handshake";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;
  const K = { navy: C.text1, slate: C.text2, white: C.background1, bg: C.background2, teal: C.accent1, coral: C.accent2, sun: C.accent3, violet: C.accent4, tealL: C.accent5, brown: C.accent6 };
  pres.defineSlideMaster({ title: "Poster", background: { color: K.bg } });
  const s = pres.addSlide({ masterName: "Poster" });

  const T = (text, o) => s.addText(text, { isTextBox: true, fontSize: 28, color: K.navy, margin: 0, valign: "top", ...o });
  const img = async (ill, x, y, w, name) => {
    const h = (w * ill.h) / ill.w;
    s.addImage({ data: "image/png;base64," + (await I.toPng(ill, 3200)).toString("base64"), x, y, w, h, altText: name, objectName: name });
    return h;
  };
  // Cartoon panel: white card, thick coloured outline, numbered badge + heading.
  const panel = (n, title, x, y, w, h, col, sub) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.5, fill: { color: K.white }, line: { color: col, width: 6 }, objectName: `panel-${n}` });
    s.addShape(pres.shapes.OVAL, { x: x + 0.45, y: y + 0.4, w: 1.15, h: 1.15, fill: { color: col }, line: { color: K.navy, width: 3 } });
    T(String(n), { x: x + 0.45, y: y + 0.4, w: 1.15, h: 1.15, fontSize: 46, bold: true, color: K.white, align: "center", valign: "middle" });
    T(title, { x: x + 1.85, y: y + 0.35, w: w - 2.3, h: 1.25, fontSize: 46, bold: true, color: col, valign: "middle" });
    if (sub) T(sub, { x: x + 1.85, y: y + 1.6, w: w - 2.3, h: 0.75, fontSize: 28, color: K.slate, italic: true });
  };
  const bullets = (items, o) => T(items.map((t, i) => ({ text: t, options: { bullet: { indent: 28 }, breakLine: i < items.length - 1 } })), { paraSpaceAfter: 9, ...o });
  const note = (x, y, w, h, head, body, col) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.35, fill: { color: K.bg }, line: { color: K.bg } });
    T([{ text: head, options: { bold: true, color: col, fontSize: 30, breakLine: true } }, { text: body, options: { fontSize: 26 } }], { x: x + 0.45, y: y + 0.4, w: w - 0.9, h: h - 0.7, paraSpaceAfter: 6 });
  };

  // ---------- Title ----------
  T([
    { text: "Salt prepares the hand", options: { color: K.navy, breakLine: true } },
    { text: "and weakens the handshake", options: { color: K.coral } },
  ], { x: M, y: 0.55, w: W - 2 * M - 4.3, h: 2.6, fontSize: 80, bold: true, lineSpacingMultiple: 0.92 });
  T("Why six published norovirus aptamers cannot simply be ranked — and how we plan to compare them fairly", { x: M, y: 3.25, w: W - 2 * M - 4.3, h: 0.7, fontSize: 32, color: K.teal, bold: true });
  T("[Your name]  ·  [Lab, Institute]  ·  [email]  ·  PhD Retreat 2026", { x: M, y: 4.0, w: W - 2 * M - 4.3, h: 0.5, fontSize: 26, color: K.slate });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: W - M - 3.5, y: 0.6, w: 3.5, h: 3.5, rectRadius: 0.3, fill: { color: K.white }, line: { color: K.navy, width: 4, dashType: "dash" } });
  T("[QR code]", { x: W - M - 3.4, y: 0.6, w: 3.3, h: 3.5, fontSize: 25, color: K.slate, align: "center", valign: "middle" });

  const FULL = W - 2 * M, C3 = (FULL - 2 * G) / 3, C2 = (FULL - G) / 2;

  // ---------- Row A — panel 1: the comparison problem ----------
  let y = 4.75;
  const hA = 5.8;
  panel(1, "Six aptamers, six histories", M, y, FULL, hA, K.navy);
  await img(I.posterBanner(), M + 0.5, y + 1.6, 17.0, "Six aptamer characters from six labs, each with an unknown Kd");
  T([
    { text: "Different labs, techniques, targets and buffers — so the published affinities are not comparable.", options: { fontSize: 27, bold: true, breakLine: true } },
    { text: "An aptamer is not a rigid object with a fixed binding strength: it explores different shapes, and the solution decides how many molecules are in a binding-competent shape. Each one must be optimised in its own conditions.", options: { fontSize: 25, breakLine: true } },
    { text: "A salt-dependent change can therefore look like a difference between aptamers when it is really a difference between conditions.", options: { fontSize: 25, color: "E85D4A", bold: true } },
  ], { x: M + 18.2, y: y + 1.55, w: FULL - 18.8, h: hA - 1.9, paraSpaceAfter: 8 });

  // ---------- Row B — panels 2, 4, 5 ----------
  y += hA + G;
  const hB = 10.4;
  panel(2, "Folding costs charge", M, y, C3, hB, K.teal, "1 · Electrostatics of folding");
  await img(I.ionAtmosphere(), M + 0.8, y + 2.6, C3 - 1.6, "Unfolded strand with a thin ion atmosphere versus a folded one with a dense atmosphere");
  bullets([
    "Folding pulls negative phosphates together — an electrostatic penalty",
    "Positive ions screen it: an ion atmosphere — diffuse and mobile, not fixed ions",
    "Folding and ion uptake are coupled: more salt can stabilise a compact fold",
  ], { x: M + 0.6, y: y + 7.3, w: C3 - 1.2, h: hB - 7.5, fontSize: 23 });

  const xB2 = M + C3 + G;
  panel(4, "Counterion release", xB2, y, C3, hB, K.violet, "3 · Entropy");
  await img(I.counterionRelease(), xB2 + 0.5, y + 2.7, C3 - 1.0, "Ions crowding each partner before binding and released into solution after");
  bullets([
    "Ions are enriched near the DNA and near positive patches on the target",
    "On association some are released into bulk solution and gain freedom → entropy",
    "As bulk salt rises there is less to gain from release, so the advantage shrinks",
    "One reason binding weakens at high salt",
  ], { x: xB2 + 0.6, y: y + 7.0, w: C3 - 1.2, h: hB - 7.3, fontSize: 24 });

  const xB3 = M + 2 * (C3 + G);
  panel(5, "Identity, not only amount", xB3, y, C3, hB, K.sun, "4 · Which ion, not just how much");
  await img(I.ionIdentity(), xB3 + 0.4, y + 2.9, C3 - 0.8, "Potassium in a G-quadruplex, magnesium competing with monovalent ions, chloride versus glutamate");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: xB3 + 0.6, y: y + 6.6, w: C3 - 1.2, h: 3.3, rectRadius: 0.35, fill: { color: K.navy }, line: { color: K.navy } });
  T([
    { text: "Two buffers are not equivalent just because both contain “salt”.", options: { fontSize: 28, bold: true, color: "FFFFFF", breakLine: true } },
    { text: "Ion identity, concentration and pH are separate variables — and we treat them that way.", options: { fontSize: 26, color: "FFFFFF" } },
  ], { x: xB3 + 1.0, y: y + 6.9, w: C3 - 2.0, h: 2.7, paraSpaceAfter: 8 });

  // ---------- Row C — panel 3: the salt curve (centrepiece) ----------
  y += hB + G;
  const hC = 9.9;
  panel(3, "…and the same ions weaken the handshake", M, y, FULL, hC, K.coral, "2 · Electrostatics at the interface");
  await img(I.saltCurve(), M + 0.5, y + 2.3, 13.4, "Non-monotonic affinity versus ionic strength with folding and interface effects");
  bullets([
    "Binding to a positively charged patch is helped by attraction to the negative backbone",
    "Salt screens that attraction too — so the ions that help the fold weaken part of the contact",
    "Affinity against salt is therefore often not monotonic: there can be a window where folding is good and the interface is still strong",
  ], { x: M + 14.3, y: y + 2.4, w: FULL - 14.9, h: 4.2, fontSize: 27 });
  note(M + 14.3, y + 6.8, FULL - 14.9, hC - 7.3, "What salt dependence does not tell us",
    "A steep fall in affinity with rising salt suggests a charge-driven interaction. It does not tell us how many ions were released: structural change, hydration and other contacts also contribute. We treat the salt response as a clue, not a full explanation.", K.coral);

  // ---------- Row D — panels 6 and 7 ----------
  y += hC + G;
  const hD = 8.2, xD2 = M + C2 + G;
  panel(6, "Specificity", M, y, C2, hD, K.brown, "5 · A strong signal is not proof of recognition");
  await img(I.specificityWindow(), M + 2.6, y + 2.45, 10.0, "Background at low salt, recognition in the window, weakened binding at high salt");
  T([
    { text: "Controls, under matched conditions:  ", options: { bold: true, color: "8A6A4F", fontSize: 26 } },
    { text: "scrambled sequences · motif mutants · unrelated viral particles · norovirus-negative stool", options: { fontSize: 25 } },
  ], { x: M + 0.6, y: y + hD - 1.05, w: C2 - 1.2, h: 0.9 });

  panel(7, "Why fluorescence polarisation", xD2, y, C2, hD, K.teal, "6 · One method, one variable: the solution");
  await img(I.fpPlusCd(), xD2 + 0.5, y + 2.5, 8.0, "Fluorescence polarization and circular dichroism side by side");
  bullets([
    "Everything in solution — nothing immobilised, no surface",
    "No wash: one buffer start to finish, at equilibrium",
    "One plate scans ion identity, concentration and pH for all six",
    "With CD: tells a change in fold from a change at the interface",
  ], { x: xD2 + 8.8, y: y + 2.55, w: C2 - 9.4, h: 3.4, fontSize: 23 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: xD2 + 0.6, y: y + hD - 2.1, w: C2 - 1.2, h: 1.8, rectRadius: 0.35, fill: { color: K.teal }, line: { color: K.teal } });
  T([
    { text: "The plan in one line:  ", options: { bold: true, color: "FFFFFF", fontSize: 27 } },
    { text: "test all six head-to-head by FP, vary ions and pH deliberately, and compare both how well each aptamer binds and how much its binding changes between conditions.", options: { color: "FFFFFF", fontSize: 25 } },
  ], { x: xD2 + 1.0, y: y + hD - 1.9, w: C2 - 2.0, h: 1.5 });

  // ---------- Takeaway + discussion ----------
  y += hD + G;
  const hE = H - y - 0.55;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y, w: FULL, h: hE, rectRadius: 0.5, fill: { color: K.navy }, line: { color: K.navy } });
  T([
    { text: "Takeaway:  ", options: { bold: true, color: "F2C14E", fontSize: 34 } },
    { text: "salt helps the fold, weakens the handshake, and changes the entropy of binding — so the binding we measure belongs to the sequence ", options: { color: "FFFFFF", fontSize: 32 } },
    { text: "and its solution together", options: { color: "F2C14E", fontSize: 32, bold: true, italic: true } },
    { text: ".", options: { color: "FFFFFF", fontSize: 32 } },
  ], { x: M + 0.8, y: y + 0.45, w: FULL - 1.6, h: 1.9, lineSpacingMultiple: 1.05 });
  const qs = [
    "Fair buffer: each aptamer's own, or one shared condition for all six?",
    "How far can stool be diluted before the question stops being realistic?",
    "Your experience with FP or CD in complex matrices — what caught you out?",
  ];
  const qw = (FULL - 1.6 - 2 * 0.5) / 3;
  qs.forEach((q, i) => {
    const qx = M + 0.8 + i * (qw + 0.5);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: qx, y: y + 2.6, w: qw, h: hE - 3.2, rectRadius: 0.35, fill: { color: K.white }, line: { color: K.sun, width: 5 } });
    T(q, { x: qx + 0.4, y: y + 2.6, w: qw - 0.8, h: hE - 3.2, fontSize: 26, valign: "middle", bold: true });
  });

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT, "| bottom", (y + hE).toFixed(2), "of", H);
})();
