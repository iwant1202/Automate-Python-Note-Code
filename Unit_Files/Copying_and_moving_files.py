import shutil

shutil.copy('c:\\spam.txt', 'c:\\delicious')
#return the new location

shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')
#This copies and then renames the file

shutil.copytree('c:\\delicious', 'c:\\deliciousbackup')
#creates a new folder and copies all contents from first file

shutil.move('c:\\spam.txt', 'c:\\delcious')
#original spam no longer exists, now in delicious

shutil.move('c:\\delicious\\walnut\\spam.txt', 'c:\\delicious\\walnut\\eggs.txt')
#Renaming a file
