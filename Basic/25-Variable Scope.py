'''
Variable Scope

        LEGB ==> Local--Enclose--Global--Builtin

'''
                        #   Local Variables

# def function(x):   # Here x is local variable it's use only in function statement only
#     print(x)
#
# function(50)
#
# #print(x)  # NameError: name 'x' is not defined

            #==============================( Global variables )================================#

# x=1000
# def fun():
#     x=9
#     print(x)
# fun()   # It's take local variable
# print(x) # Global variables x= 1000
                                    #------------------------------------------------
# x=500
# def fun():
#     #x=99
#     print(x)
# fun()   # here fun search any local value of x is their , no then go to Global variable
# print(x)


# x=100
# def funct():
#     x=555
#     print(x)
# funct()
# print(x)
#
# x=356
# def funct():
#     x=555
#     x+=45
#     print(x)
# funct()
# print(x)



# x=356
# def funct():
#     #x=555
#     x+=45   # UnboundLocalError: local variable 'x' referenced before assignment
#     print(x)
# funct()
# print(x)


                # ===========================================(  Global keybord )======================================
# '''Now we can change Global variables'''
# G=143
# def Global():
#     global G
#     G+=67
#     print(G)
#
# print(G)   # Before add 143
# Global()  # 210
# print(G)   # 210


#------------===================x---------------===============----------(  Enclose )---------------============----------------------================x-===========x-
#
# X=100
# def Function():
#     X=200
#     def Inner_Fun():
#         X=300
#         print(X)
#     Inner_Fun()
#
# Function()  # 300 Local variable X irrukainu pakuim irrutha X value ah display painnuim


# X=100
# def Function():
#     X=200
#     def Inner_Fun():
# #        X=300
#         print(X)
#     Inner_Fun()
#
# Function()  # 200 Enclose variable X , local varaiable la X inu irruka inu pakuim irrutha display painnuim,
#                                         # illna Enclose variable la X irrukainu pakuim irrutha X value ah display painnuim



# # 1st --> Local , 2nd  --> Enclose , 3rd ---> Global
# X=100
# def Function():
# #    X=200
#     def Inner_Fun():
#  #       X=300
#         print(X)
#     Inner_Fun()
#
# Function()  # 100 --->Local variable and enclose variable lainuim X
#                     # irruka inu pakuim irutha display pannuim illa na , Global variable la diaplay painnuim


                                #=====================( Non Local)==============================#

# y = 1000
# def Function():
#     y=555
#     def Inner_Func():
#         y=444         # 1
#         #nonlocal y    # 2  Used to change enclose variables
#         #global y       # 3
#         #y+=576
#         print(y)       # 1 --> UnboundLocalError: local variable 'y' referenced before assignment
#                        # 2---> 1131
#                        # 3 --> 1576
#     Inner_Func()
#
# Function()

                                #===========================( __buitins__ )==================================#

print(dir(__builtins__))
''' 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod',
  'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals',
   'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license',
    'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
     'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
      'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'


'''

