import imapclient, pyzmail, datetime
#(internet message access protocol)

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#want to use ssl encryption

conn.login('automaticemailsender73@gmail.com', 'violet_light_and_a_hum')
#returns byte object that can be seen as string, confirms success

conn.select_folder('INBOX', readonly=True)
#Makes sure cannot accidentally edit


UIDs = conn.search(['SINCE', datetime.date(2015, 8, 3)])
#This is not in the course, but works
#suggests   (['SINCE 20-Aug-2015')]
#Special imap syntax
print(UIDs)
#Returns all emails recieved since Aug 3, 2015
#Not that many, email created couple of days ago
#Also have 'ALL', 'BEFORE', 'ON'...

rawMessage = conn.fetch([1], ['BODY[]', 'FLAGS'])
#has all info about email
#First argument is the UID, second is what to get from that email
print(rawMessage)

message = pyzmail.PyzMessage.factory(rawMessage[1][b'BODY[]'])
#returns a pyzmail object

print(message.get_subject())
print(message.get_addresses('from'))
#returns list string with Name and then email address
print(message.get_addresses('to'))

print(message.get_addresses('bcc'))

print(message.text_part)
#If set to none, means no text part
print(message.html_part)
#If set to none, means no html part

print(message.text_part.get_payload().decode('UTF-8'))
#Could be encoded as something different, usually UTF-8

print(message.text_part.charset)
#returns the type of coding, usually UTF-8

print(conn.list_folders())
#Returns tuble list of folders, name third tuple

conn.select_folder('INBOX', readonly=False)

UIDs = conn.search(['SINCE', datetime.date(2015, 8, 3)])
#conn.delete_messages([2})
    #Deletes the UID passed
#conn.delete_messages(UIDs)
    #deletes everything in UID list
#conn.delete_messages([1, 2, 3, 4])

