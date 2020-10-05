import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']
#returns list of Strings

#Checks if command line arguments passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
    #Join list together into a String with spaces inbetween each item

else:
    address = pyperclip.paste()
#https://www.google.com/maps/place/<Address>
    #Google maps URL
    #Website smart enough for spaces though
webbrowser.open('https://www.google.com/maps/place/' + address)
