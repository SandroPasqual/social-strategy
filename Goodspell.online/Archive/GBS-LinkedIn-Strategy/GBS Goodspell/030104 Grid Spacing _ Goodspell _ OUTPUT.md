# 030104 Grid Spacing | Goodspell | OUTPUT
## 03010401  PAPO
### Purpose
Defines the spatial logic of the Goodspell visual system — base unit, column structure, margins, and spacing scale — so every layout feels precise, coherent, and consistent regardless of format or contributor. The grid is not an aesthetic preference. It is the structural logic that makes the visual system governable.
### Audience
Any designer, developer, or contributor producing a Goodspell layout — website, documents, presentations, LinkedIn visuals, or any branded format. The grid applies before any typographic or color decision is made.
### Process
Derived from 0301 Visual Identity System and the confirmed brand decisions: 8-column grid, 8px base unit, 1px rule weight. All format-specific adaptations documented here inherit from this core spatial logic.
### Outcome
A spatial system any contributor can apply independently and consistently. Layouts produced by different contributors at different times read as part of the same system — because they are governed by the same spatial logic.
## 03010402  Strategic Rationale
The grid communicates before the content does. A layout on a precise, consistent grid signals that the firm behind it operates with structural discipline. A layout that improvises spacing — even if the content is excellent — signals ad-hoc construction. For Goodspell's audience — founders and executives who evaluate partners by the quality of the first interaction — the grid is a credibility signal.
The 8-column grid was chosen for its balance of precision and flexibility across the formats Goodspell uses: US Letter documents, web layouts, and presentation slides. Eight columns divide cleanly into halves, thirds, and quarters — which means content areas, sidebars, and tables can all be structured without remainder.
The 8px base unit aligns with standard digital production workflows, making the system directly transferable between document design (Figma, InDesign) and web development (CSS spacing tokens).
## 03010403  Base Unit
The base unit is 8px. All spacing values in the system are multiples of 8. No value outside this scale is used in production.

Half-unit values (4px) are permitted exclusively for fine optical adjustments within components — never for layout spacing. A 4px gap between two layout elements signals a construction error, not a design decision.
## 03010404  Column Grid — Primary Formats
### Format 01 — US Letter Landscape  (279 × 216mm)  |  Primary document format
8 columns. Column width: calculated from content width minus gutter total. Outer margin: 20mm all sides. Gutter: 6mm. The 8-column grid on US Letter Landscape supports: full-width content (8 col), two-column layouts (4+4), sidebar + content (2+6 or 3+5), three-column tables (3+3+2).
#### 8-column grid — US Letter Landscape  |  Outer margin: 20mm  |  Gutter: 6mm
### Format 02 — A4 Portrait  (210 × 297mm)  |  EU-market documents
8 columns. Outer margin: 20mm all sides. Gutter: 5mm. Content width: 170mm. The A4 grid follows the same column logic as US Letter — layouts designed for one format transfer to the other without structural changes, only content reflow.

8-column grid — A4 Portrait  |  Outer margin: 20mm  |  Gutter: 5mm
### Format 03 — Website  |  Desktop viewport 1440px
12 columns at desktop. 8 columns at tablet (768–1024px). 4 columns at mobile (below 768px). Max content width: 1200px centered. Outer margin: 120px at desktop, 40px at tablet, 24px at mobile. Gutter: 24px at desktop, 20px at tablet, 16px at mobile.
12-column grid — Desktop 1440px  |  Max width 1200px  |  Gutter: 24px

The website grid uses 12 columns at desktop to support more granular content organization (thirds, quarters, sixths) while maintaining alignment with the 8-column document system through shared proportional logic.
### Format 04 — Presentation  (1920 × 1080px  or  16:9 equivalent)
8 columns. Outer margin: 80px all sides. Gutter: 24px. The presentation grid is the digital equivalent of the US Letter Landscape document grid — same column count, adapted to the widescreen aspect ratio.
8-column grid — Presentation 1920×1080  |  Margin: 80px  |  Gutter: 24px
## 030104-05  Rule Weight
The standard rule weight across the Goodspell system is 1px. This applies to all structural dividers: section separators in documents, table borders, component borders, and layout rules in the website.
The 1px rule at the document scale communicates precision without aggression. It is present enough to structure the layout, light enough not to compete with content.
No rule weight other than 1px and 2px is used in production. Decorative thick rules, gradient rules, or rules in Slate or functional tint colors are not part of this system.
## 03010406  Spacing in Documents — GBS System
The GBS document system uses a defined spacing hierarchy across all three phases. These values govern the vertical rhythm of every document — from the cover to the final page.
## 03010407  Grid Prohibitions
The following spatial decisions are not permitted in any Goodspell layout.
Free-value spacing — any spacing value not derivable from the 8px base unit. A gap of 13px, 22px, or 37px is a construction error. The correct value is the nearest token.
Asymmetric outer margins without a documented justification. Page margins are equal on all sides unless the format explicitly defines a bleed, a binding margin, or a sidebar structure that requires asymmetry.
Half-column widths for primary content areas. Content occupies whole columns. A content area that spans 3.5 columns is misaligned with the grid.
Rule weights other than 1px or 2px. A 3px or 4px decorative rule is not part of the Goodspell visual language.
Overlapping content zones without a defined z-order logic documented in the layout specification.
When a layout decision requires a value not in the spacing scale, the answer is to return to the nearest defined token — not to introduce a new value. The grid exists precisely to prevent the accumulation of one-off spatial decisions that degrade system coherence over time.

030104 Grid & Spacing | Goodspell | OUTPUT  —  v1.0
