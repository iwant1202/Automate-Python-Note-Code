import re
message = 'My number is 415-555-4242'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)

print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#Parentheses mark out where groups begin and end
#Separates phone number into two groups
#Area code: group 1, rest of number: group 2
mo = phoneNumRegex.search(message)

print(mo.group())
print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
#Slash before parentheses gives a literal parentheses

message = 'My number is (415) 555-4242'
mo = phoneNumRegex.search(message)
print(mo.group())
# | = pipe characater

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#pipe is a kind of or operator for RegEx
message = 'Batman lost the Batmobile'
mo = batRegex.search(message)
print(mo.group())
print(mo.group(1)) #Pipe section paranthesesed off

mo = batRegex.findall(message)
print(mo)

mo = bat.Regex.search('There is nothing here')
mo.group() #This will fail, b/c noneValue returned by search
#NoneType does not have group option
