exampleString = "That is Alice's Cat" #Can use double quote
exampleString2 = 'Say hi to Bob\'s mother.' # \ is an escape character

#\' = ', \" = ", \t = tab, \n = Newline(line break), \\ = backslash

print('Hello there!\nHow are you?\nI\'m fine')

print(r'That is Carol\'s cat') #Raw String

#Multi-line strings
print("""Dear Alice,
Eve's cat has been arrested for catnapping, car burgalry,
and extortion.
Sincerely,
Bob.""") #Useful for large strings

print(exampleString[1])
print(exampleString[-1])
print(exampleString[1:3])

if 'Cat' in exampleString:
    print('Cat is in examplestring')
if 'Dog' not in exampleString:
    print('Dog is not in exampleString')
