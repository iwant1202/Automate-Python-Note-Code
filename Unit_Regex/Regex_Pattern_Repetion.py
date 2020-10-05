import re

batRegex = re.compile(r'Bat(wo)?man')
#States that the 'wo' can appear in the text 0 or 1 times
#for a match
#Makes the 'wo' optional

message = 'The Adventures of Batman'
mo = batRegex.search(message)
print(mo.group())

message = 'The Adventures of Batwoman'
mo = batRegex.search(message)
print(mo.group())

message = 'The Adventures of Batwowowowowoman'
# 'wo' apears more than 1 or 0 times, returning None
mo = batRegex.search(message)
if mo == None:
    print('Nothing Found')

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'My phone number is 415-555-1234'
mo = phoneRegex.search(message)
print(mo.group())

message = 'My phone numbers are 555-1234 and 415-555-1234'
#Will not find first one w/ current system
mo = phoneRegex.search(message)
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# Makes area code optional
mo = phoneRegex.search(message)
print(mo.group())
#can escape question mark with backslash '\?'

batRegex = re.compile(r'Bat(wo)*man')
#'*' indicates that 'wo' can appear 0 or more times
message = 'I am the Batwowowowowowowoman'
message2 = 'I am the Batman'
mo = batRegex.search(message)
print(mo.group())
mo = batRegex.search(message2)
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')
#'+' means that group must appear once or more times
message = 'I am Batman'
mo = batRegex.search(message)
if mo == None:
    print('Nothing found')
message = 'I am Batwoman'
mo = batRegex.search(message)
print(mo.group())
message = 'I am Batwowowowowoman'
mo = batRegex.search(message)
print(mo.group())

haRegex = re.compile(r'(Ha){3}') #Looks for 'Ha' exactly three times
message = 'He said "HaHaHa" '
mo = haRegex.search(message)
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?)')
#Finds exactly three iterations, w/ optional area code & comma
#Edit later, did not work
message = 'My numbers are 415-555-1234, 555-4242, 212-555-0000'
mo = phoneRegex.search(message)
print(mo.group())
mo = phoneRegex.search(message)




haRegex = re.compile(r'(Ha){3,5}') #acknowledges 3-5 repetitions
message = 'HaHaHaHaHaHaHaHa'
mo = haRegex.search(message)
print(mo.group()) #Limited by first 5 Has
#Greedy matching, maximum possible of matches, longest possible string

haRegex = re.compile(r'(Ha){3,5}?') #Forces a non-greedy match
#Will go only for the first 3 if go over limit
message = 'HaHaHaHaHaHaHaHa'
mo = haRegex.search(message)
print(mo.group())
