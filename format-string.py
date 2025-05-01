angka = 42
negatif = -42

print(f"Default: {angka}")         # 42
print(f"Tanda +  : {angka:+d}")    # +42
print(f"Tanda -  : {angka:-d}")    # 42
print(f"Spasi    : {angka: d}")    #  42
print(f"Negatif  : {negatif:+d}")  # -42

pi = 3.14159265

print(f"Default: {pi:f}")       # 3.141593 (default 6 angka di belakang koma)
print(f"2 angka: {pi:.2f}")     # 3.14
print(f"0 angka: {pi:.0f}")     # 3
print(f"+ tanda: {pi:+.2f}")    # +3.14



print(f"Rata kanan   : {angka:>5d}")   #    42
print(f"Rata kiri    : {angka:<5d}")   # 42   
print(f"Rata tengah  : {angka:^5d}")   #  42 
print(f"Plus + kanan : {angka:>+5d}")  #   +42

nilai = 0.875

print(f"Default persen: {nilai:%}")     # 87.500000%
print(f"2 digit persen: {nilai:.2%}")   # 87.50%

angka1 = 225
print(f"Biner    : {angka1:b}")   # 11111111
print(f"Okta     : {angka1:o}")   # 377
print(f"Hex kecil: {angka1:x}")   # ff
print(f"Hex besar: {angka1:X}")   # FF

teks = "Halo"

print(f"Default     : {teks}")         # Halo
print(f"Rata kanan  : {teks:>10}")     # "      Halo"
print(f"Rata kiri   : {teks:<10}")     # "Halo      "
print(f"Rata tengah : {teks:^10}")     # "   Halo   "

nama = "Aldi"


print(f"{nama:<10} | Nilai: {nilai:>7.2f}")  # Aldi       | Nilai:   87.56
