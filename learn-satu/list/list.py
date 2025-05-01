data_angka = [1,2,3]

print(data_angka)

data_string = ["dani", "annas", "alisa", "maharani"]
print(data_string)


# list itu kumpulan data kaya array tapi isinya itu campuran dari tipe data, list bisa

data_campuran = ["hallo", 2, True, 4.5, False]
print(data_campuran)


data_range = range(0, 10, 3)
print(data_range)
data_list = list(data_range)
print(data_list)

# buat list dengan for
data_list_for = [list(i**3 for i in range(0, 5))]
print(data_list_for)

# buat list dengan for if
data_list_for_if = [list(i for i in range(0, 10) if i != 3)]
print(data_list_for_if)

# dapat nilai ganjil
data_list_for_if_ganjil = [list(i for i in range(0, 10) if i%2 == 1)]
print(data_list_for_if_ganjil)