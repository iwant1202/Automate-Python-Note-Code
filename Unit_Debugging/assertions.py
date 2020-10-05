market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)
    #I assert that this is true -- if it is not, something is going wrong
    #Do not use try & except, should fail quick
    #User errors should raise exceptions
    
    #Makes sure that at least one light is red
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

assert False, 'This is the error message.'
#If the value is false, it returns an error
