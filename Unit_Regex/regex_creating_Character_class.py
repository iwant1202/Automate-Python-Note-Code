import re

#Putting between square brackets creates custom character class
vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u...)
lowercaseLetters = re.compile(r'[a-z]')

allVowels  = vowelRegex.findall('Robocop eats baby food.')
print(allVowels)

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
allDoubleVowels = doubleVowelRegex.findall('Robocop eats baby food.')
print(allDoubleVowels)

consonantsRegex= re.compile(r'[^aeiouAEIOU]') #^ negates
#Matches everything not specified there
allConsonants = consonantsRegex.findall('Robocop eats baby food')
print(allConsonants)
