class Doanhnghiep: 
    def __init__(self,tendn,mst,diachi): 
        self.tendn = tendn
        self.mst = mst
        self.diachi = diachi
class DanhsachDN(): 
    ds = []
    def __init__(self,tendn,mst,diachi):
        dn = Doanhnghiep(tendn, mst, diachi)
        DanhsachDN.ds.append(dn)
        
d1 = DanhsachDN("khoa", 1, "12 y lan nguyen phi")
d2 = DanhsachDN("ngoc", 2, "31 lo giang 15")
for dn in DanhsachDN.ds:
    print(dn.tendn,dn.mst,dn.diachi)