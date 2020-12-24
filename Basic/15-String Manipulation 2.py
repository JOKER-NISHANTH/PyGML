'''

Function in String manipulation
'''

# Name = "Cyber-Nishanth"
# print(Name)
# print(Name.capitalize())
# print(Name.lower())
# print(Name.upper())


# Name = "CYbEr-NIshAntH"
# print(Name)
# print(Name.swapcase())  # Opposite in Name

# Name = "Cyber-nishanth"
# print(Name.title())
#==========================================================================================================================
'''
Count take 3 argument 1st value search " " , start , stop
'''
# Name = "Cyber-nishanth"
# print(Name.count("h"))
# print(Name.count("P"))  # Eillatha letter ah kudutha 0 ah return painnuim
#

# name="internet connection"
# print(name.count("n"))
# print(name.count("n",6))  # 6 is starting value
# print(name.count("n",6,12)) # 6 is starting value and 12 is stopping value
#
#================================================( Replace )==========================================================================
'''
Replace take 3 arg --- 1st old value " ", new value " " , how many time replace the same char in String
'''
#R="internet connection"
# print(R.replace("i" ,"I"))
# print(R.replace("i" ,"I",1))

            # How get lenth of string without white space
# print(R.replace(" ",""))  # " " Space ah irrutha "" empty Space change painnu
#
# print(len(R))   # It's take white space also
# print(len(R.replace(" ",""))) # Remove white space

#================================================( Index )==========================================================================

R="internet connection"
# print(R.index("n"))
# print(R.index("n",5))
# print(R.index("n",12,17))

#print(R.index("e",R.index("e")+1))  # Starting -- R.index("e")+1 -- Coming take for starting value

        # Now we need two e index -- put for loop
# R="internet connection"
# for i in range(len(R)):
#     #print(i)  # It's show index value
#     #print(i,R[i]) # It's show all index and string value
#
#     if R[i]=="n":
#         print(i,R[i])

#================================================( Index )==========================================================================

#R="internet connection"
#print(R.index("T"))  # ValueError: substring not found

# Avoid error throughing nut return -1

# print(R.find("T"))
# print(R.find("t"))

#================================================( Startwith it's return Boolean Values )==========================================================================
'''
Startwith take 2 Arug " " , Starting value for searching  default 0
'''
R="internet connection"

# print(R.startswith("i"))
# print(R.startswith("i",1))


        # Condition IF
#
# if R.startswith("r"):
#     print(R)
# else:
#     print(" Must start with i")

#=======================================( Endwith it's return Boolean Values )===================================

# E="internet connection"
#
#
# if R.endswith("n"):
#     print(R)
# else:
#     print(" Must Ends with n")

#=======================================( strip )===================================

name="  Nishanth  "

#print(name.lstrip())
#print(name.rstrip())
#print(name.strip())

#=======================================( Rjust )===================================
'''
RJECT take 2 Arg -- 1st one ( how many char pair painnanuim ) 2nd ( Yathuvaa pair poainnanuim)

String ah right side vaitchu ketu pair painna vaindyatha left side painnuthu
'''
# R="143"
#
# print(R.rjust(10,"#")) #O/p #######143 --Total 10 la 3 digit string laium remain 7 ah # --  pair painneruku

#=======================================( Ljust )===================================
'''
lJECT take 2 Arg -- 1st one ( how many char pair painnanuim ) 2nd ( Yathuvaa pair poainnanuim)

String ah left side vaitchu ketu pair painna vaindyatha right side painnuthu
'''
I="143"

#print(I.ljust(10,"#")) #O/p #######143 --Total 10 la 3 digit string laium remain 7 ah # --  pair painneruku

#===============================================( encode )========================================================

Encode='Nishanth'
# print(Encode.encode())  # Convert string to binary code
# print(type(Encode.encode()))


#===============================================( Split )========================================================
'''
Split is return default List
'''
Sp="internet connection"
# print(Sp.split(" "))  # Split base on Space
#
# sp="Nishanth,vaseekaran,Vijaysurya"
# A =sp.split(",")
# for i in A:

     # Or
# for i in Sp.split():
#     print(i)

#===============================================( Join )========================================================

J=["Welcome","To","Learn","Python","String","Manipulation"]
# print(J)
#
# print(''.join(J))  # '' is tall String ah-- (.join) join painnu-- (J) la irrukara list la, irrukara String ah
# print('-'.join(J)) # '-' string la irrukara values la - use painne separete painnu
# print(','.join(J))

'''
Join direct ah Int ah join painnathu

Error through

TypeError: sequence item 6: expected str instance, int found

================ ( How to  avoid this ) ===============
'''
J=["Welcome","To","Learn","Python","String","Manipulation",1,2,3,4,5,6]
#print(J)
#print(''.join(J))
#print(''.join([ str(i) for i in J]))

#===============================================( You need only alphabate )========================================================

Aplha="Nishanth@007 Cyber"

char=""
DIG=""
SPE=""

for i in Aplha:
    if i.isalpha():
        char+=i

print(char)

for i in Aplha:
    if i.isdigit():
        DIG+=i

print(DIG)

for i in range(len(Aplha)):  # Position Vanuim na range ..len of Aplha string
    if Aplha[i].isspace():
        print(i)

String="NiShAnTh"

S=""
for i in String:
    if i.isupper():
        S=S+i

print(S)

Lower="NiShAnTh"

L=""

for i in Lower:
    if i.islower():
        L=L+i

print(L)