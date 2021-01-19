from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.fr/Lazuli-Halt%C3%A8re-Bracelet-rhodium-Fitness/dp/B01MS1F3MX/ref=sr_1_3_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=bracelet&qid=1605990252&s=jewelry&sr=1-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRzQzUTkwQU9YMUlBJmVuY3J5cHRlZElkPUEwOTU4MTIyMURQUkM4TFhEU1RJRSZlbmNyeXB0ZWRBZElkPUEwNzY5NDY2RldWMjZGV1YzUTZFJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

req = requests.get(url)

soup = BeautifulSoup(req.text, "lxml")

found = soup.findAll('input')

print(type(found))

#content est une liste de tag matchés
#print(found[0].contents[0].contents[0])