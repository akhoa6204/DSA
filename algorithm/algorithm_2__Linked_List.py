class student: 
    def __init__(self, name, age, Class):
        self.name = name
        self.age = age
        self.Class = Class
        self.next = None
class dssv: 
    def __init__(self):
        self.head = None
        self.tail = None
    def Add(self, sv):
        if self.head is None: 
            self.head = sv
            self.tail = sv
        else:
            self.tail.next = sv 
            self.tail = sv
    
    def PrintHead(self):
        print(self.head.name, self.head.age, self.head.Class)
    
    def PrintTail(self):
        print(self.tail.name, self.tail.age, self.tail.Class)
    
    def Print(self): 
        cur = self.head
        while cur != None: 
            print(cur.name, cur.age, cur.Class)
            cur =cur.next
            
    def find(self, name): 
        cur = self.head
        while cur.name != name and self.head != None:
            cur =cur.next
        print(cur.name, cur.age, cur.Class)
    
    def AgeMax(self): 
        if self.head is None:
            print("Danh sách rỗng.")
            return

        cur = self.head
        max = cur
        while cur is not None: 
            if cur.age > max.age:
                max = cur
            cur = cur.next
        print(max.name, max.age, max.Class)
        
    def AgeMin(self): 
        if self.head is None:
            print("Danh sách rỗng.")
            return

        cur = self.head
        min = cur
        while cur is not None: 
            if cur.age < min.age:
                min = cur
            cur = cur.next
        print(min.name, min.age, min.Class)
    
    def Replace(self, index1, index2):
        cur = self.head
        i = 0
        A = None
        B = None

        while cur is not None and self.head is not None:
            if i == index1:
                A = cur
            elif i == index2:
                B = cur
            cur = cur.next
            i += 1

        if A is None or B is None:
            print("Vị trí không hợp lệ.")
            return

        cur = self.head
        prev_A = None
        prev_B = None

        while cur is not None and self.head is not None:
            if cur == A:
                break
            prev_A = cur
            cur = cur.next

        cur = self.head
        while cur is not None and self.head is not None:
            if cur == B:
                break
            prev_B = cur
            cur = cur.next

        if prev_A is not None:
            prev_A.next = B
            if A != B:
                self.head = B
        else:
            self.head = B

        if prev_B is not None:
            prev_B.next = A
        else:
            self.head = A

        A.next, B.next = B.next, A.next

ds = dssv()
ds.Add(student("Nguyễn Văn A", 10, "5D4"))
ds.Add(student("Nguyễn Văn B", 9, "4C3"))
ds.Add(student("Nguyễn Văn D", 8, "3B2"))
ds.Add(student("Nguyễn Văn D", 7, "2A1"))
print("------------------------")
ds.PrintHead()
print("------------------------")
ds.PrintTail()
print("------------------------")
ds.Print()
print("------------------------")
ds.find("Nguyễn Văn A")
print("------------------------")
ds.AgeMax()
ds.AgeMin()
print("------------------------")
ds.Replace(0,3) 
ds.Print()

