import os

helloFile = open('c:\\users\\nicho\\hello2.txt', 'w')
#'w' means to write to a file, overwriting.
#'a' means to append, adding on to the file
#creates a new file if it does not exist

helloFile.write('Hello!!!!!\n')
helloFile.write('Hello!!!!!\n')
helloFile.write('Hello!!!!!\n')
print(helloFile.write('Hello!!!!!\n'))
#In addition ot writing, returns number of characters

helloFile.close()

print(os.getcwd())

baconFile = open('bacon.txt', 'w')
#Creates a file in cwd(current working directory)
baconFile.write('Bacon is not a vegetable')
baconFile.close()

baconFile = open('bacon.txt', 'a')
#appends, does not overwrite the file

baconFile.write('\n\nBacon is delicious.')

baconFile.close()
