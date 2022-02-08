import os
import shutil

p = input("Enter the name of the directory to be sorted : ")

list_of_files = os.listdir(p)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    myExt = ext[1:]
    if(myExt==''):
        continue
     #png , txt , py  ,jpeg
    if os.path.exists(p+'/'+myExt):
         #/users/downloads/boy.png , /usrs/downloads/py/sam.py
        shutil.move(p+'/'+i, p+'/'+myExt+'/'+i)
    else:
        os.makedirs(p+'/'+myExt)
        shutil.move(p+'/'+i, p+'/'+myExt+'/'+i)
        