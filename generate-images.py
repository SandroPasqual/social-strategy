#!/usr/bin/env python3
"""Generează imagini pentru toate postările din To be posted/ (Personal).

Convenție: fiecare .md primește un .png cu același prefix de dată.
"""

import os, re, glob
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = os.path.expanduser("~/.fonts/syne/Syne-variable.ttf")
POSTS_DIR = "Personal/To be posted"

# Culori alternante
PALETTES = [
    {'bg': '#181715', 'text': '#868177'},  # dark
    {'bg': '#868177', 'text': '#181715'},  # light
]

# Dimensiuni
W, H = 1200, 627
MARGIN_X = 100
MARGIN_Y = 120
LINE_H = 78
FONT_SIZE = 64

def strip_yaml(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content.strip()

def extract_essence(text):
    """Extrage o frază scurtă, punchy, scroll-stopping din text."""
    # Elimină hashtag-urile de la final
    text = re.sub(r'#[A-Za-z0-9]+\s*', '', text).strip()
    
    # Împarte în propoziții
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Candidat: propoziții între 20 și 90 caractere, nu prima
    candidates = []
    for i, s in enumerate(sentences):
        s = s.strip()
        # Ignoră prima propoziție (de obicei titlul)
        if i == 0:
            continue
        # Ignoră propozițiile prea scurte sau prea lungi
        if 15 < len(s) < 100:
            candidates.append(s)
    
    if not candidates:
        # Fallback: a doua jumătate a textului, orice frază
        mid = len(text) // 2
        second_half = text[mid:]
        candidates = re.split(r'(?<=[.!?])\s+', second_half)
        candidates = [s.strip() for s in candidates if 15 < len(s) < 100]
    
    if not candidates:
        return None
    
    # Alege cea mai scurtă propoziție (punchy)
    return min(candidates, key=len)

def wrap_text(text, font, max_width):
    """Împarte textul în linii care încap în max_width."""
    words = text.split()
    lines = []
    current = ""
    
    for word in words:
        test = current + " " + word if current else word
        bbox = font.getbbox(test)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    
    return lines

def generate_image(essence, palette, output_path):
    """Generează o imagine cu textul dat."""
    img = Image.new('RGB', (W, H), palette['bg'])
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font.set_variation_by_name('ExtraBold')
    
    # Wrap text în margini
    max_w = W - 2 * MARGIN_X
    lines = wrap_text(essence, font, max_w)
    
    y = MARGIN_Y
    for line in lines[:4]:  # max 4 linii
        draw.text((MARGIN_X, y), line, fill=palette['text'], font=font)
        y += LINE_H
    
    img.save(output_path)
    return len(lines)

def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    
    md_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    print(f"📂 {len(md_files)} postări găsite\n")
    
    generated = 0
    skipped = 0
    
    for i, fpath in enumerate(md_files):
        fname = os.path.basename(fpath)
        match = re.match(r'(\d{4}-\d{2}-\d{2})\s+.+\.md$', fname)
        if not match:
            skipped += 1
            continue
        
        date_prefix = match.group(1)
        img_path = os.path.join(POSTS_DIR, f"{date_prefix}.png")
        
        # Dacă imaginea există deja, o sărim
        if os.path.exists(img_path):
            print(f"  ⏭️  {date_prefix} — imaginea există deja")
            skipped += 1
            continue
        
        with open(fpath) as f:
            content = f.read()
        
        body = strip_yaml(content)
        essence = extract_essence(body)
        
        if not essence:
            print(f"  ❌ {date_prefix} — nu am găsit text potrivit")
            skipped += 1
            continue
        
        # Alternează paleta
        palette = PALETTES[i % 2]
        
        generate_image(essence, palette, img_path)
        print(f"  ✅ {date_prefix} | {palette['bg']} | \"{essence[:50]}...\"")
        generated += 1
    
    print(f"\n---\n✅ {generated} generate | ⏭️  {skipped} sărite")

if __name__ == '__main__':
    main()
