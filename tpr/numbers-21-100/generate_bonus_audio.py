"""
Generate TTS audio untuk BONUS quiz Numbers 21-100
Jalankan setelah generate_audio.py utama
"""

import os
from gtts import gTTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOPIC = "numbers-21-100"

BONUS_WORDS = [
    "twenty-five",
    "thirty-seven",
    "forty-two",
    "fifty-eight",
    "sixty-three",
    "seventy-one",
    "eighty-four",
    "ninety-nine"
]

audio_dir = os.path.join(BASE_DIR, TOPIC, "audio")
os.makedirs(audio_dir, exist_ok=True)

print(f"📁 {TOPIC}/audio/ (bonus)")

for word in BONUS_WORDS:
    filename = word.lower().replace(" ", "-") + ".mp3"
    filepath = os.path.join(audio_dir, filename)

    if os.path.exists(filepath):
        print(f"   ⏭️  {filename} (sudah ada)")
        continue

    tts = gTTS(text=word, lang="en", slow=False)
    tts.save(filepath)
    print(f"   ✅ {filename}")

print("\n🎉 Bonus audio selesai!")
