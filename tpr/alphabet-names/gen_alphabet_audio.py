from gtts import gTTS
import os

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

os.makedirs("audio", exist_ok=True)

for letter in letters:
    print(f"Generating: {letter}.mp3 ...")
    tts = gTTS(letter, lang='en')
    tts.save(f"audio/{letter}.mp3")

print("\nDone! 26 alphabet audio files ready.")
