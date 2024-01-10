class Queue: 
    def __init__(self): 
        self.L = []
    
    def enqueue(self, sv): 
        self.L.append(sv)
    
    def dequeue(self):
        if len(self.L) == 0:
            return None; 
        else: 
            return self.L.pop(0).ten, self.L.pop(0).tuoi, self.L.pop(0).lop
        
    def peek(self): 
        return self.L[0].ten, self.L[0].tuoi, self.L[0].lop
    
class student:
    def __init__(self, ten, tuoi, lop):
        self.ten = ten 
        self.tuoi = tuoi 
        self.lop = lop 

ds = Queue()
ds.enqueue(student("Nguyễn Văn A", 10, "5D4"))
ds.enqueue(student("Nguyễn Văn B", 9, "4C3"))
ds.enqueue(student("Nguyễn Văn D", 8, "3B2"))
ds.enqueue(student("Nguyễn Văn D", 7, "2A1"))

print(*ds.dequeue())

print(*ds.peek())