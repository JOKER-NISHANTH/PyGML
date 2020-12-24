'''
Slicing Object are
        String
        List
        Tuples
        Why these are Slicing it's contain index
        Syntax ===> Letters[start:Stop:Jump]  default --> start=0 :stop= end vara irrukuim:Jump=1
'''
# Name="Nishanth"
# Num=[0,1,2,3,45,6,7,8,9]
# Letter=['A',"B","C","D","E","F","G","H"]
# #a=Name.swapcase()
# print(Name[0])
# print(Num)
# print(Letter)


#=========================================================( We we start Learning Slicing )=============================================================================

#     #   -8  -7  -6  -5  -4  -3   -2  -1
# Letter=['A',"B","C","D","E","F","G","H"]
#     #    0   1   2   3   4   5   6    7

# print(Letter[0:4])    # ['A', 'B', 'C', 'D']
# print(Letter[:4])     # ['A', 'B', 'C', 'D']
# print(Letter[1:4])    # ['B', 'C', 'D']
# print(*Letter[1:-1])  # B C D E F G
# print(*Letter[-8:5])  # A B C D E
# print(*Letter[1:])    # B C D E F G H
# print(*Letter[:])     # A B C D E F G H

             #---------------------------(  Jump )-----------------------------------#

    #   -8  -7  -6  -5  -4  -3   -2  -1
#Letter=['A',"B","C","D","E","F","G","H"]
    #    0   1   2   3   4   5   6    7

# print(Letter[0::2]) # ['A', 'C', 'E', 'G']
# print(Letter[0::4]) # ['A', 'E']
#
# print(Letter[::1])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# print(Letter[::-1]) # ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
#
# print(Letter[-2:-6:-1])  # ['G', 'F', 'E', 'D']
#
# print(*Letter[::])     # A B C D E F G H
#


    #----------------------( Inbetween Changes  using index )----------------------------------#

    #   -8  -7  -6  -5  -4  -3   -2  -1
Letter=['A',"B","C","D","E","F","G","H"]
    #    0   1   2   3   4   5   6    7

# Letter[3]=1
# print(Letter)

#Letter[1:7]=123 # TypeError: can only assign an iterable
Letter[1:7]="123"  # ['A', '1', '2', '3', 'H']

#Letter[-6:-2]="Nishanth"  # ['A', 'B', 'N', 'i', 's', 'h', 'a', 'n', 't', 'h', 'G', 'H'] String is extend to char by char

#Letter[2:6]=["Welcome to Nisha"]  # ['A', 'B', 'Welcome to Nisha', 'G', 'H']
#print(Letter)

                                    #============================( Real Time EG: )==================================#

# Websites=[
#     "www.google.com",
#     "www.yahoo.org",
#     "www.amazon.in"
# ]
# print(Websites)
# #print(Websites[0].find(".",4))  # Find the index of 2 nd .dot
#
# #for i in Website.find(".",4):  # AttributeError: 'list' object has no attribute 'find'
# #    print(i)
#
# for website in Websites:            # Find all index in list
#     #print(website.find(".",4))     # Display . index value
#     #print(website[website.find(".",4)])  # Display . only
#     #print(website[website.find(".",4):])  # Here Start--> website.find(".",4)  |  Stop : --> . la irruthu full laa
#     print(website[website.find(".", 4)+1:])  # Here . skipping  -->
#                                              # How ? -- >
#                                              # Now we find dot index +1 means --> dot ikku apro irrukaratha print or displsy painnu
#
#
                                        #

Websites=[
    "www.google.com",
    "www.yahoo.org",
    "www.amazon.in"
]

for website in Websites:
    #print(website[website.find(".")+1],website[website.find(".",4)])
           # Again Slicing                                              Start                   Stop
    print(website[website.find(".") + 1: website.find(".", 4)])  # website.find(".") + 1: website.find(".", 4)]
