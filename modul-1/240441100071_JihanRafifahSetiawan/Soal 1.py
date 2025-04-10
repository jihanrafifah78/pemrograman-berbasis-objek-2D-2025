class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur 
        self.alamat = alamat

# Method
    def berjalan(self):
        print(f"- {self.nama} yang berusia {self.umur} tahun sedang berjalan dari rumahnya yang beralamat di {self.alamat} menuju alun-alun dekat rumahnya")

    def berlari(self):
        print(f"- {self.nama} yang berusia {self.umur} tahun sedang berolahraga lari di sekitaran rumahnya yang beralamat di {self.alamat}")

# Membuat Objek
manusia1 = Manusia("Afrilia", 30, "Jl. Merdeka No. 10")
manusia2 = Manusia("Sindi", 25, "Jl. Sudirman No. 25")
manusia3 = Manusia("Vivi", 21, "Jl. Diponegoro No. 18")
manusia4 = Manusia("Manda", 17, "Jl. Ahmad Yani No. 50")
manusia5 = Manusia("Alya", 20, "Jl. Gajah Mada No. 12")
manusia6 = Manusia("Farel", 15, "Jl. Pahlawan No. 7")
manusia7 = Manusia("Lucky", 13, "Jl. Pahlawan No. 7")
manusia8 = Manusia("Dery", 10, "Jl. Raya Bogor No. 5")

#Memanggil Method Berjalan
print(f"Berjalan")
manusia1.berjalan()
manusia2.berjalan()
manusia3.berjalan()
manusia4.berjalan()
manusia5.berjalan()
manusia6.berjalan()
manusia7.berjalan()
manusia8.berjalan()

#Memanggil Method Berlari
print(f"\nBerlari")
manusia1.berlari()
manusia2.berlari()
manusia3.berlari()
manusia4.berlari()
manusia5.berlari()
manusia6.berlari()
manusia7.berlari()
manusia8.berlari()