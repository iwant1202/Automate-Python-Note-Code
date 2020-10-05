import os
import shutil
import send2trash

os.unlink('bacon.txt')
#Passing relative file path, deletes file permanently

os.rmdir('c:\\delicious')
#Deletes an empty directory
#Cannot delete a non-empty folder

shutil.rmtree('c:\\delicious')
#Deletes directory and everything within it
#NOT SENT TO RECYCLE BIN

for filename in os.litdir():
    if filename.endswith('.txt')
    #os.unlink(filename)
    print(filename)

#Dry Run: running it as printing instead of deleting first
#Go safely
    
send2trash.send2trash('c:\\users\\al\desktop......')
#Sends to recycle bin


