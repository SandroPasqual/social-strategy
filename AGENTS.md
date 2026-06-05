# AGENTS.md — Social Strategy Ecosystem

## Role
This project defines the LinkedIn content strategy for 3 accounts: Personal (Sandro Pasqual), Goodspell.online, Devorator. It collects, analyzes, and structures published posts + drafts with standardized YAML front matter.

---

## Project Architecture

```
Social strategy/
├── AGENTS.md                    ← this file
├── TEMPLATE.md                  ← standardized post format
├── Ideas/                       ← original Google Drive data (READ-ONLY)
│
├── Personal/                    ← PRIMARY ACCOUNT — trust is built here
│   ├── Posted/                  ← published posts (57 files)
│   ├── Drafts/                  ← written but unpublished (13 files)
│   ├── To be posted/            ← prepped for publication with front matter (13 files)
│   ├── Strategic Analysis.md    ← full diagnostic
│   └── Strategy Proposal.md   ← decisions, rules, differentiation
│
├── Goodspell.online/            ← SECONDARY ACCOUNT — supports, does not lead
│   ├── Posted/                  ← page posts published (10 files + images)
│   ├── To be posted/            ← 50 posts with WHITE/BLACK numbering, no dates (14 with images)
│   ├── Brand Playbook/          ← foundation, strategy proposal, content playbook, copy, comment framework, positioning, ethics
│   ├── Backup/                  ← friction moments, publication order, strategic analysis, old drafts, HTML templates
│   ├── Strategie Goodspell/     ← methodology pillars, templates
│   ├── linkedin-image-builder/  ← image generation tool (to be rebuilt with SQLite)
│   └── Archive/                 ← full historical archive (pre-Nov 2025 strategy)
│
└── Devorator/                   ← to be analyzed later
    ├── Extindere devorator.md
    └── Model devorator.md
```

---

## Channel Hierarchy

1. **Personal = PRIMARY.** The client comes to Sandro, not to Goodspell. They trust a person, not a generic team. Personal is the engine.
2. **Goodspell = SECONDARY.** Supports, does not lead. The company page complements the presence.
3. **Devorator** — not started yet.

---

## Voice Rules — Personal Account

| Principle | How it applies |
|---|---|
| **Positioning** | Gastric — enters smooth, burns after. Recognition over attack. |
| **Voice** | The Observer — philosophical, poetic, observational |
| **Position** | Alongside the reader, not above. "We're the same." |
| **Tone** | Does not teach, correct, or provoke — reflects |
| **Titles** | Punchy, with tension. First line stops the scroll |
| **Ending** | A moment of shared recognition, not a question or CTA |
| **Questions** | Only rhetorical, inside the text. No answer requested from reader |
| **Hashtags** | 1-2 per post — #Attention #DigitalCulture #Memory #Thinking #AI #Strategy etc. |
| **About design** | NO. Everything is strategy |
| **Overlap with Goodspell** | Yes, intentional. Same filter, different angle |
| **Selling** | Zero. Absolutely zero. No pitch, no "you need X," no CTA. The post just is there. The tension remains open. |
| **Frequency** | Every 2 days (shows presence, no noise) |

## Voice Rules — Goodspell Page

| Principle | How it applies |
|---|---|
| **Positioning** | Gastric + Framework — same mechanism as Personal (recognition), different delivery |
| **Voice** | The Architect — gastric with framework. Names the pattern after the feeling lands. |
| **Position** | Demonstrates through reasoning, not results |
| **Tone** | Gastric. The pattern is named after the reader has already recognized the feeling. |
| **Core theme** | The gap between actual execution and public perception |
| **Hashtags** | Zero. Goodspell does not use hashtags — they associate with the noise the brand actively avoids. |
| **Frequency** | 1-2/week |
| **Cross-pollination** | Sandro shares page posts on his personal account |

---

## Serialization Arc — Personal (13 posts in To be posted)

```
Attention → Memory → Thinking → Influence → Creation → AI
```

| # | Date | Title | Theme |
|---|---|---|---|
| 1 | Jun 5 | Saved by the bell. Or trapped by it. | Phone in conversation |
| 2 | Jun 7 | We're all wet. And we pretend we're not. | We don't finish things |
| 3 | Jun 9 | I publish. Then the categories appear. | Online identity |
| 4 | Jun 11 | Marketable. Until you're not. | How we remember people |
| 5 | Jun 13 | I can't read the operating system behind it. | Childhood as lost species |
| 6 | Jun 15 | The first stupid thought, dressed up as conviction. | Digested complexity |
| 7 | Jun 17 | The system is rigged. And that's not the whole story. | Inequality |
| 8 | Jun 19 | You weren't convinced. You were mirrored. | Influence and tribes |
| 9 | Jun 21 | No system corrupts from the outside. | People in systems |
| 10 | Jun 23 | The blue was never in the paint. | Constraints as source |
| 11 | Jun 25 | The deity hallucinated. So they grabbed the hammer. | LLMs as oracles |
| 12 | Jun 27 | The Romans had many gods. We have many models. | LLM market |
| 13 | Jul 1 | The solo operator with better tools isn't the future. | Creative work structure |
| 14 | Jul 3 | Everyone did their job. The result was still generic. | Disconnected execution |
| 15 | Jul 5 | You don't need a new look. | Structure vs surface |
| 16 | Jul 7 | The designer delivered exactly what was briefed. | The brief as foundation |
| 17 | Jul 9 | What happens in that room stays in that room. | Confidentiality as standard |
| 18 | Jul 11 | Every new project starts with the same question: where do we begin? | Orientation over speed |
| 19 | Jul 13 | Three variants. | Generic logo design, gastric tone |

**Note:** Posts #13–14 extend the serialization beyond the original arc (Attention→AI). Posts #15–18 continue the Observer voice. Post #19 is the "Three variants" post (from Claude, gastric acid tone). After Jul 13, a personal writing series of 10 texts begins ("While I Still Know") — see Notes/Personal Writing Series.md for order and status.

---

## Key Decisions (Documented in Strategy Proposal.md)

- **Pivot is correct**: The Brand Strategy phase (Aug-Sep 2025) was exhausted. The Observer is the right direction.
- **Boundary items → Personal**: Anything at the boundary between Personal and Goodspell goes to Personal.
- **Design topics eliminated**: No more posts about logos, colors, fonts. Only strategy.
- **Questions at the end → NO**: Replaced with moments of shared recognition.
- **Groups**: Founders & Startups is the most relevant. Designers Talk was an outlier, not a goal.
- **Frequency**: Every 2 days on Personal, 1-2/week on Goodspell.

---

## Useful Commands

```bash
# List published posts (Personal)
ls -1 "Personal/Posted/"*.md | wc -l

# List prepared drafts
ls -1 "Personal/To be posted/"*.md

# Move published post (after it goes live on LinkedIn)
mv "Personal/To be posted/YYYY-MM-DD Title.md" "Personal/Posted/"

# Extract data from a public LinkedIn post
curl -s -L "URL" | grep -oP '"articleBody":"(?:[^"\\]|\\.)*"'

# Quick front matter analysis
awk -F': ' '/^impressions:/{print $2}' Personal/Posted/*.md | sort -n | tail -5
```

---

## Essential Paths

- Template: `TEMPLATE.md`
- Personal analysis: `Personal/Strategic Analysis.md`
- Personal proposal: `Personal/Strategy Proposal.md`
- Goodspell analysis: `Goodspell.online/Strategic Analysis.md`
- Goodspell proposal: `Goodspell.online/Strategy Proposal.md`
- Content Playbook: `Goodspell.online/Brand Playbook/Goodspell — LinkedIn Content Playbook.md`
- Brand Foundation: `Goodspell.online/Brand Playbook/Goodspell — Brand Foundation.md`
- Client Intelligence: `Goodspell.online/Brand Playbook/Goodspell — Client Intelligence.md`
- Homepage Copy: `Goodspell.online/Brand Playbook/Goodspell — Homepage Copy.md`
- **Comment Framework** (with active thread tracking): `Goodspell.online/Brand Playbook/Goodspell — LinkedIn Comment Framework.md` — check Active Threads table first when resuming comment strategy
- Strategic Positioning Statement: `Goodspell.online/Brand Playbook/Goodspell — Strategic Positioning Statement.md`
- Tone of Voice: `Goodspell.online/Brand Playbook/Goodspell — Tone of Voice.md`
- Messaging Framework: `Goodspell.online/Brand Playbook/Goodspell — Messaging Framework.md`
- Discovery Brief: `Goodspell.online/Brand Playbook/Goodspell — Discovery Brief.md`
- Published posts: `Personal/Posted/`, `Goodspell.online/Posted/`
- Drafts: `Personal/Drafts/`, `Personal/To be posted/`
- Goodspell To be posted: `Goodspell.online/To be posted/` (50 posts, 01-WHITE through 50-BLACK)

---

## Gastric Positioning (Personal Account)

The Personal LinkedIn account is positioned as _gastric_ — not as a tone, as a market position.

While everyone else on LinkedIn educates, inspires, sells, or attacks, Sandro does something different: enters smooth, burns after. The reader doesn't feel attacked — they feel recognized. Recognition is more durable than attack.

**What gastric is:**
- Precision without explanation
- Tension correctly distributed (no one person is blamed)
- The discomfort comes from recognition, not accusation
- No moral, no conclusion, no CTA
- Silence after a sentence carries part of the meaning

**What gastric is not:**
- Not dark, cynical, or gratuitously harsh
- Not educational or didactic
- Not "LinkedIn existentialism" (fragmentation without substance)
- Not validation-seeking

### The cost

Gastric doesn't feel good. It gets fewer likes. Because the truth about someone is uncomfortable to sit with.

The same way 30 posts were deleted from the archive — cut in living flesh — the same happens in the content. The truth is told raw so the treatment can follow.

No back-patting. No mutual admiration. No validation economy.

### Why lemon doesn't work

There are people who swallow hard for a long time. They feel the burn. They know something is wrong. Some even take lemon — empirical treatment, home remedies, surface fixes. A new logo. A website refresh. A tagline change.

But lemon is not a diagnosis. It treats the symptom temporarily. The burn returns because the cause was never identified.

Goodspell doesn't sell lemon. It sells the antacid — but only after the burn has been properly diagnosed. The treatment is specific to the cause, not generic for the symptom.

This is the difference between branding as decoration and branding as medicine.

**Market value:** On a platform saturated with sameness, gastric is instantly recognizable. A reader who has read one gastric post knows it's Sandro before seeing the name. This is differentiation through a cognitive mechanism (recognition), not aesthetics.

**Documented in detail:** Sandro Voice behavioral writing architecture (v4), saved in `Notes/Strategic Assets from Claude Conversations.md` and ecosystem agents.

### The metaphor

- **Personal is the burn on the throat.** The recognition. The discomfort. The symptom that tells you something is there. It enters smooth, burns after, and doesn't explain itself. The reader feels the tension without needing to name it.
- **Goodspell is the antacid.** The same mechanism (gastric), but with a different role. After the burn is recognized, Goodspell names the pattern. It doesn't remove the burn — it diagnoses what caused it. The structure comes after the feeling.

Together they form a complete cycle: Personal identifies the tension, Goodspell shows the structure behind it. One cannot work without the other. The burn validates the diagnosis.

---

## Goodspell Offering — How It Works

Goodspell is a brand strategy practice run through a custom portal. The portal is the operating system — not a marketplace, not a platform for others to work independently.

### The Flow

The portal is built around **collaborative documents** — not questionnaires, not forms. Each document is a shared workspace where both sides contribute, edit, comment, and iterate.

**Client → Strategist flow:** The client provides input (market understanding, audience, goals). The strategist reviews, guides, supports. The client re-edits based on guidance. Back and forth until aligned.

**Strategist → Client flow (reverse):** The strategist or designer works and presents their decision to the client. The client comments. The strategist re-argues and re-explains. Back and forth until they establish a decision together.

**Key properties:**
- Every edit is saved — full version history
- The client can return at any time to modify earlier responses
- The client can consult with collaborators or associates and add their input
- Nothing is final until both sides agree
- At the right moment, the document is **locked** — phase complete, next phase begins

1. **Client onboarded** — contributes to discovery documents
2. **Specialist reviews** — comments, guides, supports
3. **Client refines** — edits based on guidance, consults collaborators
4. **Strategist/designer presents decisions** — client comments, strategist re-argues
5. **Back and forth** — until both are satisfied
6. **Document locked** — phase complete, next phase begins
7. **Result:** a brand system where every decision was derived from structured collaboration, not guesswork

### The Three Pillars

1. **Brand Strategy** — positioning, perception, narrative, audience definition. The foundation.
2. **Brand Identity** — visual system, logo, colors, typography, design guide. The expression of strategy.
3. **Design System** — component library, code, tokens, scalable UI. The engine that makes strategy work at product level.

The design system is not separate from strategy — it is the operational output of it. Posts about design systems, design guides, moodboards, and brand books are valid because they demonstrate the full delivery chain. Posts about pure UI/UX career advice, color theory trivia, or logo critiques without strategic context are not.

### The Color Principle

Color is not personal preference. The market gives you the color — audience, positioning, competitive context, psychological effect. The designer's job is to read the market, not the client's moodboard. (This principle holds even if it got removed from LinkedIn.)

## Rigor

This is not a game. Every action here affects real content that represents a person's voice and business. Carelessness is not acceptable.

- **Read before you act.** Examine the file, the context, the history. Do not assume.
- **Verify before you ask.** If the answer can be derived from existing data, derive it. Do not ask redundant questions.
- **Think before you write.** Every edit, every commit, every command — pause and check if it makes sense.
- **One thing at a time.** No rushed multi-step operations. Single moves, verified.
- **Mistakes are not trivial.** A wrong commit, a broken config, a careless question — each erodes trust. Do not repeat.

## Working Principles

1. **Personal first** — any decision affecting both accounts prioritizes Personal.
2. **We're the same** — the voice is alongside, not above. Does not teach, correct, or provoke — reflects.
3. **Flow over hardcode** — strategy evolves with real data.
4. **Preserve originals** — `Ideas/` is read-only. Modifications go to `Posted/` or `To be posted/`.
5. **One step at a time** — one post, one observation, one adjustment.

## File Safety Protocol

Never use `mv` (cut-paste) for moving files between directories. Always:

1. **Copy** the file to the destination (or rewrite the content in the new location)
2. **Verify** the destination file exists and has content (size > 0 bytes, lines > 1)
3. **Delete** the source file only after confirmation

This prevents silent data loss from failed moves, path issues, or interrupted operations.
