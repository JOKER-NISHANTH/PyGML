

'''
Store anything in List

    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
'''

#print(dir(list))

#name=["Nishanth","Sister","Bother","Son"]
#print(name)

#print(name[-1])

                #  Multi List

M_List=["Nishanth","Vijay","Surya","Dinesh",["Vasee","karan","Nisha"]]

#print(M_List[1][0])

            # How to Change or add

Chan_List1=["Soccer","Football","Basket Ball","Cricket ball"]
Chan_List2=["Ball","Basket","Cricket bad"]
#print(Chan_List1 + Chan_List2)
#print(Chan_List2*2)

a=[10,50,100,30,55,"nisha"]

#a.append(25)

#a.extend([35,77,88])
#a.extend("Hello")
a.extend(["Welcome"])
#print(a)

                                # Insert

b=[2,4,5,7,9,10,45,66,23]
b.insert(2,10)
#print(b)

                # SORT

S=[3,45,1,0,45,21,22.5,0.10,22.1,10]
# S.sort(r)
S.sort(reverse=False)

#print(S)

            # Reverse

R=[34,56,12,3,4,6,8,3,2,14,1,625,63,7]
R.reverse()
#print(R)


            #Count

C=[12,24,5,6,1,3,34,11,23,4,21,1]

#print(C.count(1))

        # Index

I = ["Vijay","Surya","Welcome","Surya","Vijay"]

#print(I.index("Surya"))

# print(I.index("Vijay"))
#
# print(I.index("Vijay",2))

    # Remove  --Pass the value for remove base on values,it's no return

R=[22,333,12,23,456,12,10]

RE=R.remove(333)
#
# print(RE)
# print(R)

        # Pop Pass the value for remove  base on index ,it's  return  remove value

P=[100,299,55,22]

POP=P.pop(0)

# print(P)
# print(POP)





        # Copy vs Append

n2=[10,20,30,40]

n1=n2
# n1.append(100)
# print(n2,"-",n1)
# print(id(n1),"\t",id(n2))


C=[10,20,30,50]
Copy=C.copy()
C.append(55)
# print(C)
# print(Copy)
# print(id(C),"-",id((Copy)))


                #  Clear


CL=[13,23,12,33,52,62,100]

R=CL.clear()

print(CL)

print(R)