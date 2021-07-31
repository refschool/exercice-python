import requests
sandbox_api = 'sandbox_c2sjvm2ad3ic1qis2cr0'
apikey = 'c2sjvm2ad3ic1qis2cqg'
key = apikey

ticker = 'AAPL'

r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={key}')
print(r.json())







"""
# Register new webhook for earnings
r = requests.post('https://finnhub.io/api/v1/webhook/add?token='+key, json={'event': 'earnings', 'symbol': 'AAPL'})
res = r.json()
print(res)

webhook_id = res['id']
# List webhook
r = requests.get('https://finnhub.io/api/v1/webhook/list?token='+key)
res = r.json()
print(res)

#Delete webhook
r = requests.post(f'https://finnhub.io/api/v1/webhook/delete?token={key}', json={'id': webhook_id})
res = r.json()
print(res)
"""