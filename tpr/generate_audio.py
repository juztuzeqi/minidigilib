"""
Generate TTS audio untuk semua topik TPR Pre-Grade 1
Pakai gTTS (Google Text-to-Speech)
"""

import os
from gtts import gTTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOPICS = {
    # ✅ Sudah beres
    "actions": [
        "sit down", "stand up", "walk", "run",
        "read", "write", "jump", "clap", "point", "touch"
    ],
    "alphabet-names": [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
    ],
    "numbers-11-20": [
        "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen", "twenty"
    ],

    # 🔜 Baru
    "numbers-21-100": [
        "twenty-one", "twenty-two", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred"
    ],
    "body-parts": [
        "head", "shoulder", "knee", "toe",
        "hand", "hands", "arm", "arms",
        "foot", "feet", "leg", "legs"
    ],
    "face-parts": [
        "eyes", "ears", "mouth", "nose",
        "hair", "cheeks", "chin",
        "teeth", "tooth"
    ],
    "classroom": [
        "table", "chair", "board", "book",
        "pencil", "pen", "bag", "eraser", "ruler"
    ],
    "colors": [
        "red", "blue", "green", "yellow",
        "orange", "purple", "black", "white"
    ]
}

for topic, words in TOPICS.items():
    audio_dir = os.path.join(BASE_DIR, topic, "audio")
    os.makedirs(audio_dir, exist_ok=True)

    print(f"📁 {topic}/audio/")

    for word in words:
        filename = word.lower().replace(" ", "-") + ".mp3"
        filepath = os.path.join(audio_dir, filename)

        if os.path.exists(filepath):
            print(f"   ⏭️  {filename} (sudah ada)")
            continue

        tts = gTTS(text=word, lang="en", slow=False)
        tts.save(filepath)
        print(f"   ✅ {filename}")

print("\n🎉 Selesai!")
