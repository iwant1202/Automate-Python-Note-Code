name = 'Alice'
place = 'Main street'
time = '6 pm'
food= 'turnips'
invitation = 'Hello ' + name + ' you are invited ot a party at ' +\
       place + ' at ' + time + ' Please bring ' + food
print(invitation)

betterInvitation = 'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
#Replace %s with corresponding strings
print(betterInvitation)

