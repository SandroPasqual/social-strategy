# 030106 Typography System | Goodspell | OUTPUT
LAYER  METHODOLOGY  ·  Client ID: —
PHASE  03  ·  Code: 030106  ·  Role: INTERN → OUTPUT
DOCUMENT  Typography System  |  Goodspell Brand Strategy
STATUS  v1.0 — Approved

Typography is not decoration. It is the structural backbone of communication. Every sizing decision, every weight, every spacing value must serve a functional purpose — readability, hierarchy, and brand precision.

1. Typeface System
Goodspell operates a three-role typeface system. Each role has a defined function. No substitutions are permitted within client-facing materials.

THE THREE ROLES

WHY THIS SYSTEM

Syne 800 at display sizes commands authority without decoration. Its geometric construction and expanded width signal precision — the visual register of a firm that has already decided. It does not invite negotiation.
Instrument Sans disappears into content. Humanist in structure, it reads cleanly at 14–18px across all screen densities without demanding attention. Body type that performs its function invisibly is body type that earns its place.
Instrument Serif Italic is used exclusively for strategic statements, client pull quotes, and positioning language in documents. It creates tension with the sans-serif system — signaling that what follows carries more deliberate weight.

PAIRING LOGIC

The pairing works because it creates tension through contrast while maintaining systemic coherence. Geometric authority at the heading level. Humanist clarity at the body level. Italic serif as the exception — used sparingly enough that its appearance signals significance.
The test: At any size, the heading must read as a different visual register than the body. If the two fonts feel interchangeable, the pairing fails.

2. Type Scale
All sizing is based on a modular scale (ratio 1.25 — Major Third), anchored at a 16px base. Line height tightens as size increases — large display text is read in single passes; body text sustains continuous reading.

3. Weight System
Limit the active weight set to four values maximum. More than four creates visual noise with no structural payoff.

4. Spacing & Rhythm
Typography lives in space. Margins and padding define readability as much as the typeface itself.

PARAGRAPH SPACING

Between body paragraphs: 1em (equals current font size)
After a heading, before body: 0.5em
Before a heading, after body: 1.5–2em
Document section breaks: 3–4em minimum

LINE LENGTH (MEASURE)

A 16px Instrument Sans body at 65 characters ≈ 560–620px column width. This is the structural basis for content containers in all GBS document layouts.

5. Color Application to Type
Typography color is a hierarchy signal — not a stylistic choice. All values are drawn from the Goodspell Brand Palette and adapted to the warm neutral base.

No color accent on type. Links and active states use Ink with underline or weight change — not color. The system maintains authority by refusing decorative color.

CONTRAST MINIMUMS — WCAG 2.1 AA

These are not preferences. They are the functional and legal baseline.

6. Responsive Behavior
Type scales must adapt fluidly. Fixed pixel sizes break at scale extremes.

FLUID TYPOGRAPHY — CSS IMPLEMENTATION

--text-display: clamp(36px, 5.5vw, 56px);
--text-h1:      clamp(28px, 4.5vw, 40px);
--text-h2:      clamp(22px, 3.5vw, 32px);
--text-body:    clamp(15px, 1.5vw, 16px);

Critical for mobile: Input fields must use a minimum of 16px to prevent automatic zoom on iOS Safari. Below 16px, the browser overrides and breaks the layout.

7. UI Component Typography
These values apply to interface components — buttons, inputs, navigation, labels, and tables.

Navigation and overline elements use all-caps with significant letter spacing — the system's primary labeling language. It creates a distinct visual register for structural information without introducing a new typeface.

8. Document-Specific Typography Rules
GBS strategy documents have additional rules that govern how typography operates within the document system. These supplement — and in some cases override — the general scale.

HIERARCHY IN DOCUMENT LAYOUTS

SIDEBAR NAVIGATION TYPE

Sidebar navigation items in GBS documents follow a fixed pattern: overline tag at 9px/600 for the phase indicator, Syne 700 at 15px for the section title, and Instrument Sans 300 at 10px for individual items. Active items increase to full opacity. Inactive items hold at 0.30–0.35 opacity.

9. What This System Prohibits
These are structural failures, not preferences.

—  Syne at body sizes.  Syne is a display typeface. At 14–16px it becomes illegible and loses its authority. Below 20px, transition to Instrument Sans.
—  Instrument Serif in UI components.  Italic serif fails at small sizes and in interactive contexts. Reserve for pull quotes and positioned statements only.
—  Weight as decoration.  Bold exists to signal hierarchy, not enthusiasm. A heading that requires bold to feel important has a structural problem, not a weight problem.
—  300 weight below 16px.  Optical size matters more than aesthetic preference. Below 16px, use 400.
—  Justified text.  Creates uneven word spacing that destroys the reading rhythm Instrument Sans is designed to produce.
—  Custom letter-spacing on body text beyond ±0.02em.  Disrupts the natural word rhythm of the typeface.
—  All-caps body text.  Acceptable only for labels, overlines, and badges at or below 13px.
—  Text over complex imagery without overlays.  Contrast cannot be guaranteed and the system does not permit uncontrolled contrast failures.
—  More than two typefaces in visual weight.  Goodspell uses three roles, but only two carry distinct visual weight. Instrument Serif is a variant, not a third independent voice.

10. Token Reference
All type tokens are defined in the GBS Design Token system [0009 GBS Design Tokens & Platforms Stack | INTERN] and consumed by Figma, web implementations, and document templates via the canonical tokens file.

/* Typefaces */
--font-display:   'Syne', sans-serif;
--font-body:      'Instrument Sans', sans-serif;
--font-editorial: 'Instrument Serif', serif;

/* Weights */
--weight-light:      300;
--weight-regular:    400;
--weight-medium:     500;
--weight-semibold:   600;
--weight-extrabold:  800;

/* Base */
--font-base:         16px;
--line-height-body:  1.75;
--line-height-tight: 1.1;

/* Text Colors */
--color-text-primary:        #1C1B18;
--color-text-secondary:      #5C5850;
--color-text-tertiary:       #8C8678;
--color-text-inverse:        #F5F2EA;
--color-text-inv-secondary:  rgba(245,242,234,0.55);
--color-text-inv-tertiary:   rgba(245,242,234,0.25);

The system is complete when nothing can be removed without losing function. Readers should never notice the type. They should only receive the message with zero friction.
This document is maintained by the Goodspell system. Any modification to typeface selection, weight assignments, or token values requires review against the full GBS document system before implementation. A typography decision that seems local is never local — it propagates across every document, every screen, and every touchpoint the system governs.
