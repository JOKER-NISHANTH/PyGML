# Nested If Else ladder in direct print statement

print(f"{Num7=} is Greater then {Num8=} and {Num9=}" if Num7>Num8 and Num7>Num9 else ( f"{Num8=} is Greater then {Num7=} and {Num9=}"if Num8>Num7 and Num8>Num9 else f"{Num9=} is Greater then {Num7=} and {Num8=}"))



#X,Y=input("Enter two number : ").split("-")


#
# if X > Y:
#     print(F"{X} is Greater than {Y}")
# else:
#     print(F"{X} is Lesser  than {Y}")

#print( F"{X=} is Greater than {Y=}" if X > Y else F"{X=} is Lesser  than {Y=}")


#=================================( elif )================================
'''Here Facing some problome Please check very line'''
#Num1,Num2=input("Enter the two values : ").split("-")
# #
# Num1=int(input("Enter the two values : "))
# Num2=int(input("Enter the two values : "))
#
# if Num1 > Num2:
#     print(f"{Num1=} is Greater then {Num2=}")
# elif Num1 < Num2:
#     print(f"{Num1=} is Lesser then {Num2=}")
# else:
#     print(f"{Num1=} and  {Num2=} Both are Same")
#
# Num3=input("Enter the two values : ")
# Num4=input("Enter the two values : ")
#
#
# # Num1=10
# # Num2=9
# # Num1=10
# # Num2=30
#
# if Num3 > Num4:
#     print(f"{Num3=} is Greater then {Num4=}")
# elif Num3 < Num4:
#     print(f"{Num3=} is Lesser then {Num4=}")
# else:
#     print(f"{Num3=} and  {Num4=} Both are Same")
#
# Num5=eval(input("Enter the two values : "))
# Num6=eval(input("Enter the two values : "))
#
# Num5,Num6=eval(input("Enter the two values : ")).split()  # SyntaxError: unexpected EOF while parsing
# Num5,Num6=eval(input("Enter the two values : ")).split("-")  # AttributeError: 'int' object has no attribute 'split'
# if Num5 > Num6:
#     print(f"{Num5=} is Greater then {Num6=}")
# elif Num5 < Num6:
#     print(f"{Num5=} is Lesser then {Num6=}")
# else:
#     print(f"{Num5=} and  {Num6=} Both are Same")



# Num5=eval(input("Enter the two values : "))
# Num6=eval(input("Enter the two values : "))
#
# print( f"{Num5=} is Greater then {Num6=}" if Num5 > Num6 else( f"{Num5=} is Lesser then {Num6=}" if Num5 < Num6 else f"{Num5=} and  {Num6=} Both are Same"))

#============================================( Nested If Else ladder )================================================================================

Num7=eval(input("Enter the First value : "))
Num8=eval(input("Enter the Second value : "))
Num9=eval(input("Enter the Third value : "))
#
# if Num7>Num8 and Num7>Num9:
#     print(f"{Num7=} is Greater then {Num8=} and {Num9=}")
#
# elif  Num8>Num7 and Num8>Num9:
#     print(f"{Num8=} is Greater then {Num7=} and {Num9=}")
# else:
#     print(f"{Num9=} is Greater then {Num7=} and {Num8=}")

print(f"{Num7=} is Greater then {Num8=} and {Num9=}" if Num7>Num8 and Num7>Num9 else ( f"{Num8=} is Greater then {Num7=} and {Num9=}"if Num8>Num7 and Num8>Num9 else f"{Num9=} is Greater then {Num7=} and {Num8=}"))
