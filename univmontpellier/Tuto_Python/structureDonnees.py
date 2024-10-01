#liste contiennet des choses homogènes
maliste = [1,2,3,4,5,6,7,8,9,10]
listeNom = ["dupont"]

# la vie sans les listes
nom1 = "dupont"
nom2 = "durant"
# etc


mescommandes = [
[150,"2020-10-15","LecteurMP3"],
[1150,"2020-10-16","Iphone"],
[15,"2020-10-17","Etui"]
]

"""
Produit         Prix        Date
====================================
LecteurMP3      150         "2020-10-15"
Iphone          1150        "2020-10-15"
Etui            15          "2020-10-15"
"""
print("Produit         Prix        Date")
print('====================================')
"""for commande in mescommandes:
    print(commande[2], commande[0], commande[1])"""



#dictionnaire cle:valeur
mescommandes = [
    {
    "Produit":"LecteurMP3",
    "Date":"2020-10-15",
    "Prix":'150'
},
    {
    "Produit":"Iphone",
    "Date":"2020-10-16",
    "Prix":'1150'
},
    {
    "Produit":"Etui",
    "Date":"2020-10-17",
    "Prix":'15'
}
]

for commande in mescommandes:
    print(commande['Produit'], commande['Prix'], commande['Date'])