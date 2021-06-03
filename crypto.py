from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json

APIKEY = "2b660bde-a5ee-4ea6-b3f5-f7ff33e83685"

cmc = CoinMarketCapAPI(APIKEY)

#r = cmc.cryptocurrency_info(symbol='BTC')
response = cmc.cryptocurrency_listings_latest()

latest = list(response.data)

for crypto in list(latest):
    print(crypto)