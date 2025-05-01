a = ["maharani", "annas", "alisa"]

b = a

print(f"data a = {a}")
print(f"data b = {b}")


a[1] = "nabila"
b.sort()

# ini itu ada satu list yang di copy maka data yang dirubah akan ngikut semuanya

print(f"data a = {a}")
print(f"data b = {b}")

# ini dikarenakan addressnya soalnya sama
print(f"address = {hex(id(a))}")
print(f"address = {hex(id(b))}")


## supaya data nggak sama / duplika list yang benar

c = a.copy()
print(f"data c = {c}")

print(f"address c = {hex(id(c))}")

c[1]= "nada"
print(f"data a = {a}")
print(f"data b = {b}")
print(f"data c = {c}")





