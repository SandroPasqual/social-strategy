# AGENTS.md — Social Strategy Ecosystem

## ⚡ Entry Point (Start Here)

**Open pi in:** `~/projects/social-strategy` (project root, not account subdirectory)

This project orchestrates **3 LinkedIn accounts** for Sandro Pasqual. The architecture is:

| Priority | Account | Voice | Rhythm | Status |
|----------|---------|-------|--------|--------|
| **1** | **Personal** (Sandro Pasqual) | Gastric / The Observer | Mon/Wed/Fri, 17:00 RO | ✅ Active — 66 posted, 40 scheduled, images generated |
| **2** | **Goodspell.online** (Page) | Gastric + Framework / The Architect | Tue/Thu | ⏸️ Paused — 20 posted, 50 queued, no images yet |
| **3** | **Devorator** (Facebook) | — | — | ❌ Not started — needs analysis |

**Current date:** 2026-06-13 (Saturday). Next post: Jun 15 (Monday) "I can't read the operating system behind it" at 17:00 RO via Buffer.

**Buffer:** Connected ✅ — 10 posts scheduled with images at 17:00 RO (10:00 ET).
**Groups:** 11 active (3 post, 7 test, 1 watch), 8 exited.
**User contact:** Romanian, English-only on LinkedIn. "Big Pickle" = me (the AI agent).

**First thing to do in a new session:** Check Buffer queue (are there free slots?), check if any posted items need moving from `To be posted/` → `Posted/`, then ask user what they want to work on.

---

## Project Architecture

```
Social strategy/
├── AGENTS.md                    ← THIS FILE — read first
├── buffer-upload.py             ← script to upload posts to Buffer (GraphQL)
├── generate-images.py           ← script to generate PNG visuals for posts
├── TEMPLATE.md                  ← standardized post format (front matter)
│
├── Personal/                    ← PRIMARY ACCOUNT — trust is built here
│   ├── Posted/                  ← published posts (66 .md files)
│   ├── To be posted/            ← prepped for publication (40 .md + 40 .png)
│   ├── Framework/               ← voice, comment strategy, field notes (10 files)
│   │   ├── README.md
│   │   ├── 00-distilare-completa.md     ← comprehensive worldview distillation
│   │   ├── 01-vocea-personala-ton.md    ← voice reference: Gastric mechanism, rules
│   │   ├── 02-engagement-comment-strategy.md
│   │   ├── 02b-commenturi-teren.md ← real-world comment cases (537 impressions)
│   │   ├── 03-seria-14-posturi-marcus-aurelius.md ← series origin
│   │   ├── 04-engagement-postari-date.md ← engagement data + "The First Line" analysis
│   │   ├── 05-prezentare-grup-nou.md ← group introduction case study
│   │   ├── 06-misiune-mordor-fundament.md ← Mordor mission framework
│   │   └── _idei-brute.md ← raw idea seeds
│   ├── buffer-config.md         ← Buffer config + API key (private repo, committed)
│   ├── Strategic Analysis.md    ← full diagnostic of past performance
│   └── Strategy Proposal.md     ← decisions, rules, positioning
│
├── Goodspell.online/            ← SECONDARY ACCOUNT — supports, does not lead
│   ├── Posted/                  ← page posts published (20 files)
│   ├── To be posted/            ← 50 posts with WHITE/BLACK numbering (14 with images)
│   ├── Drafts/                  ← drafts waiting to be structured
│   │   └── mortar-most-people-pitch.md
│   ├── Framework/               ← positioning, content, client intelligence (5 files)
│   ├── Brand Playbook/          ← original source documents (15 files)
│   ├── buffer-config.md         ← Buffer config (same API key)
│   ├── Backup/                  ← publication order, strategic analysis, friction docs
│   └── linkedin-image-builder/  ← image generation tool (to be rebuilt with SQLite)
│
└── Devorator/                   ← NOT STARTED — needs Facebook strategy analysis
    ├── Extindere devorator.md
    └── Model devorator.md
```

**Important:** The API key is stored in `Personal/buffer-config.md` and `Goodspell.online/buffer-config.md`. The repo is private, so credentials are committed. `.buffer-*.env` files are gitignored (local copies).

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
| **Hashtags** | **Zero.** Hashtags associate with noise Goodspell actively avoids. |
| **About design** | NO. Everything is strategy |
| **Overlap with Goodspell** | Yes, intentional. Same filter, different angle |
| **Selling** | Zero. Absolutely zero. No pitch, no "you need X," no CTA. The post just is there. The tension remains open. |
| **Frequency** | Every 2 days (Mon/Wed/Fri) |
| **First line** | The only thing that decides whether the post exists for 80% of audience. Must stop the scroll. |
| **Language** | English. Romanian defaults to negation before affirmation — undermines authority. |

## Voice Rules — Goodspell Page

| Principle | How it applies |
|---|---|
| **Positioning** | Gastric + Framework — same mechanism as Personal (recognition), different delivery |
| **Voice** | The Architect — gastric with framework. Names the pattern after the feeling lands. |
| **Position** | Demonstrates through reasoning, not results |
| **Tone** | Gastric. The pattern is named after the reader has already recognized the feeling. |
| **Core theme** | The gap between reality and perception |
| **Hashtags** | Zero. |
| **Frequency** | Tue/Thu, 2/week |
| **Cross-pollination** | Sandro shares page posts on his personal account |

---

## Serialization Arc — Personal (39 posts in To be posted)

### Observer Series (Jun 15 – Aug 12)

```
Attention → Memory → Thinking → Influence → Creation → AI
```

| # | Date | Day | Title | Status |
|---|------|-----|-------|--------|
| 4 | Jun 15 (Mon) | | I can't read the operating system behind it | To be posted |
| 5 | Jun 17 (Wed) | | The first stupid thought dressed up as conviction | To be posted |
| 6 | Jun 19 (Fri) | | The system is rigged and that's not the whole story | To be posted |
| 7 | Jun 22 (Mon) | | You weren't convinced you were mirrored | To be posted |
| 8 | Jun 24 (Wed) | | No system corrupts from the outside | To be posted |
| 9 | Jun 26 (Fri) | | The blue was never in the paint | To be posted |
| 10 | Jun 29 (Mon) | | The deity hallucinated so they grabbed the hammer | To be posted |
| 11 | Jul 1 (Wed) | | The Romans had many gods we have many models | To be posted |
| 12 | Jul 3 (Fri) | | The solo operator with better tools isn't the future | To be posted |
| 13 | Jul 6 (Mon) | | Everyone did their job the result was still generic | To be posted |
| 14 | Jul 8 (Wed) | | You don't need a new look | To be posted |
| 15 | Jul 10 (Fri) | | The designer delivered exactly what was briefed | To be posted |
| 16 | Jul 13 (Mon) | | What happens in that room stays in that room | To be posted |
| 17 | Jul 15 (Wed) | | Every new project starts with the same question | To be posted |
| 18 | Jul 17 (Fri) | | Three variants | To be posted |
| 19 | Jul 22 (Wed) | | Most creative work fails upstream of execution | To be posted |
| 20 | Jul 24 (Fri) | | Every agency had one | To be posted |
| 21 | Jul 27 (Mon) | | The founder hires a designer | To be posted |
| 22 | Jul 29 (Wed) | | Everyone knows they need a strategist now | To be posted |
| 23 | Jul 31 (Fri) | | Most founders don't decide who they're not for | To be posted |
| 24 | Aug 3 (Mon) | | Most founders don't write their mission | To be posted |
| 25 | Aug 5 (Wed) | | Most brands don't have a personality problem | To be posted |
| 26 | Aug 7 (Fri) | | Nobody wants to go deeper | To be posted |
| 27 | Aug 10 (Mon) | | The freelance designer problem isn't talent | To be posted |
| 28 | Aug 12 (Wed) | | Most people pitch what they have | To be posted |

### Founders & Creatives Series (Aug 14 – Sep 14)

Short, punchy "You"-format posts addressing founder-creative dynamics.

| # | Date | Day | Opening line | Status |
|---|------|-----|-------------|--------|
| 29 | Aug 14 (Fri) | | You briefed someone last week | To be posted |
| 30 | Aug 17 (Mon) | | You briefed a designer | To be posted |
| 31 | Aug 19 (Wed) | | You asked for a logo | To be posted |
| 32 | Aug 21 (Fri) | | You've worked with creatives who need total freedom | To be posted |
| 33 | Aug 24 (Mon) | | You chose the color because you liked it | To be posted |
| 34 | Aug 26 (Wed) | | Two projects. Same budget. | To be posted |
| 35 | Aug 28 (Fri) | | What style do you want? | To be posted |
| 36 | Aug 31 (Mon) | | The logo was beautiful. The market didn't care. | To be posted |
| 37 | Sep 2 (Wed) | | You hired a specialist | To be posted |
| 38 | Sep 4 (Fri) | | You opened the software before you understood the problem | To be posted |
| 39 | Sep 7 (Mon) | | The first version was close | To be posted |
| 40 | Sep 9 (Wed) | | The client kept asking for options | To be posted |
| 41 | Sep 11 (Fri) | | You paid for hours. You got execution. | To be posted |
| 42 | Sep 14 (Mon) | | You knew what the answer should be | To be posted |

**Schedule:** Mon/Wed/Fri, skipping weekends. 42 posts covering Jun 15 → Sep 14.

### Already Posted (Jun 5 – Jun 12)

| Date | Title | Type |
|------|-------|------|
| Jun 5 | Saved by the bell. Or trapped by it. | Observer |
| Jun 8 | We're all wet and we pretend we're not | Observer |
| Jun 10 | I publish then the categories appear | Observer |
| Jun 10 | Marcus Aurelius (extra — outside series) | Gastric |
| Jun 12 | Marketable until you're not | Gastric |

### Goodspell Schedule — 50 Posts (Phase 1: Recognition)

**Rhythm:** Tue/Thu, 2/week, skipping weekends. **Voice:** The Architect.

| Range | Dates | Posts |
|-------|-------|-------|
| #01–#10 | Jun 9 – Jul 9 | 10 posts with images ready |
| #11–#24 | Jul 14 – Aug 27 | 14 posts with images ready |
| #25–#50 | Sep 1 – Nov 26 | 26 posts, no images yet |

**Next:** After #50 (Phase 1 complete), Phase 2 (Gathering — 13 posts) begins. Phase 3 (Demonstrated Competence — 12 themes) follows.

---

## Key Decisions (Documented in Strategy Proposal.md)

- **Pivot is correct**: The Brand Strategy phase (Aug-Sep 2025) was exhausted. The Observer is the right direction.
- **Boundary items → Personal**: Anything at the boundary between Personal and Goodspell goes to Personal.
- **Design topics eliminated**: No more posts about logos, colors, fonts. Only strategy.
- **Questions at the end → NO**: Replaced with moments of shared recognition.
- **Groups**: 11 groups remain after audit. Active in 3 (Founders & Startups, Executive Leadership, Tech Founders), testing 7, watching 1 (CGO). 8 exited (incl. Designers Talk).
- **Frequency**: Every 2 days on Personal (Mon/Wed/Fri), 2/week on Goodspell (Tue/Thu). Both skip weekends.

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
- **Personal Framework (voice, tactics, field notes):** `Personal/Framework/`
  - `01-vocea-personala-ton.md` — tone, Gastric mechanism, what (not) to post
  - `02-engagement-comment-strategy.md` — comment strategy framework
  - `02b-commenturi-teren.md` — real-world comment cases (537 impressions)
  - `03-seria-14-posturi-marcus-aurelius.md` — series origin + Marcus Aurelius post
  - `04-engagement-postari-date.md` — engagement data, "The First Line" section
  - `05-prezentare-grup-nou.md` — group introduction case study
- Goodspell analysis: `Goodspell.online/Strategic Analysis.md`
- Goodspell proposal: `Goodspell.online/Strategy Proposal.md`
- **Goodspell Framework:** `Goodspell.online/Framework/`
  - `01-positioning-brand-foundation.md`
  - `03-content-playbook.md`
  - `04-homepage-copy.md`
  - `05-client-intelligence.md`
- Content Playbook: `Goodspell.online/Brand Playbook/Goodspell — LinkedIn Content Playbook.md`
- Brand Foundation: `Goodspell.online/Brand Playbook/Goodspell — Brand Foundation.md`
- Client Intelligence: `Goodspell.online/Brand Playbook/Goodspell — Client Intelligence.md`
- Homepage Copy: `Goodspell.online/Brand Playbook/Goodspell — Homepage Copy.md`
- **Comment Framework** (with active thread tracking): `Goodspell.online/Brand Playbook/Goodspell — LinkedIn Comment Framework.md`
- Goodspell Drafts: `Goodspell.online/Drafts/` (mortar post, future drafts)
- Published posts: `Personal/Posted/` (66 posts), `Goodspell.online/Posted/` (20)
- To be posted: `Personal/To be posted/` (40 posts + 40 images), `Goodspell.online/To be posted/` (50 posts)

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

---

## Buffer Connection

**Status:** Connected ✅ (GraphQL API)

**Account:** Personal (Sandro Pasqual)
- Channel ID: `69b58b0f7be9f8b171572aac`
- Org ID: `6717dc879d4733f183af40e3`
- Token: `wF-K65Oo_HjCzsZs0cIIB8PH412XyMmnFyYEru5L885` (personal key, not OIDC)
- Ora: **17:00 RO = 14:00 UTC = 10:00 ET** (US East Coast target)

**Files:**
- `buffer-upload.py` — script CLI (python3 buffer-upload.py personal)
- `Personal/buffer-config.md` — config + token
- `Personal/.buffer-personal.env` — env vars (gitignored, same token)
- `Goodspell.online/buffer-config.md` — template, use same token with channel ID `69b58b0f7be9f8b171572aab`

**Usage:**
```bash
# Upload next 10 posts to Buffer
python3 buffer-upload.py personal

# Upload all posts (will overwrite existing schedule)
python3 buffer-upload.py personal --dry-run  # preview only
```
**Cont gratuit — doar 10 sloturi.** Când un slot se eliberează (postare publicată), rulezi scriptul să încarci următoarea.

**Limite:**
- Buffer personal key funcționează doar cu GraphQL pe `api.buffer.com`
- Token-ul vechi (OIDC, `uMadUw...`) nu mai funcționează cu API-ul direct
- Cont gratuit = 10 postări simultan max

---

## Image Generation — Post Visuals

**Status:** ✅ Complete for all 40 Personal posts

**Font:** Syne 800 (ExtraBold via variable font `Syne[wght].ttf`)
- Path: `~/.fonts/syne/Syne-variable.ttf` (auto-downloaded from Google Fonts)
- Weight: 800 (`font.set_variation_by_name('ExtraBold')`)
- Size: **64px**

**Canvas:** 1200×627px (LinkedIn link preview)

**Margins:**
- Left/Right: **100px**
- Top: **120px**
- Line height: **78px**

**Colors (alternating dark/light):**

| Variant | Background | Text |
|---------|-----------|------|
| Dark (even index) | `#181715` | `#868177` |
| Light (odd index) | `#868177` | `#181715` |

**No author name** on images. Only extracted text.

**Text rule:** Extract **the scroll-stopping essence** — not the first line, not the title. A short, mysterious, provocative fragment. Max 3-4 lines.

**Storage:** PNG saved alongside `.md` with same date prefix: `2026-06-15.png` next to `2026-06-15 Title.md`

**Script:** `generate-images.py` — auto-extracts essence (heuristic) + wraps text. First 10 images manually refined with curated text.

**Buffer upload:** `buffer-upload.py` automatically finds matching PNG via date prefix and includes it as asset.

---

## Project Status Dashboard

### 📊 Personal Account
| Metric | Value |
|--------|-------|
| **Posted** | 66 posts (Jun 2025 – Jun 2026) |
| **To be posted** | 40 posts with 40 images (Jun 15 – Sep 14) |
| **Buffer scheduled** | 10 posts with images (Jun 15 – Jul 6, 17:00 RO) |
| **Groups active** | 3 (Founders & Startups, Executive Leadership, Tech Founders) |
| **Groups testing** | 7 (CMO Roundtable, CMO Forum, Startup Europe, Startup USA, Founders Exchange, Entrepreneurs Network, Global Entrepreneurship) |
| **Groups watch** | 1 (CGO Community) |
| **Groups exited** | 8 (Small Business, Digital Marketing, Media & Marketing, Chicago, Founders Club, AI Builders, European Entrepreneurship, Designers Talk) |

### 📊 Goodspell.online Account
| Metric | Value |
|--------|-------|
| **Posted** | 20 posts (Phase 1 started) |
| **To be posted** | 50 posts (WHITE/BLACK, #01–#50) |
| **Images** | None generated yet — needs Goodspell brand colors/fonts |
| **Buffer** | Same API key, different channel ID (`69b58b0f7be9f8b171572aab`) |
| **Status** | ⏸️ Paused — waiting for Personal to complete before resuming |

### 📊 Devorator Account
| Metric | Value |
|--------|-------|
| **Status** | ❌ Not started |
| **Files** | `Extindere devorator.md`, `Model devorator.md` (unprocessed) |
| **Next** | Needs full strategy analysis, voice definition, content audit |

---

## Next Steps (Prioritized)

1. **Maintain Buffer queue** — After each post publishes, it frees a slot. Upload next post from `To be posted/` via `python3 buffer-upload.py personal`.
2. **Refine remaining 30 images** — First 10 are manually curated; others were auto-extracted. User may want to manually pick better text for some.
3. **Resume Goodspell** — Start with Drafts/ (mortar post), then generate images (needs brand fonts/colors), then upload to Buffer.
4. **Start Devorator** — Read existing files, analyze Facebook strategy, define voice.
5. **Cross-pollination** — Personal sharing Goodspell posts (after Goodspell is active).

---

## Cleanup History (Jun 13, 2026)

| Action | Details |
|--------|---------|
| ✅ Root Personal cleaned | 27 files → 3 strategic |
| ✅ Drafts deleted | 13 ciorne procesate (all had equivalents) |
| ✅ `~ Idei.md` archived | → `Framework/_idei-brute.md` |
| ✅ Personal files moved | Orade Spania, Pasiunea, Vram, Xolo → `ecosystem/` |
| ✅ Design file deleted | "12. Negative space logo" — not posted |
| ✅ Groups audited | 18 evaluated → 11 remain, 8 exited |
| ✅ Marketable corrected | Buffer already posted on Jun 12 → moved to Posted/ |
| ✅ Buffer connected | Personal Key works via GraphQL; 10 posts with images |
| ✅ 40 images generated | All Personal posts now have PNG visuals |
