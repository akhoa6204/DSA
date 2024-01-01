class edition: 
    ds = []
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def CompareTo(self): 
        pass 
    def xuat(self):
        print(f"title: {self.title}, author: {self.author}",end= ", ")
class book(edition):
    def __init__(self, title, author, year, publisher):
        super().__init__(title, author)
        self.year = year
        self.publisher = publisher
        edition.ds.append(self)
        self.CompareTo()
    def CompareTo(self):
        edition.ds.sort(key=lambda x: x.author)
    def xuat(self):
        super().xuat()
        print(f"year: {self.year}, published: {self.publisher}")
class article(edition):
    def __init__(self, title, author, journal, year):
        super().__init__(title, author) 
        self.journal = journal
        self.year = year
        edition.ds.append(self)
        self.CompareTo()
    def CompareTo(self):
        edition.ds.sort(key=lambda x: x.author)
    def xuat(self):
        super().xuat()
        print(f"journal: {self.journal}, year: {self.year}")
class onlineresource(edition): 
    def __init__(self, title, author, link, abstract):
        super().__init__(title, author)
        self.link = link
        self.abstract = abstract
        edition.ds.append(self)
        self.CompareTo()
    def CompareTo(self):
        edition.ds.sort(key=lambda x: x.author)
    def xuat(self):
        super().xuat()
        print(f"link: {self.link}, abstract: {self.abstract}")

b1 = book("b1", "khoa", 1999, "kimdong")
b2 = book("b2", "ngoc", 2000, "kimdong")
b3 = book("b3", "khoa", 2019, "kimdong")
a1 = article("a1", "minh", "blue", 1998) 
a2 = article("a3", "thu", "red", 2008) 
a3 = article("a4", "no", "black", 2018)
o1 = onlineresource("o1", "khoa", "example.com", "hay")
o2 = onlineresource("o2", "minh", "example.com", "tam")
o3 = onlineresource("o3", "thu", "example.com", "do")

for s in edition.ds:
    s.xuat()