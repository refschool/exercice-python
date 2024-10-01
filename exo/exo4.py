# déclaration des "constantes"
IMC_inf = 18.5
IMC_sup = 25
Message_Prenom = 'Nous allons procéder au calcul de votre IMC. Veuillez saisir votre PRENOM '
Message_Poids = 'Quel est votre poids exprimé en kg (ex: 70) ? '
Message_Taille = 'Quel est votre taille exprimée en cm (ex: 175) ? '
Message_Saisie_ko = 'Saisie incorrecte'
Message_IMC = 'Votre IMC est '
Message_bravo = 'Bravo votre IMC est correct; il se situe entre 18,5 et 25'
prenom_poids = ''
prenom_taille = ''

# saisie user
prenom = input(Message_Prenom)
print('Bonjour ' + prenom)

while not prenom_poids.isdigit():
    prenom_poids = input(Message_Poids)

prenom_poids = int(prenom_poids)

while not prenom_taille.isdigit():
    prenom_taille = input(Message_Taille)

prenom_taille = int(prenom_taille)


# calcul IMC_value
IMC_value = prenom_poids / (( prenom_taille / 100)**2)


print(Message_IMC + str(IMC_value))
# IMC_value ok or ko
if  IMC_inf <= IMC_value <= IMC_sup :
    print(Message_bravo)
else :
    print('Votre IMC devrait se situer entre 18,5 et 25. \r\nVous devriez manger plus sainement et faire plus de sport...')

