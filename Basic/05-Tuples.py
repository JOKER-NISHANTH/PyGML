

'''

Tuples -- Immutable
  Special Methods
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
   '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

   Method
   [ 'count', 'index']


'''



A=("Nisha","Vasee",1,10.9)
B=("Surya","Vijay","Vasee",161,45.7)

#print(dir(A))
#print(A)
#print(type(A))

#print(A[-1])

Con=A+B
#print(Con)

P=Con.count("Vasee")

#print(P)

I=("127.23.45.0","200.78.00.02")


L=list(I)
L.append("404.12.32.0")

print(tuple(L))
