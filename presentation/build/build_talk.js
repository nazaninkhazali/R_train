// Builds ../retreat_talk.pptx (clean scientific style, 16:9).
// Content follows the user's source document; [square brackets] = still to fill in.
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
  pres.title = "From molecular recognition to a rapid test — PhD retreat";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;
  const K = { navy: C.text1, slate: C.text2, white: C.background1, mist: C.background2, teal: C.accent1, coral: C.accent2, sun: C.accent3, violet: C.accent4, tealL: C.accent5, brown: C.accent6 };

  pres.defineSlideMaster({
    title: "Dark",
    background: { color: K.navy },
    objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.7, y: 1.5, w: 6.6, h: 2.6, fontSize: 42, bold: true, color: K.white, valign: "top", align: "left" }, text: "" } }],
  });
  pres.defineSlideMaster({
    title: "Content",
    background: { color: K.white },
    objects: [{ placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 10.2, h: 1.0, fontSize: 32, bold: true, color: K.navy, valign: "middle", align: "left", margin: 0 }, text: "" } }],
    slideNumber: { x: 12.4, y: 7.0, w: 0.6, h: 0.3, fontSize: 11, color: K.slate },
  });

  const img = async (slide, ill, x, y, w, name) => {
    const h = (w * ill.h) / ill.w;
    slide.addImage({ data: "image/png;base64," + (await I.toPng(ill, 2200)).toString("base64"), x, y, w, h, altText: name, objectName: name });
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
  const QUESTION = "The donor has been screened — but what about the donation made today?";

  // ---------- 1. Title ----------
  pres.addSection({ title: "The problem" });
  let s = add("Dark", "The problem");
  s.addText(QUESTION, { placeholder: "title" });
  T(s, "A rapid aptamer-based test for enteric viruses in FMT donor stool", { x: 0.7, y: 4.4, w: 6.4, h: 0.8, fontSize: 21, color: K.tealL });
  T(s, "[Your name]  ·  [Lab / supervisors]  ·  PhD Retreat 2026", { x: 0.7, y: 6.4, w: 6.4, h: 0.4, fontSize: 15, color: K.mist });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.5, y: 2.3, w: 5.3, h: 2.6, rectRadius: 0.2, fill: { color: K.white }, line: { color: K.white } });
  await img(s, I.donationChain(), 7.7, 2.5, 4.9, "Donor, donations over time with today's unmarked, and patient");
  s.addNotes(`[0:25] I want to start with the question that drives my whole project: the donor has been screened — but what about the donation made today? To explain why that question matters, let me set the scene.`);

  // ---------- 2. FMT / active ingredient ----------
  s = add("Content", "The problem");
  s.addText("The donation cannot be sterilised — the microbes are the medicine", { placeholder: "title" });
  await img(s, I.activeIngredient(), 0.7, 1.75, 7.2, "Living microbial community that cannot be sterilised");
  chip(s, 8.3, 1.75, 4.4, 1.6, "FMT in one line", "A healthy donor's gut microbiota is transferred to a patient");
  chip(s, 8.3, 3.55, 4.4, 1.6, "Who receives it", "Often elderly, on antibiotics or immunocompromised — an infection passed on can be serious", K.mist, K.coral);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.3, y: 5.35, w: 4.4, h: 1.25, rectRadius: 0.12, fill: { color: K.navy }, line: { color: K.navy } });
  T(s, "So the donor screen is the main safety barrier", { x: 8.5, y: 5.35, w: 4.0, h: 1.25, fontSize: 18, bold: true, color: K.white, valign: "middle" });
  s.addNotes(`[0:50] Faecal microbiota transplantation transfers a healthy donor's gut microbiota to a patient. The recipients are often elderly, on antibiotics or immunocompromised, so an infection passed on through the donation can be serious. And here is the thing that makes this different from most other transplanted material: you cannot sterilise it. The living microbial community is the active ingredient — if you kill it, you have no medicine. That means the donor screen is the main safety barrier.`);

  // ---------- 3. How donors are screened + the gap ----------
  s = add("Content", "The problem");
  s.addText("Screening brackets a donation period — the donations in between are untested", { placeholder: "title" });
  await img(s, I.screeningGap(), 0.5, 1.5, 9.2, "Screening at both ends of an interval with a shedding episode in between");
  chip(s, 9.9, 1.5, 2.85, 1.9, "Before donating", "Questionnaire on health, medication, symptoms, travel, exposure + blood and stool tests");
  chip(s, 9.9, 3.6, 2.85, 1.6, "Then", "Screened at the start of the period, re-assessed at the end [schedule varies by stool bank]");
  chip(s, 9.9, 5.4, 2.85, 1.5, "The gap", "A donor can acquire a virus, shed it, and recover between the two tests", K.mist, K.coral);
  s.addNotes(`[1:10] So how are donors screened? Before someone becomes a donor they fill in a questionnaire about health, medication, symptoms, travel and possible exposure to infection, and then blood and stool samples are tested for relevant pathogens. But passing those tests does not guarantee that every later donation is free from infection. In the workflow I'm discussing, testing brackets a donation period: donors are screened at the beginning and re-assessed at the end, and the exact schedule varies between stool banks. Between those two points a donor could acquire an enteric virus, shed it in a donation, and recover before the next assessment. They might even shed without any symptoms. The donor has been screened — but the donation made today has not been tested.`);

  // ---------- 4. Why RT-qPCR doesn't close it ----------
  s = add("Content", "The problem");
  s.addText("RT-qPCR is excellent — but not for every single donation", { placeholder: "title" });
  const pcr = [["Sensitive", "detects very low viral loads"], ["Specific", "identifies the virus precisely"]];
  pcr.forEach(([h, b], i) => chip(s, 0.7, 1.8 + i * 1.4, 5.5, 1.2, h, b, K.mist, K.teal));
  const cost = [["Sample preparation", "extraction, reagents, hands-on time"], ["Equipment & trained staff", "a laboratory, not a donation room"], ["Time", "the donation waits for the result"]];
  cost.forEach(([h, b], i) => chip(s, 6.8, 1.8 + i * 1.4, 5.9, 1.2, h, b, K.mist, K.coral));
  T(s, "That is exactly why screening happens at intervals rather than per donation", { x: 0.7, y: 6.1, w: 12, h: 0.6, fontSize: 19, bold: true, color: K.navy });
  s.addNotes(`[0:45] Why don't we simply test every donation with the confirmatory method? RT-qPCR is sensitive and specific — it is the right tool for a definitive answer. But it needs sample preparation, equipment, trained staff and time. It is not practical to run on every single donation, and that is precisely why screening happens at intervals instead.`);

  // ---------- 5. Triage, not a verdict ----------
  s = add("Content", "The problem");
  s.addText("What a rapid test adds: triage, not a verdict", { placeholder: "title" });
  await img(s, I.triageFunnel(), 1.9, 1.5, 9.5, "Every donation screened rapidly; flagged ones go to RT-qPCR");
  s.addNotes(`[0:50] So what would a rapid test actually add? A fast, simple test applied donation by donation could flag suspicious donations for further testing before they are used. I want to be precise about this, because it is easy to oversell: it would not replace laboratory confirmation, and it would not declare a donation safe by itself. Its job is triage — narrowing the window in which an infected donation can go unnoticed.`);

  // ---------- 6. Why norovirus ----------
  s = add("Content", "The problem");
  s.addText("Why norovirus", { placeholder: "title" });
  await img(s, I.norovirusFacts(), 0.6, 1.5, 9.5, "Norovirus: low infectious dose, high shedding, silent shedding, prolonged in immunocompromised");
  chip(s, 10.4, 1.5, 2.35, 1.9, "Major cause", "of acute gastroenteritis");
  chip(s, 10.4, 3.6, 2.35, 1.9, "Rapid antigen tests", "perform poorly for it compared with other enteric viruses", K.mist, K.coral);
  chip(s, 10.4, 5.7, 2.35, 1.3, "Aptamers exist", "several published candidates", K.mist, K.violet);
  s.addNotes(`[1:00] Why norovirus? It is a major cause of acute gastroenteritis and a good example of exactly this problem. It can be shed in very large quantities, it needs a very low infectious dose, and it can be shed without symptoms or after someone has recovered. In immunocompromised recipients, infection may become prolonged. On top of that, existing rapid antigen tests perform poorly for norovirus compared with other enteric viruses — so there is a real gap to fill. And conveniently, several aptamers already exist that could serve as recognition elements.`);

  // ---------- 7. Roadmap ----------
  pres.addSection({ title: "Roadmap" });
  s = add("Content", "Roadmap");
  s.addText("Three work packages", { placeholder: "title" });
  s.addShape(pres.shapes.LINE, { x: 1.9, y: 3.15, w: 9.5, h: 0, line: { color: K.tealL, width: 4, dashType: "dash" } });
  const wps = [
    ["WP1", "How much does the viral picture change across the interval?", "how large is the gap", K.teal],
    ["WP2", "How do our aptamers recognise the virus — in buffer and in stool?", "the recognition", K.coral],
    ["WP3", "Can that recognition become a visible line on a strip?", "the test", K.violet],
  ];
  wps.forEach(([n, q, why, col], i) => {
    const x = 1.0 + i * 4.1;
    s.addShape(pres.shapes.OVAL, { x: x + 0.9, y: 2.35, w: 1.6, h: 1.6, fill: { color: col }, line: { color: K.white, width: 4 }, objectName: `roadmap-${n}` });
    T(s, n, { x: x + 0.9, y: 2.35, w: 1.6, h: 1.6, fontSize: 26, bold: true, color: K.white, align: "center", valign: "middle" });
    T(s, q, { x, y: 4.3, w: 3.4, h: 1.1, fontSize: 18, bold: true, align: "center" });
    T(s, why, { x, y: 5.5, w: 3.4, h: 0.5, fontSize: 15, color: K.slate, align: "center", italic: true });
  });
  s.addNotes(`[0:20] My project has three work packages. First, measure how much the viral picture actually changes across a screening interval. Second, understand how aptamers recognise the virus, in buffer and then in stool. Third, turn that recognition into a test.`);

  // ---------- 8. WP1 ----------
  pres.addSection({ title: "WP1" });
  s = add("Content", "WP1");
  s.addText("WP1: how much changes inside the interval?", { placeholder: "title" });
  progress(s, 1);
  await img(s, I.wp1Sampling(), 0.5, 1.6, 8.0, "Same donor sampled repeatedly across one screening interval");
  chip(s, 8.8, 1.6, 3.95, 1.5, "Design", "Stool samples from the same person across a screening interval");
  chip(s, 8.8, 3.25, 3.95, 1.5, "Question", "How does the diversity of viruses present change over time?");
  chip(s, 8.8, 4.9, 3.95, 1.8, "Why it matters", "Does the picture at the start still describe the donations made later?", K.mist, K.coral);
  T(s, "Planned — [n donors × n time points, method]. This tells us how large the gap really is.", { x: 0.5, y: 6.3, w: 8.0, h: 0.5, fontSize: 15, color: K.slate, italic: true });
  s.addNotes(`[1:00] We do not yet know how much changes inside that interval — and that is Work Package 1. We plan to study stool samples collected from the same person across a screening interval, and look at how the diversity of the viruses present changes over time. The point is to find out whether the viral picture at the start of the interval still describes the donations made later. In other words, WP1 measures how large the gap really is. This is planned work, so I have no results to show you yet.`);

  // ---------- 9. WP2a: recognition in buffer ----------
  pres.addSection({ title: "WP2" });
  s = add("Content", "WP2");
  s.addText("WP2: can our aptamers recognise their targets reliably?", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.sixAptamers(), 0.5, 1.75, 8.4, "Six candidate aptamers");
  chip(s, 9.3, 1.6, 3.45, 1.4, "Binding strength", "how tightly each one holds");
  chip(s, 9.3, 3.15, 3.45, 1.4, "Specificity", "the target and not its neighbours");
  chip(s, 9.3, 4.7, 3.45, 1.6, "Genotypes", "for norovirus: can it recognise different genotypes?", K.mist, K.violet);
  T(s, "Start in buffer, where conditions are controlled  ·  Norovirus is the priority; astrovirus, rotavirus and adenovirus aptamers are also investigated", { x: 0.5, y: 5.9, w: 8.4, h: 0.9, fontSize: 16, color: K.slate, italic: true });
  s.addNotes(`[1:00] In WP2 we first ask whether our aptamers can recognise their viral targets reliably. We begin in buffer, where conditions are controlled, and compare the candidates to understand their binding strength, their specificity, and — for norovirus — their ability to recognise different genotypes. Norovirus is our priority, while aptamers for astrovirus, rotavirus and adenovirus are also investigated.`);

  // ---------- 10. WP2b: target models ----------
  s = add("Content", "WP2");
  s.addText("Recognising what, exactly? The target itself is a choice", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.targetModels(), 1.0, 1.75, 11.3, "Virus-like particle, recombinant capsid protein and murine norovirus");
  T(s, "The form of the target influences recognition — so we compare the models rather than assume they agree", { x: 1.0, y: 5.95, w: 11.3, h: 0.7, fontSize: 19, bold: true, color: K.navy, align: "center" });
  s.addNotes(`[0:50] But recognising a target in buffer is only the beginning — and "the target" is not one single thing. We compare different target models: virus-like particles, recombinant capsid protein, and murine norovirus. Each is a different compromise between how easy it is to work with and how close it is to the real virus, and the form of the target influences recognition. So rather than assume they agree, we compare them.`);

  // ---------- 11. WP2c: into stool ----------
  s = add("Content", "WP2");
  s.addText("Then into stool — and the signal drops. Degraded, or interfered with?", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.degradeVsInterfere(), 1.5, 1.5, 9.3, "Signal loss in stool: degradation versus interference, each with its diagnostic");
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 1.5, y: 6.1, w: 9.3, h: 0.85, rectRadius: 0.12, fill: { color: K.navy }, line: { color: K.navy } });
  T(s, "Rather than adjusting conditions until the signal improves, we investigate the mechanism behind the loss", { x: 1.8, y: 6.1, w: 8.7, h: 0.85, fontSize: 18, bold: true, color: K.white, valign: "middle" });
  s.addNotes(`[1:10] Then we move into stool, where the challenge becomes more complex. The signal decreases — but why? Is the aptamer being degraded, or are stool components interfering with its binding? These two explanations look the same on a plate reader, but they call for completely different solutions. So rather than simply adjusting conditions until the signal improves, we investigate the mechanisms behind that loss. Degradation we can test by following the integrity of the aptamer over time; interference we can probe with spike-in and dilution experiments. Understanding which one we are facing should help us identify suitable strategies to preserve aptamer function.`);

  // ---------- 12. Method: FP ----------
  s = add("Content", "WP2");
  s.addText("To compare them fairly, the solution must be the only variable", { placeholder: "title" });
  progress(s, 2);
  await img(s, I.fpPrinciple(), 0.5, 1.5, 7.6, "Fluorescence polarization: free aptamer tumbles fast, bound aptamer slowly");
  const fp = [
    ["Nothing is immobilised", "everything happens in solution"],
    ["No wash step", "one defined buffer from start to finish"],
    ["Equilibrium measurement", "the number we fit means something"],
    ["One plate, many conditions", "ion identity, concentration and pH for every aptamer"],
  ];
  fp.forEach(([h, b], i) => chip(s, 8.35, 1.5 + i * 1.3, 4.4, 1.15, h, b));
  T(s, "Paired with circular dichroism, it helps separate a change in fold from a change at the interface", { x: 0.5, y: 5.95, w: 7.6, h: 0.9, fontSize: 17, color: K.navy, bold: true });
  s.addNotes(`[1:10] All of this needs a method where the solution is the only thing that changes. Fluorescence polarization gives us that. We put a fluorescent tag on the aptamer and excite it with polarized light. The polarization reflects how fast the molecule tumbles: a free aptamer is small and tumbles fast, so polarization is low; bound to the large norovirus particle it tumbles slowly, so polarization rises. That rise is the binding signal. Why it suits this question: everything happens in solution, with nothing immobilised and no surface to stick to. There is no wash step, so the aptamer stays in one defined buffer from start to finish and the measurement is an equilibrium. And the same plate can scan ion identity, concentration and pH for every aptamer under one method. Paired with circular dichroism, it helps us separate a change in fold from a change at the interface. That last point is the subject of my poster.`);

  // ---------- 13. WP3 ----------
  pres.addSection({ title: "WP3" });
  s = add("Content", "WP3");
  s.addText("WP3: turning recognition into a visible line", { placeholder: "title" });
  progress(s, 3);
  await img(s, I.lfaStrip(), 1.15, 1.5, 11.0, "Lateral flow strip anatomy");
  const w3 = [
    ["Immobilise", "aptamers on the membrane"],
    ["Survive drying", "keep binding after the strip dries"],
    ["Gold readout", "nanoparticles make the line visible"],
    ["Benchmark", "LOD vs RT-qPCR and WP1 viral loads"],
  ];
  w3.forEach(([h, b], i) => chip(s, 0.7 + i * 3.15, 5.45, 2.95, 1.1, h, b, K.mist, K.violet));
  T(s, "Minimum objective: a validated norovirus assay.  Next goal: a second test line.  Ambitious extension: naturally positive samples.", { x: 0.7, y: 6.75, w: 12, h: 0.5, fontSize: 15, color: K.slate, italic: true });
  s.addNotes(`[1:00] WP3 takes that knowledge and turns it into a practical detection platform: a lateral flow assay, aiming to translate aptamer–virus binding into a visible coloured signal on a test strip, starting with norovirus. We investigate how to immobilise the aptamers on the membrane, how to preserve their binding after drying, and how to use gold nanoparticles to generate the readout. Then we optimise the assay for stool and assess whether its detection limit is compatible with the viral loads observed in WP1, benchmarking against RT-qPCR. If the results from WP2 support it, we add a test line for a second virus. A validated norovirus assay is the minimum technological objective; multiplex detection is the next goal, and testing on naturally positive samples is the ambitious extension.`);

  // ---------- 14. Take-home ----------
  pres.addSection({ title: "Close" });
  s = add("Dark", "Close");
  s.addText("Take-home", { placeholder: "title" });
  const th = [
    ["WP1", "First measure how the viral picture changes across the interval"],
    ["WP2", "Understand the recognition — in buffer, in stool, and in between"],
    ["WP3", "Then build a test that says something about each donation"],
  ];
  th.forEach(([n, t], i) => {
    s.addShape(pres.shapes.OVAL, { x: 0.7, y: 2.7 + i * 1.05, w: 0.75, h: 0.75, fill: { color: [K.teal, K.coral, K.violet][i] }, line: { color: K.navy } });
    T(s, n, { x: 0.7, y: 2.7 + i * 1.05, w: 0.75, h: 0.75, fontSize: 13, bold: true, color: K.white, align: "center", valign: "middle" });
    T(s, t, { x: 1.7, y: 2.7 + i * 1.05, w: 5.6, h: 0.75, fontSize: 18, color: K.white, valign: "middle" });
  });
  T(s, QUESTION, { x: 0.7, y: 5.95, w: 6.6, h: 1.0, fontSize: 19, color: K.sun, bold: true, italic: true });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.7, y: 2.0, w: 5.1, h: 2.7, rectRadius: 0.2, fill: { color: K.white }, line: { color: K.white } });
  await img(s, I.donationChain(), 7.85, 2.2, 4.8, "Donor, donations over time, patient");
  T(s, "Why salt makes the comparison hard → my poster [#__]", { x: 7.7, y: 5.3, w: 5.1, h: 0.5, fontSize: 16, color: K.tealL, bold: true, align: "center" });
  s.addNotes(`[0:40] To bring it together: we will first measure how the viral picture changes across the screening interval; then understand how our aptamers recognise the virus, in buffer and in stool; and then build a test that can say something about each individual donation — as triage, not as a verdict. Which brings me back to where I started: the donor has been screened — but what about the donation made today? If you want to hear why comparing six aptamers fairly is harder than it sounds, and what salt has to do with it, come to my poster.`);

  // ---------- 15. Thanks ----------
  s = add("Dark", "Close");
  s.addText("Thank you — questions?", { placeholder: "title" });
  T(s, "[Supervisors]  ·  [Lab members]  ·  [Collaborators / stool bank]  ·  [Funding]", { x: 0.7, y: 4.4, w: 11.5, h: 0.6, fontSize: 18, color: K.mist });
  T(s, "[email]", { x: 0.7, y: 5.2, w: 6, h: 0.4, fontSize: 16, color: K.tealL });
  s.addNotes(`[0:10] Thank you — I'm happy to take questions.`);

  // ---------- Backups ----------
  pres.addSection({ title: "Backup" });
  s = add("Content", "Backup");
  s.addText("Backup: how fluorescence polarization becomes a Kd", { placeholder: "title" });
  T(s, [
    { text: "Polarization", options: { bold: true, color: K.teal, breakLine: true } },
    { text: "P = (I∥ − G·I⊥) / (I∥ + G·I⊥)      reported as mP = 1000·P", options: { breakLine: true } },
    { text: "Anisotropy  r = (I∥ − G·I⊥) / (I∥ + 2G·I⊥)", options: { breakLine: true } },
    { text: " ", options: { fontSize: 10, breakLine: true } },
    { text: "Fraction bound (ligand depletion; labelled aptamer L, target T)", options: { bold: true, color: K.teal, breakLine: true } },
    { text: "f = [(L+T+Kd) − √((L+T+Kd)² − 4·L·T)] / (2·L)", options: { breakLine: true } },
    { text: "r_obs = r_free + f·(r_bound − r_free)   — correct for a brightness change on binding if present", options: { breakLine: true } },
    { text: " ", options: { fontSize: 10, breakLine: true } },
    { text: "Controls under matched conditions", options: { bold: true, color: K.teal, breakLine: true } },
    { text: "scrambled sequence · motif mutant · unrelated viral particles · norovirus-negative stool · dye-only blank" },
  ], { x: 0.7, y: 1.6, w: 12, h: 4.8, fontSize: 18, paraSpaceAfter: 6 });

  s = add("Content", "Backup");
  s.addText("Backup: the six aptamer candidates", { placeholder: "title" });
  const hdr = ["Aptamer", "Target", "Selection method", "SELEX buffer", "Published Kd (method)", "Source"].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: "1B2A41" } } }));
  const rows = [1, 2, 3, 4, 5, 6].map((n) => [`Apt-${n}`, "[ ]", "[ ]", "[ ]", "[ ] ([ ])", "[ ]"]);
  s.addTable([hdr, ...rows], { x: 0.7, y: 1.6, w: 11.9, colW: [1.4, 1.9, 2.2, 2.3, 2.3, 1.8], fontSize: 14, color: "1B2A41", border: { type: "solid", pt: 0.75, color: "C9D3DC" }, rowH: 0.52, fontFace: "Calibri" });
  T(s, "Published affinities come from different labs, techniques, targets and buffers — they are not directly comparable, which is why we re-measure all six by one method.", { x: 0.7, y: 6.2, w: 11.9, h: 0.6, fontSize: 15, color: K.slate, italic: true });

  s = add("Content", "Backup");
  s.addText("Backup: what salt does, in one slide", { placeholder: "title" });
  await img(s, I.saltCurve(), 1.6, 1.5, 8.6, "Non-monotonic affinity versus ionic strength");
  T(s, "Folding needs ions; the interface is weakened by them; counterion release adds entropy. The binding we measure belongs to the sequence and its solution together.", { x: 1.6, y: 6.5, w: 8.6, h: 0.7, fontSize: 16, color: K.navy, bold: true });

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
