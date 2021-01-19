import requests

#https://www.nylas.com/blog/use-python-requests-module-rest-apis/


apikey = 'f1739d80d7f0995ce57277d5861a6566'
city = 'Londres'
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey

response = requests.get(url)

#print(response.content)
#print(response.text)
#print(response.json())
print(response.headers)


"""# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})"""

