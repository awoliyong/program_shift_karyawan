#  program algoritma tubes # 


karyawan = []   # ini teh list, isinya nampung semua karyawan 
id_auto = 1     # ini id auto, jadi pas nambah data id nya udah ada 
shift_valid = ("Pagi", "Siang", "Malam")  # tuple ga bisa di ubah 

# kebawah semua fungsi

def tambah_data():
    global id_auto

    nama = input("Masukkan nama karyawan: ")
    shift = input("Masukkan shift (Pagi/Siang/Malam): ") # kalo mau ubah dari atas, soalnya tuple 

    if shift not in shift_valid:
        print("Shift invalid\n")
        return

    data = {
        "id": id_auto,
        "nama": nama,
        "shift": shift
    } 

    karyawan.append(data)  
    id_auto += 1

    print("Data ditambahkan\n")

# tampilan data semuanya

def tampilkan_data():
    if not karyawan:
        print("Data karyawan kosong\n")
        return

    print("\nData Karyawan")
    for data in karyawan: 
        print(f"ID: {data['id']} | Nama: {data['nama']} | Shift: {data['shift']}")
    print()

# update

def update_data():
    id_cari = int(input("ID yang mau di update: "))

    for data in karyawan:
        if data["id"] == id_cari:
            shift_baru = input("Shift Baru: ")

            if shift_baru not in shift_valid:
                print("Shift invalid (harus Pagi, Siang, Malam)\n") # tuple tea gk mau di ubah, mesti dari atas di ubah nya
                return

            data["shift"] = shift_baru
            print("Shift updated\n")
            return

    print("ID not found\n")

# hapus data tapi mesti pake id ga bisa nama, bebas sih kalo mau lewat nama juga, tinggal tambah call nya

def hapus_data():
    id_hapus = int(input("ID yang di hapus: "))

    for data in karyawan:
        if data["id"] == id_hapus:
            karyawan.remove(data)
            print("Data dihapus\n")
            return

    print("ID not found\n")

# sorting

def sorting_data():
    if not karyawan:
        print("Data kosong\n")
        return

    karyawan.sort(key=lambda x: x["nama"])
    print("Data di urutkan sesuai abjad\n")

# ini cari data, tapi mesti berdasar id sama nama, kalo mau cari data berdasarkan yang shift juga bisa tingagal di tambahin di if awal

def cari_data():
    keyword = input("Cari berdasarkan ID atau Nama: ")

    hasil = []
    for data in karyawan:
        if (keyword.lower() == str(data["id"]).lower() or
            keyword.lower() in data["nama"].lower()):
            hasil.append(data)

    if not hasil:
        print("Data tidak ada\n")
    else:
        print("\nResult:")
        for h in hasil:
            print(f"ID: {h['id']} | Nama: {h['nama']} | Shift: {h['shift']}")
        print()

# bagian buat menu nya

while True:   
    print("Main Menu")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Sorting Data")
    print("6. Cari Data")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        sorting_data()
    elif pilihan == "6":
        cari_data()
    elif pilihan == "7":
        print("Program selesai.")
        break
    else:
        print("Invalid\n")
