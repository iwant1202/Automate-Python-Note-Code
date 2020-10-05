#Pattern Matching and Regular Expressions
#Regular Expressions meant to find specific text patterns
#SUPER Ctrl-f

#Non-regular expression example
def isPhoneNumber(text):
    if len(text) != 12:
        return False #not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
        if text[3] != '-':
            return False #missing dash
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False # no first three digits

        if text[7] != '-':
            return False #missing second dash
        for i in range (8, 12):
            if not text[i].isdecimal():
                return False #missing last 4 digits
        return True

print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('222-3231523'))

#non-RegEx code to find phone number in message
message = 'Call me 415-555-1011 tomorrow,' +\
          'or at 415-555-1012, my office line'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12] #Slice can go past end index
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
            

        
