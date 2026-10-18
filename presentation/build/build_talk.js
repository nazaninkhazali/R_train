// Builds ../retreat_talk.pptx (clean scientific style, 16:9).
// Placeholders the presenter must fill are written in [square brackets].
const pptxgen = require("pptxgenjs");
const path = require("path");
const I = require("./illus");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const THEME = {
  name: "Retreat Talk",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2A41", lt1: "FFFFFF", dk2: "5C6B7D", lt2: "EEF3F6",
    accent1: "138A8A", accent2: "E85D4A", accent3: "F2C14E", accent4: "7A5BA6",
    accent5: "7CC6C2", accent6: "8A6A4F", hlink: "138A8A", folHlink: "7A5BA6",
  },
};
const OUT = path.join(__dirname, "..", "retreat_talk.pptx");

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
  pres.title = "Rapid aptamer-based viral screening — PhD retreat";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;
  const K = { navy: C.text1, slate: C.text2, white: C.background1, mist: C.background2, teal: C.accent1, coral: C.accent2, sun: C.accent3, violet: C.accent4, tealL: C.accent5 };

  pres.defineSlideMaster({
    title: "Dark",
    background: { color: K.navy },
    objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.7, y: 1.6, w: 6.6, h: 2.6, fontSize: 44, bold: true, color: K.white, valign: "top", align: "left" }, text: "" } }],
  });
  pres.defineSlideMaster({
    title: "Content",
    background: { color: K.white },
    objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 10.2, h: 1.0, fontSize: 32, bold: true, color: K.navy, valign: "middle", align: "left", margin: 0 }, text: "" } }],
    slideNumber: { x: 12.4, y: 7.0, w: 0.6, h: 0.3, fontSize: 11, color: K.slate },
  });

  const img = async (slide, ill, x, y, w, name) => {
    const h = (w * ill.h) / ill.w;
    slide.addImage({ data: "image/png;base64," + (await I.toPng(ill, 2000)).toString("base64"), x, y, w, h, altText: name, objectName: name });
    return h;
  };
  const T = (slide, text, o) => slide.addText(text, { isTextBox: true, fontSize: 16, color: K.navy, margin: 0, valign: "top", ...o });
  // Roadmap progress indicator (top-right): which work package we're in.
  const progress = (slide, active) => {
    ["WP1", "WP2", "WP3"].forEach((wp, i) => {
      const on = i + 1 === active;
      slide.addShape(pres.shapes.OVAL, { x: 11.05 + i * 0.62, y: 0.6, w: 0.48, h: 0.48, fill: { color: on ? K.teal : K.mist }, line: { color: on ? K.teal : K.tealL, width: 1 }, objectName: `progress-${wp}` });
      T(slide, String(i + 1), { x: 11.05 + i * 0.62, y: 0.6, w: 0.48, h: 0.48, fontSize: 14, bold: true, align: "center", valign: "middle", color: on ? K.white : K.slate });
    });
  };
  const chip = (slide, x, y, w, h, head, body, fill = K.mist, headCol = K.teal) => {
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: fill }, line: { color: fill } });
    T(slide, [{ text: head, options: { bold: true, color: headCol, fontSize: 17, breakLine: true } }, { text: body, options: { fontSize: 15, color: K.navy } }], { x: x + 0.2, y: y + 0.15, w: w - 0.4, h: h - 0.3, paraSpaceAfter: 4 });
  };
  const add = (master, section) => pres.addSlide({ masterName: master, sectionTitle: section });

  // ---------- 1. Title / hook ----------
  pres.addSection({ title: "Opening" });
  let s = add("Dark", "Opening");
  s.addText("Finding a few viruses in a very crowded sample — fast", { placeholder: "title" });
  T(s, "Aptamer-based rapid viral screening of donor stool", { x: 0.7, y: 4.3, w: 6.4, h: 0.5, fontSize: 22, color: K.tealL });
  T(s, "[Your name]  ·  [Lab / supervisors]  ·  PhD Retreat 2026", { x: 0.7, y: 6.4, w: 6.4, h: 0.4, fontSize: 15, color: K.mist });
  s.addShape(pres.shapes.OVAL, { x: 7.65, y: 0.75, w: 5.6, h: 5.6, fill: { color: K.white }, line: { color: K.white }, objectName: "hook-backdrop" });
  await img(s, I.hookCrowd(), 7.9, 1.0, 5.1, "Magnifier finding three viruses among bacteria and debris");
  s.addNotes(`[0:20] Imagine looking for three specific viruses in a sample that contains a trillion bacteria per gram, food remains, bile, salts and pigments — and you need the answer in minutes, not days. That is my PhD in one sentence. Today I'll show you how I'm trying to build such a test, and the surprise that changed my plan along the way.`);

  // ---------- 2. Recap ----------
  s = add("Content", "Opening");
  s.addText("Recap: safe donors need a faster virus check", { placeholder: "title" });
  await img(s, I.recapTimeline(), 0.7, 1.75, 9.3, "Timeline: central-lab PCR takes days versus a 15-minute rapid test");
  chip(s, 10.3, 1.75, 2.45, 2.0, "The gap", "A test that can run at every donation, on site, in minutes", K.mist, K.coral);
  T(s, "FMT works — but every donation must be pathogen-free, and today's screening is slow and periodic.", { x: 0.7, y: 5.6, w: 11.9, h: 0.8, fontSize: 18, color: K.slate, italic: true });
  s.addNotes(`[0:40] Quick reminder from last time: in faecal microbiota transplantation, stool from a healthy donor becomes a medicine, so every donation must be free of pathogens. Today donors are screened with PCR panels in a central lab. That takes days, and it only tells you about the sample you tested — not the next donation. What's missing is a test that can run at every donation, on site, in minutes.`);

  // ---------- 3. Bigger picture ----------
  s = add("Content", "Opening");
  s.addText("The bigger problem: detection in messy samples", { placeholder: "title" });
  const apps = [["Clinical", "stool, blood, saliva"], ["Food", "e.g. norovirus in shellfish"], ["Environment", "wastewater surveillance"]];
  apps.forEach(([h, b], i) => chip(s, 0.6, 1.7 + i * 1.25, 3.6, 1.05, h, b));
  T(s, "Same challenge everywhere: a rare target in a crowded, variable matrix", { x: 0.6, y: 5.55, w: 3.6, h: 1.0, fontSize: 15, color: K.slate, italic: true });
  await img(s, I.antibodyVsAptamer(), 4.6, 1.7, 8.1, "Antibody versus aptamer comparison");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 4.6, y: 5.75, w: 8.1, h: 0.85, rectRadius: 0.1, fill: { color: K.navy }, line: { color: K.navy } });
  T(s, "Most aptamer sensors are characterised in clean buffer; few are tested in stool  [add ref]", { x: 4.8, y: 5.75, w: 7.7, h: 0.85, fontSize: 16, color: K.white, valign: "middle", bold: true });
  s.addNotes(`[1:00] This is not just an FMT problem. Clinical diagnostics, food safety and wastewater surveillance all face the same challenge: find a rare target in a crowded, variable matrix. Rapid tests usually rely on antibodies. I use aptamers — short DNA strands that fold into a 3D shape and bind a target. They are made chemically, so every batch is identical; they're cheap, stable and easy to label. But here's the catch relevant to the field: most published aptamer sensors are characterised in clean buffer. Far fewer are tested in real samples like stool. That gap is where my project sits.`);

  // ---------- 4. Roadmap ----------
  pres.addSection({ title: "Roadmap" });
  s = add("Content", "Roadmap");
  s.addText("Three work packages, one question each", { placeholder: "title" });
  s.addShape(pres.shapes.LINE, { x: 1.9, y: 3.15, w: 9.5, h: 0, line: { color: K.tealL, width: 4, dashType: "dash" } });
  const wps = [
    ["WP1", "Does a donor's virome change over time?", "→ why we need a rapid test", K.teal],
    ["WP2", "Which aptamer binds best — in buffer and in stool?", "→ choosing the binder", K.coral],
    ["WP3", "Can it work on a paper strip?", "→ the rapid test itself", K.violet],
  ];
  wps.forEach(([n, q, why, col], i) => {
    const x = 1.0 + i * 4.1;
    s.addShape(pres.shapes.OVAL, { x: x + 0.9, y: 2.35, w: 1.6, h: 1.6, fill: { color: col }, line: { color: K.white, width: 4 }, objectName: `roadmap-${n}` });
    T(s, n, { x: x + 0.9, y: 2.35, w: 1.6, h: 1.6, fontSize: 26, bold: true, color: K.white, align: "center", valign: "middle" });
    T(s, q, { x, y: 4.3, w: 3.4, h: 1.0, fontSize: 19, bold: true, align: "center" });
    T(s, why, { x, y: 5.35, w: 3.4, h: 0.5, fontSize: 15, color: K.slate, align: "center", italic: true });
  });
  s.addNotes(`[0:20] My project has three work packages. WP1 asks whether a donor's viruses change over time — which tells us how often we need to test. WP2 asks which aptamer is the best binder, in buffer and in stool. And WP3 turns the winner into a paper-strip test.`);

  // ---------- 5. WP1 design ----------
  pres.addSection({ title: "WP1" });
  s = add("Content", "WP1");
  s.addText("WP1: Is a donor's virome stable over time?", { placeholder: "title" });
  progress(s, 1);
  await img(s, I.wp1Calendar(), 0.5, 1.6, 7.4, "Donors sampled repeatedly over time");
  chip(s, 8.3, 1.6, 4.4, 1.25, "Design", "Same donors, stool sampled repeatedly over [weeks / months]");
  chip(s, 8.3, 3.0, 4.4, 1.25, "Measure", "Enteric viruses: presence, load, diversity  [method: qPCR / sequencing]");
  chip(s, 8.3, 4.4, 4.4, 1.25, "Status", "[n donors × n time points] — sampling & analysis ongoing", K.mist, K.coral);
  T(s, "Results not yet available — next slide shows the hypothesis, not data", { x: 0.6, y: 6.2, w: 11, h: 0.4, fontSize: 14, color: K.slate, italic: true });
  s.addNotes(`[1:10] WP1 is a longitudinal study. We follow the same donors and collect stool repeatedly over [time frame]. In each sample we look for enteric viruses — whether they're present, how much, and how diverse — using [method]. We're currently at [status]. I don't have results yet, so on the next slide I'll show you what we expect and why it matters.`);

  // ---------- 6. WP1 hypothesis ----------
  s = add("Content", "WP1");
  s.addText("Hypothesis: negative today ≠ negative next week", { placeholder: "title" });
  progress(s, 1);
  await img(s, I.wp1Hypothesis(), 0.6, 1.55, 8.0, "Hypothetical timeline of one donor with virus appearing and disappearing");
  const steps = ["Viral shedding is intermittent", "→ one screen is not enough", "→ test every donation", "→ the test must be rapid & cheap"];
  steps.forEach((t, i) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.0, y: 1.7 + i * 1.1, w: 3.75, h: 0.85, rectRadius: 0.1, fill: { color: i === 3 ? K.teal : K.mist }, line: { color: i === 3 ? K.teal : K.mist } });
    T(s, t, { x: 9.15, y: 1.7 + i * 1.1, w: 3.5, h: 0.85, fontSize: 16, bold: i === 3, color: i === 3 ? K.white : K.navy, valign: "middle" });
  });
  T(s, "Illustration only — WP1 will test this hypothesis", { x: 0.6, y: 6.2, w: 8, h: 0.4, fontSize: 14, color: K.slate, italic: true });
  s.addNotes(`[0:40] Our hypothesis: a donor who tests negative today might shed a virus next week — shedding can be intermittent, often without symptoms. If WP1 confirms this, one screen per donor is not enough. You'd want to test every donation, and that is only realistic if the test is rapid and cheap. That's what WP2 and WP3 are about.`);

  // ---------- 7. WP2 question ----------
  pres.addSection({ title: "WP2" });
  s = add("Content", "WP2");
  s.addText("WP2: Which aptamer binds best — even in stool?", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.aptamerLineup(), 0.6, 1.6, 8.3, "Four candidate aptamers and buffer versus stool");
  chip(s, 9.3, 1.6, 3.45, 1.25, "Affinity", "How tightly? (Kd)");
  chip(s, 9.3, 3.0, 3.45, 1.25, "Specificity", "Only the target virus?");
  chip(s, 9.3, 4.4, 3.45, 1.25, "Robustness", "Same answer in stool?", K.mist, K.coral);
  T(s, "Candidates: [Apt-A … Apt-D: names / sources]  ·  Target: [virus / protein]", { x: 0.6, y: 6.2, w: 11, h: 0.4, fontSize: 14, color: K.slate, italic: true });
  s.addNotes(`[1:00] For [target], several aptamers have been published — I'm comparing [number] of them. They differ in sequence, in shape and in where they came from. To pick a winner I need three things: affinity — how tightly they bind; specificity — they shouldn't grab other viruses; and robustness — does the ranking hold when we move from clean buffer into stool? That last question is the one nobody has really answered.`);

  // ---------- 8. Why ELISA ----------
  s = add("Content", "WP2");
  s.addText("First approach: an ELISA-style plate assay", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.elisaWell(false), 0.6, 1.6, 6.6, "ELISA well: coated target, biotinylated aptamer, HRP colour readout");
  chip(s, 7.7, 1.6, 5.0, 1.15, "Familiar & available", "Standard lab method, plates and readers in-house");
  chip(s, 7.7, 2.95, 5.0, 1.15, "Many conditions at once", "96 wells → aptamers × buffers in one run");
  chip(s, 7.7, 4.3, 5.0, 1.15, "Colour readout", "Like the final strip test");
  T(s, "target coated → labelled aptamer binds → wash → enzyme makes colour", { x: 0.6, y: 6.2, w: 6.6, h: 0.4, fontSize: 14, color: K.slate, italic: true, align: "center" });
  s.addNotes(`[0:50] My first choice was an ELISA-style assay: coat the target in a plate, add the labelled aptamer, wash, and let an enzyme make colour. It's familiar, everything is in the lab, I can test many aptamers and buffers in one plate, and the colour readout resembles what the final strip will do. It seemed perfect.`);

  // ---------- 9. Plot twist ----------
  s = add("Content", "WP2");
  s.addText("Plot twist: ELISA measured the assay, not the aptamer", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.elisaWell(true), 0.6, 1.6, 5.6, "ELISA well with weak patchy signal");
  const probs = [
    ["Surface changes the players", "Coated target / tethered aptamer may not fold or bind as in solution"],
    ["Washing removes fast binders", "Aptamers with fast off-rates are lost — affinity underestimated"],
    ["Each aptamer wants its own buffer", "Salt & Mg²⁺ change folding; one wash buffer is unfair to some"],
    ["Stool raises background", "Blocking agents and matrix stick to the plate and the DNA"],
  ];
  probs.forEach(([h, b], i) => {
    const y = 1.6 + i * 1.18;
    s.addShape(pres.shapes.OVAL, { x: 6.6, y: y + 0.12, w: 0.6, h: 0.6, fill: { color: K.coral }, line: { color: K.coral } });
    T(s, String(i + 1), { x: 6.6, y: y + 0.12, w: 0.6, h: 0.6, fontSize: 18, bold: true, color: K.white, align: "center", valign: "middle" });
    T(s, [{ text: h, options: { bold: true, fontSize: 17, breakLine: true } }, { text: b, options: { fontSize: 15, color: K.slate } }], { x: 7.4, y, w: 5.4, h: 1.05 });
  });
  T(s, "[Optional: add your ELISA result — e.g. low signal / no ranking / high stool background]", { x: 0.6, y: 6.3, w: 11.5, h: 0.4, fontSize: 14, color: K.slate, italic: true });
  s.addNotes(`[1:20] And then the plot twist. The signals were [weak / inconsistent], and the ranking of the aptamers didn't make sense. Looking closer, ELISA has four problems for this question. One: the surface. Immobilising the target or the aptamer can change how they fold and bind. Two: washing. Aptamers often bind and release quickly, so the washes remove exactly the binders I want to measure. Three: buffer. Each aptamer was selected in its own salt conditions — magnesium, potassium — and one shared wash buffer is unfair to some of them. Four: stool adds background. So ELISA was telling me more about the assay than about the aptamers.`);

  // ---------- 10. FP ----------
  s = add("Content", "WP2");
  s.addText("The fix: fluorescence polarization, binding in solution", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.fpPrinciple(), 0.5, 1.55, 7.6, "Fluorescence polarization principle: free aptamer tumbles fast, bound aptamer slowly");
  const conc = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000];
  const fit = (kd) => conc.map((x) => Math.round(40 + (160 * x) / (kd + x)));
  s.addChart(pres.charts.LINE, [
    { name: "Apt-A (Kd 5 nM)", labels: conc.map(String), values: fit(5) },
    { name: "Apt-B (Kd 80 nM)", labels: conc.map(String), values: fit(80) },
  ], {
    x: 8.35, y: 1.5, w: 4.5, h: 3.5, chartColors: ["138A8A", "E85D4A"], lineSize: 3, lineDataSymbolSize: 6,
    showTitle: true, title: "Illustrative binding curves", titleFontSize: 14, titleColor: "1B2A41", titleFontFace: "+mn-lt",
    showLegend: true, legendPos: "b", legendFontSize: 11, legendFontFace: "+mn-lt",
    showCatAxisTitle: true, catAxisTitle: "[target] (nM, log steps)", catAxisTitleFontSize: 11, catAxisLabelFontSize: 10, catAxisLabelColor: "5C6B7D", catAxisLabelFontFace: "+mn-lt", catAxisTitleColor: "5C6B7D",
    showValAxisTitle: true, valAxisTitle: "polarization (mP)", valAxisTitleFontSize: 11, valAxisLabelFontSize: 10, valAxisLabelColor: "5C6B7D", valAxisLabelFontFace: "+mn-lt", valAxisTitleColor: "5C6B7D",
    valAxisMinVal: 0, valAxisMaxVal: 220, valGridLine: { color: "E1E7EC", size: 0.5 }, catGridLine: { style: "none" },
  });
  const pros = [["No surface", "aptamer folds freely"], ["No washes", "equilibrium Kd"], ["Mix & read", "minutes, any buffer"], ["Ratiometric", "tolerant to dilute stool"]];
  pros.forEach(([h, b], i) => chip(s, 0.5 + i * 3.1, 5.35, 2.85, 1.15, h, b));
  s.addNotes(`[1:20] So I switched to fluorescence polarization. The idea is simple: attach a small dye to the aptamer and excite it with polarized light. A free aptamer is small and tumbles fast, so the emitted light is scrambled — low polarization. When it binds the much bigger virus, it tumbles slowly and the light stays polarized — high polarization. Everything happens in solution: no surface, no washes, just mix and read. I can titrate the target, get a real equilibrium Kd for each aptamer, and do it in each aptamer's preferred buffer, in a common buffer, and in diluted stool. These curves are illustrative — [first FP data: …].`);

  // ---------- 11. WP3 ----------
  pres.addSection({ title: "WP3" });
  s = add("Content", "WP3");
  s.addText("WP3: The winning aptamer goes onto a paper strip", { placeholder: "title" });
  progress(s, 3);
  await img(s, I.lfaStrip(), 1.15, 1.55, 11.0, "Lateral flow strip: sample pad, conjugate pad, membrane with test and control lines, absorbent pad");
  const w3 = [["1  Pick", "best aptamer from FP, in stool"], ["2  Build", "aptamer–gold conjugate + test line"], ["3  Validate", "spiked & real donor stool vs PCR"]];
  w3.forEach(([h, b], i) => chip(s, 0.7 + i * 4.05, 5.75, 3.75, 0.95, h, b, K.mist, K.violet));
  s.addNotes(`[1:00] In WP3 the winning aptamer goes onto a lateral flow strip — the same format as a pregnancy or COVID test. The stool extract flows along the strip, picks up aptamer-coated gold nanoparticles, and if the virus is there, a red test line appears. The plan: pick the best aptamer from the FP comparison, build the strip, and validate it with spiked and real donor samples against PCR. The goal is a result in about fifteen minutes, read by eye.`);

  // ---------- 12. Take-home ----------
  pres.addSection({ title: "Close" });
  s = add("Dark", "Close");
  s.addText("Take-home", { placeholder: "title" });
  const th = [
    ["WP1", "If virus shedding fluctuates, donors need testing at every donation"],
    ["WP2", "Compare aptamers in solution and in the real matrix — the method shapes the answer"],
    ["WP3", "Turn the winner into a 15-minute strip test"],
  ];
  th.forEach(([n, t], i) => {
    s.addShape(pres.shapes.OVAL, { x: 0.7, y: 2.75 + i * 1.05, w: 0.75, h: 0.75, fill: { color: [K.teal, K.coral, K.violet][i] }, line: { color: K.navy } });
    T(s, n, { x: 0.7, y: 2.75 + i * 1.05, w: 0.75, h: 0.75, fontSize: 13, bold: true, color: K.white, align: "center", valign: "middle" });
    T(s, t, { x: 1.7, y: 2.75 + i * 1.05, w: 5.6, h: 0.75, fontSize: 18, color: K.white, valign: "middle" });
  });
  T(s, "Beyond FMT: any rapid test in a messy sample needs binders validated in that sample.", { x: 0.7, y: 6.0, w: 6.6, h: 0.7, fontSize: 16, color: K.tealL, italic: true });
  s.addShape(pres.shapes.OVAL, { x: 7.95, y: 1.0, w: 4.9, h: 4.9, fill: { color: K.white }, line: { color: K.white } });
  await img(s, I.hookCrowd(), 8.15, 1.2, 4.5, "Magnifier finding viruses in a crowded sample");
  T(s, "The salt saga in detail → my poster [#__]", { x: 7.95, y: 6.15, w: 4.9, h: 0.5, fontSize: 16, color: K.sun, bold: true, align: "center" });
  s.addNotes(`[0:50] To wrap up: WP1 will tell us whether donors need testing at every donation. WP2 taught me that how you measure aptamer binding shapes the answer — so I compare them in solution and in the real matrix. WP3 turns the winner into a fifteen-minute strip. And beyond FMT: any rapid test that has to work in a messy sample needs binders that were validated in that sample. Back to the magnifying glass — finding a few viruses in a crowded sample, fast. If you want the full story of why salt makes this so tricky, come to my poster.`);

  // ---------- 13. Thanks ----------
  s = add("Dark", "Close");
  s.addText("Thank you — questions?", { placeholder: "title" });
  T(s, "[Supervisors]  ·  [Lab members]  ·  [Collaborators / stool bank]  ·  [Funding]", { x: 0.7, y: 4.4, w: 11.5, h: 0.6, fontSize: 18, color: K.mist });
  T(s, "[email]", { x: 0.7, y: 5.2, w: 6, h: 0.4, fontSize: 16, color: K.tealL });
  s.addNotes(`[0:10] Thank you — I'm happy to take questions.`);

  // ---------- Backups ----------
  pres.addSection({ title: "Backup" });
  s = add("Content", "Backup");
  s.addText("Backup: how FP becomes a Kd", { placeholder: "title" });
  T(s, [
    { text: "Polarization", options: { bold: true, color: K.teal, breakLine: true } },
    { text: "P = (I∥ − G·I⊥) / (I∥ + G·I⊥)      (reported as mP = 1000·P)", options: { breakLine: true } },
    { text: "Anisotropy  r = (I∥ − G·I⊥) / (I∥ + 2G·I⊥)", options: { breakLine: true } },
    { text: " ", options: { breakLine: true } },
    { text: "Fraction bound (ligand depletion, aptamer L, target T)", options: { bold: true, color: K.teal, breakLine: true } },
    { text: "f = [(L+T+Kd) − √((L+T+Kd)² − 4·L·T)] / (2·L)", options: { breakLine: true } },
    { text: "r_obs = r_free + f·(r_bound − r_free)      (correct for brightness change on binding if needed)", options: { breakLine: true } },
    { text: " ", options: { breakLine: true } },
    { text: "Controls", options: { bold: true, color: K.teal, breakLine: true } },
    { text: "scrambled aptamer · dye-only · stool-only blank (scatter/autofluorescence) · unlabelled competition" },
  ], { x: 0.7, y: 1.6, w: 12, h: 4.8, fontSize: 18, paraSpaceAfter: 6 });

  s = add("Content", "Backup");
  s.addText("Backup: aptamer candidates", { placeholder: "title" });
  const hdr = ["Aptamer", "Target", "Length", "SELEX buffer", "Reported Kd (method)", "Reference"].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: "1B2A41" } } }));
  const rows = ["A", "B", "C", "D"].map((n) => [`Apt-${n}`, "[ ]", "[ ] nt", "[ ]", "[ ] nM ([ ])", "[ ]"]);
  s.addTable([hdr, ...rows], { x: 0.7, y: 1.6, w: 11.9, colW: [1.5, 2.0, 1.2, 2.6, 2.6, 2.0], fontSize: 15, color: "1B2A41", border: { type: "solid", pt: 0.75, color: "C9D3DC" }, rowH: 0.6, fontFace: "Calibri" });

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
