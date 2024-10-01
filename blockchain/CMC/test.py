from bs4 import BeautifulSoup
import requests
import time
token = {
'ohm':{'url' : "https://coinmarketcap.com/currencies/olympus/",},
'voice':{'url' : "https://coinmarketcap.com/currencies/nix-bridge-token/"},
'joe':{'url' : "https://coinmarketcap.com/currencies/joe/"},
'sin':{'url' : "https://coinmarketcap.com/currencies/sincity-token/"},
'noia':{'url' : "https://coinmarketcap.com/currencies/syntropy/"},
'vnla':{'url' : "https://coinmarketcap.com/currencies/vanilla-network/"},
'mlt':{'url' : "https://coinmarketcap.com/currencies/milc-platform/"},

}
token_list = ['sin','ohm','voice','joe','noia','vnla','mlt']

for t in token_list:
    req = requests.get(token[t]['url'])
    soup = BeautifulSoup(req.text, "lxml")
    found = soup.findAll('div',class_="priceValue")
    price = found[0].contents[0][1:]
    print(t.upper(),'@',price)

    time.sleep(0.75)




