# ===============================
# PERULANGAN WHILE DI PYTHON
# ===============================

# 1. Struktur dasar while
# while kondisi:
#     blok kode yang diulang selama kondisi True

# Contoh sederhana:
counter = 0
while counter < 5:
    print(counter)  # Output: 0,1,2,3,4
    counter += 1  # Penting untuk mengubah kondisi agar tidak infinite loop

# 2. Infinite loop (perulangan tanpa henti)
# Hati-hati jika kondisi selalu True tanpa perubahan
# while True:
#     print("Ini akan jalan terus!")

# 3. Menggunakan break untuk keluar dari while
counter = 0
while counter < 10:
    if counter == 5:
        break  # Langsung keluar dari loop saat counter == 5
    print(counter)
    counter += 1
# Output: 0,1,2,3,4

# 4. Menggunakan continue untuk melompati ke iterasi berikutnya
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Lewati print saat counter == 3
    print(counter)
# Output: 1,2,4,5

# 5. While dengan kondisi yang sudah False dari awal
# Jika kondisi awal False, blok while tidak akan jalan sama sekali
counter = 10
while counter < 5:
    print(counter)  # Tidak akan tampil apa-apa karena kondisi langsung False

# ===============================
# CATATAN PENTING WHILE LOOP
# ===============================
# - while digunakan untuk mengulang selama kondisi True
# - Harus ada perubahan kondisi supaya tidak infinite loop
# - Tidak menggunakan range() atau enumerate() seperti for
# - Bisa menggunakan break dan continue di dalam while
