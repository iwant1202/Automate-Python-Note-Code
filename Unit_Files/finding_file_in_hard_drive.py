import os

print('Please Enter File or Folder Name: ')
Name = input()
print('Please Enter Starting Directory (enter nothing for root): ')
startingDirectory = input()


if startingDirectory == '':
    startingDirectory = 'c:\\'

print('Please wait. This program may take a couple minutes')
currentDir = startingDirectory
for folderName, subfolders, fileNames in os.walk(startingDirectory):
      for filename in fileNames:
        if filename == Name:
            print(os.path.join(folderName, Name))
            
      for foldername in subfolders:
          if foldername == Name:
              print(os.path.join(folderName, Name))
input()
              


