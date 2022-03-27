menu_item = 0
namelist =[]
while menu_item != 9 :
    print("--------")
    print("1. mencetak list")
    print("2. menambahkan nama ke dalam list")
    print("3. menghapus nama dari list")
    print("4. mengubah data dalam list")
    print("5. menampilkan data dalam list")
    print("6. memeriksa data dalam list")
    print("7. mencari index")
    print("9. keluar")
    menu_item = int(input("pilih menu:"))
    if menu_item == 1 :
        barang = 0
        if len (namelist) > 0 :
            while barang < len(namelist[barang]):
                print(barang,".",namelist[barang])
                barang = barang = 1
        else :
            print("list kosong :")
    elif menu_item == 2 :
        name = input("masukkan nama barang :")
        namelist.append(name)
        print(namelist)
    elif menu_item == 3 :
        del_name = input("nama barang yang ingin dihapus :")
        if del_name in namelist :
            item_number = namelist.index(del_name)
            del namelist [item_number]
            print(namelist)
        else :
            print (del_name, "tidak ditemukan")
    elif menu_item == 4 :
        old_name = input("nama barang apa yang ingin di ubah :")
        if old_name in namelist :
            item_number = namelist.index(old_name)
            new_item = input("nama baru :")
            namelist[item_number]= new_item
            print(namelist)
        else :
            print(old_name, "tidak ditemukan")
    elif menu_item == 5 :
        print(namelist)
    elif menu_item == 6 :
        barang_yang_ingin_dicari = input("masukkan barang yang ingin dicari :")
        if barang_yang_ingin_dicari in namelist :
            print("barang ini terdapat dalam namelist")
        elif barang_yang_ingin_dicari not in namelist :
            print("barang ini tidak terdapat dalam namelist")
    elif menu_item == 7 :
        print(namelist)
        barang_yang_ingin_dicari = input("masukkan barang yang ingin dicari :")
        print(barang_yang_ingin_dicari,"berada pada indeks",namelist.index(barang_yang_ingin_dicari))
        
print("good bye")
