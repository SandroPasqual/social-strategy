# Social Strategy — Post Template & Workflow

> Documents how we save local posts for analysis.
> Updated: 2026-06-05

---

## 1. Folder Structure

```
Social strategy/
├── Goodspell.online/          ← brand strategy consultancy
│   ├── Posted/                ← published posts
│   └── Drafts/                ← unpublished drafts
├── Personal/                  ← Sandro Pasqual personal account
│   ├── Posted/                ← published posts
│   ├── Drafts/                ← raw drafts from Ideas
│   └── To be posted/          ← prepped for publication
├── Devorator/                 ← Devorator page (pending)
│   ├── Posted/                ← published posts
│   └── Drafts/                ← unpublished drafts
└── Ideas/                     ← original source (Drive backup, unchanged)
```

---

## 2. Post Format

Each post is a `.md` file with **YAML front matter** followed by the exact post text.

### Template:

```markdown
---
date: YYYY-MM-DD
platform: LinkedIn
likes: N
comments: N
impressions: N
link: https://www.linkedin.com/posts/...
type: text | image | carousel
---

Exact post text...

#Hashtag1 #Hashtag2
```

### Fields:

| Field | Required | Description |
|---|---|---|
| `date` | yes | Publication date (YYYY-MM-DD) |
| `platform` | yes | Always `LinkedIn` (for now) |
| `likes` | yes | Number of likes |
| `comments` | yes | Number of comments |
| `impressions` | yes | Impressions count (from logged-in LinkedIn) |
| `link` | yes | Full post URL |
| `type` | yes | `text`, `image`, `carousel` — visual format |
| hashtags | optional | Kept in the post text at the end |

### File name:

```
YYYY-MM-DD Short descriptive title.md
```

- Date first for chronological sorting
- No quotes, slashes, or special characters in the name
- Max ~50 characters

---

## 3. Extracting a LinkedIn Post

### Terminal method:

```bash
# 1. Fetch the post page
curl -s -L "LINKEDIN_URL" > /tmp/post.html

# 2. Extract date
grep -o '"datePublished":"[^"]*"' /tmp/post.html | head -1

# 3. Extract text
grep -oP '"articleBody":"(?:[^"\\]|\\.)*"' /tmp/post.html | head -1

# 4. Extract likes
grep -oP '"interactionType":"http://schema.org/LikeAction","userInteractionCount":\d+' /tmp/post.html | grep -oP '\d+$'

# 5. Extract comments
grep -oP '"interactionType":"https://schema.org/CommentAction","userInteractionCount":\d+' /tmp/post.html | grep -oP '\d+$'

# 6. Extract images (if any)
grep -o '"image":[^]]*\]' /tmp/post.html
```

### Technical notes:

- LinkedIn embeds structured data in JSON-LD (`<script type="application/ld+json">`)
- `articleBody` may contain escaped characters (`\"`, `\n`) — the regex above handles them
- Likes appear twice in JSON-LD (once in the post, once in another block). The first value is correct.
- Impressions are NOT publicly available — must be read from a logged-in LinkedIn session

---

## 4. Full Workflow for a New Post

1. Receive link + impressions from user
2. Extract structured data with curl
3. Write `.md` file with front matter + text
4. Save to `[Project]/Posted/` as `YYYY-MM-DD Title.md`
5. (Optional) Update later with additional stats

---

## 5. Centralized Statistics

To keep the full picture, maintain a stats table in `[Project]/stats.md`:

```markdown
| # | Post | Date | Impressions | Likes | Comments |
|---|---|---|---|---|---|
| 1 | Title | 2025-MM-DD | N | N | N |
| 2 | ... | ... | ... | ... | ... |
```

---

## 6. Examples

### Text post (most common):

```yaml
---
date: 2025-08-24
platform: LinkedIn
likes: 1
comments: 0
impressions: 484
link: https://www.linkedin.com/posts/sandropasqual_...
type: text
---

A logo is not a painting. It's a flag.

Your logo isn't meant to be hung in a gallery...

#LogoDesign #BrandIdentity #GraphicDesign
```

### Image post (short text):

```yaml
---
date: 2025-08-29
platform: LinkedIn
likes: 0
comments: 0
impressions: 82
link: https://www.linkedin.com/posts/...
type: image
---

A design system is like an artist's limited palette...
```

---

## 7. Applying to Other Projects

### Goodspell.online

Existing posts (01-44) are already documented in:
`../goodspell-linkedin-strategy/GBS-LinkedIn-Strategy/03_Posts/`

Need to convert to the same format:
- Extract real stats from LinkedIn
- Add YAML front matter
- Move to `Goodspell.online/Posted/`

### Devorator

No published posts yet. When we start, use the same template.
