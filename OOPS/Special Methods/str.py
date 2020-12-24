'''
Important One
    In __str__ or __repr__ function only handle strings only

            ==> Object ah direct ah print la pass pannapothutha __str__ function calling
                        eg: print(D)
            ==> Suppose Object ah list ah print pannuimpothu or anywhere like(cmd) la run pannuimpothu  __repr__ function calling or running
                        eg: print([D]) ,In cmd >>D

    Suppose we use int , that time we use format_string like f"This is format String { }"

    Here Format_String return  String

    __str__ creating for endusers
'''
from datetime import date

class Student:
    def __init__(self, name):
        self.name = name
        self.age=18
    def __str__(self):
        return f"Hello {self.name} , you {self.age} years old ?"

    
std1 = Student("Soccer")
print(std1)  # <__main__.Student object at 0x0000021048DE85B0>

# Create data class

D = date(year=2020, month=11, day=1)
print(type(D)) # <class 'datetime.date'> datetime is module, then here date is also class , so we create object like D
#print(dir(D)) #  '__str__'
print(D) # background print function calling '__str__' function