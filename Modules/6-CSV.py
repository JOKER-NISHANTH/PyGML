"""
CSV is Comma seprater
Reader-- method is use to Read the file , it's take 1st arg (file-name)
Line_num -- it's return 0
"""
'''
# <===========> ( CSV read file) <===========>
import csv

#print(dir(csv))


csv_file=open("report.csv",mode="r") # Open Method default take read mode
reader = csv.reader(csv_file)
#print(reader.line_num)  # ref 1
#print(reader)  # It's return object

for i in reader:  # Iterated it , its split comma bases then return list type

	#----- It's return coloum name also
#    print(i)
	print(reader.line_num)  # Ref 1
	print(i[-1])
	'''
#==============( You don't need coloum name )  ref top 1

"""
import csv

csv_file = open("report.csv", mode = "r")
reader = csv.reader(csv_file)

for i in reader:
	#print(reader.line_num) # How to avoid the number
	if reader.line_num !=1:  # Now we check coloums not display
		print(i)

"""

# <==========> ( CSV Write ) <========>
'''
Writerow -- Hyterbole object ah input vakuim (data) list ah irruku so pass painnalaim,

'''

"""

import csv

csv_file = open("report.csv", mode = "r")

reader = csv.reader(csv_file)

#

new_file = open("report1.csv", mode = "w" , newline="")    # ref 1 --| newline="" |
writer = csv.writer(new_file)


for data in reader:

	data[1:-1] = []  # Slice the list 2nd and 3rd value
	writer.writerow(data)   #  It's write one by one on new line  , so we need to avoid that | ref top 1
	#print(data)

"""



# <=============> ( Now we can read or write on dict ) <=============>
'''
DictReader -- It's take file Object for input
'''
"""
import csv

csv_file = open("report.csv")
reader = csv.DictReader(csv_file)   # It's return dic format


for data in reader:
	# Two method to access the dic elements -- 1st one [key]  ,2nd get
	#print(data["Name "])  # 1st method it's risk, why suppose miss the keyword crtly through error ,like space mistake
	 print(data.get('Name '))  # 2nd method suppose miss the keyword crtly through none
"""
#===================x=================================x=(  Now we write dic format )===========x=================x=====
'''
DictWriter --- 1st file name then input fieldname ah namaa list ah pass painnanuim
'''
import csv

csv_file = open("report1.csv",mode="w",newline="")  # newline = remove the space
writer = csv.DictWriter(csv_file,fieldnames=["First_Name",'Salary'])

writer.writeheader()  # ref 1 Field name mention
employees = [
	{
    "First_Name":"Vijay",
    'Salary': 10000
},
{
    "First_Name":"Yalini",
    'Salary': 20000
},
]

for data in employees:
	writer.writerow(data)  # Here coloum name or field not mention the displaying output ref top 1
	print(data)
