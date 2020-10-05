
print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)
#Not an explicit error, but prints them as digits
#Turn on debugger in shell

#Over executes current highlighted line, highlights next line
    #"Step-Over"
#Go runs program normally
#Step moves debugger into function call
    #"Step-In"
#Out keep executing lines until current function returns
    #"Step-Out"
#Quit terminates program

def blahBlahBlah():
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    #Right-click, set breakpoint, the code will now stop when pressing Go
    #on debugger
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')
    moreBlah()
    print('blah')
    print('blah')
    print('blah')
    moreBlah()

def moreBlah():
    print('more blahs')
    print('more blahs')
    print('more blahs')
blahBlahBlah()
