for i in [0, 1, 2, 3 ]: #runs program with i=0, i=1, etc...
	print(i)
print(list(range(4))) #creates a list 0 to 4
print(list(range(0, 100, 2))) #creates a list 0-100, incrementing by 2

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)): # common code, goes through a list
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
# Inefficient method of assigning variables to list
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat # efficient assigning method
size, color, disposition = 'skinny', 'black', 'quiet' # used often to swap

a = 'AAA'
b = 'BBB'
print(a + b)
a, b = b, a #swapping variables
print(a +b)
spam = 42
spam = spam + 1
spam += 1#Augmented assignment operators, for all operations
print(str(spam))
