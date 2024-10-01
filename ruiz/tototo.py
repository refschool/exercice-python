#variable

prenom3 = "Bob"
prenom = "pablo"
# afficher dans la console le contenu de la variable prenom
#print("bonjour " + prenom) #concatenation

prenom = "Jesus" # chaine de caractère String
#print(prenom)
#type : la nature de la donnée contenue dans une variable
age1 = 15 # nombre donc le type est Integer
age2 = "15" #
somme = age2 + str(1)
#print(somme)

#les chaines et manipulation de chaines (string manipulation)
chaine = "Une chaine de caractères"
chaine2 = 'apostrophe'
#phrase = chaine + age
#print(type(chaine))
#la fonction print est utilisé en phase de développement (pour le débuggage)
# concaténation, et multiparamètre

#concaténation avec la fonction print()
print("bonjour " + "Pablo")
#multiparamètre
print("bonjour","Pablo") #la fonction print prend 2 paramètres (ou argument)
print("comment","allez","vous?")

#les f-string
age = 17
#print("Bonjour j'ai " + str(age) + " ans")
#print(f"Bonjour j'ai  {age}  ans")
txt ="Bonjour j'ai {} ans"

print(txt.format(age))

# les objets, en python tout est objet
# fonction strip
mavar = "   beaucoup d'espace       "


#print(mavar)

#opérateur modulo donne le reste de la division euclidienne
# division classique : 5/2=2.5
# division euclidienne : 5 / 2 = 2 + 1(reste)

for i in range(0,10):
    #print(i % 3)
    pass

#opérateur de comparaison
# ==, !=, >=,>,<,<=,
#print("🍔" == "🍔")
"""prenom2 = "Jules"
print(prenom2 == "jules") # la casse  (majuscule ou minuscule) sensibilité à la casse

print(prenom2.lower() == "jules")
print(5 > 10)"""
#!!!   faire la différence entre = et ==
#= pour affection (càd on donne une valeur à une variable)
#==  c'est une comparaison

print('comparaison',prenom3 == "Alice")
#if ... else
# ce qui est dans les parenthèses c'est une instruction de comparaison
# dont le résultat vaut True ou False
if(prenom3 == "Alice"): # comparaison
    '''si le résulata vaut True on exécute le code de ce bloc'''
    print("vous êtes bien Alice")
else:
    '''si le résultat vaut False on exécute le code de ce bloc'''
    print("vous n'êtes pas Alice")


""" !!! on n'est pas obligé de mettre une comparaison dans la condition"""
""" notion de valeur truthy ou falsy"""
""" 0 (zéro) est considéré comme falsy (assimilé faux (dans une expression de comparaison bien sûr !)"""
temperature = input("Entrez une valeur pour meteo :")
print("type : ",type(int(temperature)))
#si temperature > 30°, affichez "Canicule", sinon afficher il fait bon
#si < 15 il fait froid
if(30 > 30):
    print("canicule")
else:
    print("il fait bon")




