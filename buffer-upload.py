#!/usr/bin/env python3
"""Încarcă postările din Personal/To be posted/ în Buffer, programate conform datei din nume."""

import os
import re
import json
import glob
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# (GraphQL variables handles escaping automatically)

# Config
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(REPO_ROOT, '.buffer-personal.env')
POSTS_DIR = os.path.join(REPO_ROOT, 'Personal', 'To be posted')
BUFFER_API = 'https://api.buffer.com'

def load_env(env_file):
    """Citește .env file."""
    env = {}
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, _, val = line.partition('=')
                    env[key.strip()] = val.strip()
    return env

def load_posts(posts_dir):
    """Citește postările din director. Numele fișierului conține data: YYYY-MM-DD Titlu.md"""
    posts = []
    for fpath in sorted(glob.glob(os.path.join(posts_dir, '*.md'))):
        fname = os.path.basename(fpath)
        # Parse date from filename: 2026-06-05 Titlu scurt.md
        match = re.match(r'(\d{4}-\d{2}-\d{2})\s+(.+)\.md$', fname)
        if not match:
            print(f"⚠️  Skipping (no date in name): {fname}")
            continue
        date_str = match.group(1)
        title = match.group(2)
        
        with open(fpath) as f:
            content = f.read()
        
        # Extract text after YAML front matter
        text = content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                text = parts[2].strip()
        
        # Remove hashtags from the text for Buffer (they stay in the markdown)
        # Buffer doesn't support LinkedIn hashtags natively via API
        
        posts.append({
            'path': fpath,
            'filename': fname,
            'date': date_str,
            'title': title,
            'text': text
        })
    return posts

def graphql_request(token, query, variables=None):
    """Trimite un request GraphQL la Buffer API."""
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
    
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = Request(BUFFER_API, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', f'Bearer {token}')
    
    try:
        resp = urlopen(req)
        return json.loads(resp.read())
    except HTTPError as e:
        return json.loads(e.read())

def schedule_post(token, channel_id, text, due_at):
    """Programează o postare în Buffer folosind GraphQL variables."""
    query = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            text
            dueAt
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
            "dueAt": due_at
        }
    }
    
    result = graphql_request(token, query, variables)
    
    if 'data' in result and result['data'].get('createPost', {}).get('post'):
        post = result['data']['createPost']['post']
        return True, post['id']
    else:
        error = result.get('errors', [{'message': 'unknown error'}])[0]['message']
        return False, error

def main():
    env = load_env(ENV_FILE)
    token = env.get('BUFFER_ACCESS_TOKEN')
    channel_id = env.get('BUFFER_CHANNEL_ID')
    
    if not token:
        print(f"❌ Token negăsit în {ENV_FILE}")
        sys.exit(1)
    if not channel_id:
        print(f"❌ Channel ID negăsit în {ENV_FILE}")
        sys.exit(1)
    
    posts = load_posts(POSTS_DIR)
    if not posts:
        print(f"📂 Niciun fișier găsit în {POSTS_DIR}")
        return
    
    print(f"📂 Găsite {len(posts)} postări:")
    
    success = 0
    fail = 0
    
    for post in posts:
        # Due at 10:00 AM Bucharest time (UTC+3) on the scheduled date
        due_at = f"{post['date']}T07:00:00.000Z"  # 10:00 RO time = 07:00 UTC
        
        print(f"  📝 {post['filename']}", end=' ')
        ok, result = schedule_post(token, channel_id, post['text'], due_at)
        
        if ok:
            print(f"✅ (id: {result})")
            success += 1
        else:
            print(f"❌ {result}")
            fail += 1
    
    print(f"\n---\n✅ {success} postări programate | ❌ {fail} eșuate")

if __name__ == '__main__':
    main()
