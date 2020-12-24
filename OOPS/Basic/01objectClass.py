# Class_Object.Variable_name or Attribute --> is called instance variable

from  datetime import date
name = "Welcome Nishanth"

class Student:
    def __init__(self, name, rollno, dob, city): # Instance Variable
        self.name = name
        self.dob = dob
        self.city = city
        self.rollno = rollno
    def address(self):
        addr = f"Name : {self.name} \n DOB : {self.dob} \n RollNo : {self.rollno} \n City : {self.city}"
        return addr
    def age(self):
        current_Year = date.toDay().year
        return current_Year - self.dob

stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Student(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167)
print(stu1.name)
print(stu1.address())
print(stu2.name)
print(stu2.address())
print(stu1.fees())
print(stu1.fees())
