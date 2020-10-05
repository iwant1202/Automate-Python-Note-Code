import bs4, requests

def getSteamPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#game_area_purchase > div:nth-child(2) > div > div.game_purchase_action > div > div.discount_block.game_purchase_discount > div.discount_prices > div.discount_final_price')
    return elems[0].text.strip()
price = getSteamPrice('https://store.steampowered.com/app/550/Left_4_Dead_2/')
print('The price is ' + price)
