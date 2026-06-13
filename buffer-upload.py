#!/usr/bin/env python3
"""Încarcă postări în Buffer. Suportă text + imagini din GitHub raw."""

import os
import re
import json
import glob
import sys
import urllib.request
import urllib.error

# Config
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
GITHUB_RAW = 'https://raw.githubusercontent.com/SandroPasqual/social-strategy/master'
BUFFER_API = 'https://api.buffer.com'
SCHEDULE_HOUR = 14  # 14:00 UTC = 17:00 RO = 10:00 ET (US East Coast target)

ACCOUNTS = {
    'personal': {
        'env': '.buffer-personal.env',
        'dir': 'Personal',
        'channel_id': '69b58b0f7be9f8b171572aac',
    },
    'goodspell': {
        'env': '.buffer-goodspell.env',
        'dir': 'Goodspell.online',
        'channel_id': '69b58b0f7be9f8b171572aab',
    },
}

def load_env(env_file):
    env = {}
    path = os.path.join(REPO_ROOT, env_file)
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, _, val = line.partition('=')
                    env[key.strip()] = val.strip()
    return env

def strip_yaml(content):
    """Elimină front matter YAML dacă există."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content.strip()

def load_posts(posts_dir):
    """Citește postările .md din director."""
    posts = []
    md_files = sorted(glob.glob(os.path.join(posts_dir, '*.md')))
    
    for fpath in md_files:
        fname = os.path.basename(fpath)
        match = re.match(r'(\d{4}-\d{2}-\d{2})\s+(.+)\.md$', fname)
        if not match:
            continue
        date_str = match.group(1)
        
        with open(fpath) as f:
            content = f.read()
        
        text = strip_yaml(content)
        
        # Caută o imagine PNG asociată (același prefix numeric gen "11-BLACK")
        prefix_match = re.match(r'\d{4}-\d{2}-\d{2}\s+(\d+)-', fname)
        image_url = None
        if prefix_match:
            num_prefix = prefix_match.group(1)
            for f in os.listdir(posts_dir):
                if f.endswith('.png') and f.startswith(num_prefix):
                    # Cale relativă de la rădăcina repo-ului
                    rel_path = os.path.relpath(os.path.join(posts_dir, f), REPO_ROOT)
                    # Codifică fiecare componentă a căii pentru URL
                    parts = rel_path.split(os.sep)
                    encoded_parts = [urllib.parse.quote(p) for p in parts]
                    image_url = f"{GITHUB_RAW}/{'/'.join(encoded_parts)}"
                    break
        
        posts.append({
            'path': fpath,
            'filename': fname,
            'date': date_str,
            'text': text,
            'image_url': image_url,
        })
    
    return posts

def graphql_request(token, query, variables=None):
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(BUFFER_API, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', f'Bearer {token}')
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read())

def schedule_post(token, channel_id, text, due_at, image_url=None):
    """Programează o postare cu sau fără imagine (folosind GraphQL variables)."""
    
    assets = []
    if image_url:
        assets.append({'image': {'url': image_url}})
    
    query = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            text
            dueAt
            assets { id mimeType }
          }
        }
        ... on MutationError {
          message
        }
      }
    }
    """
    
    variables = {
        "input": {
            "text": text,
            "channelId": channel_id,
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": due_at,
        }
    }
    if assets:
        variables["input"]["assets"] = assets
    
    result = graphql_request(token, query, variables)
    
    if 'data' in result and result['data'].get('createPost', {}).get('post'):
        post = result['data']['createPost']['post']
        return True, post['id'], post.get('assets', [])
    else:
        error = result.get('errors', [{'message': 'unknown error'}])[0]['message']
        return False, error, []

def main():
    if len(sys.argv) < 2:
        print("Folosire: python3 buffer-upload.py <account> [--dry-run]")
        print(f"  account: personal | goodspell | devorator")
        print(f"  --dry-run: doar arată ce ar face, nu postează")
        sys.exit(1)
    
    account_name = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    if account_name not in ACCOUNTS:
        print(f"Cont necunoscut: {account_name}. Opțiuni: {', '.join(ACCOUNTS.keys())}")
        sys.exit(1)
    
    cfg = ACCOUNTS[account_name]
    env = load_env(cfg['env'])
    token = env.get('BUFFER_ACCESS_TOKEN')
    channel_id = cfg['channel_id']
    
    if not token:
        print(f"❌ Token negăsit în {cfg['env']}")
        sys.exit(1)
    
    posts_dir = os.path.join(REPO_ROOT, cfg['dir'], 'To be posted')
    if not os.path.isdir(posts_dir):
        print(f"❌ Director negăsit: {posts_dir}")
        sys.exit(1)
    
    posts = load_posts(posts_dir)
    if not posts:
        print(f"📂 Niciun fișier .md găsit în {posts_dir}")
        return
    
    print(f"📂 {account_name}: {len(posts)} postări găsite\n")
    
    success = 0
    fail = 0
    
    for post in posts:
        due_at = f"{post['date']}T{SCHEDULE_HOUR - 3:02d}:00:00.000Z"  # 10 RO = 07 UTC
        has_img = " 🖼️" if post['image_url'] else ""
        
        print(f"  {post['date']} — {post['filename'][:60]}...{has_img}", end=' ')
        
        if dry_run:
            print(f"⏭️  (dry-run)")
            continue
        
        ok, result, assets = schedule_post(
            token, channel_id, post['text'], due_at, post['image_url']
        )
        
        if ok:
            img_info = f" + {len(assets)} asset(s)" if assets else ""
            print(f"✅ (id: {result[:12]}){img_info}")
            success += 1
        else:
            print(f"❌ {result}")
            fail += 1
    
    print(f"\n---\n✅ {success} programate | ❌ {fail} eșuate" + (" | ⏭️  dry-run" if dry_run else ""))

if __name__ == '__main__':
    # Need urllib.parse for image URL encoding
    import urllib.parse
    main()
