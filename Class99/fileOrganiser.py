import os
from pickle import EXT1
import shutil

path=input("enter the path of directory")
list_of_files=os.listdir(path)

for file in list_of_files:
    name,ext=os.path.splitext(path)
    ext=ext[1:]

    if ext=="" :
        continue
    
    if os.path.exists(path+"/"+ ext):
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
    
    else:
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
