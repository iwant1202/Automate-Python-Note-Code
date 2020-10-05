print(list('Hello')) #Strings kind of lists of characters

name = 'Zophie'

print(name[0]) #char index
print(name[:3]) #slice
print(name[-2]) #reverse index, start from back

if 'Zo' in name: #in function
    print('Zo is in the name')

if 'xxx' in name:
    print('xxx is in the name')
else:
    print('xxx is not in the name')

for letter in name:
    print(letter)

#Difference: String is immutable data type
#name[3] = 'X'    not possible

name = 'Zophie a cat'
print(name)
newName = name[0:7] + 'the' + name[8:12] #change name by making new one with slices
print(newName)


