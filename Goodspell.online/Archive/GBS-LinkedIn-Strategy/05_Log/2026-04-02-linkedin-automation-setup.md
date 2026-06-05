# Session Log — 2026-04-02

## Session 1 — LinkedIn Automation Setup

### Topic
Discussed and planned LinkedIn auto-posting system to replace Buffer.

### Decisions Made
1. **Platform**: WordPress (goodspell.online) as central hub
2. **Scheduling**: SiteGround Cron Jobs + WP Cron (not external services)
3. **Image workflow**: Manual export via admin.html → upload to WP → publish
4. **Trigger**: When WP publishes a post, LinkedIn API posts automatically
5. **AI**: OpenCode Zen for coding tasks (not content generation)

### LinkedIn Developer Setup
- Created app: "Goodspell AutoPoster"
- Client ID: 77nngkdmbc32wc
- Verified: Goodspell Brand Strategy page
- Requested: Community Management API (Page management + Page analytics)
- Status: Pending approval from LinkedIn

## Session 2 — WordPress Implementation

### What Was Built

1. **MCP Connection**: novamira-goodspell-online
   - Added to ~/.config/opencode/config.json
   - Connected to goodspell.online WordPress

2. **Custom Post Type**: `linkedin_post`
   - Location: `wp-content/mu-plugins/goodspell-linkedin-cpt.php`
   - Fields: li_theme, li_image_url, li_original_post_number, li_published_on_linkedin, li_linkedin_post_id

3. **Metabox**: LinkedIn Options
   - Theme selector: White/Black
   - Original post number field
   - Publishing status indicator

4. **Draft Posts Created**: 10-14
   - Post 10: Google returns a version of you (white)
   - Post 11: The referral you've been waiting for (black)
   - Post 12: Your LinkedIn and your website (white)
   - Post 13: You built something serious (white)
   - Post 14: You were invited to speak (black)

5. **Documentation Created**
   - `10_WordPress-Setup/wordpress-setup.md` — full workflow documented
   - Updated ROADMAP.md with new completed tasks

### Workflow Documented
1. Create draft in WP (not visible on site)
2. Set publish date (schedule)
3. SiteGround Cron triggers every 30 min
4. PHP script checks for scheduled posts
5. Posts to LinkedIn via API
6. Updates meta to mark as published

### Next Steps
1. Wait for LinkedIn API approval
2. Upload images for posts 10-44
3. Create LinkedIn API mu-plugin
4. Set up SiteGround Cron Jobs

## Session 3 — LinkedIn API Script + All Drafts Imported

### What Was Built

1. **LinkedIn API Script**: `linkedin-poster.php`
   - Location: `wp-content/mu-plugins/linkedin-poster.php`
   - Functions: OAuth token management, text posts, image upload, batch processing
   - Includes WP Cron hook: `li_check_pending_posts`

2. **All Drafts Imported**: Posts 10-44
   - Total: 35 posts as drafts in WP
   - All content from strategy files imported
   - Theme metadata set correctly

3. **Images Copied**: Posts 10-44
   - Copied from `/home/sandro/Downloads/` to strategy folders
   - Location: `03_Posts/upcoming/XX-*/image.png`

### Current WP Status
- Custom Post Type: linkedin_post (active)
- Draft posts: 35 (posts 10-44)
- Featured images: 0 (not uploaded to WP yet)
- Published posts: 0

### Pending Before Going Live
1. Upload images to WP Media Library (WP Admin)
2. Attach images to posts (Featured Image)
3. LinkedIn API approval + Client Secret
4. Fill in LI_CLIENT_SECRET in linkedin-poster.php
5. Configure SiteGround Cron Jobs

---
*Session date: 2026-04-02*
