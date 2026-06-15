#!/usr/bin/env python3
"""Generează imagini pentru toate postările din To be posted/ (Personal).

Convenție: fiecare .md primește un .png cu același prefix de dată.
"""

import os, re, glob
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = os.path.expanduser("~/.fonts/syne/Syne-variable.ttf")
POSTS_DIR = "Personal/To be posted"
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# Culori alternante
PALETTES = [
    {'bg': '#181715', 'text': '#868177'},  # dark
    {'bg': '#868177', 'text': '#181715'},  # light
]

# Dimensiuni
W, H = 1200, 627
MARGIN_X = 100
MARGIN_Y = 220  # textul începe mai jos, departe de deco
LINE_H = 78
FONT_SIZE = 64
DECO_SIZE = 48
DECO_Y_OFFSET = 120  # distanța de la text la deco (220 - 100 = 120)

def parse_front_matter(content):
    """Extrage front matter YAML și body. Returnează (front_matter_dict, body)."""
    fm = {}
    body = content.strip()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            raw = parts[1].strip()
            body = parts[2].strip()
            for line in raw.split('\n'):
                if ':' in line:
                    k, _, v = line.partition(':')
                    fm[k.strip()] = v.strip()
    return fm, body

def extract_essence(text, font=None, max_width=None, forced=None):
    """Extrage o frază scurtă, punchy, scroll-stopping din text.
    Dacă primește font + max_width, validează și layout-ul.
    Dacă primește forced, folosește direct textul respectiv.
    """
    if forced:
        if font and max_width:
            ok, msg = validate_essence(forced, font, max_width)
            return (forced, msg) if ok else (None, f'❌ forced text invalid: {msg}')
        return forced, None

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
        return None, None
    
    # Sortează după lungime (preferăm mai scurt = punchy)
    candidates.sort(key=len)
    
    for essence in candidates:
        if font and max_width:
            ok, msg = validate_essence(essence, font, max_width)
            if not ok:
                continue  # încearcă următorul candidat
        return essence, msg if font else None
    
    return None, None

def load_font():
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font.set_variation_by_name('ExtraBold')
    return font


def word_width(word, font):
    bbox = font.getbbox(word)
    return bbox[2] - bbox[0]


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


def validate_essence(essence, font, max_width, max_lines=3):
    """Verifică dacă textul încape în layout. Returnează (ok, motiv)."""
    # Verifică fiecare cuvânt individual
    for word in essence.split():
        w = word_width(word, font)
        if w > max_width:
            return False, f'cuvântul "{word}" e prea lat ({w}px > {max_width}px)'
    
    # Verifică numărul de linii după wrap
    lines = wrap_text(essence, font, max_width)
    if len(lines) > max_lines:
        return False, f'textul intră pe {len(lines)} linii (max {max_lines})'
    
    return True, f'{len(lines)} din {max_lines} linii'

def generate_image(essence, palette, output_path, deco=None):
    """Generează o imagine PNG cu textul dat. Opțional un decor deasupra (ex: asterisc sau SVG)."""
    from PIL import Image as PILImage
    
    img = PILImage.new('RGB', (W, H), palette['bg'])
    draw = ImageDraw.Draw(img)
    
    font = load_font()
    
    # Wrap text în margini
    max_w = W - 2 * MARGIN_X
    lines = wrap_text(essence, font, max_w)
    
    # Safety: dacă totuși textul depășește 3 linii, nu trunchia silent
    if len(lines) > 3:
        print(f"    ⚠️  textul intră pe {len(lines)} linii — se va trunchia! Verifică manual.")
    
    y = MARGIN_Y
    
    # Decor deasupra textului
    if deco:
        if deco.endswith('.svg'):
            # Render SVG cu ImageMagick și paste ca overlay
            svg_path = os.path.join(REPO_ROOT, deco) if not os.path.isabs(deco) else deco
            if os.path.exists(svg_path):
                import subprocess, tempfile
                with open(svg_path) as f:
                    svg_data = f.read()
                svg_data = svg_data.replace('currentColor', palette['text'])
                
                tmp_svg = tempfile.NamedTemporaryFile(suffix='.svg', delete=False, mode='w')
                tmp_svg.write(svg_data)
                tmp_svg.close()
                tmp_png = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
                tmp_png.close()
                
                try:
                    subprocess.run(['convert', '-background', 'none', tmp_svg.name, tmp_png.name],
                                 check=True, capture_output=True)
                    deco_img = PILImage.open(tmp_png.name).convert('RGBA')
                    # Redimensionăm la ~36px înălțime
                    deco_h = 36
                    ratio = deco_h / deco_img.height
                    deco_w = int(deco_img.width * ratio)
                    deco_img = deco_img.resize((deco_w, deco_h), PILImage.LANCZOS)
                    # Poziționăm deasupra textului
                    deco_x = MARGIN_X
                    deco_y = y - deco_h - 16
                    img.paste(deco_img, (deco_x, deco_y), deco_img)
                finally:
                    os.unlink(tmp_svg.name)
                    if os.path.exists(tmp_png.name):
                        os.unlink(tmp_png.name)
        else:
            # Text character (✳, *, etc.)
            deco_font = ImageFont.truetype(FONT_PATH, DECO_SIZE)
            draw.text((MARGIN_X, y - DECO_Y_OFFSET), deco, fill=palette['text'], font=deco_font)
    
    for line in lines[:3]:  # max 3 linii
        draw.text((MARGIN_X, y), line, fill=palette['text'], font=font)
        y += LINE_H
    
    img.save(output_path)
    return len(lines)


def generate_svg(essence, palette, output_path, deco=None):
    """Generează un SVG vectorial editabil, identic ca layout cu PNG-ul.
    Opțional un decor deasupra (ex: asterisc sau favicon.svg).
    """
    max_w = W - 2 * MARGIN_X
    
    # Wrap text identic cu PNG-ul
    font = load_font()
    lines = wrap_text(essence, font, max_w)[:3]
    
    text_parts = []
    
    # Decor deasupra
    if deco:
        if deco.endswith('.svg'):
            # Încorporăm SVG-ul inline (doar conținutul, fără wrapper)
            svg_path = os.path.join(REPO_ROOT, deco) if not os.path.isabs(deco) else deco
            if os.path.exists(svg_path):
                with open(svg_path) as f:
                    inner = f.read()
                # Extragem doar interiorul (ce e după <svg...>)
                inner = re.sub(r'<svg[^>]*>', '', inner)
                inner = inner.replace('</svg>', '')
                inner = inner.replace('currentColor', palette['text'])
                # Ajustăm viewBox să fie relativ
                text_parts.append(f'    <g transform="translate({MARGIN_X}, {MARGIN_Y - DECO_Y_OFFSET}) scale(0.85)">{inner.strip()}</g>')
        else:
            # Text character
            text_parts.append(
                f'    <text x="{MARGIN_X}" y="{MARGIN_Y - DECO_Y_OFFSET}"'
                f' font-family="Syne" font-size="{DECO_SIZE}"'
                f' fill="{palette["text"]}">{deco}</text>'
            )
    
    # Textul principal
    y = MARGIN_Y
    for line in lines:
        text_parts.append(
            f'    <text x="{MARGIN_X}" y="{y}"'
            f' font-family="Syne" font-size="{FONT_SIZE}" font-weight="800"'
            f' fill="{palette["text"]}">{line}</text>'
        )
        y += LINE_H
    
    text_block = '\n'.join(text_parts)
    
    svg_content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg"\n'
        f'     width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'  <rect width="{W}" height="{H}" fill="{palette["bg"]}"/>\n'
        f'{text_block}\n'
        '</svg>\n'
    )
    
    with open(output_path, 'w') as f:
        f.write(svg_content)
    return len(lines)

def main():
    os.makedirs(POSTS_DIR, exist_ok=True)
    
    md_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    print(f"📂 {len(md_files)} postări găsite\n")
    
    generated = 0
    skipped = 0
    
    font = load_font()
    max_w = W - 2 * MARGIN_X
    
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
        
        fm, body = parse_front_matter(content)
        forced_text = fm.get('image_text', '').strip(' "\'') or None
        deco = fm.get('image_deco', '').strip(' "\'') or None
        essence, validation_msg = extract_essence(body, font, max_w, forced=forced_text)
        
        if not essence:
            print(f"  ❌ {date_prefix} — nu am găsit text potrivit (toți candidații depășesc layout-ul)")
            skipped += 1
            continue
        
        # Alternează paleta
        palette = PALETTES[i % 2]
        
        num_lines = generate_image(essence, palette, img_path, deco=deco)
        svg_path = os.path.join(POSTS_DIR, f"{date_prefix}.svg")
        generate_svg(essence, palette, svg_path, deco=deco)
        print(f"  ✅ {date_prefix} | {palette['bg']} | {validation_msg} | \"{essence[:50]}...\" -> PNG + SVG")
        generated += 1
    
    print(f"\n---\n✅ {generated} generate | ⏭️  {skipped} sărite")

if __name__ == '__main__':
    main()
