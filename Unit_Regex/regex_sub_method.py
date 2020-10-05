import re

namesRegex = re.compile(r'Agent \w+')
secretMessage = 'Agent Alice gave documents to Agent Bob'
print(namesRegex.findall(secretMessage))
#Redact secret names

print(namesRegex.sub('REDACTED', secretMessage))
#Sub method finds and replaces (w/ 1st argument)

namesRegex = re.compile(r'Agent (\w)\w*')
#First letter made into group, only returns that group
print(namesRegex.findall(secretMessage))
print(namesRegex.sub(r'Agent \1', secretMessage))
#\1 indicates to use text from group 1
#Need r', so as to not have literal backslash
