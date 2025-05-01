# ===============================
# PERULANGAN FOR DI PYTHON
# ===============================

# 1. Perulangan dengan range() → digunakan untuk mengulang berdasarkan angka
for i in range(5):  # default start=0, stop=5, step=1
    print(i)  # Output: 0,1,2,3,4

# 2. Perulangan dengan range(start, stop, step)
for i in range(1, 10, 2):  # mulai dari 1, sampai sebelum 10, loncat 2
    print(i)  # Output: 1,3,5,7,9

# 3. Perulangan dengan enumerate() → digunakan untuk mendapatkan indeks + item
buah = ['apel', 'pisang', 'jeruk']
for index, item in enumerate(buah, start=1):
    print(f"Indeks {index}: {item}")  # Output: Indeks 1: apel, dst

# 4. Perulangan langsung pada list (tanpa indeks)
for item in buah:
    print(item)  # Output: apel, pisang, jeruk

# 5. Perulangan pada string
teks = "halo"
for huruf in teks:
    print(huruf)  # Output: h, a, l, o

# 6. Perulangan pada tuple
angka = (10, 20, 30)
for a in angka:
    print(a)  # Output: 10, 20, 30

# 7. Perulangan pada set (urutan tidak dijamin)
angka_set = {1, 2, 3}
for a in angka_set:
    print(a)  # Output: bisa 1,2,3 (acak)

# 8. Perulangan pada dictionary dengan .items()
data = {'nama': 'Budi', 'umur': 17}
for key, value in data.items():
    print(f"{key} = {value}")  # Output: nama = Budi, umur = 17
