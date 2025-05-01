# latihan
print("Latihan List")

data_buku = []
ulang = True

while True:
    judul = input("Masukan Judul buku\t: ")
    penulis = input("Masukan Penulis buku\t: ")

    # masukin dulu di buku_baru guna jadiin list
    buku_baru = [judul, penulis]

    # tarus data list itu di simpan ke list data_buku
    data_buku.append(buku_baru)

    for i, buku in enumerate(data_buku):
        print(f"buku ke- {i} | judul =  {buku[0]} | Penulis = {buku[1]}")
    
    print("=="*10)

    isLanjut = input("Apakah mau lanjut?(y/n) ")
    ## bisa gini 
    # if isLanjut == "n":
    #     ulang = False

    ## atau gini
    if isLanjut == "n":
        break

print("Program Selesai")

    