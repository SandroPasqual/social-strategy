# Roadmap — Goodspell LinkedIn Strategy

## Project
Goodspell Brand Strategy — LinkedIn Company Page
https://www.linkedin.com/company/goodspell-brand-strategy

## Current State (April 4, 2026)
- 9 posts published with images (matching PNGs exist in post folders)
- 2 followers, 550 total impressions, 1 like
- Buffer free (10 post limit) — queue empty
- Source of truth: `GBS Goodspell/` (18 .md files, untouched)
- **35 drafts in WP** (posts 10-44) — content + theme set
- **All 44 images** created, uploaded to WP Media Library, and attached to their posts as Featured Images
- LinkedIn Developer App: pending approval
- LinkedIn API script: ready (waits for Client Secret)

## LinkedIn Developer Setup (April 2, 2026)
- Created LinkedIn Developer App: "Goodspell AutoPoster"
- Client ID: 77nngkdmbc32wc
- Associated Page: Goodspell Brand Strategy (verified)
- Requested access: Community Management API (Page management + Page analytics)
- Status: Pending approval (formular completat)

## Automation Architecture
- Platform: WordPress (goodspell.online) via Novamira MCP
- Scheduling: SiteGround Cron Jobs + WP Cron
- Publishing flow: Draft post in WP → Cron triggers → LinkedIn API posts
- Image workflow: Manual export via admin.html → upload to WP
- AI integration: OpenCode Zen (coding tasks)

## ⚠️ Agent Rules — SEE `AGENTS.md`
**All AI agent rules are in `AGENTS.md` at the project root. Read it first.**

Key rules:
- **WordPress access: Novamira MCP ONLY** — never REST API, never direct file access
- **Plan before acting** — discuss with user, get approval, then execute
- **One attempt then stop** — if it fails once, stop and report
- **No random files in WP** — any WP modification requires explicit approval

## Structure
```
GBS LinkedIn Strategy/
├── 00_Source-of-Truth/       → Index into GBS Goodspell/
├── 01_Strategy/              → the-recipe.md, voice-and-tone.md, messaging-pillars.md, positioning.md, publication-schedule.md
├── 02_Calendar/              → schedule.md, buffer-queue.md, posting-rhythm.md
├── 03_Posts/
│   ├── published/             → 9 folders (posts 01-09), each with post.md + image.png + image.svg
│   └── upcoming/              → 35 folders (posts 10-44), each with post.md + image.png
├── 04_Assets/
│   ├── templates/             → template-white.svg, template-black.svg, template-spec.md
│   ├── visuals-white/        → EMPTY
│   ├── visuals-black/        → EMPTY
│   └── brand/                → Logo web Goodspell.svg
├── 05_Log/                   → published.md, session logs
├── 06_Archive/               → EMPTY
├── 07_Experiments/           → buffer-alternatives.md
├── 08_History/               → session logs
├── 09_Hashtags/              → strategy.md
├── 10_WordPress-Setup/       → wordpress-setup.md (automation workflow)
├── GBS Goodspell/             → SOURCE OF TRUTH
└── Start here/                → Original files (pending cleanup)
```

## Visual Template Specification
- **Canvas**: 1080×1080px
- **Text block**: 920px wide
- **Font**: Syne (loaded via Google Fonts)
- **Sentence 1** (line 1-2): Syne 800
- **Sentence 2** (line 3-4): Syne 800
- **Sentence 3** (line 5-6): Syne 700
- **Spacing**: 72px within sentences, 216px between sentences

### Colors — WHITE
| Element | Color |
|---|---|
| Background | `#E2DFD9` |
| Sentence 1 | `#1C1B18` |
| Sentence 2 | `#646057` |
| Sentence 3 (resolution) | `#86581D` |
| Accent line | `#86581D` |

### Colors — BLACK
| Element | Color |
|---|---|
| Background | `#181715` |
| Sentence 1 | `#FAF9F7` |
| Sentence 2 | `#D5D1C9` |
| Sentence 3 (resolution) | `#86581D` |
| Accent line | `#86581D` |

## Open Decisions
1. ~~Posting rhythm~~ — RESOLVED: calendar-driven, WP Cron
2. ~~Buffer replacement~~ — RESOLVED: WP + SiteGround Cron + LinkedIn API
3. ~~Image production~~ — RESOLVED: all 35 images created
4. **Upload images to WP Media Library** — must be done manually
5. **Attach images to posts** — Featured Image per post
6. **Community Management API** — waiting for LinkedIn approval

## Completed Tasks
- [x] Created folder structure
- [x] Converted all .docx to .md
- [x] Created strategy documents in 01_Strategy/
- [x] Created all 44 post folders with post.md
- [x] Copied 24 PNGs to post folders
- [x] Created SVG templates with correct weights/colors
- [x] Added Google Fonts import to templates
- [x] Scraped LinkedIn and captured real analytics
- [x] Created hashtag strategy
- [x] Updated published.md with real data (dates, impressions, engagement)
- [x] Tested Paper (removed) — Penpot recommended as alternative to Figma
- [x] Created LinkedIn Developer App "Goodspell AutoPoster"
- [x] Verified Goodspell Brand Strategy page
- [x] Requested Community Management API access (Page management + Page analytics)
- [x] Designed automation architecture (WP + Cron + LinkedIn API)
- [x] Planned image workflow (admin.html → WP upload)
- [x] Created WP Custom Post Type "linkedin_post" (mu-plugin)
- [x] Created WP metabox for theme selection (white/black)
- [x] Imported posts 10-44 as drafts in WP
- [x] Copied images 10-44 to strategy folders
- [x] Created LinkedIn API script (linkedin-poster.php)

## Key Documents
| What | Where |
|---|---|
| Template spec | `04_Assets/templates/template-spec.md` |
| Voice & tone | `01_Strategy/voice-and-tone.md` |
| Messaging pillars | `01_Strategy/messaging-pillars.md` |
| The Recipe | `01_Strategy/the-recipe.md` |
| Publishing schedule | `01_Strategy/publication-schedule.md` |
| Hashtags | `09_Hashtags/strategy.md` |
| Published log | `05_Log/published.md` |
| WP Automation Setup | `10_WordPress-Setup/wordpress-setup.md` |

## Rules
- `GBS Goodspell/` is never modified
- All content in English
- Voice: precise, declarative, evidence-grounded, calm
- No forbidden words: authentic, story, passion, journey, transform, empower
- Same 3 hashtags: #BrandStrategy #Positioning #BusinessGrowth

---
*Updated: 2026-04-02*