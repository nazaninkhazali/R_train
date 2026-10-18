# Retreat talk and poster: story guide

## Files
| File | What it is |
|---|---|
| `retreat_talk.pptx` | The 11-minute talk: 13 slides plus 2 backup slides. The script and timing for each slide are in the speaker notes. |
| `aptamer_poster.pdf` / `.pptx` | A0 portrait poster, "Which aptamer wins? It depends on the salt." The PDF is ready to print; the pptx can be edited. |
| `build/` | Scripts that regenerate everything: `node build_talk.js`, `node build_poster.js`. Run them from `build/` with `NODE_PATH` set to a folder that contains `pptxgenjs` and `sharp`, and `PPTX_SKILL` set. |
| `input/` | Put your figures and data here so I can replace the placeholders. |

## The story arc (11 min)
The hook is **"Finding a few viruses in a very crowded sample, fast."** Use it at the start and come back to it at the end.

| Time | Beat | Slides |
|---|---|---|
| 0:00–1:00 | Hook, then a one-slide FMT recap (the audience already knows it) | 1–2 |
| 1:00–2:00 | Bigger picture: messy samples, antibodies vs aptamers, the buffer-only gap in the field | 3 |
| 2:00–4:10 | Roadmap, then WP1: design and hypothesis ("negative today ≠ negative next week") | 4–6 |
| 4:10–8:40 | **WP2, the heart of the talk**: question → ELISA → *plot twist* → FP solution | 7–10 |
| 8:40–9:40 | WP3: the strip test | 11 |
| 9:40–11:00 | Take-home, loop back to the hook, poster teaser, thanks | 12–13 |

The speaker notes are about 950 words, which takes about 7.5 minutes at a calm pace. That leaves about 3 minutes for pauses, pointing at figures, and your own data once you add it. Rehearse with a timer at least twice.

## Delivery tips
- **Slide 1:** pause after the hook sentence. Don't read the title.
- **Slide 9 ("Plot twist"):** this is your most engaging moment. Tell it as a story: "I thought ELISA was perfect… then the data didn't make sense." Audiences love an honest plan B.
- **Slide 10:** explain FP with your hands. A fast-spinning small thing scrambles the light; a big slow thing keeps it aligned.
- Say each slide's headline out loud: the headline *is* the message.
- End on the poster teaser so people come to your poster.

## Likely questions (prepare answers)
1. *Why not just use PCR on site?* Cost, equipment, trained staff and time. Rapid isothermal PCR exists; compare it honestly with your strip test.
2. *Is FP sensitive enough for stool?* FP is for **choosing** the aptamer (measuring Kd), not for the final test. The final test is the LFA.
3. *Does the dye change binding?* Check this with an unlabelled competitor and by comparing labelling at the 5′ and 3′ ends.
4. *Stool autofluorescence and scatter?* Use red-shifted dyes, a stool-only blank, and a dilution series.
5. *Which buffer is "fair"?* Test each aptamer in its own SELEX buffer **and** in a shared buffer. The difference between the two is itself a result.
6. *How many donors and time points in WP1?* Have the numbers ready.

## Poster vs talk (they complement each other, as the organisers asked)
- The poster has **no** FMT background, no roadmap and no WP1. It zooms in on the WP2 challenge: why salt, method and matrix make aptamer comparison hard.
- All poster figures are new cartoon illustrations; none of the talk figures are reused.
- The poster's "Let's discuss!" questions are there to start conversations at your poster.

## Placeholders still to fill (`[…]` in the files)
**Talk**
- Slide 1: your name, lab, supervisors.
- Slide 3: a reference for "most aptamer sensors are characterised in buffer".
- Slide 5: WP1 time frame, detection method, number of donors × time points, status.
- Slide 7: aptamer names and sources, target virus or protein.
- Slide 9: your actual ELISA observation.
- Slide 10: the binding curves are **illustrative**. Replace them with your first FP data if you have it.
- Slide 12: poster number.
- Slide 13: acknowledgements, email.
- Backup slide 15: aptamer table.

**Poster**
- Name, lab, email, QR code (top right).
- Target virus name.
- The "What we saw" column of the ELISA table (panel 4). The current entries are examples; replace them with your real observations.
- Stool dilution ratio.
- Which aptamers are G-quadruplexes (the K⁺ column; currently only Apt-B is marked).
- Example buffer and label details on the "apples vs oranges" scale, which are invented examples. Replace them with your aptamers' real details.
