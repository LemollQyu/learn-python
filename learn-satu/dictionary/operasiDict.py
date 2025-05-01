print("Operasi Dictionary")

data_dict = {
    "ans":"Annas Rahman",
    "mhr":"Maharani Putri",
    "als":"Alisa Nada",
}

print(data_dict)

# kalo variable const harus kapital
LENDICT = len(data_dict)
print(f"panjang = {LENDICT}")

# mendeteksi key apakah ada di dictionary
KEY = "mhr"
CHECKED_MHR = KEY in data_dict
print(f"apakah ada {KEY} di data dictionary = {CHECKED_MHR}")

# mendeteksi key apakah ada di dictionary
KEY = "rhm"
CHECKED_RHM = KEY in data_dict
print(f"apakah ada {KEY} di data dictionary = {CHECKED_RHM}")


## akses data dictionary (read value) dengan get

print(data_dict["als"]) # ini jug bisa
print(data_dict.get("als")) # kebanyakan digunakan

# bedanya ambil data dict get dengan yang langsung ambil name keynya tuh
# print(data_dict["qwr"]) # ini hasilnya error
print(data_dict.get("qwr")) # ini hasilnya None

# dan dengan get itu bisa gini
print(data_dict.get("qwr", "key tidak ada")) # ini hasilnya key tidak ada
# atau cek key dengan message

# pengambilan data dictionary di sarankan dengan get


## update data dictionary
data_dict["mhr"] = "Nabila putri"
print(data_dict)

# menambah data dictionary
data_dict["fhm"] = "Fahima nabila"
print(data_dict)

# dengan update
data_dict.update({"als": "Alisa qotru"})
print(data_dict)
data_dict.update({"qwr": "Qwert iop"})
print(data_dict)

# ket
# jadi dengan update itu semisal keynya itu ada di data dictionary maka datanya itu akan diubah/update. Tapi jika keynya itu tidak ada maka data itu akan ditambahkan ke data dictionary

# update / tambah data dictionary disarankan dengan update


## delete / meghapus data dictionary
del data_dict["qwr"]
print(data_dict)



