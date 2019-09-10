class Kelilinglingkaran(object):
   def __init__(self, phi, r):
      self.phi = phi
      self.jarijari = r
   def hitungKeliling(self):
      return 2 * self.phi * self.jarijari

def main():
   Kelilinglingkaran1 = Kelilinglingkaran(3.14, 27)

   print('Objek kotak1')
   print('nilai phi\t: ', Kelilinglingkaran1.phi)
   print('nilai jarijari\t: ', Kelilinglingkaran1.jarijari)
   print('nilai Keliling\t= ', Kelilinglingkaran1.hitungKeliling())

   Kelilinglingkaran2 = Kelilinglingkaran(3.14, 9)

   print("\nObjek kotak2")
   print("nilai phi\t: ", Kelilinglingkaran2.phi)
   print("nilai jarijari\t: ", Kelilinglingkaran2.jarijari)
   print("nilai Keliling\t= ", Kelilinglingkaran2.hitungKeliling())

if __name__ == "__main__":
   main()
