#list
daftar = ["merry",123,2.98,True]
for i in (daftar):
    print(i)
print("="*30)
i = 0
while i < len(daftar):
    print(daftar[i])
    i += 1

#mengupdate nilai list
# 0
daftar [0] = "wulan"
print(daftar)
daftar [2] = "suhu"
print(daftar)

#menghapus nilai pada list
# del, remove, pop

#del
del daftar [1]
print(daftar)
#remove
daftar.remove('wulan')
print(daftar)
#pop
daftar.pop()
print(daftar)

#menambah nilai baru pada list
# append, extend, insert

#append
daftar.append("wulan")
print(daftar)
#extend
daftar.extend(["mayang"])
print(daftar)
#insert
daftar.insert(1,"andi")
print(daftar)