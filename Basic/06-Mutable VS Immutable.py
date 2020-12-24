

'''
Mutable:
    -- List
    -- Dictionary
    -- Set

Immutable:
    -- Tuple
    -- Integer
    -- String
    -- Float

    Mutable means suppose add any type of values it's address doesn't change

    Immutable means suppose add any type of values it's address can change
'''

   #  List Changing based on Index

I = [10,20,30]
I[2]=100

#print(I)


M=(23,45,64,19)
#M[2]=100
#print(M)


print(" Mutable ")

L=[1,2,3]
print(L)
print(" Before Change ",id(L))

print(L)
L.append(100)
print(" After Append ",id(L))


print(" Immutable ")
t=(1,2,34,56,9)
print(" Before Change ",id(t))
t=t+(4,56,)
print(" After Change ",id(t))

