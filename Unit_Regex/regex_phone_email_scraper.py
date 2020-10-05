#! python3
import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 135, x12345
(
((\d\d\d)|(\(\d\d\d\)))?  #area code (optional
(\s|-)            # first separator
\d\d\d            # first 3 digits
-            # separator
\d\d\d\d           # last 4 digits
(((ext(\.)?\s)|x)   (\d{2,5}))?  # extension (optional)
) #Mega group, group zero
''', re.VERBOSE)

#TODO: Create a regex fro email addreses
emailRegex = re.compile('''
[a-zA-z0-9_.,+]+                   #name
@                    #@ symbol
[a-zA-z0-9_.,+]+                 #domain name



''', re.VERBOSE)
#TODO: Get the text off the clipboard
text = pyperclip.paste()

#TODO: Extract the email\phone from this text
extractedPhone = phoneRegex.findall(text)
#Returns list of Tuples
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone: #enhanced for loop
    allPhoneNumbers.append(phoneNumber[0])
    
print(extractedPhone)
print(allPhoneNumbers)

print(extractedEmail)

#TODO: COPY the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

