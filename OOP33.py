class Organization: 
    def __init__(self, Name, Country, Address, Telephone): 
        self.name = Name 
        self.country = Country 
        self.address = Address 
        self.telephone = Telephone
        if self.telephone == "" or len(str(self.telephone)) != 10: 
            print("Nhập thông tin lỗi và Dừng chương trình.")
        else: self.xuat()
    def xuat(self): 
        print(self.name,self.country,self.address,self.telephone)
n1 = Organization("n1", "c1", "a1", 1234567890)