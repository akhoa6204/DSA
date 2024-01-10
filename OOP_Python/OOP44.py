class info: 
    def __init__(self, id, hoten, group,tp1, tp2, tp3): 
        self.id = id 
        self.hoten = hoten
        self.group = group
        dtp = DiemTP(tp1, tp2, tp3)
class DiemTP() : 
    def __init__(self, tp1, tp2, tp3):
        self.tp1 = tp1
        self.tp2 = tp2
        self.tp3 = tp3
        print("Diemtb =",tp1 * 0.1 + tp2 * 0.3 + tp3 * 0.6)

sv1 = info("1", "khoa", "1", 10, 1, 2) 
sv2 = info("2", "ngoc", "2", 10, 10, 5) 