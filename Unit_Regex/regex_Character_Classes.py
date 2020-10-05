import re
#\d syntax, represent any numeric digit
digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)')
#Same thing as \d

#\D any character not 0-9 numeric digit
#\w any letter, numeric digit, or underscore character
#\s Any space, tab, newling character
#Capital letter inverts

lyrics = '12 drummers, 11 pipers, 15 people sad bad, 5 sadly happy'

xmasRegex = re.compile(r'\d+\s\w+')
#Looks for one or more digits
#Followed by single space
#followed by one or more word characters
#Until reaches a non-word character (i.e. space)
allLyrics = xmasRegex.findall(lyrics)
print(allLyrics)
