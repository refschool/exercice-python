import requests
import matplotlib.pyplot as plt
from datetime import datetime
""" 2021-07-31 20:43:11.323161"""
#datetime.now()
"""  1, 5, 15, 30, 60, D, W, M  """



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
start = '01/07/2021'
end = '31/07/2021'

start= int(datetime.strptime(start,'%d/%m/%Y').timestamp())
#test = datetime.utcfromtimestamp(int(start)).strftime('%Y-%m-%d %H:%M:%S')
#print(test)
end = int(datetime.strptime(end,'%d/%m/%Y').timestamp())
url = f"crypto/candle?symbol=BINANCE:BTCUSDT&resolution=D&from={start}&to={end}"
final_url = base_url + url+f'&token={key}'
print(final_url)
r = requests.get(f'{base_url}{url}&token={key}')
object = r.json()
candle = dict()
candle['o'] = object['o']
candlederiv = []


candle['h'] = object['h']
candle['l'] = object['l']
candle['c'] = object['c']
candle['t'] = object['t']
for i in range(0,len(candle['o'])-1):
    d = (candle['o'][i+1] - candle['o'][i])
    print('d',d,candle['o'][i+1] ,'-', candle['o'][i])
    candlederiv.append(d)


candle['v'] = object['v']
""" x first then y if two arrays are provided"""

#candle['t'] = [ datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') for t in object['t']]
candle['t'] = [ datetime.utcfromtimestamp(t).strftime('%Y-%m-%d') for t in object['t']]

fig = plt.figure(figsize=(18,8))
ax1 = fig.add_subplot(111)
ax1.set_ylabel('y1')
ax1.plot(candle['t'],candle['o'],'b')

ax2 = ax1.twinx()
ax2.plot(candle['t'][:len(candle['t'])-1],candlederiv,'r',marker='o')
plt.ylabel('USD')
plt.xlabel('Time')
plt.gcf().autofmt_xdate()
plt.grid()
plt.show()