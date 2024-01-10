class Sach: 
    def __init__(self): 
        self.__tensach =  "" 
        self.__tacgia = "" 
        self.__nam = 0 
        self.__soluong = 0 
    def nhap(self): 
        self._tensach = input("ten sach: ")
        self.__tacgia = input("tac gia: ")
        self.__nam = int(input("nam: "))
        self.__soluong = int(input("soluong: "))
    def xuat(self): 
        print(self.__tensach, self.__tacgia, self.__nam, self.__soluong)

sach1 = Sach() 
sach1.nhap()
sach1.xuat()     