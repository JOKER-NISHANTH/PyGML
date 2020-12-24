# Hierarchical, Multi-Level , Multiple Inheritance

from datetime import date
class Person:
    def __init__(self, name, dob, city):
        self.name = name
        self.dob = dob
        self.city = city
    def find_age(self):
        return date.today().year - self.dob
class Student(Person):
    # Classvariable
    fees = 10000
    no_of_stu =0
    def __init__(self, name, dob, city, rollno):
        super().__init__(name,dob,city)
        self.rollno = rollno
        Student.no_of_stu = Student.no_of_stu + 1

class Computer(Student):
    def __init__(self, name, dob, city, rollno, year):
        super().__init__(name, dob, city, rollno)
        self.year = year

class Teacher(Person): # Person class is inherite two class Student , Teacher --> Hierarchical Inheritance
    def __init__(self, name, dob, city,students=[]):
        super().__init__(name, dob, city)
        self.students=students

    def show_student(self):
        for student in self.students:
            #print(student) # see down return object
            print(student.name)
            print(student.city)


print("\n\t Multi_Level Inheritance ")
stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Computer(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167,year=2050)
print(stu1.find_age())
print(stu2.year)

print("\n\t  Hierarchical Inheritance ")

t = Teacher("Sandy", 2001, "Sathy")
print(t.__dict__)
print(t.find_age())

print("\n\t  After Overriding the Person class in Teacher class  ")
T = Teacher("Sandy", 2001, "Sathy",[stu1,stu2])
T.show_student()# Return Object ==> <__main__.Student object at 0x000002939F295D90> ,
                # <__main__.Computer object at 0x000002939F295DF0>