'''
Important One
    In __str__ or __repr__ function only handle strings only

    Suppose we use int , that time we use format_string like f"This is format String { }"

    Here Format_String return  String

        __repr__ creating for developer and debugging
'''
from datetime import date

class Student:
    def __init__(self, name):
        self.name = name
        self.age=18
    def __str__(self):
        return f"Hello {self.name} , you {self.age} years old ?"

    def __repr__(self):
        return f"Student Class ({self.name}) and Student Class ({self.age})"

std1 = Student("Soccer")
print([std1])  # <__main__.Student object at 0x0000021048DE85B0>

# Create data class

D = date(year=2020, month=11, day=1)
print(type(D))
# Here D convert To List then Print
print([D]) # [datetime.date(2020, 11, 1)]