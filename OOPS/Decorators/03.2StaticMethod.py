'''
        In your method we don't use instance and class variable or attribute , that time we use static method
'''

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

    @staticmethod
    def department(dept):
        available_dept = ["CS", "Maths"]
        if dept in available_dept:
            return True
        return False

stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Student(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167)

print(stu1.department("CSS"))
print(stu1.department("CS"))