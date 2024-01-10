class student:
    def __init__(self, ten, tuoi, lop):
        self.ten = ten 
        self.tuoi = tuoi 
        self.lop = lop 
    def xuat(self): 
        print(f"Name: {self.ten}, {self.tuoi} tuoi va hoc lop {self.lop}")
        
sv1 = student('Nguyễn Văn A', 6, "1A3")
sv1.xuat()
sv1.lop = "1A7"
sv1.xuat()
del sv1
