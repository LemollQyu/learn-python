import random

# Daftar kata acak (bisa diganti sesuai selera)
word_list = [
    "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
    "adventure", "mystery", "space", "time", "galaxy", "warrior", "kingdom",
    "portal", "dimension", "battle", "shadow", "light", "ancient", "power",
    "magic", "forest", "dragon", "sword", "hero", "villain", "quest", "fate"
]

# Jumlah kata yang mau dibuat
num_words = 12300

# Bikin teks sepanjang 12.000 kata
generated_words = [random.choice(word_list) for _ in range(num_words)]
long_text = ' '.join(generated_words)

# Tampilkan sebagian hasil
print(long_text[:1000])  # Preview 1000 karakter pertama
print(f"\nTotal karakter: {len(long_text)}")
print(f"Total kata: {len(long_text.split())}")
