import random

# Fungsi untuk melakukan nucleus sampling
def nucleus_sampling(words, probabilities, p=0.8):
    """
    Melakukan nucleus sampling berdasarkan probabilitas kata dan threshold p.

    Parameters:
    - words: list of words yang mungkin untuk dipilih
    - probabilities: list of probabilitas untuk setiap kata
    - p: threshold kumulatif untuk memilih kata (default 0.8)

    Returns:
    - kata terpilih berdasarkan nucleus sampling
    """

    # Urutkan kata berdasarkan probabilitasnya
    word_prob_pairs = list(zip(words, probabilities))
    word_prob_pairs.sort(key=lambda x: x[1], reverse=True)  # Sort by probability

    # Hitung kumulatif probabilitas
    cumulative_prob = 0
    nucleus_set = []
    for word, prob in word_prob_pairs:
        cumulative_prob += prob
        nucleus_set.append((word, prob))
        if cumulative_prob >= p:
            break

    # Pilih kata secara acak dari nucleus set berdasarkan probabilitasnya
    total_prob = sum(prob for _, prob in nucleus_set)
    random_choice = random.uniform(0, total_prob)

    cumulative_prob = 0
    for word, prob in nucleus_set:
        cumulative_prob += prob
        if cumulative_prob >= random_choice:
            return word

# Contoh penggunaan
words = ["makan", "bermain", "minum", "bekerja", "tidur"]
probabilities = [0.4, 0.3, 0.2, 0.05, 0.03]

# Melakukan nucleus sampling dengan p = 0.8
selected_word = nucleus_sampling(words, probabilities, p=0.8)
print(f"Kata yang dipilih: {selected_word}")
