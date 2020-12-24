

name=["Nishanth"]

#print(dir(name), type(name))

#print(help(name))

#print(name.__doc__)

# print(name.append.__doc__)
# print(name.extend.__doc__)


import os

class StorageCal:
    """ This is My Own Class """
    def __init__(self,path):
        self.path=path

    def size(self):
        ''' Return Total Size '''
        tot_size=0
        for root,dir,files in os.walk(self.path):
            for file in files:
                tot_size=tot_size+(os.stat(root+"\\"+file).st_size)
        return tot_size/(1024/1024)

x=StorageCal(r"C:\Users\Nishanth\PycharmProjects")
#print(dir(x))

print([ i for i in dir(x)if i[0] != "_"])

print(x.__doc__)