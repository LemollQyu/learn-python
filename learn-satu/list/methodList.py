# operasi list
# dipyhthon index list bisa 
# 0 = -3, 1 = -2, 2 = -1
data = ["annas", "maharani", "alisa"]
print(data[0])

print(f"data index 1 = {data[1]}")

# mengambil jumlah data
panjang_data = len(data)
print(f"panjang_data ={panjang_data}")

print(data)
# tambah data di list
data.insert(1,"Mizzy")
print(data)

# tambah data di akhir
data.append("Nabila")
print(data)

# menambah data baru list

data_baru = ["Aulia", "Putri", "Qotru"]
data.extend(data_baru)

print(f"data gabungan = {data}")

# merubah data
data[1] = "Rahman"
print(data)

# menghapus data
# akan error jika huruf ada yang besar atau kecil
data.remove("Putri")
print(data)

# menghapus data di belakan 
# dan juga mengambil data yang paling belakang
print(f"datanya = {data}")
data_akhir = data.pop()
print(f"data setelah di pop = {data}")
print(f"data yang diambil = {data_akhir}")
