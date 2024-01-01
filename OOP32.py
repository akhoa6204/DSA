class Meo: 
    i = 0 
    L=[]
    def __init__(self,Ten, Giong, Gioitinh, Tuoi):
        self.ten = Ten 
        self.giong = Giong
        self.gioitinh = Gioitinh
        self.tuoi = Tuoi
        Meo.L.append(self.ten + " " + self.giong + " " + self.gioitinh + " " + self.tuoi)
        Meo.i += 1
    def xuat(self): 
        print(self.ten,self.giong,self.gioitinh,self.tuoi)
         
meo1 = Meo("m1", "g1", "gt1", "t1")
meo2 = Meo("m2", "g2", "gt2", "t2")
meo3 = Meo("m3", "g3", "gt3", "t3")
meo4 = Meo("m4", "g4", "gt4", "t4")
for j in range(Meo.i):
    print(Meo.L[j])
print("so luong:", Meo.i)