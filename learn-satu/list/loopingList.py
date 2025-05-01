# looping list
data = ["Annas", "Maharani", "Alisa"]

for list in data: 
    print(f"data  = {list}")


# for loop list enumerate

angka = [12, 4, 5,6 ,6, 3,1]
panjang = len(angka)
# ada indexnya
for i in range(panjang):
    print(f"angka = {i}")



# while 
i = 0
while i < panjang:
    print(f"angka = {i}")
    i += 1
    

# list comprehension

kumpulan_data = ["ucup", 1,2,3, "otong"]

[print(f"datanya = {i}") for i in kumpulan_data]
angka = [2, 5, 6, 7]
angka_kuadrat = [i**2 for i in angka]
print(f"angka = {angka}")
print(f"angka kuadrat = {angka_kuadrat}")



# enumerate
# ini ngambil data juga index

for index, data in enumerate(kumpulan_data):
    print(f"data ke-{index} = {data}")

# biasakan looping list dengan enumerate