'''
#  Default Read mode
 Methods-->    'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering',
                        'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines',
      '           reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines'
'''

File=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="r")
print(dir(File))
#============================ Name and Mode ==========================================
print(File.name) # Showing or get File Name and path -- F:\NotePad ++\Text Files\File Handling.txt
print(File.mode) # Get mode r
#============================Readable================================================
print(File.readable())  # Get readable or not -->True

X=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="w")
print(X.readable())  # False

#============================Read==========================================================

R=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="r")
print(R.read())

print(R.read(10)) # You need 1st 10 char in the file that time we use pass the values
print(R.read()) # Return Balance Char

#=========  How to find crt position ==============
P=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="r")


print(P.tell())     # 0  --> Before read

print(P.read(9))    #

print(P.tell())     # 9 --> After Read

#===> ( Seek -- Used to Direct ah ena position la irruthu read  painnanuimmoo apo seek use painnalaim ) <====

S=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="r")
print(S.read(10))
print(S.tell())
S.seek(0)
print(S.read())

#====>( Readline and Readlines ) <====
'''
You need to read line by line --> That time use readline
'''
R=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="r")

print(R.readline())
print("---------------------")
print(R.readline())
print("---------------------")
print(R.readline())

for i in R:
    #print(i,type(i))
    print(i.strip())  # Strip is use to remove space

#==============( Readlines )===============
'''
Readlines --> Take every line or element , then convert into List

'''
R_L=open(r"F:\NotePad ++\Text Files\File Handling.txt",mode="r")
print(R_L.readlines())

#===============================(  Write Mode )==========================================
W=open(r"F:\NotePad ++\Text Files\File Handling Write",mode="w")
                        #How to Create new file
W_C=open(r"F:\NotePad ++\Text Files\File Handling W Mode.txt",mode="w")
W_C.write("Cyber Nishanth")
W_C.write("Nishanth") # Overriding

#===============================(  Append Mode )==========================================
A=open(r"F:\NotePad ++\Text Files\File Handling A Mode.txt",mode="a")
A.write("Welcome to Learn ")
A.write("Append Mode")

#===============================(  Flush and Close )==========================================

F = open(r"F:\NotePad ++\Text Files\File Handling F ","w")
F.write(("Hey Babe"))  # It's store in Buffer memory
F.flush() # Now Store in File
F.write("I Love Python")
F.flush()
C = open(r"F:\NotePad ++\Text Files\File Handling F ","w")
C.write("Close Method")
C.close()
C.write("Bye") # ValueError: I/O operation on closed file.

#===============================(  With , Closed -- Contained Manager )==========================================
W = open(r"F:\NotePad ++\Text Files\File Handling F ","w")
with open(r"F:\NotePad ++\Text Files\File Handling.txt ","r") as d:
    print(d.read())
    print(d.closed)
#print(d.read()) # ValueError: I/O operation on closed file.
# How to Check File is Closed or not
print(d.closed)
#====> ( Image read ) <====

with open(r"F:\Mobile Pic\Kiss.jpg","rb") as J:
    #print(J.read()) # read Bytes
    #print(type(J.read()))
    Img_byt=J.read()
    with open(r"F:\Mobile Pic\Winner.jpg","wb") as W:
        W.write(Img_byt)

import requests
from bs4 import BeautifulSoup

def ExtractLinks(url):
    R = requests.get(url=url).content
    Soup = BeautifulSoup(r,"lxml")
    Li = Soup.find("div",)