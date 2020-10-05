import os

print('\\')
#'\\' is a literal backslash
print(r'c:\spam\eggs.png')
#raw string allows backslashes to be used literally

print('\\'.join(['folder1', 'folder2', 'folder3', 'file.png']))
#joins these with literal backslashes, works for windows

print(os.path.join('folder1', 'folder2', 'folder3', 'folder4'))
#Takes several string arguments, return string value of path, appropriate for OS
#Reverse slashes on Windows & Linux/Mac

print(os.getcwd())
#If you call just a filename, the method will operate in current directory
os.chdir('c:\\')
#Moves to a diff. directory
print(os.getcwd())

#'c:\\folder1\\spam.png'
#Absolute file path, starts at root folder
#'spam.png'
#Relative file path, relative to current working directory

#'.' stands for "this directory/folder"
#returns the location of current directory
#".\etc" accesses the etc directory within the current directory
#.\ is optional

#'..' "Parent folder
#"..\happy\etc" Goes to parent folder to happy within parent, to etc within happy
