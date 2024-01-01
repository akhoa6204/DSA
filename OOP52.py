class people:
    def __init__(self, id, hoten, tuoi, diachi): 
        self.id = id
        self.hoten = hoten
        self.tuoi = tuoi
        self.diachi = diachi
    def xuat(self): 
        print(f"id: {self.id} hoten: {self.hoten} tuoi: {self.tuoi} diachi: {self.diachi}")
class students(people):
    ds = []
    def __init__(self, id, hoten, tuoi, diachi, tp1, tp2, tp3): 
        super().__init__(id, hoten, tuoi, diachi) 
        self.tp1 = tp1
        self.tp2 = tp2
        self.tp3 = tp3
        students.ds.append(self)
    def gpa(self): 
        return self.tp1 * 0.2 + self.tp2 * 0.2 + self.tp3 *0.6
    def xuat(self):
        super().xuat()
        print(f"tp1: {self.tp1}, tp2: {self.tp2}, tp3: {self.tp3}, gpa: {self.gpa()}")
class lecture(people): 
    ds = []
    def __init__(self, id, hoten, tuoi, diachi, kinhnghiem, hocvi, chucvu): 
        super().__init__(id, hoten, tuoi, diachi)
        self.kinhnghiem = kinhnghiem
        self.hocvi = hocvi
        self.chucvu = chucvu
        lecture.ds.append(self)
    def sapxep(): 
        for i in range(len(lecture.ds) - 1): 
            for j in range (i+1, len(lecture.ds)): 
                if lecture.ds[i].kinhnghiem < lecture.ds[j].kinhnghiem: 
                    lecture.ds[i], lecture.ds[j] = lecture.ds[j], lecture.ds[i]
    def xuat(self): 
        super().xuat()
        print(f"kinhnghiem: {self.kinhnghiem}, hocvi: {self.hocvi}, chucvu: {self.chucvu}")
st1 = students(1, "khoa", 18, "61 y lan nguyen phi", 10, 10, 9)
st2 = students(2, "ngoc", 18, "31 y lan nguyen phi", 10, 5, 6)
st3 = students(3, "no", 18, "51 y lan nguyen phi", 10, 7, 8)
for st in students.ds:
    st.xuat()
print("--------------------------------------------------------")
lt1 = lecture(1, "chi", 50, "70 han thuyen", 5, "giao su", "truong khoa")
lt2 = lecture(2, "thu", 40, "70 han thuyen", 4, " pho giao su", "truong bm")
lt3 = lecture(3, "ngoc", 30, "70 han thuyen", 2, "thac si", "truong khoa")
lt4 = lecture(4, "tram", 60, "70 han thuyen", 15, "tien si", "truong bm")
lt5 = lecture(5, "bu", 55, "70 han thuyen", 6, "giao su", "truong bm")
lt6 = lecture(6, "uyen", 45, "70 han thuyen", 7, "thac si", "truong khoa")
lecture.sapxep()
for lt in lecture.ds:
    lt.xuat()


  