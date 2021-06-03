import requests


url = "https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=f1739d80d7f0995ce57277d5861a6566"

req = requests.get(url)


print(req.json())