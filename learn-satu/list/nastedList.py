data_0 = [1,2]
data_1 = [3,4]
data_list = [1,2,3,4]

print(f"data = {data_0}")
print(f"data list biasa= {data_list}")

list_2d = [data_0, data_1, data_list, 6, 20]
print(f"data list 2D = {list_2d}")


# penggunaanya

data_peserta_0 = ["annas", 20, "laki laki"]
data_peserta_1 = ["maharani", 20, "perempuan"]
data_peserta_3 = ["alisa", 21, "perempuan"]
list_peserta = [data_peserta_0, data_peserta_1, data_peserta_3]

print(f"peserta = {list_peserta}")

for i in list_peserta:
    print(f"nama: {i[0]}")
    print(f"umur: {i[1]}")
    print(f"jenis kelamin: {i[2]}\n")


# permasalahan dengan refrence
list_copy = list_peserta.copy()

print(f"peserta copy = {list_copy}")




data_peserta_0[0] = "rahman"
print(f"peserta = {list_peserta}")
print(f"peserta copy = {list_copy}")
