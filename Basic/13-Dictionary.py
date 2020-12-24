'''

[
'clear'  --->

'copy'  --->

'fromkeys' -->

'get'   --> eg: D={1:"A",2:"B}  print(D[1]) output --A  , Suppose  print(D[3]) output -- KeyError
                (== Here we use get to avoid error through==> print(D[3]) output -- None)
                It's take tow arg 1st one key value , 2nd one suppose key not found means  what we can display
'items'
'keys'
'pop'
'popitem'
'setdefault'
'update'
'values'
]

'''
# print([i for i in dir(Dic1) if "_" not in i])  # Find the function in Dictionary
#d={}
#print(help(d))
#print(type(d))

#Dic1={1:'A',2:"B",3:"C"}

#print(Dic1)
#print(Dic1[1])
                # Adding

#Dic1[4]="D"
#print(Dic1)

                # Get Function
#Dic1={1:'A',2:"B",3:"C"}
#print(Dic1[5])
#print(Dic1.get(5))
#print(Dic1.get(5,"Sorry! Enter correct Key "))

#========================================= Only Keys you need means use ( .keys )=====================================================================
# Dic1={1:'A',2:"B",3:"C"}
#
# #print(Dic1.keys())
# for i in Dic1.keys():
#     print(i)


#=============================================== Only values you need means use ( .values )======================================================
# Dic1={1:'A',2:"B",3:"C"}
#
# #print(Dic1.values())
# for i in Dic1.values():
#     print(i)

#================================== Both values and keys you will need means use ( .itmes )======================================================
#Dic1={1:'A',2:"B",3:"C"}

#print(Dic1.items())
#for i in Dic1.items():
#    print(i)

#================================== setdefault  means Setdefault values in Dic   ( .setdefault )======================================================
'''
Suppose Entered key, has already values means, It's return already excited value
'''
#Dic1={1:'A',2:"B",3:"C"}

#print(Dic1.setdefault(3,"N"))

#print(Dic1)

#==================================   means use ( .fromkeys )======================================================
'''

Dict la irrukara keys vanuim with same values kudaa ,

    print(Dic1.fromkey(Dic1)) or  print({}.fromkey(Dic1))--->

      ethu ena painnuim na dic la irrukara key yalathaiuim  display painnuim
    but key values ah (default none) inu display painnuim

----------------------------------------------------------------------------------------------------------------------

       print(Dic1.fromkey(Dic1,"Nishanth")) or  print({}.fromkey(Dic1, "Nishanth"))--->

        It's change all values in dic and add enterted word --
        It's Set All Values are Same

'''

# Dic1={1:'A',2:"B",3:"C"}
#
# #print(Dic1.fromkeys(Dic1))
#
# print(Dic1.fromkeys(Dic1,"Nishanth"))

#================================== POP  ======================================================
'''
POP  --- It's delete + Return  (Values)
'''

#Dic1={1:'A',2:"B",3:"C"}
#print(Dic1.pop(1)) # or
# A =Dict.pop(1)
#print(A)
#print(Dic1)
#==================================  POPITEM  ======================================================
'''
POPITEM -- It's Delete + Return (key and Values ) in beckward one by one

'''
# Dic1={1:'A',2:"B",3:"C"}
#
# B=Dic1.popitem()
# print(B)
#
# print(Dic1)

#==================================  Copy  ======================================================
#
# Dic1 = {1: 'A', 2: "B", 3: "C"}
#
# Copy_Dic1=Dic1.copy()
# print(Dic1)
# print(Copy_Dic1)

#==================================  Clear  It's Return Blank DIC ======================================================

#
# Dic1 = {1: 'A', 2: "B", 3: "C"}
#
# Clear_Dic1=Dic1.clear()
# print(Dic1)
# print(Clear_Dic1)