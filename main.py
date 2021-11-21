#Kelas utama
class Laptop:
  SSD_sekarang = 256
  penggunaan_laptop = []
  __activePenggunaanLaptop = None

#fungsi construktor
  def __init__ (self, nama_merk, kapasitas_RAM, CPU_processor):
    self.nama_merk = nama_merk
    self.kapasitas_RAM = kapasitas_RAM
    self.CPU_processor = CPU_processor
    self._scan()

#membuat fungsi dari laptop    
  def nyalakanLaptop(self):
    print('Laptop menyala ', self.nama_merk)

  def matikanLaptop(self):
    print('Laptop dimatikan ', self.nama_merk)

  def menambahSSD(self):
    self.SSD_sekarang = self.SSD_sekarang + 256
    print('SSD_sekarang ', self.SSD_sekarang)

 
  def _scan(self):
    self.__penggunaan_laptop = ['Education', 'Produktivitas', 'Informasi']

  def _setPenggunaanLaptop(self):
    self.__activePenggunaanLaptop = self.__penggunaan_laptop[0]

  def getActivePenggunaanLaptop(self):
    self.__activePenggunaanLaptop = self.__penggunaan_laptop[0]
    return self.__activePenggunaanLaptop

#membuat objek
laptop_kuliah = Laptop('Dell','8 GB','Intel core I7')

#Kelas turunan
class Laptop2(Laptop):
    def __init__(self, nama_merk, kapasitas_RAM, CPU_processor):
        super(Laptop2, self).__init__(nama_merk, kapasitas_RAM, CPU_processor)
        self._scan()
        self._setPenggunaanLaptop()
        
    def menambahSSD(self, menambahSSD):
        self.SSD_sekarang = self.SSD_sekarang + menambahSSD
        print('SSD_sekarang ', self.SSD_sekarang)

#carLaptop = Laptop2('Dell','8 GB','Intel core I7')
#print(laptop_kuliah.nama_merk)
#print(laptop_kuliah.kapasitas_RAM)
#print(laptop_kuliah.CPU_processor)
#print(laptop_kuliah.getActivePenggunaanLaptop())
#print('SSD Sekarang', laptop_kuliah.SSD_sekarang)
#print(laptop_kuliah.SSD_sekarang + 256)


carLaptop = Laptop2('Dell','8 GB','Intel core I7')
print(carLaptop.nama_merk)
print(carLaptop.kapasitas_RAM)
print(carLaptop.CPU_processor)
print(carLaptop.getActivePenggunaanLaptop())
print('SSD Sekarang', laptop_kuliah.SSD_sekarang)
print('SSD setelah ditambah', laptop_kuliah.SSD_sekarang + 256)