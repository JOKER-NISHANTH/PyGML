# Check for Looping runing Successful
# Name="Nishanth"
# for i in Name:
#      print(i)
#
# else:
#     print(" For Else Part ")

# Name="Nishanth"
# for i in Name:
#     if i=="n":
#         break
#     print(i)
#
# else:
#     print(" For Else Part ")

#=======================================================( While Loop )===================================================================
#
# a="Welcome to Learn"
# print(len(a))
# cnt=0
# while cnt < len(a):

#     print(a[cnt])
#     cnt=cnt+1
# else:
#     print("While Else Part")
#


# a="Welcome to Learn"
# print(len(a))
# cnt=0
# while cnt < len(a):
#     if a[cnt] == " ":
#         break
#     print(a[cnt])
#     cnt=cnt+1
# else:
#     print("While Else Part")

#=============================================================( Prime member )================================================================
'''
Here We Gen a value start with 2 becoz, one is prime number --> Now here gen a value like num -7(2,num) 2,3,4,5,6
  here 7/2 , 7/3 ,7/4,7/5,7/6 remainder is 0 => is not a prime number else  prime number
  Now 7 is not a prime

# '''
# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             result=f'{num} is Not Prime'
#             break
#     else:
#         result =f"{num} is prime number"
#     return result
#
# X= prime(7)
# Y=prime(15)
# print(X)
# print(Y)
#


# for i in range(2,50):
#     print(prime(i))