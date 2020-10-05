import traceback
"""
***************
*             *
*             *
*             *
***************
"""
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    #traceback.format_exc() returns a String of the error message
    errorFile.close()
    print('The traceback info was written error_log.txt')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a length of one"')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than or equal to 2')
    print(symbol * width)
    for i in range(height-2): #Top and bottom row included in height
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)
boxPrint('*', 15, 5)
boxPrint('**', 15, 5) #Bug, not working as anticipated
        


#Whole error message is called a Traceback
raise Exception('This is the error message.')

