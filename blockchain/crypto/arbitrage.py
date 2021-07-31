from bs4 import BeautifulSoup
import requests


url1 = "https://www.huobi.com/en-us/markets/?tab=exchange"
req = requests.get(url1)

soup = BeautifulSoup(req.text, "lxml")
print(soup)
#found = soup.findAll('input')