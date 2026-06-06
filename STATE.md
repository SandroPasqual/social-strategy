# STATE — Navigation & Status Reference

Not a status snapshot. A map. Read this to know where to look and what to check.

---

## 1. Rhythm Rules (All Accounts)

| Account | Rhythm | Days | Weekend |
|---------|--------|------|---------|
| Personal | Every 2 days | Mon / Wed / Fri | Skipped |
| Goodspell | 2/week | Tue / Thu | Skipped |
| Devorator | Not started | — | — |

Rule: if `last_date + N_days` falls on Sat or Sun, post on the next Monday instead.

---

## 2. Where to Find Current State

### Personal (PRIMARY)
| What | Where | How |
|------|-------|-----|
| **Last published** | `Personal/Posted/` | Find the most recent file by filename date (format: `YYYY-MM-DD Title.md`) |
| **Next to publish** | `Personal/To be posted/` | Find the file with the earliest date |
| **Drafts (raw)** | `Personal/Drafts/` | Files here need editing before they can be published |
| **Front matter** | Inside each `.md` file | `date:` field in YAML front matter must match filename date |
| **After #19 (Jul 17)** | `Notes/Personal Writing Series - While I Still Know.md` | Series order, status, dates |
| **Full texts** | `Notes/Personal Writing Series - Full Texts.md` | 10 complete texts |

### Goodspell.online (SECONDARY)
| What | Where | How |
|------|-------|-----|
| **Last published** | `Goodspell.online/Posted/` | Most recent file by filename date |
| **Next to publish** | `Goodspell.online/To be posted/` | Earliest date among files (files are named `YYYY-MM-DD NN-COLOR Title.md`) |
| **Number system** | Filename prefix `NN-COLOR` | `01`–`50`, `WHITE` = external/market, `BLACK` = internal/censorship |
| **Images** | Same directory as `.md` | Files named `NN-COLOR Title.png` — check if image exists for each post |
| **Voice rules** | `Goodspell.online/Brand Playbook/` | See Content Playbook, Tone of Voice, Comment Framework |

---

## 3. Serial Structure

### Personal — Observer Arc (#1–19)
```
Order: fixed by date in To be posted/
Themes: Attention → Memory → Thinking → Influence → Creation → AI → Practice
Voice: Observer (philosophical, alongside reader)
End: #19 "Three variants" — gastric gateway post
```

### Personal — "While I Still Know" (after #19)
```
10 texts, 2/week (Mon/Fri), published from Personal voice (not Observer)
Order defined in Notes/Personal Writing Series - While I Still Know.md
```

### Goodspell — Phase 1: Recognition (#01–50)
```
50 WHITE/BLACK posts. No Goodspell mention, no solution, no CTA.
#01–#10: published? check Posted/
#11–#24: have images
#25–#50: no images yet
After #50: Phase 2 (Gathering — 13 posts), Phase 3 (Competence — 12 themes)
```

---

## 4. Comment Strategy

| File | Purpose |
|------|---------|
| `Goodspell.online/Brand Playbook/Goodspell — LinkedIn Comment Framework.md` | Evaluation criteria, post type patterns, active thread tracking table |
| Active Threads section | Check first — 4 tracked threads: Martin Zarian, Mark Omlor, Ogilvy, Simon Dixon |

Rules: caustic openings, 3-5 sentences, never mention Goodspell, never CTA.

---

## 5. Memory System

Location: `~/projects/memory/`
```
./mem doctor       — health check + FTS repair
./mem ingest       — index markdown files
./mem embed        — generate semantic vectors (after ingest)
./mem recall       — semantic search
./mem query        — full-text search
```

---

## 6. Key Decision Files

| File | Contains |
|------|----------|
| `AGENTS.md` | Full architecture, voice rules, all commands, gastric positioning |
| `Personal/Strategy Proposal.md` | Voice rules, serialization arc, publication decisions |
| `Goodspell.online/Brand Playbook/Strategy Proposal.md` | 4-phase plan, gastric + framework, 12 Phase 3 themes |
| `Goodspell.online/Brand Playbook/Goodspell — LinkedIn Content Playbook.md` | Authority Through Reasoning, confidentiality, first line rules |
| `Notes/Strategic Assets from Claude Conversations.md` | All strategic insights extracted from conversations |
| `TEMPLATE.md` | Extraction commands, format, workflow |

---

## 7. File Safety Protocol (from AGENTS.md)

Never use `mv` directly. When moving files between directories:
1. Copy to destination
2. Verify destination (size > 0 bytes, lines > 1)
3. Delete source

---

## How to Use This File

When the user says "check the state":
1. Read this file
2. Scan `Personal/To be posted/` and `Goodspell.online/To be posted/` for the earliest-dated files
3. Scan `Personal/Posted/` and `Goodspell.online/Posted/` for the latest-dated files
4. Report: what was published last, what should publish next, any gaps or overlaps
5. Check rhythm: does the next date follow the rhythm rule (2-day skip, no weekends)?
