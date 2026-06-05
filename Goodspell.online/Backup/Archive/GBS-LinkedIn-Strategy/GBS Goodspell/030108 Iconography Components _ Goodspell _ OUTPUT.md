# 030108 Iconography Components | Goodspell | OUTPUT
## 03010801  PAPO
### Purpose
Defines the visual language, construction rules, and usage logic for all reusable graphic elements in the Goodspell system — icons, UI components, and graphic components. Ensures visual consistency at the micro level, with elements that scale across formats and contributors without improvisation.
### Audience
Designers and developers building the Goodspell website, presentations, documents, or any branded output that uses system-level elements. The Logic Manager when onboarded. Any external contributor briefed on the brand system.
### Process
Derived from 0301 Visual Identity System, 030104 Grid & Spacing, and 030105 Color System. Icons and components are a downstream expression of the spatial and color decisions already confirmed. No iconographic or component decision introduces a new spatial value, color, or style logic not already present in the system.
### Outcome
A micro-level visual language that reads as part of the same system as the typography, color, and grid — because it is governed by the same logic.
## 03010802  Strategic Context
Goodspell's iconography and component system is minimal by design. The firm's primary visual instruments are typography and structure — not graphic elements. Icons and UI components exist to support function, not to express personality.
This means the icon library is small and grows only when a documented functional need requires a new icon. Components are defined to the minimum required for the Goodspell website and document system — not pre-built for hypothetical future complexity.
At launch, Goodspell's digital presence is the website and LinkedIn. The component scope reflects this. Components for features not present at launch are not built in advance.
## 030108-03  Icon Library — Style and Construction
### Style
Single style: outline. No filled variants. No dual-weight combinations within the same interface context. Style consistency is what makes icons read as a system — a single filled icon in an outline set breaks the visual logic of the entire page.
### Construction rules
Master construction grid: 24×24px. All icons are designed at this size before scaling through the token system. Every icon drawn outside this grid is not a system icon — it is a custom graphic that must be reviewed before entering the library.
Stroke weight scales proportionally: 1px at 16px display size, 2px at 32px display size. The relationship is linear. Stroke weight is never adjusted manually per icon or per context.
Corner radius: all rectangular and geometric elements within icons use a consistent 2px radius. Circular and organic forms are exempt. This keeps icons visually aligned with the UI component radius scale.
Path economy: each icon uses the minimum number of paths required to communicate the subject. No icon uses more than three distinct path elements. Complexity for its own sake is not permitted.

No icon is displayed at a size outside these four tokens without a documented exception in 030110 Key Applications.
## 03010804  Icon Color
Icons inherit color from the token context in which they appear. They are never assigned a hard-coded color. An icon inside a primary button uses the button's foreground color token. An icon in a document metadata row uses color.stone.meta.
Icons are never used in a chromatic color — no colored icons as decorative elements, no category-color icon sets. The Goodspell visual system does not use color to categorize or to signal personality at the icon level.

## 03010805  UI Components
UI components are the building blocks of the Goodspell website. Every component is defined by a fixed set of properties. No component enters production without a complete specification — including all states.
### Shared construction principles
Corner radius follows a single scale derived from the 8px base unit. The scale is: none (0px), sm (4px), md (8px), lg (16px), full (9999px / pill). A component uses one radius value consistently across all its states.
### Buttons

All button variants: default, hover (background lightens one token step), active (background darkens one step), focus (2px outline in color.ink.primary offset 2px), disabled. No state is constructed ad hoc.
### Inputs

Error state uses color.alert — the warm-tinted red from the functional palette. Never a manually chosen red outside the token system.
### Cards
Cards are container components. Three variants: flat (no border, Paper surface), outlined (1px border color.paper.deep), and elevated (box-shadow sm token). Variant is selected by context — not by preference.
Internal card padding: space.4 (32px) on all sides for standard cards. space.3 (24px) for compact cards in document contexts. Radius: lg (16px) for website cards, none for document cards.
## 03010806  Graphic Components
### Dividers
1px horizontal rule in color.paper.deep. Spacing before and after: space.3 (24px). Used as section separators in documents and as content zone boundaries on the website. No decorative variants — thicker rules, colored rules, or gradient rules are not part of the Goodspell component library.
### Badges
Short text labels — status, category, document role (INPUT / INTERN / OUTPUT). Padding: space.1 (8px) horizontal, 4px vertical. Radius: sm (4px). Color: Slate background (color.slate.light) + Ink text for document badges. Paper background + Ink text for website badges. No chromatic badge colors.
### Frames and Containers
Structural graphic elements that group content or create brand-color sections within a layout. The primary frame application in Goodspell layouts is the Ink-background band — a full-width section with color.ink.primary or color.ink.mid background and Paper text. No gradients in frames. No textures.
## 03010807  Misuse
Filled icons alongside outline icons in the same interface context. The style is single — outline only.
Icons at sizes outside the four defined tokens. No 18px, 28px, or 40px icons without a documented exception.
Hard-coded color values assigned to icon assets. Color is always applied through the consuming token context.
Corner radius values outside the defined scale (0, 4, 8, 16, 9999). A 12px radius on a button is a construction error.
Component states constructed ad hoc. Every state — hover, focus, active, disabled, error — uses a defined token. Manual color adjustments for states are not permitted.
Graphic components (dividers, badges, frames) using free-value colors or dimensions not in the spacing scale.
New icons introduced to the library without review against the 24×24px construction grid and the stroke weight rules.
## 03010808  Token Naming Convention

Token names encode role and variant — never visual description or color value. A token named 'color-dark-button' or 'rounded-card' is a naming error. Names describe function and hierarchy.

030108 Iconography & Components | Goodspell | OUTPUT  —  v1.0
