#PlainText files can also be opened by notepad
#Python programs also PlainText
#Binary Files - all other types of files:
    #exe, png, pdf, doc, etc.
    #Each binary file has to be dealt with individually
    #likely with modules

helloFile = open(r'C:\Users\nicho\hello.txt')
#opens the files in read mode, can also do 'pathName', 'r'
contents = helloFile.read()
#Returns contents of file

helloFile.close()
helloFile = open(r'C:\Users\nicho\hello.txt')
#have to close and reopen the file w/ each reading

contentLines = helloFile.readlines()
#Reutrns list of Strings(each line)

print(contents)
print(contentLines)

