from bs4 import BeautifulSoup


fichier = "example.html"
handler = open(fichier,encoding="utf-8")

soup = BeautifulSoup(handler, "html.parser")

found = soup.find_all('p')

#print(soup.title.contents[0])

var = found[2].contents[0].strip()
list = var.split(' ')
#print(list)
print(list[0])

#variante
"""url = "example.html"
page = open(url)
soup = BeautifulSoup(page.read())"""