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
│   ├── Posted/                  ← page posts published (10 files)
│   ├── Brand Playbook/          ← brand foundation, content playbook, copy
│   ├── Strategie Goodspell/     ← drafts, templates, pillars
│   ├── Strategic Analysis.md    ← diagnostic
│   └── Strategy Proposal.md   ← action plan
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
| **Voice** | The Observer — philosophical, poetic, observational |
| **Position** | Alongside the reader, not above. "We're the same." |
| **Tone** | Does not teach, correct, or provoke — reflects |
| **Titles** | Punchy, with tension. First line stops the scroll |
| **Ending** | A moment of shared recognition, not a question or CTA |
| **Questions** | Only rhetorical, inside the text. No answer requested from reader |
| **Hashtags** | 1-2 per post — #Attention #DigitalCulture #Memory #Thinking #AI #Strategy etc. |
| **About design** | NO. Everything is strategy |
| **Overlap with Goodspell** | Yes, intentional. Same filter, different angle |
| **Selling** | Zero direct. Subtly directs through the angle |
| **Frequency** | Every 2 days (shows presence, no noise) |

## Voice Rules — Goodspell Page

| Principle | How it applies |
|---|---|
| **Voice** | The Architect — strategic, precise, with framework |
| **Position** | Demonstrates through reasoning, not results |
| **Tone** | The Professor from Phase 2 (Personal), applied to positioning |
| **Core theme** | The gap between actual execution and public perception |
| **Hashtags** | 3-5 — #BrandStrategy #Positioning #BusinessGrowth |
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
- Published posts: `Personal/Posted/`, `Goodspell.online/Posted/`
- Drafts: `Personal/Drafts/`, `Personal/To be posted/`

---

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
