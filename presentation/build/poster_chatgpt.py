"""
=============================================================================
 SCIENTIFIC POSTER GENERATOR — "Six aptamers. Six numbers. One problem."
 DIN A0 portrait (841 x 1189 mm), built with python-pptx + matplotlib.
=============================================================================

-----------------------------------------------------------------------------
 DESIGN BRIEF  (read this before changing anything)
-----------------------------------------------------------------------------
 WHAT THE POSTER ARGUES
 ----------------------
 The author must choose one of six published DNA aptamers against norovirus
 for a rapid test. The literature reports a dissociation constant (Kd) for
 each, which looks like a ranking. It is not one. The poster proves why, in
 this chain:

   1. Naive expectation : six Kd values -> pick the smallest.
   2. First failure     : an aptamer is not a rigid object. It explores many
                          shapes; only some can bind. What you measure is
                          (fraction in a binding-competent shape) x (how well
                          that shape binds). The SOLUTION sets the first term.
   3. Folding term      : the phosphate backbone is all negative. Folding
                          pulls those charges together = an electrostatic
                          penalty. Counterions gather around the strand (a
                          diffuse, mobile "ion atmosphere", NOT site-bound
                          ions) and screen it. The folded state holds a denser
                          atmosphere than the unfolded one, so folding and ion
                          uptake are COUPLED. More salt -> more folded.
                          => salt HELPS.
   4. Interface term    : the aptamer grips a positively charged patch on the
                          target. That attraction is electrostatic too, and
                          salt screens it just as efficiently.
                          => salt HURTS.
   5. Release term      : before binding, cations crowd the DNA and anions
                          crowd the target's positive patch. On association
                          some are released to bulk solution and gain freedom
                          -> an entropic gain that favours binding. The gain
                          depends on the contrast between local and bulk, so
                          it SHRINKS as bulk salt rises.
                          => salt's bonus FADES.
   6. Sum               : affinity vs ionic strength is therefore a CURVE,
                          typically with a peak, not a single number.
   7. The trap          : each lab selected and measured its aptamer in its
                          own buffer, i.e. at a different, unknown point on
                          its own curve. The published ranking is partly a
                          ranking of whose buffer was luckiest.
   8. Worse             : ion IDENTITY matters separately from concentration
                          (K+ can occupy a structural site in a G-quadruplex;
                          Mg2+ shapes structure and competes with monovalents;
                          even anions differ). Two buffers are not equivalent
                          because both contain "salt".
   9. No easy fix       : one shared buffer standardises the protocol while
                          handicapping whichever aptamers want something else;
                          letting each use its own optimum compares best cases
                          that may not survive a real sample.
  10. Resolution        : measure the CURVE, not the point. Three genuinely
                          comparable quantities then exist - peak height (how
                          good at best), peak position (what it wants), and
                          peak width (how forgiving). Fluorescence
                          polarisation (FP) is the method that lets the
                          solution be the only variable: nothing immobilised,
                          no wash step, equilibrium. Circular dichroism (CD)
                          separates "the fold changed" from "the interface
                          changed".
  11. Honest limit      : the shape of the salt dependence is a CLUE that the
                          interaction is charge-driven. It does NOT count how
                          many ions were released - structure, hydration and
                          other contacts contribute too.

 LAYOUT PRINCIPLE
 ----------------
 The hero figure sits near the TOP, before the mechanism panels. A viewer
 should meet the problem first and the physics second: mechanism is only
 interesting once you want the answer.

 Reading order, top to bottom:
   Zone 1  Title + the one-sentence problem
   Zone 2  HERO figure: "six dots, six curves"  <- carries the whole argument
   Zone 3  Three mechanism panels: folding / interface / release
   Zone 4  The budget figure (three terms -> the observed curve) + ion identity
   Zone 5  What becomes comparable + why FP
   Zone 6  Takeaway + honest caveat + controls

 RULES THAT KEEP IT READABLE (please preserve these when editing)
 ----------------------------------------------------------------
   * Three-distance test. At 3 m: title + hero silhouette. At 1 m: panel
     headings + figures. At 30 cm: body text. Shrink the poster to 10 cm wide;
     if the hero still reads, it works.
   * Word budget: about 700 words for the whole board. No panel over ~60
     words. Cutting text buys figure space.
   * Body text never below 24 pt at A0 (here: 26-30 pt).
   * One visual family: same palette, same line weights, same figure style.
   * Every drawn element must make a claim. Nothing decorative.

 HOW TO EDIT
 -----------
   * Colours and fonts: the PALETTE and FONT constants below.
   * Geometry: the "LAYOUT GEOMETRY" block. Every zone's y-position is derived
     from the previous zone's height, so changing one height reflows the rest.
   * Figures: the three make_fig_*() functions. They are plain matplotlib and
     are saved as PNG, then placed on the slide.
   * Text: each zone is built in its own function, so you can rewrite one zone
     without touching the others.

 DEPENDENCIES
 ------------
   pip install python-pptx matplotlib numpy

 OUTPUT
 ------
   aptamer_problem_poster.pptx   (open in PowerPoint; export to PDF to print)
   fig_hero.png / fig_budget.png / fig_comparable.png  (the figures, reusable)

 NOTE ON THE DATA
 ----------------
 All numbers in the figures are ILLUSTRATIVE and are labelled as such on the
 poster. They show the SHAPE of the argument, not measured results. Replace
 them with real values once the salt titrations are done - see the
 `LITERATURE_POINTS` and `APTAMER_CURVES` tables below.
=============================================================================
"""

import matplotlib
matplotlib.use("Agg")                      # render to file, no screen needed
import matplotlib.pyplot as plt
import numpy as np
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# =============================================================================
# 1. CONFIG — palette, fonts, page geometry
# =============================================================================

# Palette. Keep one dominant colour (INK), one for "helps" (TEAL), one for
# "hurts" (VIOLET), one for the result (CORAL), one highlight (GOLD).
PALETTE = {
    "bg":     "EEF4F4",   # pale background of the whole board
    "card":   "FFFFFF",   # panel fill
    "ink":    "1B2A41",   # all body text, dark bands
    "slate":  "5C6B7D",   # secondary text, axis labels
    "teal":   "138A8A",   # the FOLDING term (salt helps)
    "violet": "7A5BA6",   # the INTERFACE term (salt hurts)
    "gold":   "E9B23C",   # the RELEASE term / highlights
    "coral":  "E85D4A",   # the RESULTING affinity curve, and "the problem"
    "line":   "C9D3DC",   # hairlines, borders
}
def rgb(key):
    """'1B2A41' -> RGBColor. Accepts a palette key or a raw hex string."""
    h = PALETTE.get(key, key)
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))
def hx(key):
    """Palette key -> '#RRGGBB' for matplotlib."""
    return "#" + PALETTE.get(key, key)

FONT = "Calibri"        # safe on Windows/Mac/Office. Swap for a brand font.

# --- LAYOUT GEOMETRY (inches) ------------------------------------------------
# A0 portrait = 841 x 1189 mm = 33.11 x 46.81 in.
W, H = 33.11, 46.81
M     = 1.0                     # outer margin
GAP   = 0.45                    # gap between zones and between panels
FULL  = W - 2 * M               # usable content width
COL3  = (FULL - 2 * GAP) / 3    # width of a three-column panel
COL2  = (FULL - GAP) / 2        # width of a two-column panel

# Zone heights. Change one and everything below reflows, because each zone's
# y is computed from the running cursor in build_poster().
H_TITLE  = 3.9
H_HERO   = 13.6
H_MECH   = 7.4
H_BUDGET = 7.6
H_COMP   = 6.4
# Running total: 0.8 + 3.9 + (13.6+GAP) + (7.4+GAP) + (7.6+GAP) + (6.4+GAP)
# = 41.5 in, leaving ~4.3 in for zone 6 down to the bottom margin. If you make
# a zone taller, take the inches from another one or zone 6 will overflow.
# Zone 6 (takeaway) simply fills whatever is left down to the bottom margin.


# =============================================================================
# 2. THE DATA BEHIND THE FIGURES
# =============================================================================
# Each aptamer: a label, the lab it came from, the ionic strength (mM) at which
# that lab happened to measure it, where ITS OWN optimum sits (mM), how good it
# is at that optimum (arbitrary affinity units), and how forgiving it is
# (width, in log10 units — larger = flatter response).
#
# REPLACE THESE with your real aptamers once you have them. The figure code
# does not care how many rows there are.
APTAMER_CURVES = [
    # label,    lab,     measured_at, optimum, peak_height, width
    ("Apt-1",  "lab A",      50,        140,      0.92,     0.42),
    ("Apt-2",  "lab B",     150,        160,      0.78,     0.30),
    ("Apt-3",  "lab C",     300,         90,      0.85,     0.26),
    ("Apt-4",  "lab D",     100,        320,      0.95,     0.38),
    ("Apt-5",  "lab E",     200,        200,      0.66,     0.50),
    ("Apt-6",  "lab F",      75,         70,      0.73,     0.34),
]
# One colour per aptamer, so a dot in panel A and its curve in panel B match.
CURVE_COLOURS = ["coral", "teal", "violet", "gold", "slate", "ink"]


def affinity(ionic_mM, optimum, height, width):
    """
    Illustrative model of affinity (1/Kd, arbitrary units) vs ionic strength.

    A log-normal bump: affinity rises as ions pay the folding penalty, peaks,
    then falls as the same ions screen the interface and the entropic bonus
    from counterion release fades. This is a SHAPE, not a fitted physical
    model — it exists to make the argument visible.
    """
    z = (np.log10(ionic_mM) - np.log10(optimum)) / width
    return height * np.exp(-0.5 * z ** 2)


# =============================================================================
# 3. FIGURES (matplotlib)
# =============================================================================
# House style for every figure, so they read as one family.
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Calibri", "Carlito", "DejaVu Sans"],
    "axes.edgecolor": hx("slate"),
    "axes.labelcolor": hx("ink"),
    "text.color": hx("ink"),
    "xtick.color": hx("slate"),
    "ytick.color": hx("slate"),
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.facecolor": "white",
})


def make_fig_hero(path="fig_hero.png"):
    """
    THE HERO FIGURE — "six dots, six curves". This single figure is the poster.

    Panel A: what the literature hands you. Six Kd values on one axis, with lab
             tags. It looks like a clean ranking, and the viewer believes it.
    Panel B: the same six measurements revealed as single points sitting on six
             DIFFERENT curves, each peaking at a different ionic strength. The
             ranking dissolves: the "best" dot was simply measured nearest its
             own peak.

    The two panels share colours, so the eye carries each dot into panel B.
    """
    # Wide and short: the card it sits in is much wider than it is tall, so a
    # tall figure would float in the middle with big empty margins.
    fig, (axA, axB) = plt.subplots(
        2, 1, figsize=(24, 8.6), height_ratios=[1, 2.3]
    )

    # ---------------- Panel A: the apparent ranking --------------------------
    # Convert each aptamer's measured affinity into an apparent Kd, so panel A
    # is genuinely derived from panel B — the figure cannot contradict itself.
    apparent = []
    for (label, lab, measured_at, opt, height, width) in APTAMER_CURVES:
        a = affinity(measured_at, opt, height, width)
        apparent.append(50.0 / max(a, 1e-3))      # arbitrary nM scale
    order = np.argsort(apparent)                  # best (smallest Kd) first

    axA.set_title("A    What the literature hands you",
                  loc="left", fontsize=27, fontweight="bold", pad=16)
    for rank, i in enumerate(order):
        label, lab, *_ = APTAMER_CURVES[i]
        col = hx(CURVE_COLOURS[i])
        axA.scatter(apparent[i], 0, s=900, color=col, zorder=3,
                    edgecolor="white", linewidth=3)
        # Dots often cluster on a log axis, so labels alternate above and
        # below the line. Without this they overprint each other.
        above = (rank % 2 == 0)
        axA.annotate(f"{label}\n{lab}", (apparent[i], 0),
                     textcoords="offset points",
                     xytext=(0, 30 if above else -62),
                     ha="center", fontsize=19, color=hx("ink"),
                     fontweight="bold", linespacing=1.3)
    axA.set_xscale("log")
    axA.set_xlabel("reported $K_d$  (nM, log scale)", fontsize=21, labelpad=12)
    axA.set_yticks([])
    axA.spines["left"].set_visible(False)
    axA.set_ylim(-1.15, 1.35)
    axA.annotate("looks rankable — smallest $K_d$ wins",
                 xy=(0.98, 0.90), xycoords="axes fraction", ha="right",
                 fontsize=22, style="italic", color=hx("slate"))

    # ---------------- Panel B: the curves underneath -------------------------
    axB.set_title("B    What is actually underneath",
                  loc="left", fontsize=27, fontweight="bold", pad=16)
    x = np.logspace(np.log10(15), np.log10(1200), 400)
    for i, (label, lab, measured_at, opt, height, width) in enumerate(APTAMER_CURVES):
        col = hx(CURVE_COLOURS[i])
        y = affinity(x, opt, height, width)
        axB.plot(x, y, color=col, linewidth=5, alpha=0.95, zorder=2)
        # the one point this lab actually published
        ym = affinity(measured_at, opt, height, width)
        axB.plot([measured_at, measured_at], [0, ym], color=col,
                 linestyle=":", linewidth=3, alpha=0.8, zorder=1)
        axB.scatter([measured_at], [ym], s=460, color=col, zorder=4,
                    edgecolor="white", linewidth=3.5)
        axB.annotate(label, (measured_at, ym), textcoords="offset points",
                     xytext=(0, 24), ha="center", fontsize=18,
                     fontweight="bold", color=col)
    axB.set_xscale("log")
    axB.set_xlabel("ionic strength  (mM, log scale)", fontsize=21, labelpad=12)
    axB.set_ylabel("affinity  (1/$K_d$, arbitrary units)", fontsize=21, labelpad=12)
    axB.set_ylim(0, 1.12)
    axB.tick_params(labelsize=17)
    axB.annotate("each published number is ONE point on a DIFFERENT curve",
                 xy=(0.5, 0.93), xycoords="axes fraction", ha="center",
                 fontsize=24, fontweight="bold", color=hx("coral"))

    fig.tight_layout(pad=2.0)
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def make_fig_budget(path="fig_budget.png"):
    """
    THE BUDGET FIGURE — why the curve has a peak at all.

    Top: the three competing terms, each normalised to 0-1 so they can share
         an axis.
            folding  (teal)   rises  — ions pay the electrostatic penalty
            interface(violet) falls  — the same ions screen the contact
            release  (gold)   falls  — less to gain as bulk salt rises
    Bottom: their product, which is the affinity actually measured (coral).

    Shared x-axis, so the peak lines up visually with where the three terms
    cross over. This turns "there is a peak" into "here is why".
    """
    x = np.logspace(np.log10(15), np.log10(1200), 400)
    lx = np.log10(x)

    folding   = 1 / (1 + 10 ** ((np.log10(120) - lx) * 3.2))   # sigmoid up
    interface = 1 / (1 + 10 ** ((lx - np.log10(260)) * 2.6))   # sigmoid down
    release   = 1 / (1 + 10 ** ((lx - np.log10(200)) * 1.5))   # gentle decay
    observed  = folding * interface * release
    observed /= observed.max()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 9.0), sharex=True,
                                   height_ratios=[1.2, 1])

    ax1.plot(x, folding,   color=hx("teal"),   lw=5,
             label="folding: ions pay the penalty  (helps)")
    ax1.plot(x, interface, color=hx("violet"), lw=5,
             label="interface: ions screen the grip  (hurts)")
    ax1.plot(x, release,   color=hx("gold"),   lw=5,
             label="counterion release: entropic bonus  (fades)")
    ax1.set_ylabel("each term\n(normalised)", fontsize=19)
    ax1.set_ylim(-0.05, 1.12)
    ax1.legend(fontsize=17, frameon=False, loc="center left",
               bbox_to_anchor=(0.02, 0.42))
    ax1.tick_params(labelsize=15)

    ax2.fill_between(x, observed, color=hx("coral"), alpha=0.18)
    ax2.plot(x, observed, color=hx("coral"), lw=6)
    peak = x[np.argmax(observed)]
    ax2.axvline(peak, color=hx("gold"), lw=3, ls="--")
    ax2.annotate("the optimum", xy=(peak, 1.0), xytext=(0, 14),
                 textcoords="offset points", ha="center", fontsize=19,
                 fontweight="bold", color=hx("ink"))
    ax2.set_xscale("log")
    ax2.set_xlabel("ionic strength  (mM, log scale)", fontsize=19, labelpad=10)
    ax2.set_ylabel("what you measure\n(affinity)", fontsize=19)
    ax2.set_ylim(0, 1.25)
    ax2.tick_params(labelsize=15)

    fig.tight_layout(pad=1.6)
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def make_fig_comparable(path="fig_comparable.png"):
    """
    WHAT BECOMES COMPARABLE once you have a whole curve instead of a point.

    The same curve, annotated three times:
       1. peak HEIGHT   — how good it is at its best
       2. peak POSITION — which conditions it wants
       3. peak WIDTH    — how forgiving it is (measured at half maximum)

    For an assay that must run in stool, (3) may matter more than (1): a
    slightly weaker but flat-responding aptamer beats a sharp-peaked champion
    that collapses as soon as conditions drift.
    """
    x = np.logspace(np.log10(15), np.log10(1200), 400)
    y = affinity(x, optimum=180, height=1.0, width=0.36)

    fig, ax = plt.subplots(figsize=(13, 6.4))
    ax.fill_between(x, y, color=hx("coral"), alpha=0.16)
    ax.plot(x, y, color=hx("coral"), lw=6)

    peak_x = 180.0
    # 1. height
    ax.annotate("", xy=(peak_x, 1.0), xytext=(peak_x, 0),
                arrowprops=dict(arrowstyle="<->", lw=3.5, color=hx("teal")))
    ax.annotate("1  how good\n    at its best", xy=(peak_x, 0.52),
                xytext=(16, 0), textcoords="offset points", fontsize=19,
                color=hx("teal"), fontweight="bold", linespacing=1.3)
    # 2. position
    ax.plot([peak_x], [1.0], marker="v", ms=20, color=hx("gold"), zorder=4)
    ax.annotate("2  what it wants", xy=(peak_x, 1.0), xytext=(0, 30),
                textcoords="offset points", ha="center", fontsize=19,
                color=hx("ink"), fontweight="bold")
    # 3. width at half maximum
    half = 0.5
    lo = 10 ** (np.log10(peak_x) - 0.36 * np.sqrt(2 * np.log(2)))
    hi = 10 ** (np.log10(peak_x) + 0.36 * np.sqrt(2 * np.log(2)))
    ax.annotate("", xy=(lo, half), xytext=(hi, half),
                arrowprops=dict(arrowstyle="<->", lw=3.5, color=hx("violet")))
    ax.annotate("3  how forgiving", xy=(np.sqrt(lo * hi), half),
                xytext=(0, -42), textcoords="offset points", ha="center",
                fontsize=19, color=hx("violet"), fontweight="bold")

    ax.set_xscale("log")
    ax.set_xlabel("ionic strength  (mM, log scale)", fontsize=19, labelpad=10)
    ax.set_ylabel("affinity", fontsize=19)
    ax.set_ylim(0, 1.3)
    ax.tick_params(labelsize=15)
    fig.tight_layout(pad=1.4)
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


# =============================================================================
# 4. POSTER HELPERS (python-pptx)
# =============================================================================

def add_text(slide, x, y, w, h, runs, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, line_spacing=1.0):
    """
    Place a text box.

    `runs` is a list of (text, size_pt, bold, colour_key) tuples. Each tuple
    becomes its own paragraph, so you can mix a heading and body text in one
    box and they stay glued together when you move it.
    """
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.08)
    tf.margin_top = tf.margin_bottom = 0
    for i, (text, size, bold, colour) in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.name = FONT
        r.font.color.rgb = rgb(colour)
    return box


def add_card(slide, x, y, w, h, fill="card", border=None, radius=0.03):
    """A rounded panel. `border` is a palette key, or None for no outline."""
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.adjustments[0] = radius          # corner roundness, 0 = square
    shp.fill.solid()
    shp.fill.fore_color.rgb = rgb(fill)
    if border:
        shp.line.color.rgb = rgb(border)
        shp.line.width = Pt(5)
    else:
        shp.line.fill.background()
    shp.shadow.inherit = False           # flat look; no PowerPoint drop shadow
    shp.text_frame.text = ""
    return shp


def add_number_badge(slide, x, y, d, n, colour):
    """The numbered circle that marks each panel's place in the argument."""
    c = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y),
                               Inches(d), Inches(d))
    c.fill.solid()
    c.fill.fore_color.rgb = rgb(colour)
    c.line.fill.background()
    c.shadow.inherit = False
    tf = c.text_frame
    tf.text = str(n)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.runs[0].font.size = Pt(42)
    p.runs[0].font.bold = True
    p.runs[0].font.name = FONT
    p.runs[0].font.color.rgb = rgb("card")
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    return c


def add_picture_fit(slide, path, x, y, w, h):
    """
    Place an image inside the box (x, y, w, h) WITHOUT distorting it, and
    centre it. python-pptx will stretch an image if you give it both width and
    height, so we compute the aspect ratio ourselves.
    """
    from PIL import Image
    iw, ih = Image.open(path).size
    scale = min(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    return slide.shapes.add_picture(path, Inches(x + (w - dw) / 2),
                                    Inches(y + (h - dh) / 2),
                                    Inches(dw), Inches(dh))


# =============================================================================
# 5. THE ZONES
# =============================================================================

def zone_title(slide, y):
    """Zone 1 — the title and the one-sentence problem, in a dark band."""
    add_text(slide, M, y, FULL - 7.0, 1.9, [
        ("Six aptamers. Six numbers. One problem.", 86, True, "ink"),
    ], line_spacing=0.92)

    # The claim the whole poster defends. Dark band = the thing to remember.
    band_y = y + 2.05
    add_card(slide, M, band_y, FULL - 7.0, 1.55, fill="ink")
    add_text(slide, M + 0.5, band_y + 0.12, FULL - 8.0, 1.3, [
        ("Every published affinity is a single point on a curve nobody "
         "measured — and each aptamer sits on a different curve.",
         34, True, "gold"),
    ], anchor=MSO_ANCHOR.MIDDLE)

    # Author block + placeholder for a QR code, top right.
    add_text(slide, W - M - 6.6, y + 0.15, 6.6, 1.9, [
        ("[Your name]", 30, True, "ink"),
        ("[Lab, Institute]", 26, False, "slate"),
        ("[email]", 26, False, "slate"),
    ], align=PP_ALIGN.RIGHT)
    qr = add_card(slide, W - M - 2.6, y + 1.5, 2.6, 2.1, fill="card",
                  border="line")
    add_text(slide, W - M - 2.5, y + 1.5, 2.4, 2.1,
             [("[QR]", 24, False, "slate")],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return y + H_TITLE


def zone_hero(slide, y, fig_path):
    """
    Zone 2 — the hero figure. Deliberately placed high: the viewer should meet
    the PROBLEM before the mechanism that explains it.
    """
    add_card(slide, M, y, FULL, H_HERO, fill="card", border="coral")
    add_number_badge(slide, M + 0.5, y + 0.45, 1.2, 1, "coral")
    add_text(slide, M + 2.0, y + 0.45, FULL - 10.0, 1.2, [
        ("The ranking that is not a ranking", 50, True, "coral"),
    ], anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, W - M - 8.2, y + 0.5, 7.7, 1.2, [
        ("illustrative data — shows the shape of the problem, not results",
         24, False, "slate"),
    ], align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

    add_picture_fit(slide, fig_path, M + 0.6, y + 1.85, FULL - 1.2, H_HERO - 3.3)

    add_text(slide, M + 0.8, y + H_HERO - 1.35, FULL - 1.6, 1.1, [
        ("Each lab selected and measured its aptamer in its own buffer, so "
         "each number sits at a different, unknown place on its own curve. "
         "The literature ranking is partly a ranking of whose buffer was "
         "luckiest.", 30, False, "ink"),
    ])
    return y + H_HERO + GAP


def zone_mechanism(slide, y):
    """
    Zone 3 — the three competing terms, one panel each, left to right in the
    order they are introduced in the argument.
    """
    panels = [
        (2, "Folding costs charge", "teal", "salt HELPS",
         "Every phosphate is negative. Folding pulls those charges together — "
         "an electrostatic penalty. Counterions gather and screen it: a "
         "diffuse, mobile atmosphere, not fixed bound ions. The folded state "
         "holds a denser atmosphere, so folding and ion uptake are coupled."),
        (3, "The same ions weaken the grip", "violet", "salt HURTS",
         "The aptamer binds a positively charged patch on the target. That "
         "attraction is electrostatic too, and screening does not know which "
         "attraction it is cancelling. More salt, weaker contact."),
        (4, "Binding spends ions", "gold", "the bonus FADES",
         "Ions crowd both partners before binding. On association some are "
         "released into bulk and gain freedom — an entropic gain. The gain "
         "depends on the contrast with bulk, so it shrinks as salt rises."),
    ]
    for i, (n, title, colour, verdict, body) in enumerate(panels):
        x = M + i * (COL3 + GAP)
        add_card(slide, x, y, COL3, H_MECH, fill="card", border=colour)
        add_number_badge(slide, x + 0.45, y + 0.45, 1.1, n, colour)
        add_text(slide, x + 1.8, y + 0.45, COL3 - 2.3, 1.1,
                 [(title, 38, True, colour)], anchor=MSO_ANCHOR.MIDDLE)
        add_text(slide, x + 0.55, y + 1.85, COL3 - 1.1, H_MECH - 3.3,
                 [(body, 28, False, "ink")], line_spacing=1.12)
        # The verdict strip: the one thing to remember from this panel.
        add_card(slide, x + 0.55, y + H_MECH - 1.35, COL3 - 1.1, 0.95,
                 fill=colour)
        add_text(slide, x + 0.55, y + H_MECH - 1.35, COL3 - 1.1, 0.95,
                 [(verdict, 32, True, "card")],
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return y + H_MECH + GAP


def zone_budget(slide, y, fig_path):
    """Zone 4 — the three terms add up to the curve, plus the ion-identity trap."""
    # Left: the budget figure.
    add_card(slide, M, y, COL2, H_BUDGET, fill="card", border="coral")
    add_number_badge(slide, M + 0.45, y + 0.4, 1.1, 5, "coral")
    add_text(slide, M + 1.8, y + 0.4, COL2 - 2.3, 1.1,
             [("Add them up: a curve, not a number", 38, True, "coral")],
             anchor=MSO_ANCHOR.MIDDLE)
    add_picture_fit(slide, fig_path, M + 0.5, y + 1.7, COL2 - 1.0, H_BUDGET - 2.3)

    # Right: ion identity, then why the obvious fix fails.
    x2 = M + COL2 + GAP
    add_card(slide, x2, y, COL2, H_BUDGET, fill="card", border="violet")
    add_number_badge(slide, x2 + 0.45, y + 0.4, 1.1, 6, "violet")
    add_text(slide, x2 + 1.8, y + 0.4, COL2 - 2.3, 1.1,
             [("And “same salt” is not the same condition",
               38, True, "violet")], anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, x2 + 0.55, y + 1.8, COL2 - 1.1, 3.0, [
        ("K⁺ can occupy a structural site in a G-quadruplex — not general "
         "screening.   Mg²⁺ shapes nucleic-acid structure strongly and "
         "competes with monovalent ions.   Even anions differ: swapping "
         "chloride for glutamate shifts affinity in some systems.",
         28, False, "ink"),
    ], line_spacing=1.12)
    add_card(slide, x2 + 0.55, y + 4.95, COL2 - 1.1, 1.0, fill="violet")
    add_text(slide, x2 + 0.55, y + 4.95, COL2 - 1.1, 1.0,
             [("ionic strength, ion identity and pH are three variables, not one",
               29, True, "card")],
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, x2 + 0.55, y + 6.2, COL2 - 1.1, 1.8, [
        ("So one shared buffer is fair in procedure, not in physics: it "
         "measures every aptamer at an arbitrary point on its own curve.",
         27, False, "slate"),
    ], line_spacing=1.1)
    return y + H_BUDGET + GAP


def zone_comparable(slide, y, fig_path):
    """Zone 5 — the resolution: measure the curve, and why FP is the method."""
    add_card(slide, M, y, FULL, H_COMP, fill="card", border="teal")
    add_number_badge(slide, M + 0.45, y + 0.4, 1.1, 7, "teal")
    add_text(slide, M + 1.8, y + 0.4, FULL - 2.3, 1.1,
             [("Measure the curve, not the point", 44, True, "teal")],
             anchor=MSO_ANCHOR.MIDDLE)

    add_picture_fit(slide, fig_path, M + 0.5, y + 1.6, COL2 - 0.5, H_COMP - 2.2)

    x2 = M + COL2 + GAP
    add_text(slide, x2, y + 1.75, COL2 - 0.3, H_COMP - 2.4, [
        ("Fluorescence polarisation lets the solution be the only variable:",
         30, True, "ink"),
        ("•  nothing immobilised, no surface to stick to", 28, False, "ink"),
        ("•  no wash step — one buffer start to finish, at equilibrium", 28, False, "ink"),
        ("•  one plate scans ion identity, concentration and pH for all six", 28, False, "ink"),
        ("•  with circular dichroism: tells a change in fold from a change "
         "at the interface", 28, False, "ink"),
    ], line_spacing=1.16)
    return y + H_COMP + GAP


def zone_takeaway(slide, y):
    """Zone 6 — the takeaway, the honest caveat, and the controls."""
    h = H - M - y
    add_card(slide, M, y, FULL, h, fill="ink")
    add_text(slide, M + 0.8, y + 0.45, FULL - 1.6, 1.5, [
        ("Salt prepares the hand and weakens the handshake — so the binding "
         "we measure belongs to the sequence and its solution together.",
         38, True, "gold"),
    ], line_spacing=1.05)
    add_text(slide, M + 0.8, y + 2.1, (FULL - 2.4) / 2, h - 2.5, [
        ("What salt dependence does not tell us", 30, True, "card"),
        ("A steep fall with rising salt suggests a charge-driven interaction. "
         "It does not tell us how many ions were released: structural change, "
         "hydration and other contacts contribute too. We treat the salt "
         "response as a clue, not a full explanation.", 26, False, "card"),
    ], line_spacing=1.1)
    add_text(slide, M + 0.8 + (FULL - 2.4) / 2 + 0.8, y + 2.1,
             (FULL - 2.4) / 2, h - 2.5, [
        ("Controls, under matched conditions", 30, True, "card"),
        ("scrambled sequences  ·  motif mutants  ·  unrelated viral particles  "
         "·  norovirus-negative stool", 26, False, "card"),
    ], line_spacing=1.1)


# =============================================================================
# 6. BUILD
# =============================================================================

def build_poster(filename="aptamer_problem_poster.pptx"):
    # 1. Make the figures first, so they exist when the layout needs them.
    hero = make_fig_hero()
    budget = make_fig_budget()
    comparable = make_fig_comparable()

    # 2. One slide, A0 portrait, blank layout (index 6 = "Blank").
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # 3. Background. python-pptx has no page-fill API, so we draw a rectangle
    #    covering the whole slide and send nothing behind it.
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0,
                                Inches(W), Inches(H))
    bg.fill.solid()
    bg.fill.fore_color.rgb = rgb("bg")
    bg.line.fill.background()
    bg.shadow.inherit = False

    # 4. Lay out the zones top to bottom. Each returns the next free y, so
    #    changing any zone height reflows everything below it automatically.
    y = M - 0.2
    y = zone_title(slide, y)
    y = zone_hero(slide, y, hero)
    y = zone_mechanism(slide, y)
    y = zone_budget(slide, y, budget)
    y = zone_comparable(slide, y, comparable)
    zone_takeaway(slide, y)

    prs.save(filename)
    print(f"Saved {filename}  ({W} x {H} in = A0 portrait)")
    print("Open in PowerPoint and export as PDF to print. "
          "Check body text is >= 24 pt before sending to the printer.")
    return filename


if __name__ == "__main__":
    build_poster()
