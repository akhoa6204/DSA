class standard: 
    ds = []
    tong = 0
    def __init__(self, tenkh, cmnd, songaythue):
        self.tenkh = tenkh
        self.cmnd = cmnd
        self.songaythue = songaythue
        if self not in standard.ds:
            standard.ds.append(self)
        
    def tienthue(self):
        if self.songaythue <= 5: 
            standard.tong += self.songaythue * 500
            return self.songaythue * 500
        else: 
            standard.tong += (self.songaythue - 5) * 400 + 5 * 500 
            return (self.songaythue - 5) * 400 + 5 * 500 
    
    def xuat(self):
        print(f"ten: {self.tenkh}, cmnd: {self.cmnd}, songaythue: {self.songaythue}, tienthue: {self.tienthue()}")

class vip(standard):
    def __init__(self, tenkh, cmnd, songaythue, loaiphong): 
        super().__init__(tenkh, cmnd, songaythue)
        self.loaiphong = loaiphong
    def tienthue(self):
        if self.loaiphong == "luxury": 
            if self.songaythue <= 5: 
                standard.tong += self.songaythue * 1100
                return self.songaythue * 1100
            else: 
                standard.tong += (self.songaythue - 5) * 1000 + 5 * 1100 
                return (self.songaythue - 5) * 1000 + 5 * 1100 
        elif self.loaiphong == "president": 
            if self.songaythue <= 5: 
                return self.songaythue * 1300
            else: 
                return (self.songaythue - 5) * 1000 + 5 * 1300 

    def xuat(self):
        print(f"loaiphong: {self.loaiphong}", end=" | ")
        super().xuat()

s1 = standard("khoa", 221121514115, 10)
s2 = standard("thu", 221121514117, 4)
s3 = standard("minh", 221121514112, 2)
v1 = vip("ngoc", 221121514140, 12, "president")
v2 = vip("dung", 221121514107, 6, "luxury")
v3 = vip("hien", 221121514108, 5, "luxury")

for kh in standard.ds: 
    kh.xuat()
print("--------------------------------")
print("Tong tien thue phong:", standard.tong)
print("--------------------------------")
for kh in standard.ds: 
    if not isinstance(kh, vip): # kiểm tra đối tượng kh có phải là vip không, not là không
        kh.xuat()               # nếu là kế thừa từ cha, nếu ktra có phải standard thì vip cũng đúng
print("--------------------------------")
tong = 0
for kh in standard.ds: 
    if isinstance(kh, vip):
        if kh.loaiphong == "luxury":
            tong += kh.tienthue() 
print("Tong tien thue phong Luxury:",tong)
