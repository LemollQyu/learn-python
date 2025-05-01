from copy import deepcopy

data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1]
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

# ambil data

data = data_2d[0][1]
print(f"data = {data}")


## addressnya
# ini address beda
print(f"address data_2d = {hex(id(data_2d))}")
print(f"address data_2d_copy = {hex(id(data_2d_copy))}")


## addres member data ke 1
# addres tiap anggota di data list itu sama, dari yang asli sama copy
print(f"member 1 data ke 1 address data_2d = {hex(id(data_2d[0]))}")
print(f"member 1 data ke 1 address data_2d_copy = {hex(id(data_2d_copy[0]))}")

print(f"member 1 data ke 2 address data_2d = {hex(id(data_2d[1]))}")
print(f"member 1 data ke 2 address data_2d_copy = {hex(id(data_2d_copy[1]))}")


# jadi address tiap member data list asli dengan yang copy itu sama
# meski address list asli sama list copy beda

data_2d_copy[0][1] = 10
# ini merubah semuanya baik asli maupun copy


print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")



# jadi ketika ingin copy list yang didalam isinya list itu pake deepcopy
data_2d_asli = [data_0, data_1, 10]
data_2d_deepcopy = deepcopy(data_2d_asli)

print(f"data_2d_asli = {data_2d_asli}")
print(f"data_2d_deepcopy = {data_2d_deepcopy}")

print(f"address data_2d_asli = {hex(id(data_2d_asli))}")
print(f"address data_2d_deepcopy = {hex(id(data_2d_copy))}")


# ini baru address data dari membernya akan berbeda
print(f"member 1 data ke 1 address data_2d_asli = {hex(id(data_2d_asli[0]))}")
print(f"member 1 data ke 1 address data_2d_deepcopy = {hex(id(data_2d_deepcopy[0]))}")

data_2d_asli[2] = 20

print(f"data_2d_asli = {data_2d_asli}")
print(f"data_2d_deepcopy = {data_2d_deepcopy}")
