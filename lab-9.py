class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class House:
    def __init__(self,addr,rooms):
        self.address=addr
        self.rooms=rooms
        self.persons=[]
    def add_person_c(self,name,age):
        person=Person(name,age)
        self.persons.append(person)
    def add_person_a(self,person):
        self.persons.append(person)
    def remove_person(self,person):
        self.persons.remove(person)
    def display(self):
        for i in self.persons:
            i.display()

Ali = Person("Ali",28)
House1=House("210 Canal Road","4")
House1.add_person_c("Mustafa",20)
House1.add_person_a(Ali)
House1.display()
