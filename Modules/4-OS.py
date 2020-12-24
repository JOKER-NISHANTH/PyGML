'''
getcwd -- current working directory
listdir --- current directory la irrukaratha list painnuim
chdir --Change the working directory
mkdir -- Make directory or new floder
rmdir -- delete the directory or floder ,there we put input of the name within " "
remove -- File remove
rename -- to rename the file or floders  , it's take 2 arg ---,1for old file/floder ,next one for new name
stat -- get file information
st_size -- to return file size in bytes code

                Two Important function
                1.system  -- dir is use to list the dir like (ls in Linux)
                2.popen  -- it's return one object


# In this python terminal cls cammands not working so we create (cls function in python commentprompt)
                def cls():
                    import os
                    os.system("cls")

                    Most Used function
                    1. walk -- it's get one path input , then it's return object value

=========================================================================================================================
                         OS PATH MOUDLES WE SEE IN BELOW

'''

'''
import os

# print(dir(os))

# print(os.getcwd())

# print(os.listdir())   # Here we can pass argument like C:Nishanth\.... ,F:\Visual Studio Code
# print(os.listdir(r"F:\Visual Studio Code Projects"))

# os.chdir(r"") # Now here move this dir ,then get current dir using getcwd
# print(os.getcwd)

#os.mkdir("5-Random.py")

# os.rmdir("5-Random.py")

#os.remove("Here we put some name")

#os.mkdir("DEMO")
#os.rename("DEMO","DemO")

#print(os.stat("1-Requests.py"))
#print(os.listdir())

# os.system("dir")
#x = os.system("dir")
#print(x)

#y = os.popen("dir")
#print(y)   # Here return one object
#print(y.read())  # Here we read the object using read function


#z = os.walk(os.getcwd())  # This retun one object values
#print(next(z))     # it's return 3 values in tuples , 1st's -- PATH  , 2nd's -- Floders , 3rd's -- Files
# Now we put for loop to iterator this
#for i in z:
 #   print(i)

'''

#========x========x=========x==========x=============x=============x===============x===========x===========x========x
"""
function:
join -- it's join the path+file
isdir --  we give a input path or file
            Floder means return --> TRUE | Flie means return --> FLASE
isfile

split-- SPLIT the one file and path
split extension
"""
import os
from os import path

# print(dir(path))

files = os.listdir()  # List out the file

for file in files: # print one by one floders/files
#    print(file)
#    print(os.getcwd(),file)  # get Path using getcwd
    #print(os.getcwd()+"\\"+file) # suppose we will made some mistake in fast coding , so see below code
    #print(path.join(os.getcwd(),file))  # It's take 2 arg , 1st path--> 2nd file

    fullpath = path.join(os.getcwd(), file)
    #print(path.isdir(fullpath))
    I = path.isdir(fullpath)
    # particular path la irrukara floder's extract painnanuim na we use if statement
    '''if I == True:
        print("It's Floder")
    else:
        print("It's File")'''

    #if path.isdir(fullpath):  # It's return floder only becoz floder is 1 that means TRUE
     #   print(fullpath)

    #if path.isfile(fullpath): #  It's return file only becoz file is 1 that means TRUE
     #   print(fullpath)

    #print(path.split(fullpath)) # Its return tuples , so we need file name only ,we give [1] , or [-1]
    #print(path.split(fullpath)[1])
    #print(path.split(fullpath)[-1])

    # We need path name [0]
    #print(path.split(fullpath)[0])

    # --- SPLIT EXTENSION--------
    #print(path.splitext(fullpath))
    print(path.splitext(fullpath)[1])