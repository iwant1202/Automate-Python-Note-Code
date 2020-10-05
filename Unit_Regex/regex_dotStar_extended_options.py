import re

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)
dotStar  = re.compile(r'.*')
print(dotStar.search(prime)) #Only returns the first line

dotStarAll = re.compile(r'.*', re.DOTALL)
#This makes '.'s mean truly everything, with new lines
print(dotStarAll.search(prime))

vowelRegex = re.compile(r'[aeiou]')
exampleText = 'Al, why does your programming book talk about RoboCop'
print(vowelRegex.findall(exampleText)) # only does lower case

vowelRegex = re.compile(r'[aeiou]', re.I) #I stands for IGNORECASE
print(vowelRegex.findall(exampleText))
