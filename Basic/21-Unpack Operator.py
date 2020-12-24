
list_fruits=["Apple","Mango","Grapes"]
tuples_fruits=("Apple","Mango","Grapes")
set_fruits={"Apple","Mango","Grapes"}
dic_fruits={"Apple":4,"Mango":2,"Grapes":5}
range_num = range(1,5)
generator_num=(i for i in range(1,5))

#num = 123 # Not Iterable
print(dir(generator_num))
print(list_fruits)
print(tuples_fruits)
print(dic_fruits)
print(range_num)
print(generator_num)
#         # Unpack -- Iterable object only Unpacking
print(*list_fruits)
print(*tuples_fruits)
print(*dic_fruits)
print(*range_num)
print(*generator_num)


        # Now we try to Unpack Int
num = 123
#print(*num) # TypeError: print() argument after * must be an iterable, not int

            #  Convert to Str

print(*str(num))

def func(a,b,c):
    return a,b,c

#print(func(list_fruits))  # TypeError: func() missing 2 required positional arguments: 'b' and 'c'
print(func(list_fruits[0],list_fruits[1],list_fruits[2]))

             # or

print(func(*list_fruits))

#================================X=================================( ** )===X=========================================X=======================================X
'''
    Must of use in DIC
  We can use * also but some disad (- points ) -- Keys only extract or iterable

'''

list_fruits=["Apple","Mango","Grapes"]
tuples_fruits=("Apple","Mango","Grapes")
set_fruits={"Apple","Mango","Grapes"}
dic_fruits={"Apple":4,"Mango":2,"Grapes":5}
range_num = range(1,5)
generator_num=(i for i in range(1,5))

def func(a,b,c):
    return a,b,c

print(f" Dic unpack {func(*dic_fruits)}")

#print(func(**dic_fruits)) # TypeError: func() got an unexpected keyword argument 'Apple' -- Becoz keys are different

def func(Apple,Mango,Grapes):
    return Apple,Mango,Grapes

print(func(**dic_fruits))  # (4, 2, 5) Keys only extract


            # ** Kwargs   -- Keyword args


def func(**kwargs):
    return kwargs

print(func(**dic_fruits))  # It's take dict format


a = (i for i in "Hello")
print(a, type(a)) # <generator object <genexpr> at 0x0000015E4CF35900> ,  <class 'generator'>
print(*a) # H e l l o