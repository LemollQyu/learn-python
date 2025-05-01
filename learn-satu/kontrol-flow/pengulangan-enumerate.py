fruits = ['apel', 'pisang', 'jeruk', 'mangga']

for index, fruit in enumerate(fruits):
    print(f"Indeks {index}: {fruit}")

# enumerate(iterable, start=0)
# start itu defaultnya 0
# iterable itu apa yang ingin di iterasi/ obyek yang diiterasi


for index, fruit in enumerate(fruits, start=1):
    print(f"Indeks {index}: {fruit}")

# nah kalo semisal ingin mengubah nilai awalnya itu di mulai dari mana
# bisa dengan start = value
# nanti indeksnya dimulai dari 1

# note penting

# enumerate() menghitung indeks berdasarkan posisi elemen di dalam iterable, tapi indeks yang ditampilkan bisa disesuaikan dengan menggunakan parameter start.

# start=1 hanya berarti indeks pertama yang dicetak adalah 1, tapi tetap mengiterasi seluruh elemen sesuai urutannya di dalam list.

# pokoknya di enumerate() itu yang start hanya mempengaruhi urutan indeks, bukan urutan dari objek yang di iterasi, jadi tetap object yang diiterasi itu mulai dari indeks ke 0, namun start akan set indeksnya dari angka 1