'''
List la irrukara everyelement ikkku change painnanuim na use map
This month every wages salary + 2500 , then
after 2 month every wages salary - 1500
'''
#
# Salary=[("Nisahnth",50000),("vaseekaran,",10000),("Vijaysurya",398276)]
#
# # Map get two Args 1st ine function ,2nd list or any  ==> Salary la irrukara oru oru value lambda ( x ) la store yakuim
# # Salary -- vainthu list(tuple)--> tuple la irruku irruku money vainthu 1 index la irruku ,then i am add 100 Rs in Salary
#
# #Map=map(lambda x: x[1]+100 ,Salary)  # Values only
# Map=map(lambda x:(x[0] ,x[1]+500 ), Salary)
# print(Salary)
# print(Map)
#
# #print(list(Map))
#
# for i in Map:
#     print(*i,end="-")

                    #============================( Filter)===========================#

'''
List la irrukara particular data ah filter la painna use painnalaim

'''

# Salary=[("Nisahnth",50000),("vaseekaran,",10000),("Vijaysurya",398276)]
#
# #Map get two Args 1st ine function ,2nd list or any  ==> Salary la irrukara oru oru value lambda ( x ) la store yakuim
# Filter=filter(lambda x: x[1] > 50000 , Salary)  # x[1] value vainthu 50000 greater then ah irrukara tha maittuim print painnu
# print(list(Filter))


                    # Complex
import os
path=r"D:\Certificates"
ListDirectory=os.listdir(path=path)  # List out the file
#print(ListDirectory)

def TotalSize(directory):
    size=[]
    for file in directory:
        #size.append(os.stat(path + "\\" + file)) # Os la file size calc painna stat oru method irruku
        size.append(os.stat(path + "\\" + file).st_size)  # We need size only
    return size
#print(TotalSize(ListDirectory))

print(sum(TotalSize(ListDirectory)))# Calc the list size coming Bytes


            #  Map With Lambda

total=map(lambda x : os.stat(path + "\\" + x).st_size,ListDirectory)
print(sum(list(total)))

            # Filter with Lambda

# def ExtractFile(ListDirectory):
#     Files=[]
#     for pdf in ListDirectory:
#
#         if pdf.endswith("pdf"):
#             Files.append(pdf)
#     return Files
# print(ExtractFile(ListDirectory))

                    #======================================================================

zipfiles=filter(lambda x: x.endswith("pdf"),ListDirectory)
print(list(zipfiles))
