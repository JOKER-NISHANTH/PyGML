'''
Instance_Method  ==> Normal method --> eg: address method ,age method

        print(stu1.address())
            Etha function ah call pannuimpothu 1st arg ah Object tha pass yakuim , etha hold pannatha function la **self** arg irruku..

        --->* First arg ah Object pass yatchu na , that is called Instance Method  *<---

Class_Method

        --> Oru fun or method ah call pannuimpothu 1st arg ah class_name pass yatchu na , that is called Class Method

        --> Etha function ah call pannuimpothu 1st arg ah Class_name tha pass yakuim , etha hold pannatha function la **cls** arg irruku..

Static_Method

        In this method , object or class_name pass yakathu , that is called Static_method

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
    # Instance_Method
    def address(self):
        addr = f"Name : {self.name} \n DOB : {self.dob} \n RollNo : {self.rollno} \n City : {self.city}"
        return addr
    # Instance_Method
    def age(self):
        current_Year = date.today().year
        return current_Year - self.dob

    def pay_fees(self, amount):
        self.fees = self.fees - amount

    # Class_Method
    @classmethod
    def change_fees(cls, amount):
        #Student.fees=amount
        cls.fees=amount



stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Student(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167)

print("\n\t Now we change via Class_name ")
Student.change_fees(5555)
print(f"Student one Address : {stu1.address()}")
print(f"Student 1 Fees : {stu1.fees}")
print(f"Student 2 Fees : {stu2.fees}")
print("\n\t Now we change via Class_Object ")
stu1.change_fees(6666)
print(f"Student Two Address : {stu2.address()}")
print(f"Student 1 Fees : {stu1.fees}")
print(f"Student 2 Fees : {stu2.fees}")
