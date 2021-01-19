from bs4 import BeautifulSoup
import requests


url = 'https://www.creatissus.com/tissu-eponge-de-bambou-ecru/'
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")


found = soup.find_all('p',class_= "price")
print(found[0].contents[0].contents[0])


#print(found[0].contents[0].contents[0])

