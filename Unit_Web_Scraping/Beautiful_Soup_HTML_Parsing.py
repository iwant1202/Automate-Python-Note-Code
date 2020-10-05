import bs4, requets
res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_2?crid=2J7SFZ5O30RR&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1601262731&s=books&sprefix=automate+the+%2Caps%2C158&sr=1-2')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Saves a beautiful soup object
#brings up a warning that no specific parser was mentioned
#Does not break

#Use inspect element to see what contains the price
elems = soup.select('#price')
elems[0].txt # prints out the text
elems[0].text.strip() #Returns something without white space
