import re

atRegex = re.compile(r'.at')
#Anything followed by at
allAt = atRegex.findall('The cat in the hat sat on the flat mat')
#lat returned, not flat, b/c '.' only looks for one character prior
print(allAt)

atRegex = re.compile(r'.{1,2}at')
#at preceeded by one or two characters of anything
allAt = atRegex.findall('The cat in the hat sat on the flat mat')
#Also returns space characters
print(allAt)

nameData = 'First Name: Al Last Name: Sweigart'
print(nameData.find(':') ) # Returns index
#Can keep on doing this to find slices, etc.

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#.* means all characters there
# Returns two groups, that being first and last name
#.* is greedy, try to match as much stuff as possible
fullName = nameRegex.findall(nameData)
print(fullName)

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
#Keep on going until finding 1st closed angle bracket
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))
#Realizes that it can go further

