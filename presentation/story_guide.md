# Retreat talk and poster: story guide

Built from your source document (`poster_and_presentation.docx`). Everything still to fill in is marked `[in brackets]`.

## Files
| File | What it is |
|---|---|
| `retreat_talk.pptx` | 15 slides + 3 backup slides. Script and timing per slide in the speaker notes. |
| `aptamer_poster.pdf` / `.pptx` | A0 portrait, print-ready PDF plus editable source. |
| `build/` | `node build_talk.js`, `node build_poster.js` regenerate both. Needs `NODE_PATH` pointing at a folder with `pptxgenjs` + `sharp`, and `PPTX_SKILL` set. |

---

## The talk

**Spine:** *"The donor has been screened — but what about the donation made today?"* It opens slide 1 and returns word-for-word on the take-home slide.

**Timing** — speaker notes total about 1,240 words, roughly 9.5 minutes spoken. That leaves ~1.5 minutes of slack inside the 11, which you will use on pauses and pointing at figures. Rehearse twice with a timer.

| Time | Beat | Slides |
|---|---|---|
| 0:00–2:25 | The question → FMT can't be sterilised → the screening gap | 1–3 |
| 2:25–4:00 | Why RT-qPCR can't close it → triage, not a verdict | 4–5 |
| 4:00–5:20 | Why norovirus → roadmap | 6–7 |
| 5:20–6:20 | WP1: how much changes inside the interval | 8 |
| 6:20–9:40 | **WP2**: recognition in buffer → which target? → into stool → why FP | 9–12 |
| 9:40–11:00 | WP3 → take-home → thanks | 13–15 |

**Why it's built this way.** The organisers asked for the broader context and for a story non-specialists can follow. So the first six slides are the *problem*, told in plain language, and the work packages only arrive once the audience wants them. The broader relevance is the screening gap itself — a structural problem in any screen-and-quarantine workflow — rather than a generic "rapid tests are useful" claim.

**Delivery notes**
- **Slide 1:** ask the question, then pause. Don't explain it yet.
- **Slide 2:** "you cannot sterilise it — the living community *is* the medicine" is the line that makes the rest inevitable.
- **Slide 5:** say "triage, not a verdict" out loud. It's the claim most likely to be misheard as overselling, and stating the limit makes the rest more credible.
- **Slide 11 (degraded or interfered with?):** your strongest slide. Two explanations, same readout, different fixes. Land the point that you investigate the mechanism rather than tune until the signal looks better.
- **Slide 12:** explain FP with your hands — small and fast scrambles the light, big and slow keeps it aligned.
- **Slide 14:** repeat the opening question, then point at the poster.

**Backup slides:** FP equations and controls; the six-aptamer table; the salt curve (in case someone asks before your poster session).

---

## The poster

**Title:** *Salt prepares the hand and weakens the handshake* — your sentence, and the best one in the document.

Seven panels, numbered in reading order, with the mechanism numbers from your text as subtitles:
1. **Six aptamers, six histories** — why published affinities aren't comparable; an aptamer isn't rigid.
2. **Folding costs charge** (1 · electrostatics of folding) — the ion atmosphere, drawn as a diffuse cloud rather than fixed dots, denser around the folded strand.
3. **…and the same ions weaken the handshake** (2 · the interface) — **the centrepiece**: the non-monotonic affinity-vs-salt curve with the usable window marked, and the two opposing effects as gradient bars beneath. Next to it, the caveat that salt dependence does not count released ions.
4. **Counterion release** (3 · entropy).
5. **Identity, not only amount** (4) — K⁺ in the quadruplex channel, Mg²⁺ competing with monovalents, Cl⁻ vs glutamate.
6. **Specificity** (5) — background at low salt, recognition in the window, weakened binding at high salt, plus your four controls.
7. **Why fluorescence polarisation** (6) — the four reasons, the CD pairing, and your one-line plan.

Then the takeaway sentence and three discussion questions.

**It complements the talk, as required:** no FMT background, no WP1, no shared figures. The talk gives FP four bullet points; the poster gives the physics that makes FP the right choice.

**Standing at the poster:** lead visitors to panel 3 first. The curve is the argument — everything else explains one half of it.

---

## Questions to expect

1. *How many ions are released?* — You deliberately don't claim this. Salt dependence is a clue, not a count: structure, hydration and other contacts contribute. (This is on the poster; it's a good answer to have ready.)
2. *Isn't a salt-sensitive interaction just non-specific?* — No, and that's panel 6. Charge-driven background and real recognition both respond to salt, which is why controls under matched conditions do the work.
3. *Why not surface methods (SPR, ELISA, BLI)?* — Immobilisation adds a surface and, for most formats, a wash. You need the solution to be the only variable.
4. *Why not ITC?* — Sample consumption and throughput; you need to scan many conditions × six aptamers.
5. *Does the fluorophore change binding?* — Label position and an unlabelled competitor control. Worth being upfront that it's a real caveat.
6. *Doesn't stool wreck fluorescence?* — Scatter and autofluorescence are real; dilution series, blanks and red-shifted dyes. Also the reason WP2 asks the degradation-vs-interference question.
7. *Is a rapid test for FMT actually safe?* — Triage, not a verdict. It narrows the window; it never clears a donation.
8. *Why six aptamers and not the best one from the literature?* — Because "best" is not defined across labs, buffers and methods. That's the whole poster.

---

## Still to fill in

**Talk**
You're filling these in yourself — this is just the checklist so none gets missed.

**Talk**
- Slide 1 and 15: your name, lab, supervisors, acknowledgements, email.
- Slide 3: your stool bank's screening schedule, if you want to be concrete.
- Slide 8: number of donors × time points, and the detection method for WP1.
- Slide 13: your LOD target, if you have one.
- Slide 14: poster number.
- Backup slide 17: the six-aptamer table — the columns are laid out, the cells are empty.

**Poster**
- Name, lab, email, QR code (top right).
- Panel 1 labels read "lab A–F". Swap in the real aptamer names if you want them shown; the panel works as it is, since the point is that the six histories differ.

No FP data yet, so nothing on either file claims any: slide 12 explains the method only, and poster panel 7 states the plan. When the first results arrive, poster panel 7 is the place for a figure — say the word and I'll restructure it.
