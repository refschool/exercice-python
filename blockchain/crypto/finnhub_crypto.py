import requests
sandbox_api = 'sandbox_c2sjvm2ad3ic1qis2cr0'
apikey = 'c2sjvm2ad3ic1qis2cqg'
key = apikey
base_url = "https://finnhub.io/api/v1/"

"""
url ="crypto/exchange"
r = requests.get(f'{base_url}{url}?token={key}')
print(r.json())


url = "crypto/symbol?exchange=binance"
r = requests.get(f'{base_url}{url}&token={key}')
print(r.json())
"""

start='1625159977'
end='1627665577'
url = f"crypto/candle?symbol=BINANCE:BTCUSDT&resolution=D&from={start}&to={end}"
final_url = base_url + url+f'&token={key}'
print(final_url)
r = requests.get(f'{base_url}{url}&token={key}')
object = r.json()
candle = dict()
candle['o'] = object['o']
candle['h'] = object['h']
candle['l'] = object['l']
candle['c'] = object['c']
candle['t'] = object['t']
candle['v'] = object['v']

print(len(candle['v']))
print(len(candle['o']))
