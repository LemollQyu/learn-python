# =========================
# Tipe Data di Python
# =========================

# integer
umur = 25
print(umur, "tipenya =", type(umur))  # int: bilangan bulat

# float
tinggi = 175.5
print(tinggi, "tipenya =", type(tinggi))  # float: bilangan desimal

# string
nama = "Budi"
print(nama, "tipenya =", type(nama))  # str: teks/kalimat

# boolean
is_online = True
print(is_online, "tipenya =", type(is_online))  # bool: True/False

# list
angka = [1, 2, 3, 4]
print(angka, "tipenya =", type(angka))  # list: array dinamis, bisa campur isi

# dictionary
user = {
    "nama": "Ani",
    "umur": 22,
    "aktif": True
}
print(user, "tipenya =", type(user))  # dict: mirip object di JS, pasangan key:value

# tuple
koordinat = (10, 20)
print(koordinat, "tipenya =", type(koordinat))  # tuple: mirip list tapi tidak bisa diubah

# set
angka_unik = {1, 2, 3, 3, 4}
print(angka_unik, "tipenya =", type(angka_unik))  # set: kumpulan unik, tidak berurutan, tidak ada duplikat


# =========================
# PENJELASAN TIPE DATA
# =========================

# int     → Bilangan bulat, tanpa koma. Contoh: 1, -5, 100
# float   → Bilangan desimal (mengandung koma). Contoh: 3.14, -0.5
# str     → Teks atau kalimat. Harus diapit dengan tanda kutip ('' atau "")
# bool    → Hanya dua nilai: True atau False. Dipakai untuk logika/kondisi
# list    → Kumpulan nilai, bisa campur tipe. Bisa diubah (mutable), bisa diakses lewat index
# dict    → Kumpulan pasangan key:value, mirip object di JavaScript
# tuple   → Mirip list, tapi immutable (tidak bisa diubah isinya)
# set     → Kumpulan data unik, tidak ada index, tidak menerima duplikat
