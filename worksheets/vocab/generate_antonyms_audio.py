from gtts import gTTS
import os

# 8 pasangan lawan kata (ambil kata kiri dan kanan)
words = [
    "big", "small",
    "tall", "short",
    "up", "down",
    "hot", "cold",
    "new", "old",
    "in", "out",
    "boy", "girl",
    "few", "many"
]

# Folder output
output_dir = "audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate per kata
for word in words:
    print(f"Generating: {word}.mp3")
    tts = gTTS(text=word, lang='en', slow=False)
    tts.save(f"{output_dir}/{word}.mp3")

print(f"\n✅ Selesai! {len(words)} file audio disimpan di folder '{output_dir}'")
