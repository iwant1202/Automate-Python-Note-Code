import shelve

shelfFile = shelve.open('mydata')
#Allows you to store lists, dictionaries, etc.
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

#Creates special binary files
shelfFile = shelve.open('mydata')
print(shelfFile.keys())
print(list(shelfFile.keys()))
print(shelfFile.values())
print(list(shelfFile.values()))

#Keys and values just like dictionaries
