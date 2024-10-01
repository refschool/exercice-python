apikey = 'ff520c1417918c34daee6be726d4ae707332bcca'
import requests,pprint

url = f"https://api.nomics.com/v1/markets?key={apikey}&exchange=binance&base=BTC,ETH,LTC,XMR&quote=BTC,ETH,BNB"
#url = f"https://api.nomics.com/v1/currencies/ticker?key={apikey}&ids=BTC,ETH&interval=1h,30d&convert=USD&per-page=100&page=1"
r = requests.get(url)

pprint.pprint(r.json())