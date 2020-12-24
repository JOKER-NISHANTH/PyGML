# # Normal
# Em_LIST=[]
#
# for i in range(1,11):
#     Em_LIST.append(i)
#
# print(Em_LIST)
#
# # x=["======================================================================================================================================================"]
# # print(x)
# #
# #             # List Comprehension
# #
# # x=[ i for i in range(1,11)]   # Front i is appending in same list
# # print(x)
# #
# # x=["======================================================================================================================================================"]
# # print(x)
# #
# # String="This is an Apple"
# #
# # Vowels=[]
# #
# # for i in String:
# #     if i.lower() in "aeiou":
# #         Vowels.append(i)
# #
# # print(Vowels)
# #
# # x=["======================================================================================================================================================"]
# # print(x)
# #
# # x=[i for i in String if i.lower() in "aeiou"]
# # print(x)
# #
# # x=["======================================================( Nested for loop)==========================================================================="]
# # print(x)
# #
#
# L1 = ["live","arp","strong"]
# L2 = ["lively","harp","sun","armstrong"]
#
# Words = []
#
# for i in L1:
#     for j in L2:
#         if i in j:
#             Words.append(j)
#
# print(Words)
#
# x=[ j for i in L1 for j in L2 if i in j]
# print(x)


x=["======================================================( if elfi else )==========================================================================="]
# print(x)
#
# numbers=[]
#
# for i in range(1,10):
#     if i%2==0:
#         numbers.append(str(i) + " : Even")
#     else:
#         numbers.append(str(i) + " : ODD")
#
# print(numbers)
#
# x = [  str(i) + " : Even "if i%2==0 else str(i) + " : ODD" for i in range(1,10) ]
# print(x)


x=["==============================( Nested List Comprehension )====================================="]
print(x)

numbers=[]

for i in range(5):
    nest=[]
    for j in range(5):
        nest.append(i)
    numbers.append(nest)

print(numbers)

x = [[ i for j in range(5)]for i in range(5)]
print(x)