#!/usr/bin/env python3
"""
Generează imagini pentru postările Goodspell (1080×1080 pătrat).

Layout (from linkedin-image-builder):
  1. Gold accent line: 200×5px la y=140, #86581D
  2. 3 propoziții: Syne 72px (S1 principal, S2 gri, S3 auriu)
  3. Logo Goodspell jos (500×77px la 80px de bottom)
  4. Paletă alternantă dark/light
"""

import os, re, glob, base64
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = os.path.expanduser("~/.fonts/syne/Syne-variable.ttf")
POSTS_DIR = "goodspell/To be posted"
LOGO_PATH = "goodspell/goodspell-logo.png"
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# Dimensiuni canvas
W, H = 1080, 1080

# Palete Goodspell (alternante după index)
PALETTES = [
    {  # dark
        'bg': '#1C1B18',
        's1': '#E2DFD9',
        's2': '#646057',
        's3': '#86581D',
        'gold_line': '#86581D',
    },
    {  # light
        'bg': '#E2DFD9',
        's1': '#1C1B18',
        's2': '#646057',
        's3': '#86581D',
        'gold_line': '#86581D',
    },
]

# Layout
LINE_Y = 140
LINE_W, LINE_H = 200, 5
S1_Y = 175           # draw y — primul rând
VISUAL_GAP = 35      # gap vizibil între blocuri
FONT_SIZE = 72
GAP_BETWEEN_LINES = 2
LOGO_MARGIN_BOTTOM = 80
LOGO_W, LOGO_H = 500, 77


def parse_front_matter(content):
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
                    fm[k.strip()] = v.strip().strip('"\'')
    return fm, body


def load_font(variation='ExtraBold'):
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font.set_variation_by_name(variation)
    return font


def split_sentences(text):
    if not text:
        return []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def wrap_sentence(sentence, font, max_width):
    """Word-wrap a sentence into lines that fit max_width."""
    words = sentence.split()
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


def generate_image(sentences, palette, output_path):
    """Generează PNG cu poziționare dinamică a blocurilor de text."""
    img = Image.new('RGB', (W, H), palette['bg'])
    draw = ImageDraw.Draw(img)
    max_w = W - 2 * 80
    font_eb = load_font('ExtraBold')
    font_b = load_font_bold()

    # 1. Gold accent line
    draw.rectangle([80, LINE_Y, 80 + LINE_W, LINE_Y + LINE_H], fill=palette['gold_line'])

    # 2. Logo at bottom
    logo_path = os.path.join(REPO_ROOT, LOGO_PATH)
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo_resized = logo.resize((LOGO_W, LOGO_H), Image.LANCZOS)
        logo_y = H - LOGO_MARGIN_BOTTOM - LOGO_H
        img.paste(logo_resized, (80, logo_y), logo_resized)

    # 3. Sentences — dinamic, cu VISUAL_GAP constant între blocuri
    cursor_y = S1_Y
    n = len(sentences[:3])

    for i, sentence in enumerate(sentences[:3]):
        # Color: first = s1, middle = s2, last = s3 (mereu ultima e aurie)
        if i == n - 1:
            color = palette['s3']
            fnt = font_b
        elif i == 0:
            color = palette['s1']
            fnt = font_eb
        else:
            color = palette['s2']
            fnt = font_eb

        wrapped = wrap_sentence(sentence, fnt, max_w)
        if not wrapped:
            continue

        for line in wrapped:
            bbox = fnt.getbbox(line)
            if bbox[2] - bbox[0] > max_w:
                while line and (fnt.getbbox(line + '…')[2] - fnt.getbbox(line + '…')[0]) > max_w:
                    line = line[:-1]
                line += '…'
            draw.text((80, cursor_y), line, fill=color, font=fnt)
            cursor_y += FONT_SIZE + GAP_BETWEEN_LINES

        # Avans cursor pentru următorul bloc:
        #   last_line_draw = cursor_y - (FONT_SIZE + GAP_BETWEEN_LINES)
        #   last_visible_end = last_line_draw + 62 + 20 = last_line_draw + 82
        #   next_visible_start = last_visible_end + VISUAL_GAP
        #   next_draw = next_visible_start - 20
        #     = cursor_y - (FONT_SIZE + GAP_BETWEEN_LINES) + 82 + VISUAL_GAP - 20
        #     = cursor_y + VISUAL_GAP + 62 - (FONT_SIZE + GAP_BETWEEN_LINES)
        cursor_y += VISUAL_GAP + 62 - (FONT_SIZE + GAP_BETWEEN_LINES)

    img.save(output_path)


def generate_svg(sentences, palette, output_path):
    """Generează SVG vectorial cu poziționare dinamică."""
    # Load logo as base64
    logo_path = os.path.join(REPO_ROOT, LOGO_PATH)
    logo_b64 = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()

    lines_xml = []

    # Gold line
    lines_xml.append(
        f'  <rect x="80" y="{LINE_Y}" width="{LINE_W}" height="{LINE_H}" fill="{palette["gold_line"]}"/>'
    )

    # Logo
    logo_y = H - LOGO_MARGIN_BOTTOM - LOGO_H
    lines_xml.append(
        f'  <image x="80" y="{logo_y}" width="{LOGO_W}" height="{LOGO_H}" '
        f'href="data:image/png;base64,{logo_b64}"/>'
    )

    # Sentences — compute positions same as PNG
    max_w = W - 2 * 80
    font_eb = load_font('ExtraBold')
    font_b = load_font_bold()
    cursor_y = S1_Y
    n = len(sentences[:3])

    for i, sentence in enumerate(sentences[:3]):
        if i == n - 1:
            color = palette['s3']
            fnt = font_b
            fw = '700'
        elif i == 0:
            color = palette['s1']
            fnt = font_eb
            fw = '800'
        else:
            color = palette['s2']
            fnt = font_eb
            fw = '800'

        wrapped = wrap_sentence(sentence, fnt, max_w)
        if not wrapped:
            continue

        for line in wrapped:
            safe_text = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
            lines_xml.append(
                f'  <text x="80" y="{cursor_y}" font-family="Syne" font-size="{FONT_SIZE}" '
                f'font-weight="{fw}" fill="{color}">{safe_text}</text>'
            )
            cursor_y += FONT_SIZE + GAP_BETWEEN_LINES

        cursor_y += VISUAL_GAP + 62 - (FONT_SIZE + GAP_BETWEEN_LINES)

    svg_content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg"\n'
        f'     width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        f'  <rect width="{W}" height="{H}" fill="{palette["bg"]}"/>\n'
        + '\n'.join(lines_xml) + '\n'
        '</svg>\n'
    )

    with open(output_path, 'w') as f:
        f.write(svg_content)


def load_font_bold():
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    font.set_variation_by_name('Bold')
    return font


def main():
    import sys
    specific = None
    if len(sys.argv) > 1:
        specific = int(sys.argv[1])

    os.makedirs(POSTS_DIR, exist_ok=True)

    md_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    print(f"📂 {len(md_files)} postări Goodspell găsite\n")

    posts_txt_path = os.path.join(REPO_ROOT, "goodspell/linkedin-image-builder/posts.txt")
    post_texts = {}
    if os.path.exists(posts_txt_path):
        with open(posts_txt_path) as f:
            content = f.read()
        blocks = content.split('---')
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            lines = [l.strip() for l in block.split('\n') if l.strip()]
            if not lines:
                continue
            m = re.match(r'^(\d+)-(white|black)-(.+)$', lines[0])
            if m:
                num = int(m.group(1))
                post_texts[num] = lines[1:]

    print(f"📖 {len(post_texts)} posturi cu text pre-extras (posts.txt)\n")

    generated = 0
    skipped = 0

    for i, fpath in enumerate(md_files):
        fname = os.path.basename(fpath)
        match = re.match(r'(\d{4}-\d{2}-\d{2})\s+(.+)\.md$', fname)
        if not match:
            skipped += 1
            continue

        date_prefix = match.group(1)
        img_path = os.path.join(POSTS_DIR, f"{date_prefix}.png")

        if os.path.exists(img_path):
            print(f"  ⏭️  {date_prefix} — imaginea există deja")
            skipped += 1
            continue

        with open(fpath) as f:
            content = f.read()

        fm, body = parse_front_matter(content)
        num = int(fm.get('number', 0))
        image_text = fm.get('image_text', '').strip()

        sentences = post_texts.get(num, [])
        if not sentences:
            sentences = split_sentences(image_text)

        if not sentences:
            paragraphs = [p.strip() for p in body.split('\n\n') if p.strip()]
            if paragraphs:
                s = split_sentences(paragraphs[0])
                if s:
                    sentences = s[:3]

        if not sentences:
            print(f"  ❌ {date_prefix} (#{num}) — nu am găsit text pentru imagine")
            skipped += 1
            continue

        if specific and num != specific:
            print(f"  ⏭️  {date_prefix} (#{num}) — sărit (specificat #{specific})")
            skipped += 1
            continue

        palette = PALETTES[i % 2]

        generate_image(sentences, palette, img_path)
        svg_path = os.path.join(POSTS_DIR, f"{date_prefix}.svg")
        generate_svg(sentences, palette, svg_path)

        s_text = " | ".join(s[:35] for s in sentences)
        print(f"  ✅ {date_prefix} (#{num:2d}) {'D' if i%2==0 else 'L'} | {s_text}")
        generated += 1

    print(f"\n---\n✅ {generated} generate | ⏭️  {skipped} sărite")


if __name__ == '__main__':
    main()
