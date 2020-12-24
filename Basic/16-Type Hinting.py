
'''
Name vainthu input ah string ah maittuim tha vakuim inu soilla str use painnaroim

  Namaa Kuduthu irrukara function crt ah irruku inu text painna
        Third Party Mod use painnalaim
            pip install mypy
'''

"""

def reverse(name:str) -> str:
    return 0

    -> Return value string ah irrukanuim solla ( -> str )
    but below 0 --> it's return int

    program expect str but here int
         so through error

"""


# def reverse(name:str):
#     return name[::-1]
#
# print(reverse("Nishanth"))
# #print(reverse(["Vasee","Surya"]))
# print(help(reverse))
#
#
#



# def reverse(name:str) ->str:
#     return 0
#
# print(reverse("Nishanth"))
# #print(reverse(["Vasee","Surya"]))
# print(help(reverse))
#
#
#



#========================================(  Same time la list and string ah pass painnanuim)=======================================
'''
Typing Module == Multiple type of data ah pass painna mudiuim

    union -- Inu oru object irruku etha use painne , Multiple type of data ah pass painna mudiuim
'''
import typing

# def reverse(name: typing.Union[str,list]) -> typing.Union[str,list]:
#     return name[::-1]
# 
# print(reverse("Nishanth"))
# print(reverse(["Vasee","Surya"]))
# print(help(reverse))


# def  add_list(numbers):
#     return sum(numbers)
#
# print(add_list([1,2,3]))
# print(add_list([4,5,6]))
# print(add_list([4,5,'6']))  --> Eroor through ,why means strinh here

def  add_list(numbers: typing.List[int]) -> int:
    return sum(numbers)

print(add_list([1,2,3]))
print(add_list([4,5,6]))



def add(x,y):
    return x + y