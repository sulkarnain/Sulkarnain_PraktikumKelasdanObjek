class MyFile(object):
    def __init__(self, namafile):
        print("Open file %s... \n" % namafile)
        self.file = open(namafile)
    def __del__(self):
        print("\Close file...")
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris, end="")

def main():
    f = MyFile ("E:\pemrograman lanjut\paragraph.txt")
    f.bacadata()
if __name__=="__main__":
    main()
