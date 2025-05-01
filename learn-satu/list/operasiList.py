data_angka = [1,2,4,5,2,4,3,8,7,6,5,3,5]
data = ["annas", "maharani", "alisa", "ara", "nada"]

print(f"data angka = \n{data_angka}")


# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_1 = data_angka.count(1)

print(f"jumlah data angka_4 = {jumlah_data_4}")
print(f"jumlah data angka_1 = {jumlah_data_1}")

# ambil posisi data

print(f"data = {data}")

index_maharani = data.index("maharani")

print(f"posisi maharani = {index_maharani}")

# note jika yang dicari itu data yang tidak ada di list maka akan error

# mengurutkan list angka
data_angka.sort()
print(f"data yang urut sort() = {data_angka}")

# sort() itu langsung dijalankan, tidak mengembalikan nilai kedalam variable
# kalo ingin data yang telah di urutkan tersimpan ke variable maka menggunakan data sorted()
data_angka_new = [1,2,9,4,5,2,4,3,8,7,6,5,3,10]
data_urut = sorted(data_angka_new)
print(f"data yang urut sorted() = {data_urut}")



# membalik urutannya
data_angka.reverse()
print(f"data yang direverse = {data_angka}")

# ini juga sama seperti sort dan sorted harus reversed
data_kebalik = list(reversed(data_angka_new))
print(data_kebalik)