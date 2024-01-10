class stack: 
    def __init__(self):
        self.L = []
    
    def push(self, sv): 
        self.L.append(sv)
    
    def pop(self): 
        if len(self.L) == 0:
            return None; 
        else: 
            return self.L.pop(len(self.L) - 1).ten, self.L.pop(len(self.L) - 1).tuoi, self.L.pop(len(self.L) - 1).lop
        
    def peek(self):
        if len(self.L) == 0:
            return None; 
        else:
            return self.L[0].ten, self.L[0].tuoi, self.L[0].lop

class student:
    def __init__(self, ten, tuoi, lop):
        self.ten = ten 
        self.tuoi = tuoi 
        self.lop = lop 

ds = stack()
ds.push(student("Nguyễn Văn A", 10, "5D4"))
ds.push(student("Nguyễn Văn B", 9, "4C3"))
ds.push(student("Nguyễn Văn D", 8, "3B2"))
ds.push(student("Nguyễn Văn D", 7, "2A1"))

print(*ds.pop())
    
print(*ds.peek())