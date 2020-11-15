from bs4 import BeautifulSoup
import requests

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://code.tutsplus.com/fr/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211

req = requests.get('https://www.creatissus.com/tissu-eponge-de-bambou-ecru/')

soup = BeautifulSoup(req.text, "lxml")

#print(soup.title.contents[0])

found = soup.find_all('p',class_= "price")

print(found[0].contents[0].contents[0])