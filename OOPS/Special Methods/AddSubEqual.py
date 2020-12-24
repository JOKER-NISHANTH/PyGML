

# __add__

x = 1
y = 2
print(x + y)
# or
print("\t Background Process in adding two int ")
print(f"It's From INT class --> __add__ method {int.__add__(x,y)}")

a = '1'
b = '1'
print(a + b)
# or
print("\t Background Process in adding two str ")
print(f"It's From STR class --> __add__ method {str.__add__(a,b)}")



class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    # For print function
    def __str__(self):
        return f'{self.name}'

    # For adding int ( + )
    def __add__(obj_1,obj_2):
        return obj_1.fees + obj_2.fees

    # For adding int ( + )
    def __sub__(obj_1,obj_2):
        return obj_1.fees - obj_2.fees

    # For checking the name is equal or not  ( == )
    def __eq__(obj_1,obj_2):
        return obj_1.name == obj_2.name

    def __len__(self):
        return len(self.name)

    # __getitem__ is used to String Slicing [ start:stop:step ]
                #   name , [0]
    def __getitem__(self, key):
            return self.name[key]

    # For in Operator
    def __contains__(self, value):
        if value in self.name:
            return True
        return False


stu1 = Student("John", 2500)
stu2 = Student("John", 5050)
print(stu1 + stu2)
print(stu1 == stu2)
stu2 = Student("Ram", 5750)
print(stu1 == stu2)
print(stu1 - stu2)

#print(len(stu1)) # TypeError: object of type 'Student' has no len()
# Because stu1 is we create object so it's not have len function

print("\n\t After Creating __len__ function ")
print(f" Length of student name {len(stu1)}")
print(f" Length of student name {len(stu2)}")

print(f"\n\t Using __str__ function : {stu1}")
print(stu1, type(stu1))
name = "Nishanth"
print(name,type(name))
print("\n\t Using Index")
print(name[0])
#print(stu1[0]) # TypeError: 'Student' object is not subscriptable
print("\n\t After Creating __getitem__ function ")
print(stu1[0:3])

print("\n\t After Create __contains__ method ")
print('J' in stu1)


print(dir(name))