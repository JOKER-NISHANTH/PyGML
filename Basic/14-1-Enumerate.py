"""

Enumerate -- Create Auto Index Default index Value 0 , We can Change also
"""
#             # Complex Step
# Names=["Nishanth","Vaseekaran","VijaySurya","Nishanth","VijaySurya","Nishanth"]
# enu=enumerate(Names)
#
# print(Names.index("Nishanth")) # It's Return (0) , suppose we have one more Nishanth Check below
# print(Names.index("Nishanth",1))


#================================================( Use Enumerate to convert easy)===============================================================================

Names=["Nishanth","Vaseekaran","VijaySurya","Nishanth","VijaySurya","Nishanth"]

enum = enumerate(Names)
#print(enum)  # Its also Return OBject
#print(list(enum))

#for i in enum:
#    print(i)

                # Now Split Index(index) and Value(value)  -- Avoid tuples
# for index,values in enum:
#     print(index,values)


for index,values in enum:
    if values == "Nishanth":
        print(index,values)