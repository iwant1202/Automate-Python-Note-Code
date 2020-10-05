import logging
logging.basicConfig(filename = 'MyProgramLog.txt', level=logging.DEBUG, format= '%(asctime)s - ' +\
                    '%(levelname)s - %(message)s')

        #Filename makes it so that it writes all log messages to text file
#Logs bugs
#Provide timestamp, DEBUG log level, print out
#logging.disable(logging.CRITICAL)
    #Disables all log messages, CRITICAL and lower
    #All, since CRITICAL is highest level
#log levels
    #5 levels lowest to highest
    #DEBUG lowest level
    #CRITICAL highest level
    #DEBUG, INFO, WARNING, ERROR, CRITICAL


#Buggy factorial program
    #Fac(7) = 7*6*5*4*3*2*1

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i #Multiplying by 0
        logging.info('i is %s, total is %s' % (i, total))
            #Higher level
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program')
