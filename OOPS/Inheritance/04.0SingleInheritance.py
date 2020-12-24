# Single
from datetime import date
class Student:
    # Classvariable
    fees = 10000
    no_of_stu =0
    def __init__(self, name, rollno, dob, city):
        self.name = name
        self.dob = dob
        self.city = city
        self.rollno = rollno
        Student.no_of_stu = Student.no_of_stu + 1

    def find_age(self):
        return date.today().year - self.dob

class Computer_SCience(Student):
    fees = 99000  # AO
    # Method one but it's bad practice --> DRY ==> Don't Repeat your self , Use Method 2 using super built-in-function
    # def __init__(self, name, rollno, dob, city,year):
    #     self.name = name
    #     self.dob = dob
    #     self.city = city
    #     self.rollno = rollno
    #     self.year = year

    # Method 2 --> BestOne
    def __init__(self, name, rollno, dob, city,year):
        super().__init__(name, rollno, dob, city)
        self.year=year


stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Computer_SCience(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167,year=2050)

print(dir(stu1))
print(stu2.__dict__)

# Find  which order to searching in class  using __mro__  --> Method Resolution Order
print(Computer_SCience.__mro__)  # (<class '__main__.Computer_SCience'>, <class '__main__.Student'>, <class 'object'>)

print("\n\t Attribute Overriding")
print(stu1.fees)
print(stu2.fees)

print("\n\t Method Overriding")
print(stu2.year)