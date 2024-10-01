from bs4 import BeautifulSoup
import requests


url = 'https://www.creatissus.com/tissu-eponge-de-bambou-ecru/'

url = 'https://www.creatissus.com/lingettes-lavableslingettes-demaquillantes/'
req = requests.get(url)


soup = BeautifulSoup(req.text, "html.parser")


found = soup.find_all('p',class_= "price")
print(found[0].contents[0].contents[0])

print(found[0].contents[0].contents[0])

"""
2,50<span class="woocommerce-Price-currencySymbol">€</span>


['2,50', <span class="woocommerce-Price-currencySymbol">€</span>]
"""
