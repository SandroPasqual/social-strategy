# WordPress Setup — LinkedIn Auto-Posting

## Site
- **URL**: https://goodspell.online
- **MCP**: novamira-goodspell-online (Novamira MCP connection)
- **WP Version**: 6.9.4
- **Theme**: Kadence

## IMPORTANT — Communication Method
**NICIODATA REST API.** Doar MCP Novamira WP plugin.
- Pentru toate operațiunile WordPress: folosește Novamira MCP
- Pentru execuție PHP pe server: novamira/execute-php
- Pentru scriere fișiere: novamira/write-file

## Architecture Overview

```
[Content Source] → [WordPress Draft] → [Schedule] → [Cron] → [LinkedIn API] → [Company Page]
                    ↑
              CPT: linkedin_post
              (not visible on site)
```

## WP Custom Post Type

### linkedin_post
Custom post type for managing LinkedIn posts. Not visible on site (`public: false`).

**Location**: `wp-content/mu-plugins/goodspell-linkedin-cpt.php`

**Fields**:
| Meta Key | Type | Description |
|----------|------|-------------|
| `li_theme` | string | `white` or `black` |
| `li_image_url` | string | URL to image (optional) |
| `li_original_post_number` | int | Original post number (10, 11, etc.) |
| `li_published_on_linkedin` | bool | Has been published to LinkedIn |
| `li_linkedin_post_id` | string | LinkedIn post ID after publishing |

## Workflow: From Draft to LinkedIn Post

### Step 1 — Create Draft
1. WP Admin → LinkedIn Posts → Add New
2. Title: "Post XX — [first few words]"
3. Content: Full post body with hashtags
4. Metabox (right sidebar):
   - Theme: White or Black
   - Original Post Number: e.g. 15

### Step 2 — Schedule
1. In WP Admin, set **Publish date** to desired date/time
2. Post remains a draft internally — NOT visible on website
3. CPT is set to `public: false` — no public-facing content

### Step 3 — Cron Trigger (SiteGround)
1. SiteGround Cron Jobs runs every 30 minutes
2. PHP script checks WP for posts with `post_date <= NOW()`
3. Script skips if `li_published_on_linkedin` = true

### Step 4 — LinkedIn API Publish
1. Script calls LinkedIn Community Management API
2. Posts text + image (if attached) to Company Page
3. Updates `li_published_on_linkedin` = true
4. Stores LinkedIn post ID in `li_linkedin_post_id`

### Step 5 — Done
Post is live on LinkedIn. WP post remains as record (never published on site).

---

## Why Drafts Never Publish to Site?

CPT `linkedin_post` has:
```php
'public' => false,
'show_ui' => true,
```

- Post appears in WP Admin for management
- Post is NOT visible on frontend
- WP only "marks" it as published internally
- Script detects status change via `get_posts()` query

---

## Manual Publish (for Testing)

To test immediately:
1. Click "Publish" in WP Admin (not "Schedule")
2. Script detects new published post
3. Posts to LinkedIn instantly

---

## Current Status

### Draft Posts
All 35 posts (10-44) are created as drafts in WP.

### Images
Images are created and copied to strategy folders:
- Location: `03_Posts/upcoming/XX-*/image.png`
- Status: Copied locally, NOT uploaded to WP Media Library yet

### To Upload Images
1. WP Admin → Media → Add New
2. Upload all PNGs from `03_Posts/upcoming/XX-*/image.png`
3. Then attach each to corresponding post (Featured Image)

## Next Steps

1. Upload images to WP Media Library
2. Attach images to posts (Featured Image)
3. Wait for LinkedIn API approval + Client Secret
4. Fill in LI_CLIENT_SECRET in linkedin-poster.php
5. Set up SiteGround Cron Jobs

---
*Created: 2026-04-02*
*Updated: 2026-04-02*
