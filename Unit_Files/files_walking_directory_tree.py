import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
#Returns string of folder name, string list of subfolders
#and string list of filenames

#Then goes through each subfolder and does the same thing
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The files in ' + folderName + ' are: ' + str(filenames))
    print()
    #Prints out a new line
    for file in filenames:
        if file.endswith('.png'):
            shutil.copy(os.join(folderName, file), os.join(file, folderName) + ' .backup')
