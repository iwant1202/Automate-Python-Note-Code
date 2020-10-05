import os


print(os.path.abspath('Nonesense.txt'))
#Returns absolute path passed on current directory
#File does not need to exist, just assumes it does


print(os.path.abspath('..\\..\\Folder1\\Folder2\\Nonesense.txt'))

print(os.path.isabs('..\\..\\folder\\Nonesense.txt'))
print(os.path.isabs('c:\\Folder1\\Folder2\\Nonesense.txt'))
#Returns true if path is absolute, False if negative

print(os.path.relpath('c:\\Folder1\\Folder2\\Nonesense.txt', 'c:\\Folder1'))
#Provides relative path given absolute path, and point to go up to

print(os.path.dirname('c:\\Folder1\\Folder2\\Nonesense.txt'))
#Gets directory names
print(os.path.basename('c:\\Folder1\\Folder2\\Nonesense.txt'))
#Gets base file name

print(os.path.exists('c:\\Folder1\\Folder2\\Nonesense.txt'))
print(os.path.exists('c:\\Windows\\system32\\calc.exe'))
#Returns true if the path exists, FALSE if not

print(os.path.isfile('c:\\Folder1\\Folder2\\Nonesense.txt'))
print('Check' + str(os.path.isfile('Nonesense.txt')))
#Returns true if path ends in file
print(os.path.isdir('c:\\Folder1\\Folder2'))
#Returns true if path ends in directory

print(os.path.getsize('c:\\Windows\\system32\\calc.exe'))
#Returns size of final program
print(os.listdir('c:\\'))
#Returns list of Strings (sub-directories)
