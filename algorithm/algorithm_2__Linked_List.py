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
        while cur is not None:
            if cur.name == name:
                break
            cur =cur.next
        if cur is not None: 
            print(cur.name, cur.age, cur.Class)
        else: print("Không có sv cần tìm kiếm ")
    
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
    
    def swap_nodes(self, index_x, index_y):
        if index_x == index_y:
            return

        prevX, currX, i = None, self.head, 0
        while currX and i != index_x:
            prevX, currX = currX, currX.next
            i += 1

        prevY, currY, i = None, self.head, 0
        while currY and i != index_y:
            prevY, currY = currY, currY.next
            i += 1

        if currX is None or currY is None:
            return

        if prevX is not None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY is not None:
            prevY.next = currX
        else:
            self.head = currX

        currX.next, currY.next = currY.next, currX.next

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
ds.find("Nguyễn Văn C")
print("------------------------")
ds.AgeMax()
ds.AgeMin()
print("------------------------")
ds.swap_nodes(1,2) 
ds.Print()

