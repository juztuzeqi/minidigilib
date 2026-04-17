#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# Template BoW (diambil dari 04-hardworking-courier.html yang sudah stabil)
BOW_TEMPLATE = '''  function generateDiffBoW(original, user) {
    // Normalisasi super cepat
    const norm = (text) => {
      let result = '';
      for (let i = 0; i < text.length; i++) {
        const c = text[i].toLowerCase();
        if (c >= 'a' && c <= 'z') result += c;
        else if (c === ' ' && result[result.length-1] !== ' ') result += ' ';
      }
      return result.trim();
    };
    
    const oWords = norm(original).split(' ');
    const uWords = norm(user).split(' ');
    const oDisplay = original.split(/\\s+/);
    const uDisplay = user.split(/\\s+/);
    
    const freq = {};
    for (let i = 0; i < oWords.length; i++) {
      const w = oWords[i];
      freq[w] = (freq[w] || 0) + 1;
    }
    
    let html = '';
    let correct = 0;
    
    // Proses user words
    for (let i = 0; i < uDisplay.length; i++) {
      const normWord = uWords[i];
      if (freq[normWord] > 0) {
        freq[normWord]--;
        html += '<span class="diff-correct">' + uDisplay[i] + '</span> ';
        correct++;
      } else {
        html += '<span class="diff-wrong" title="Extra/typo">' + uDisplay[i] + '</span> ';
      }
    }
    
    // Kumpulkan missing words
    const missingWords = [];
    for (let i = 0; i < oDisplay.length; i++) {
      const normWord = oWords[i];
      if (freq[normWord] > 0) {
        missingWords.push(oDisplay[i]);
        freq[normWord]--;
      }
    }
    
    const total = oWords.length;
    const percent = total ? Math.round((correct / total) * 100) : 0;
    
    return { html, percent, correct, total, missingWords };
  }'''

SHOW_COMPARISON_TEMPLATE = '''  function showComparison() {
    const saved = localStorage.getItem(STORY_KEY) || '';
    document.getElementById('userTextDisplay').innerHTML = saved.replace(/\\n/g, '<br>') || '(No writing yet)';
    
    if (!saved) {
      document.getElementById('diffDisplay').innerHTML = '<em>No writing to compare.</em>';
      document.getElementById('checkFeedback').textContent = '';
      document.getElementById('missingBox').style.display = 'none';
      return;
    }
    
    const result = generateDiffBoW(originalStory, saved);
    document.getElementById('diffDisplay').innerHTML = result.html;
    
    // Tampilkan missing words
    if (result.missingWords.length > 0) {
      const missingHtml = result.missingWords.map(w => 
        '<span class="missing-word">• ' + w + '</span>'
      ).join('');
      document.getElementById('missingList').innerHTML = missingHtml;
      document.getElementById('missingBox').style.display = 'block';
    } else {
      document.getElementById('missingBox').style.display = 'none';
    }
    
    const percent = result.percent;
    const diff = result.total - result.correct;
    
    if (percent === 100) {
      document.getElementById('checkFeedback').innerHTML = '🎉 Perfect! 100% match! Excellent work!';
      document.getElementById('checkFeedback').style.color = '#27ae60';
    } else if (percent >= 70) {
      document.getElementById('checkFeedback').innerHTML = '👍 Good effort! ' + percent + '% match. ' + diff + ' word(s) to fix.';
      document.getElementById('checkFeedback').style.color = '#e67e22';
    } else {
      document.getElementById('checkFeedback').innerHTML = '📝 ' + percent + '% match. ' + diff + ' word(s) different. Keep practicing!';
      document.getElementById('checkFeedback').style.color = '#e74c3c';
    }
  }'''

CSS_ADDITIONS = '''    .missing-box { background: #fff3cd; border: 2px solid #f59e0b; border-radius: 10px; padding: 15px; margin-top: 20px; text-align: left; }
    .missing-title { font-weight: bold; color: #856404; margin-bottom: 10px; }
    .missing-list { display: flex; flex-wrap: wrap; gap: 8px; }
    .missing-word { background: white; padding: 4px 10px; border-radius: 20px; border: 1px solid #f59e0b; font-size: 0.9rem; }'''

HTML_MISSING_BOX = '''
    <div id="missingBox" class="missing-box" style="display: none;">
      <div class="missing-title">📋 Missing Words (you didn't write):</div>
      <div id="missingList" class="missing-list"></div>
    </div>
    '''

def upgrade_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip jika sudah ada missingBox
    if 'missingBox' in content:
        print(f"  ⏭️  Already upgraded: {os.path.basename(filepath)}")
        return False
    
    # 1. Tambah CSS missing-box sebelum </style>
    content = content.replace('    .hidden { display: none; }', 
                              '    .hidden { display: none; }\n' + CSS_ADDITIONS)
    
    # 2. Ganti fungsi generateDiff lama dengan BoW
    # Cari dan hapus fungsi generateDiff lama
    pattern = r'  function generateDiff\(original, user\) \{[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\}'
    content = re.sub(pattern, BOW_TEMPLATE, content, flags=re.DOTALL)
    
    # 3. Ganti fungsi showComparison
    pattern2 = r'  function showComparison\(\) \{[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\n[^}]*?\}'
    content = re.sub(pattern2, SHOW_COMPARISON_TEMPLATE, content, flags=re.DOTALL)
    
    # 4. Tambah HTML missingBox sebelum <button id="backToWrite">
    content = content.replace('    <button class="nav-btn" id="backToWrite">← Back to Write</button>',
                              HTML_MISSING_BOX + '\n    <button class="nav-btn" id="backToWrite">← Back to Write</button>')
    
    # 5. Hapus text-decoration: line-through jika ada
    content = content.replace('text-decoration: line-through;', '')
    
    # 6. Ganti panggilan generateDiff di showComparison (kalau masih ada)
    content = content.replace('generateDiff(originalStory, saved)', 'generateDiffBoW(originalStory, saved)')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# Main
stories_dir = "stories"
upgraded = []
skipped = []

for filename in sorted(os.listdir(stories_dir)):
    if filename.endswith('.html') and filename != '04-hardworking-courier.html':
        filepath = os.path.join(stories_dir, filename)
        if upgrade_file(filepath):
            upgraded.append(filename)
            print(f"✅ {filename}")
        else:
            skipped.append(filename)

print(f"\n🎉 Upgraded: {len(upgraded)} files")
if skipped:
    print(f"⏭️  Skipped: {len(skipped)} files (already upgraded)")
