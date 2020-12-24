
''' == it's Check the Value only '''

List_1=[1,2,3]
List_2=[1,2,3]

print(id(List_1),id(List_2))

print(List_1 == List_2)
if List_1==List_2:
    print("Equal")
else:
    print("Not Equal")


''' is it's Check the Address only '''
List_3=[1,2,3]
List_4=[1,2,3]
#List_4=List_3
print(id(List_3),id(List_4))

print(List_3 is List_4)
if List_3 is List_4:
    print("Equal")
else:
    print("Not Equal")