class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

# Method
    def info_mahasiswa(self):
        print("\nTampilkan Data Mahasiswa")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Alamat  : {self.alamat}")

# Membuat List
mahasiswa_list = []

# Masukkan Objek
for i in range(3):
    print(f"\nMasukkan Data Mahasiswa Ke-{i+1}:")

    while True:
        nama = input("Nama: ")
        if nama == "":
            print("Data harus diisi!")
        else:
            break

    while True:
        nim = input("NIM: ")
        if nim == "":
            print("Data harus diisi!")
        else:
            break

    while True:
        jurusan = input("Jurusan: ")
        if jurusan == "":
            print("Data harus diisi!")
        else:
            break

    while True:
        alamat = input("Alamat: ")
        if alamat == "":
            print("Data harus diisi!")
        else:
            break

    # Membuat Objek Mahasiswa
    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)

# Tampilkan semua data mahasiswa
for mahasiswa in mahasiswa_list:
    mahasiswa.info_mahasiswa()
