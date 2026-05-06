from gtts import gTTS
import os

words = [
    "sit-down",
    "stand-up",
    "walk",
    "run",
    "read",
    "write",
    "jump",
    "clap",
    "point",
    "touch"
]

labels = [
    "sit down",
    "stand up",
    "walk",
    "run",
    "read",
    "write",
    "jump",
    "clap",
    "point",
    "touch"
]

os.makedirs("audio", exist_ok=True)

for i, word in enumerate(words):
    label = labels[i]
    print(f"Generating: {word}.mp3 ...")

    tts = gTTS(label, lang='en')
    # Langsung simpan ke file final, timpa yang lama
    tts.save(f"audio/{word}.mp3")

print("\nDone! Semua file ada di folder 'audio/'")
