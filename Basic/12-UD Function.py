'''



'''

#
# def sample():
#   #  print("Hello World")
#     return "Hello Worlds"
#
#
#
# X=sample()
# print(X)


#================================================(  Argument )====================================================================================
# # None Default Arg
# def add(num1,num2):
#     return num1 + num2
# X=add(50,50)
# print(X)


# Default Arg
#
# def add(num1,num2=9):
#     return num1 + num2
#
# #X=add()
# X=add(50,7)
# print(X)
#=========================================================================================================================

            # It's take  No of Arg  -- * used to take all value then store in tuples
#
# def add(*num):
#     #return num
#     return sum(num)
#
# #X=add()
# X=add(23,37)
# print(X)

#==========================================================================================================================

            # It's take  No of Arg -- **  used to take all value then store in Dict

#
# def add(**num):
#     #return num
#     for i in num.items():
#         print(i)
#
# #X=add()
# X=add(name="Nishanth",age="20")
# print(X)

#========================================================================================================================

                # Len

#print(len("abc"))

def length(n):
    cnt=0               #
    if type(n)==int:    #  Ref 1
        n=str(n)        #
    for i in n:
        cnt+=1
    return cnt
print(length(" NISHANTH "))
print(length(246801357))  # Ref 1


