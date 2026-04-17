#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# Baca template dari 04-hardworking-courier.html (yang sudah stabil)
with open('stories/04-hardworking-courier.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

def extract_original_story(content):
    """Ekstrak originalStory dari file HTML"""
    match = re.search(r'const originalStory = `([^`]+)`;', content)
    if match:
        return match.group(1)
    return None

def extract_story_key(content):
    """Ekstrak STORY_KEY dari file HTML"""
    match = re.search(r"const STORY_KEY = '([^']+)';", content)
    if match:
        return match.group(1)
    return 'story'

def extract_next_prev(content):
    """Ekstrak NEXT_PAGE dan PREV_PAGE"""
    next_match = re.search(r"const NEXT_PAGE = '([^']+)';", content)
    prev_match = re.search(r"const PREV_PAGE = '([^']+)';", content)
    return {
        'next': next_match.group(1) if next_match else '',
        'prev': prev_match.group(1) if prev_match else ''
    }

def extract_title(content):
    """Ekstrak judul dari <title>"""
    match = re.search(r'<title>(.*?) · Grade 4</title>', content)
    if match:
        return match.group(1)
    return 'Story'

# Proses semua file kecuali 04
stories_dir = "stories"
upgraded = []

for filename in sorted(os.listdir(stories_dir)):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(stories_dir, filename)
    
    # Skip file yang sudah pakai missingBox
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'missingBox' in content:
        print(f"⏭️  {filename} (already upgraded)")
        continue
    
    # Ekstrak data dari file lama
    original_story = extract_original_story(content)
    story_key = extract_story_key(content)
    nav = extract_next_prev(content)
    title = extract_title(content)
    
    if not original_story:
        print(f"⚠️  {filename} (could not extract story, skipping)")
        continue
    
    # Buat konten baru dari template
    new_content = template_content
    
    # Ganti data spesifik
    new_content = new_content.replace(
        "const STORY_KEY = 'courier';",
        f"const STORY_KEY = '{story_key}';"
    )
    new_content = new_content.replace(
        "const NEXT_PAGE = '05-alice-jungle.html';",
        f"const NEXT_PAGE = '{nav['next']}';"
    )
    new_content = new_content.replace(
        "const PREV_PAGE = '03-may-disney.html';",
        f"const PREV_PAGE = '{nav['prev']}';"
    )
    new_content = new_content.replace(
        '<title>The Hardworking Courier · Grade 4</title>',
        f'<title>{title} · Grade 4</title>'
    )
    new_content = new_content.replace(
        '<h2>📖 The Hardworking Courier</h2>',
        f'<h2>📖 {title}</h2>'
    )
    new_content = new_content.replace(
        'src="../audio/The Hardworking Courier.mp3"',
        f'src="../audio/{title}.mp3"'
    )
    new_content = new_content.replace(
        f'const originalStory = `{extract_original_story(template_content)}`;',
        f'const originalStory = `{original_story}`;'
    )
    
    # Simpan
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ {filename}")
    upgraded.append(filename)

print(f"\n🎉 Upgraded: {len(upgraded)} files")
