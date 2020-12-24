
# def Fun():
#     return "Nisahanth"
# print(Fun())

#======================================= Intro lambda ================================================================

#print(lambda : "Hello Python") # It's return object
#print((lambda :"Hello Python")())  # () Hold the String

# X=lambda :"Hello Python"
# print(X())
#
#===================================== Normal lambda  ====================================================================

# def Function(firstname,lastname):
#     return f"Hello! {firstname}{lastname}"
#
# print(Function("Cyber ","Nishanth"))
#
# x=lambda firstname,lastname : f"Hello! {firstname}{lastname}"
# print(x("Innocent ","Nishanth"))

#========================================= If else ===========================================================

# def Function(name):
#     if name[0] =="N" or name[0] =="n":
#         return f"Hi {name}"
#     else:
#         return "Name must Startwith 'N'"
#
# #print(Function("Vasee"))
# print(Function("Nishanth"))

# A=lambda name: f"Hi {name}" if name[0] =="N" or name[0] =="n" else "Name must startwith 'N'"
#
# print(A("Nishanth"))
# print(A("Vasee"))

 #================================  N no of args get in single line  ==========================================================

# def Addvalues(*args):
#     return sum(args)

#print(Addvalues(1,2,34,5,67,10))

# L=lambda *args:sum(args)
# print(L(10,30,60))

#============================================= Keyword arguments ==========================================================

# def KeyWord(**kwargs):
#     Result=""
#     for name in kwargs.values():
#         Result+=name
#     return Result
# print(KeyWord(Name1="Cyber ",Name2=" Nishanth" ))

# K= lambda **kwargs: [ i for i in kwargs.values()]
# print(K(Name3="Immortal ",name4="Nishanth"))

# K= lambda **kwargs: [ i for i in kwargs.items()]
# print(K(Name5="Innocent ",Name6="Nisha"))

# X=lambda **kwargs:"".join([ i for i in kwargs.values()])  # "" --> Empty string == .join --> For loop join painnekalim
# print(X(name7="Vasee ", name8="Karan"))

#======================================= Lambda Prime ==========================================================

# def Prime(x):
#     for i in range(2,x):
#        if x%i==0:
#            return f"{x}  is not Prime Number"
#        else:
#            return f"{x} is Prime Number"
# #print(Prime(11))
# for i in range(2,15):
#     print(Prime(i) ,end="\t")
#

#PRE=lambda x:[ i for i in range(2,x)   if x%i==0 ]
#Here anyvalues appending in i means not a  prime number , becoz input values remainder is =0
#  So , How to find anyvalues apppending ? --> Use len == 0 means , anyvalues Appending that time len function ==0 so a prime , != Not a prime number

PRE=lambda x:len([ i for i in range(2,x)   if x%i==0 ])==0
#for i in range(3,15):

print(PRE(3))
print(PRE(29))
print(PRE(15))