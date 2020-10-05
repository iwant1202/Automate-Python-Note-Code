import pprint

message = 'It was a bright cold day in April, and the clocks were' +\
          'striking thirteen'
count = {} #Empy dictionary
count2 = {}

for character in message:
        count.setdefault(character, 0)#necessary for first time character appears
        #Keys are each character, values are amount of times appeared
        count[character] = count[character] + 1
        #Counts number of times a character appears

print(count)
pprint.pprint(count) #Pretty Print!
for character in message.upper(): #sets all lower to uppercase, no diff now
        count2.setdefault(character, 0) #Keys are each character, values are index position
        count2[character] = count2[character] + 1
        #Counts number of times a character appears

print(count2)   
pprint.pprint(count2)
begintext = pprint.pformat(count2) #creates a String of the pretty print
print(begintext)
