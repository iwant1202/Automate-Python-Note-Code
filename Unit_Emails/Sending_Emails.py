import smtplib
#Simple mail transfer protocol library

conn = smtplib.SMTP('smtp.gmail.com', 587)
#first param is domain name
#Second param is port number, usually 587
print(type(conn))
print(conn)

conn.ehlo()
#Starts connection, the "hello" function
#Returns response code, anything 2XX is good
#byte objects start with a b

conn.starttls()
#Start TLS encryption
#most modern email services require encryption

conn.login('automaticemailsender73@gmail.com', 'violet_light_and_a_hum')
#Username, password
#Might need to generate app specific password

conn.sendmail('autmaticemailsender73@gmail.com', 'autmaticemailsender73@gmail.com', ''+\
'Subject: So long...\n\nDear Nick, \nSo long, and thanks for' +\
              'all the fish.\n\n-Nick')
              
#First param is the sender, second is the reciever, third is message
#Need to make emails accept low-trust apps

conn.quit()
#Disconnects
