import re

beginsWithHelloRegex = re.compile(r'^Hello')
#^ means that the it must appear at beginning of string
helloStart = beginsWithHelloRegex.search('Hello There!')
print(helloStart)
helloNotStart = beginsWithHelloRegex.search('There Hello!')
#Returns None value
print(helloNotStart)

endWithWorldRegex = re.compile(r'world!$')
endsWithWorld = endWithWorldRegex.search('Hello world!')
print(endsWithWorld)
#returns none value

helloWorldRegex = re.compile(r'^Hello world!')
helloWorldSearch = helloWorldRegex.search('Hello world!')
print(helloWorldSearch)
helloWorldSearch = helloWorldRegex.search('---Hello world!---')
print(helloWorldSearch)
allDigitsRegex = re.compile(r'^\d+$')
#The entire String must be one or more digits
findOnlyDigits = allDigitsRegex.search('28397509238721')
print(findOnlyDigits)
findOnlyDigits = allDigitsRegex.search('98279x7920345')
#Does not only have digits all throughout, returns None
print(findOnlyDigits)
