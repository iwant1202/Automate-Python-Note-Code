import re #imports Regular Expressions

message = 'Call me 415-555-1011 tomorrow,' +\
          'or at 415-555-1012, my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
#re.compile generally uses raw strings
#\d indicates looking for a digit

mo = phoneNumRegex.search(message)
#stores a match object
#only first match found
print(mo.group())

mo = phoneNumRegex.findall(message)
#returns a list of strings which match
print(mo)
