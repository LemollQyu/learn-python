# range(start, stop, step):

# start: Titik awal perulangan. Default: 0.

# stop: Titik berhenti perulangan (tidak termasuk). Wajib diisi.

# step: Langkah perulangan. Default: 1.

# Perulangan dengan step = 1:
# range(5) → 0, 1, 2, 3, 4

# Perulangan maju (positif step):
# range(2, 6) → 2, 3, 4, 5

# Perulangan mundur (negatif step):
# range(10, 0, -1) → 10, 9, 8, ..., 1
# start harus lebih besar dari stop untuk mundur.

# Kesalahan perulangan mundur:
# range(0, 10, -1) → Tidak ada output (karena start < stop).

# Contoh perulangan mundur:
# range(-10, -2, -1) → -10, -11, -12, ..., -19

for i in range(11,20,2): 
    print(i)