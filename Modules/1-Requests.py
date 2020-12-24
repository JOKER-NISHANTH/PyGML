
import requests

url = "https://www.w3schools.com/cert/default.asp"

# print(dir(requests))


headers = { "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}   # re 1
response = requests.get(url=url,headers=headers)  # ref 1
#response = requests.get(url=url)



# print(response)

# print(response.status_code)    # STATUS_CODE IS VERY IMPORTANT

# print (response.headers)

print (response.request.headers)
"""
# How to change User-Agent  Refer Top  re 1

# print(response.content)    # It's display the HTML code in bytes code  and here read the pages  , file operation (read mode)

# print(type(response.content)) # used to check the types

''' How to download the img or videos or songs 

 print(response,content) in read mode 
    we can convert read mode to write mode by useing file operation '''

img = response.content

# Here we write the file using (wb) --> Write Byte

writes = open(" Here we put some name eg: nishanth.jpg", "wb")

writes.write(img)
"""
# ---------------------------------x--------------------------x---( TEXT Return String )--------------------------------x------------------x---------------
"""
import requests

url = "https://www.w3schools.com/cert/default.asp"

response = requests.get(url=url)

# print(response.text)
print(type(response.text))

"""

#----------------x-------------------------x----- How get unique data sets ------------------x----------------------------x-----------------------------x-----------
'''

import requests

url = "https://www.w3schools.com/cert/default.asp"


params = {

    "Month":"May"
}


response = requests.get(url=url, params=params)

print(response.text)

# How to check the URL

# print(response.url)
'''
# -------------------------X-------------------- How to send data input in web ( post requrest) X-----------------------X---------------------X---------------
'''
import requests

url = ""

payload = {
    " ": " ",
    " ": " "
    
}

response = requests.post(url=url, data=payload)

print(response.text)
'''
#--------------x-------------------x-----------------How to upload text files  ()----------x-------------------------------------x-------------------------------x---
                    # Create one txt file in same directory
"""
import requests

url = ""   # Use inspect element to get the POST requrest link

File = {

    "" : open("text.txt", mode="rb")
}
response = requests.post(url=url, file=File)

print(response.text)
"""
#-------------------------X-----------------------x------------How to download the file---------------x--------------------------------x-----------------------x-------

"""
import requests

url = ""   # Domin name + a href tages
File = {

    "" : open("text.txt", mode="rb")
}
response = requests.get(url=url)

views = response.content

# Download process

Download = open("views.txt", mode="wb")
Download.write((views))
"""

#----------------------x-----------------------------------x-- TimeOut----------------------------x---------------------------------x------------------
'''
import requests

url = "https://www.learnpython.org/"



response = requests.get(url=url ,timeout=0)

print(response.text)
'''