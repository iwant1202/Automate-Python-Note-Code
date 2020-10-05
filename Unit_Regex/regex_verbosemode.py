import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

verbosePhoneRegex = re.compile(r'''
(\d\d\d-)|              # area code (without parentheses, without dash)
(\(\d\d\d\))          #  -or- area code with parens and no dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last 4 digits
\sx\d{2,4}  #extension, like x1234''', re.VERBOSE)
#Verbose means that white spaces is not counted
#Can make it separate lines for read-ability
#Can also comment within

verbosePhoneRegex = re.compile(r'''
(\d\d\d-)|              # area code (without parentheses, without dash)
(\(\d\d\d\))          #  -or- area code with parens and no dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last 4 digits
\sx\d{2,4}  #extension, like x1234''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
#Bitwise operators, combines the second arguments to the compile function
