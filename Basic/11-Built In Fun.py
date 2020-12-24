

"""
len, --> ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
  '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
   '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

dir, -->  check Special method , Normal Method

chr   --> ASCII Char

ord   --> ASCII Value

eval,

min,

max,

sum,

reversed,

sorted

input take's default value string




"""
#print(dir())
S = "Nishanth"
L = len(S)
#print(L)

num=123
#print(dir(num))

#--------------------------------------------------------------------------------------------------------------

#print(chr(65))
#
# letters=[]
# for i in range(65,91):
# #    print(chr(i))
#     letters.append(chr(i))
#     print(letters)


#---------------------------------------------------------------------------------------------------------------

# print(ord('N'))


#-------------------------------------------------------------------------------------------------------------

#for  i in range(ord("F"),ord("Q")):

#    print(i)


#-------------------------------------------------------------------------------------------------------------

#num=input("Enter Value : ")
#print(type(num))
#
# try:
#     num1=eval(input("Enter Any Number : "))
# except NameError:
#     num1 = input("Enter Any Number : ")
# finally:
#     print(num1,type(num1))
#


#-------------------------------------------------------------------------------------------------------------

Num1=100
Num2="100"
#
# print(Num1 + int(Num2))
#
# print(str(Num1) + Num2)




#--------------------(  min -- max -- sum )-----------------------------------------------------------------------------------------

F = [10,20,30,40,50,100]
print(min(F),max(F) ,sum(F))



#-------------------------(  Reversed )------------------------------------------------------------------------------------

R = [1,2,3,4,5,67,7]
#print(list(reversed(R)))
#for i in reversed(R):
    #print(i)

X =reversed(R)
# print(next(X))
# print(next(X))
# print(next(X))
# print(next(X))
# print(next(X))

#-------------------------(  Sorted )------------------------------------------------------------------------------------

Sort=[2,3,4,2,1,5,7,1,0]

print(sorted(Sort,reverse=False))
print(sorted(Sort,reverse=True))