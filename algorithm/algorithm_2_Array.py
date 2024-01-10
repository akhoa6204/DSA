class student: 
    L = []
    def __init__(self, name, age, Class):
        self.name = name
        self.age = age
        self.Class = Class

    def Add(sv, index):
        student.L.insert(index, sv)

    def Print():
        for i in range(len(student.L)):
            print(student.L[i].name, student.L[i].age, student.L[i].Class)

    def find(name): 
        for i in range(len(student.L)):
            if student.L[i].name == name:
                print(student.L[i].name, student.L[i].age, student.L[i].Class)
    
    def AgeMax():
        if len(student.L) == 0 :
            print("Danh sách rỗng")
            return
        max = student.L[0]
        for i in range(len(student.L)):
            if student.L[i].age > max.age:
                max = student.L[i]
        print(max.name, max.age, max.Class)  
    
    def AgeMin(): 
        if len(student.L) == 0 :
            print("Danh sách rỗng")
            return
        min = student.L[0]
        for i in range(len(student.L)):
            if student.L[i].age < min.age:
                min = student.L[i]
        print(min.name, min.age, min.Class)          
    
    def Replace(index1, index2):
        A = student.L[index1]
        B = student.L[index2]
        for i in range(len(student.L)):
            if i == index1: 
                student.L[i] = B
            elif i == index2:
                student.L[i] = A 

sv1 = student("Nguyễn Văn A", 10, "5D4")
sv2 = student("Nguyễn Văn B", 9, "4C3")
sv3 = student("Nguyễn Văn D", 8, "3B2")
sv4 = student("Nguyễn Văn D", 7, "2A1")
student.Add(sv1, 0)
student.Add(sv2, 1)
student.Add(sv3, 2)
student.Add(sv4, 3)
student.Print()
print("---------------")
student.find("Nguyễn Văn A")
print("---------------")
student.AgeMax()
student.AgeMin()
print("---------------")
student.Replace(0, 3)
student.Print()