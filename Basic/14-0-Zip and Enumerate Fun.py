'''

ZIP  -- Two methods to display 1st Convert to list , 2nd put in for loop for iterating the values

        It's take least Number of Values in list , Suppose compare L1,L2 list it's check with one is least (Take that List)

Enumerate See in Next File
'''


# Eg:  L1 And L2 la irrukara [1 A] [2 B] [3 C] [4 D] [5 E] etha format la return painnuim
l1=[1,2,3,4,5]
l2=["A","B","C","D","F"]

# for i in range(len(l1)):
#     #print(i)   # Here we use i has index
#     print(l1[i],l2[i])

L1=[10,20,30,40,50]
L2=["A","B","C","D","F"]

#Zipped = zip(L1,L2)
#print(Zipped)  # It's Return object

#print(list(Zipped))

# for i in Zipped:
#     print(i)

            # Real-Time Example

# First_Name=["NISHANTH","VASEE","VIJAY"]
# Last_Name=["AFRICA","KARAN","SURYA"]
# Salary=["50k","30K","45K"]
# Zipped = zip(First_Name,Last_Name,Salary)
#print(Zipped) # It's return one Object

# for i in Zipped:
#     print(i)

#for FN ,LN in Zipped:                   # FN is FirstName ,LN is LastName stored --> Becoz here two values
 #    print(FN,LN)                # (Mai reason remove the tuple becoz now we store two diff values in diff variable)


# for FN,LN,SAL in Zipped:
#     print(f"{FN}{LN} Salary is {SAL}")


#======================================================( We can UnZip Also)=========================================================================

First_Name=["NISHANTH","VASEE","VIJAY"]
Last_Name=["AFRICA","KARAN","SURYA"]
Salary=["50k","30K","45K"]
Zipped = zip(First_Name,Last_Name,Salary)


Unziped=zip(*Zipped)  # * is used to Unzip
print(list(Unziped))  # It's return List Format

