dictionary = {"wiwi" :"belajar python","sumber" :"jago ngoding"}

#perulangan
for key in (dictionary):
    print(key,dictionary[key])

#mengupdate nilai pada dictionary
dictionary["wiwi"] = "belajar java"
print(dictionary)

#menghapus nilai pada dictionary
dictionary.pop("sumber")
print(dictionary)

#menambahkan nilai pada dictionary
dictionary["like"] = "belajar java"
print(dictionary)
