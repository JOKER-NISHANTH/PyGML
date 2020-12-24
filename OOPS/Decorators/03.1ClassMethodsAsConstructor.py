'''
    --> Classmthod return ====> Object
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

    # Class_Method
    @classmethod
    def change_fees(cls, amount):
        #Student.fees=amount
        cls.fees = amount

    @classmethod
    def data_splitter(cls, data):
        s_name, s_rollno, s_dob, s_city = data.split(',')
        return cls(s_name, s_rollno, s_dob, s_city) # Like Student(s_name, s_rollno, s_dob, s_city)

stu1 = Student(name="Nishanth",dob=2000,city="Chennai",rollno=160)
stu2 = Student(name="Cyber_Nishanth",dob=2010,city="Africa",rollno=167)

# data = 'Sree,134,1956,Asia'.split(",")
# print(data) # Split_fun return String format ['Sree', '134', '1956', 'Asia'] ,we can store in variable via index
print("\n Without function ")
#['Sree', '134', '1956', 'Asia']
name, rollno, dob, city = 'Sree,134,1956,Asia'.split(",")
print(name, rollno, dob, city)

stu3 = Student(name, rollno, dob, city)
print(stu3.__dict__)


print("\n With Class Methods ")

cm_data = 'karthick,167,1996,snakeland'
stu4 = Student.data_splitter(cm_data) # Here stu4 , data_splitter --> classmethod returns one object ,so hold pannatha stu4
print(stu4.__dict__)