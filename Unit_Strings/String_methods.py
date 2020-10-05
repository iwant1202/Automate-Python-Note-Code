#128-141
#String methods return new value rather than altering old
#Strings immutable

spam = 'Hello world!'
print(spam.upper()) #Returns upper-case version
print(spam) #OG variable remains unchanged

spam = spam.upper()
print(spam)

spam = spam.lower() #retursn lower-case version
print(spam)
print('Please enter yEs')
answer = input()
if answer == 'yes':
    print('Playing again') # will fail if enter upper case
if answer.lower() == 'yes': #non-case sensitives
    print('Playing again')

spam = 'Hello World!'

print(spam.islower()) # checks to see if all lower-case
print(spam.isupper()) # checks to see if all upper-case

spam = spam.upper()
print(spam.isupper())

spam = spam.lower()
print(spam.islower())

print(spam.upper().isupper()) #upper returns string, isupper returns boolean yese    
#lots of is___ methods, return boolean value
#isalpha: only alphabet, isalnum: only alphabet and numerics
#isspace: only blank spce, istitle: all title case, begin with lower case

spam = 'Hello world!'
spam.startswith('Hello') #checks for beginning, returns boolean
spam.startswith('H') #True
spam.startswith('Ello') #False

spam.endswith('world!') # checks end, returns boolean
spam.endswith('world') #False, checks back to front

animalList = ['cats', 'rats', 'bats']
animalListString = ','.join(animalList)

#joins together all items with first string inbetween
#returns string afterwards
print(animalListString) 

animalListString = '\n\n'.join(animalList)
print(animalListString)

splitList = 'My name is Simon'.split() #Splits each word into list, divide at spaces
print(splitList)

splitList = 'My name is Simon'.split('m') #Divides at 'm'
print(splitList)

print('Hello'.rjust(10)) #adds blank spaces to beginning, txt to the right
#Makes the text a total of 10 characters
print('Hello'.ljust(10)) #blank space in beginning, txt to left
print('Hello'.ljust(20, '*'))

print(spam.center(20, '=')) #adds =s, with String at center

spam = 'Hello'.rjust(10)
spam = spam.strip() # removes all white spaces from either side of string
spam = 'Hello'.center(10)
print(spam.lstrip()) #Just removes left side
print(spam.rstrip()) #Just removes right side

print('Hello'.strip('ollHe'))
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
#pass String argument, remove all occurences ofString
#basic strip() starts at both ends, stops once the letter combination
#is no longer appearint

spam = 'Hello there!'
spamXYZ = spam.replace('e', 'XYZ')
#first value target, second value replaces
print(spamXYZ)


