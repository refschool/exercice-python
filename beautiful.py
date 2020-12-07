from bs4 import BeautifulSoup
import requests



req = requests.get('https://www.creatissus.com/tissu-eponge-de-bambou-ecru/')

soup = BeautifulSoup(req.text, "html.parser")

#print(soup.title.contents[0])

found = soup.find_all('p',class_= "price")

print(found[0].contents[0].contents[0])