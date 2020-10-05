import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
#res stores an Object(response the web server gives)

print(res.status_code)
#404, file not found
#200, all good
len(res.text)
print(res.text[:500])

playFile = open('RomeoAndJuliet.txt', 'wb')
#Write in binary, to maintain unicode

for chunk in res.iter_content(100000):
    #iter_content returns chunks of bytes. How many bytes each chunk contains
    playFile.write(chunk)
playFile.close()
res.raise_for_status()
#returns nothing if all good
#badRes = requests.get('https:\\google.com\badbadslkdfaljk')
#badRes.raise_for_status()
#Returns exception when not found
