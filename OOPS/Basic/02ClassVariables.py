'''
# Class_name.Variable_name or Attribute --> is called Class variable
# We can access useing both class_name and class_object

no_of_stu =0 ==> Every time class_object create pannapothu ( init ) constructor calling , so  we can add 1 every time
'''
from  datetime import date
name = "Welcome Nishanth"

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
    def address(self):
        addr = f"Name : {self.name} \n DOB : {self.dob} \n RollNo : {self.rollno} \n City : {self.city}"
        return addr
    def age(self):
        current_Year = date.today().year
        return current_Year - self.dob
    def pay_fees(self, amount):
        self.fees = self.fees - amount

stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Student(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167)


stu2.fees = 12000
print(f"--- Total_Students_Fees --> {Student.fees} <------")
print(f"--- Student_1_Fees --> {stu1.fees} <-------")
print(f"--- Student_2_Fees --> {stu2.fees} <------")
stu1.pay_fees(4444)
print(f"---After Student_1 Paying Some fees --> {stu1.fees} <-------")
# Find Instant Variables
print("Instant Variables -->  \n",Student.__dict__)
print("Instant Variables -->  \n",stu1.__dict__)
print("Instant Variables -->  \n",stu2.__dict__)

print(stu2.no_of_stu)
