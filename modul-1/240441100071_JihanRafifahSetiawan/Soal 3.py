class Kucing:
    def __init__(self, nama, jenis, warna, umur):
        self.nama = nama 
        self.jenis = jenis
        self.warna = warna
        self.umur = umur

# Method Kucing
    def menampilkan_data_kucing(self):
            print(f"\nData Kucing")
            print(f"Nama    : {self.nama}")
            print(f"Jenis   : {self.jenis}")
            print(f"Warna   : {self.warna}")
            print(f"Umur    : {self.umur}")
    
# Membuat Objek dalam List
data_kucing = [("Mochi", "Ragdoll", "Putih Abu-abu", "2 tahun"),
               ("Mocha", "Maine Coon", "Hitam", "1 tahun"),
               ("Minnie", "Domestic Shorthair", "Orange", "3 tahun")]
list_kucing = [Kucing(nama, jenis, warna, umur) for nama, jenis, warna, umur  in data_kucing]
for kucing in list_kucing:
    kucing.menampilkan_data_kucing()

class Monyet:
    def __init__(self, nama, jenis, warna, umur):
        self.nama = nama
        self.jenis = jenis 
        self.warna = warna
        self.umur = umur

# Method Monyet
    def menampilkan_data_monyet(self):
            print(f"\nData Monyet")
            print(f"Nama    : {self.nama}")
            print(f"Jenis   : {self.jenis}")
            print(f"Warna   : {self.warna}")
            print(f"Umur    : {self.umur}")

# Membuat objek monyet dalam list
data_monyet = [("Chico", "Capuchin", "Coklat", "4 tahun"),
               ("Lala", "Macaque", "Abu-abu", "5 tahun"),
               ("Bobby", "Baboon", "Coklat Muda", "3 tahun")]
list_monyet = [Monyet(nama, jenis, warna, umur) for nama, jenis, warna, umur  in data_monyet]
for monyet in list_monyet:
    monyet.menampilkan_data_monyet()

class Kelinci:
    def __init__(self, nama, jenis, warna, umur):
        self.nama = nama 
        self.jenis = jenis
        self.warna = warna
        self.umur = umur

# Method Kelinci
    def menampilkan_data_kelinci(self):
            print(f"\nData Kelinci")
            print(f"Nama    : {self.nama}")
            print(f"Jenis   : {self.jenis}")
            print(f"Warna   : {self.warna}")
            print(f"Umur    : {self.umur}")

# Membuat objek kelinci dalam list
data_kelinci = [("Snowy", "Anggora", "Putih", "2 tahun"),
                ("Oreo", "Dutch", "Hitam Putih", "1.5 tahun"),
                ("Coco", "Holland Lop", "Coklat", "3 tahun")]
list_kelinci = [Kelinci(nama, jenis, warna, umur) for nama, jenis, warna, umur  in data_kelinci]
for kelinci in list_kelinci:
    kelinci.menampilkan_data_kelinci()
    