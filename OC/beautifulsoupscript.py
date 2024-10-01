import requests
from bs4 import BeautifulSoup
import csv

def clean_data(data):
     # Supprimer les caractères de nouvelle ligne, les espaces en excès et les caractères spéciaux
    cleaned_data = data.strip().replace('\n', '').replace('\r', '').replace('\t', '')
    return cleaned_data
# Fonction pour extraire les informations de la page produit
def extract_product_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    #soup = BeautifulSoup(input, "html.parser")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraire les informations nécessaires
    product_page_url = url
    upc = soup.select('th')[0].find_next('td').text
    title = soup.h1.text
    price_including_tax = soup.select('th')[3].find_next('td').text
    price_excluding_tax = soup.select('th')[2].find_next('td').text
    number_available = soup.select('th')[5].find_next('td').text
    product_description = soup.find('meta', attrs={'name': 'description'})['content']
    category = soup.select('a')[3].text
    review_rating = soup.select('p')[2]['class'][1]
    image_url = soup.select('img')[0]['src']

    return {
        "product_page_url": product_page_url,
        "upc": upc,
        "title": title,
        "price_including_tax": price_including_tax.replace('Â',''),
        "price_excluding_tax": price_excluding_tax.replace('Â',''),
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url
    }

# URL de la page produit que vous souhaitez extraire
product_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Appeler la fonction pour extraire les informations
product_info = extract_product_info(product_url)

# Vérifier si les informations ont été extraites avec succès
if product_info:
    # Écrire les données dans un fichier CSV
    with open('uneseulepage2.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = product_info.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(product_info)
    print("Données extraites avec succès et enregistrées dans uneseulepage2.csv")
else:
    print("Impossible d'extraire les données de la page produit.")