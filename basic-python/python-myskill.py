# basic-python-myskill/python-myskill.py
# strings
one = "Hello"
two = 'World'
three = """This is a galh student in pyhsics"""

# menggabungkan string
gabung = one + " " + two
print(gabung)

# mengulang string
ulang = one * 3
print(ulang)

# mengakses karakter dalam string
akses = one[-1]
print(akses)

# indexing dan slicing
kata = "Galh Student"

# indexing
indexing_0 = kata[0]
indexing_1 = kata[5]
print(indexing_0)
print(indexing_1)

# slicing
slicing_0 = kata[0:4]
slicing_1 = kata[5:12]
print(slicing_0)
print(slicing_1)

# method pada string
teks = "hello world, welcome to python programming"
# upper
print(len(teks))                        # menghitung panjang string
print(teks.upper())                     # mengubah ke huruf besar
print(teks.lower())                     # mengubah ke huruf kecil
print(teks.replace("world", "galh"))    # mengganti kata
print(teks.split(","))                  # memisahkan string berdasarkan karakter tertentu
print(teks.find("welcome"))             # mencari posisi kata
print(teks.count("o"))                  # menghitung jumlah kemunculan karakter tertentu
print("python" in teks)                 # mengecek keberadaan substring

# dictionary
data_dict = {
    "name": "Galh",
    "age": 21,
    "city": "Surabaya"
}
print(data_dict)
print(data_dict["name"])

# menambah data pada dictionary
data_dict["university"] = "UNESA"
print(data_dict)

# mengubah data pada dictionary
data_dict["age"] = 20
print(data_dict)

# menghapus data pada dictionary
del data_dict["city"]
print(data_dict)

# akses dengan .get()
print(data_dict.get("name"))
print(data_dict.get("city", "not found"))  # default value jika key tidak ada

# looping pada dictionary
for key, value in data_dict.items():
    print(key, ":", value)

# nasted dictionary
data_class = {
    "mhs1" : {"name": "Galh", "NIM": "105"},
    "mhs2" : {"name": "Imeld", "NIM": "049"},
}
print(data_class)
print(data_class["mhs1"]["name"])