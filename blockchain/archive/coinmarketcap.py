from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json
import numpy as np

APIKEY = "2b660bde-a5ee-4ea6-b3f5-f7ff33e83685"

cmc = CoinMarketCapAPI(APIKEY)

#r = cmc.cryptocurrency_info(symbol='BTC')
response = cmc.cryptocurrency_listings_latest()

latest = list(response.data)
arr = []
for crypto in list(latest):
    quote = crypto['quote']['USD']
    liste = [crypto['name'], float(quote['percent_change_1h']),float(quote['percent_change_24h']),float(quote['percent_change_7d'])]
    arr.append(liste)
''' plus rapide de convertir la liste en array '''
np_arr = np.array(arr,dtype='object')

"""for crypto in list(latest):
    print(crypto['id'],crypto['name'],crypto['quote'])"""

"""
{'price': 31844.873093123057, 'volume_24h': 18276287717.518513, 'percent_change_1h': 0.37411178, 'percent_change_24h': 1.4830346, 'percent_change_7d': -5.76745594, 'percent_change_30d': -15.65053106, 'percent_change_60d': -18.20391267, 'percent_change_90d': -44.1877872, 'market_cap': 597399851781.7104, 'last_updated': '2021-07-18T12:05:02.000Z'

"""
b = np_arr[np.argsort(np_arr[:,2])]
b = b[::-1]
print(b[:50])
