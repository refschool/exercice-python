import requests
import matplotlib.pyplot as plt
from datetime import datetime
""" 2021-07-31 20:43:11.323161"""
#datetime.now()
"""  1, 5, 15, 30, 60, D, W, M  """
resolution = '60'


sandbox_api = 'sandbox_c2sjvm2ad3ic1qis2cr0'
apikey = 'c2sjvm2ad3ic1qis2cqg'
key = apikey
base_url = "https://finnhub.io/api/v1/"


start = '25/07/2021'
end = '31/07/2021'

start= int(datetime.strptime(start,'%d/%m/%Y').timestamp())
end = int(datetime.strptime(end,'%d/%m/%Y').timestamp())
url = f"crypto/candle?symbol=BINANCE:SUSHIUSDT&resolution={resolution}&from={start}&to={end}"
final_url = base_url + url+f'&token={key}'
print(final_url)
r = requests.get(f'{base_url}{url}&token={key}')
object = r.json()
candle = dict()
candle['o'] = object['o']
candlepercent = []


candle['h'] = object['h']
candle['l'] = object['l']
candle['c'] = object['c']
candle['t'] = object['t']
for i in range(0,len(candle['o'])-1):
    p = (  (candle['o'][i+1] - candle['o'][i]) /candle['o'][i] * 100)
    p = round(p,2)
    print('p',p,candle['o'][i+1] ,'-', candle['o'][i])
    candlepercent.append(p)


candle['v'] = object['v']
""" x first then y if two arrays are provided"""

#candle['t'] = [ datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') for t in object['t']]
candle['t'] = [ datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H-%M-%S') for t in object['t']]




print(len(candle['t']))
print(len(candle['o']))
fig = plt.figure(figsize=(18,8))
ax1 = fig.add_subplot(111)
ax1.set_ylabel('y1')
ax1.plot(candle['t'],candle['o'],'b')


ax2 = ax1.twinx()
ax2.plot(candle['t'][:len(candle['t'])-1],candlepercent,'r',marker='o')


plt.ylabel('%')
plt.xlabel('Time')
plt.gcf().autofmt_xdate()
plt.grid()

plt.xticks(candle['t'][:len(candle['t'])-1][::5])
plt.show()