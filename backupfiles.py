import os 
import shutil
import time
days = 0
path = 'home/User/Document/my.txt'
status = os.stat(path)
print(status)
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 2000:" , ticks)
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('Test', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')

source = input("enter source folder name")
destination = input("enter destination folder name")
listoffiles = os.listdir(source)
for file in listoffiles:
    shutil.move((source+"/"+file),destination+"/"+file)
