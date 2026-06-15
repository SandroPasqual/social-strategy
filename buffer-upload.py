#!/usr/bin/env python3
"""Încarcă postări în Buffer. Suportă text + imagini din GitHub raw."""

import os
import re
import json
import glob
import sys
import time
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
        'org_id': '6717dc879d4733f183af40e3',
    },
    'goodspell': {
        'env': '.buffer-goodspell.env',
        'dir': 'Goodspell.online',
        'channel_id': '69b58b0f7be9f8b171572aab',
        'org_id': '6717dc879d4733f183af40e3',
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
        
        # Caută o imagine PNG asociată
        image_url = None
        # 1) Convenția Personal: YYYY-MM-DD.png (același prefix de dată)
        date_prefix = match.group(1)  # e.g. "2026-06-15"
        for f in os.listdir(posts_dir):
            if f.endswith('.png') and f.startswith(date_prefix):
                rel_path = os.path.relpath(os.path.join(posts_dir, f), REPO_ROOT)
                parts = rel_path.split(os.sep)
                encoded_parts = [urllib.parse.quote(p) for p in parts]
                image_url = f"{GITHUB_RAW}/{'/'.join(encoded_parts)}"
                break
        # 2) Convenția Goodspell: prefix numeric gen "11-BLACK"
        if not image_url:
            prefix_match = re.match(r'\d{4}-\d{2}-\d{2}\s+(\d+)-', fname)
            if prefix_match:
                num_prefix = prefix_match.group(1)
                for f in os.listdir(posts_dir):
                    if f.endswith('.png') and f.startswith(num_prefix):
                        rel_path = os.path.relpath(os.path.join(posts_dir, f), REPO_ROOT)
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

def check_posts_to_move(posts_dir, posted_dir):
    """Verifică local dacă vreo postare din To be posted a fost deja publicată (data în urmă) și nu a fost mutată."""
    if not os.path.isdir(posts_dir) or not os.path.isdir(posted_dir):
        return 0

    import datetime
    today = datetime.date.today().isoformat()

    posted_files = set()
    for fname in os.listdir(posted_dir):
        if fname.endswith('.md'):
            match = re.match(r'(\d{4}-\d{2}-\d{2})\s+', fname)
            if match:
                posted_files.add(match.group(1))

    to_move = []
    for fname in sorted(os.listdir(posts_dir)):
        if fname.endswith('.md'):
            match = re.match(r'(\d{4}-\d{2}-\d{2})\s+(.+\.md$)', fname)
            if match:
                date_str = match.group(1)
                if date_str < today and date_str not in posted_files:
                    to_move.append((date_str, fname))

    if not to_move:
        return 0

    print(f"  ⚠️  {len(to_move)} postări cu data în urmă, posibil publicate:")
    for date_str, fname in to_move:
        print(f"     {date_str} — {fname[:60]}")
    print("     rulează: mv ... (manual, după verificare)\n")
    return len(to_move)


def show_queue(token, channel_id, org_id):
    """Arată postările programate în Buffer — un API call."""
    query = '''
    query GetQueue($input: PostsInput!) {
      posts(input: $input) {
        totalCount
        edges {
          node {
            id
            text
            dueAt
            status
            assets { id mimeType }
          }
        }
      }
    }
    '''
    variables = {
        'input': {
            'organizationId': org_id,
            'filter': {
                'channelIds': [channel_id],
                'status': 'scheduled',
            },
        }
    }
    result = graphql_request(token, query, variables)
    posts = result.get('data', {}).get('posts', {})
    edges = posts.get('edges', [])
    
    if not edges:
        print("📭 Queue goală — 0 postări programate.")
        return

    print(f"📋 {len(edges)} postări în queue:\n")
    for edge in edges:
        node = edge['node']
        due = node['dueAt'][:10] if node.get('dueAt') else '??'
        text_preview = node['text'][:70].replace('\n', ' ')
        has_asset = ' 🖼️' if node.get('assets') else ''
        print(f"  {due} — {text_preview}...{has_asset}")
    print()


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

def delete_queue(token, channel_id, org_id):
    """Șterge TOATE postările programate din queue."""
    # 1) Ia postările
    query = '''
    query GetQueue($input: PostsInput!) {
      posts(input: $input) {
        totalCount
        edges {
          node {
            id
            text
            dueAt
          }
        }
      }
    }
    '''
    variables = {
        'input': {
            'organizationId': org_id,
            'filter': {
                'channelIds': [channel_id],
                'status': 'scheduled',
            },
        }
    }
    result = graphql_request(token, query, variables)
    edges = result.get('data', {}).get('posts', {}).get('edges', [])
    
    if not edges:
        print("📭 Queue goală — nimic de șters.")
        return 0
    
    print(f"🗑️ Șterg {len(edges)} postări din queue...")
    
    mutation = '''
    mutation DeletePost($input: DeletePostInput!) {
      deletePost(input: $input) {
        ... on DeletePostSuccess {
          id
        }
        ... on VoidMutationError {
          message
        }
      }
    }
    '''
    
    deleted = 0
    for edge in edges:
        post_id = edge['node']['id']
        due = edge['node']['dueAt'][:10]
        text_preview = edge['node']['text'][:50].replace('\n', ' ')
        
        del_vars = {'input': {'id': post_id}}
        del_result = graphql_request(token, mutation, del_vars)
        
        if del_result.get('data', {}).get('deletePost', {}).get('id'):
            print(f"    ✅ {due} — {text_preview}...")
            deleted += 1
        else:
            err = del_result.get('errors', [{}])[0].get('message', 'unknown')
            print(f"    ❌ {due} — {err}")
    
    print(f"\n🗑️ {deleted} șterse din queue.")
    return deleted


def show_check(token, channel_id, org_id, posts_dir, posted_dir):
    """Startup checklist complet: queue + postări de mutat."""
    print("═" * 50)
    print("🔍 STARTUP CHECK — Buffer + Local")
    print("═" * 50)
    show_queue(token, channel_id, org_id)
    n = check_posts_to_move(posts_dir, posted_dir)
    print("═" * 50)
    if n > 0:
        print(f"📦 {n} postări de verificat/mutat")
    else:
        print("📦 Nimic de mutat — local e curat")
    print()


def main():
    if len(sys.argv) < 2:
        print("Folosire: python3 buffer-upload.py <account> [--dry-run] [--queue] [--check]")
        print(f"  account: personal | goodspell | devorator")
        print(f"  --dry-run: doar arată ce ar face, nu postează")
        print(f"  --queue:   arată ce e în queue-ul Buffer (1 API call)")
        print(f"  --check:   startup checklist complet (queue + local)")
        print(f"  --flush:   șterge TOATE postările din queue")
        sys.exit(1)
    
    account_name = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    show_q = '--queue' in sys.argv
    do_check = '--check' in sys.argv
    do_flush = '--flush' in sys.argv
    
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
    posted_dir = os.path.join(REPO_ROOT, cfg['dir'], 'Posted')

    if show_q:
        show_queue(token, channel_id, cfg['org_id'])
        return

    if do_flush:
        delete_queue(token, channel_id, cfg['org_id'])
        return

    if do_check:
        show_check(token, channel_id, cfg['org_id'], posts_dir, posted_dir)
        return
    if not os.path.isdir(posts_dir):
        print(f"❌ Director negăsit: {posts_dir}")
        sys.exit(1)
    
    posts = load_posts(posts_dir)
    if not posts:
        print(f"📂 Niciun fișier .md găsit în {posts_dir}")
        return
    
    print(f"📂 {account_name}: {len(posts)} postări locale, gata de upload\n")
    
    success = 0
    fail = 0
    
    for post in posts:
        due_at = f"{post['date']}T{SCHEDULE_HOUR - 3:02d}:00:00.000Z"  # 10 RO = 07 UTC
        has_img = " 🖼️" if post['image_url'] else ""
        
        print(f"  {post['date']} — {post['filename'][:60]}...{has_img}", end=' ')
        
        if dry_run:
            print(f"⏭️  (dry-run)")
            continue
        
        # Pauză între postări să nu stresăm API-ul
        time.sleep(2)
        
        ok, result, assets = schedule_post(
            token, channel_id, post['text'], due_at, post['image_url']
        )
        
        if ok:
            img_info = f" + {len(assets)} asset(s)" if assets else ""
            print(f"✅ (id: {result[:12]}){img_info}")
            success += 1
        elif "rate limit" in result.lower() or "too many requests" in result.lower():
            print(f"⏸️  rate limit — pauză 30s...")
            time.sleep(30)
            # reîncercare o singură dată
            ok, result, assets = schedule_post(
                token, channel_id, post['text'], due_at, post['image_url']
            )
            if ok:
                img_info = f" + {len(assets)} asset(s)" if assets else ""
                print(f"   ✅ după pauză (id: {result[:12]}){img_info}")
                success += 1
            else:
                print(f"   ❌ după pauză: {result}")
                fail += 1
        else:
            print(f"❌ {result}")
            fail += 1
    
    if not dry_run:
        total_after = success
        print(f"\n---\n✅ {total_after} programate | ❌ {fail} eșuate")
    else:
        print(f"\n---\n⏭️  dry-run — 0 postări trimise efectiv")

if __name__ == '__main__':
    # Need urllib.parse for image URL encoding
    import urllib.parse
    main()
