import os
import shutil

s = input("Enter a source folder name:- ")
d = input("Enter a destination folder name:- ")

s= s+'/'
d= d+'/'
allFiles = os.listdir(s)
for i in allFiles:
    shutil.copy((s+i), d)