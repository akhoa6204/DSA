class Sach: 
    def __init__(self): 
        self.tensach =  "" 
        self.tacgia = "" 
        self.nam = 0 
        self.soluong = 0 
    def nhap(self): 
        self.tensach = input("ten sach: ")
        self.tacgia = input("tac gia: ")
        self.nam = int(input("nam: "))
        self.soluong = int(input("soluong: "))
    def xuat(self): 
        print(self.tensach, self.tacgia, self.nam, self.soluong)

sach1 = Sach() 
sach1.nhap()
sach1.xuat()        