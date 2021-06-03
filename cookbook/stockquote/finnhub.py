import requests
apikey = ''
# Register new webhook for earnings
r = requests.post('https://finnhub.io/api/v1/webhook/add?token='+apikey, json={'event': 'earnings', 'symbol': 'AAPL'})
res = r.json()
print(res)

webhook_id = res['id']
# List webhook
r = requests.get('https://finnhub.io/api/v1/webhook/list?token=')
res = r.json()
print(res)

#Delete webhook
r = requests.post('https://finnhub.io/api/v1/webhook/delete?token=', json={'id': webhook_id})
res = r.json()
print(res)