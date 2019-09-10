class Luaslingkaran(object):
   def __init__(self, phi, r):
      self.phi = phi
      self.jarijari = r
   def hitungLuas(self):
      return self.phi * self.jarijari**2

def main():

   Luaslingkaran1 = Luaslingkaran(3.14, 27)

   print('Objek kotak1')
   print('nilai phi\t: ', Luaslingkaran1.phi)
   print('nilai jarijari\t: ', Luaslingkaran1.jarijari)
   print('nilai Luas\t= ', Luaslingkaran1.hitungLuas())

   Luaslingkaran2 = Luaslingkaran(3.14, 9)

   print("\nObjek kotak2")
   print("nilai phi\t: ", Luaslingkaran2.phi)
   print("nilai jarijari\t: ", Luaslingkaran2.jarijari)
   print("nilai Luas\t= ", Luaslingkaran2.hitungLuas())

if __name__ == "__main__":
   main()
