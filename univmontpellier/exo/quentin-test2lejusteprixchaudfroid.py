import random
valeurmax = int(input("Entrez un nombre pour définir l'intervalle : "))
nm = random.randint(1,valeurmax)
NbrTentative=0
Str_valeurmax = str(valeurmax)
DerniereTentative = None
DistanceActuelle = None
DistancePrecedente = None

Tentative = int(input("Devinez le nombre mystère (1-" + Str_valeurmax +") : "))
    

while Tentative != nm:
    NbrTentative= NbrTentative+1

    if DerniereTentative is not None :
        DistanceActuelle = abs(nm - Tentative)
        DistancePrecedente = abs(nm - DerniereTentative)

        #print("DistanceActuelle",DistanceActuelle)
        #print("DistancePrecedente",DistancePrecedente)

        if DistanceActuelle <= DistancePrecedente:
            print("chaud")
            DerniereTentative = Tentative
            Tentative = int(input("Devinez le nombre mystère (1-" + Str_valeurmax +") : "))
            
        else :
            print("froid")
            DerniereTentative = Tentative
            Tentative = int(input("Devinez le nombre mystère (1-" + Str_valeurmax +") : "))
            
    else :
        DerniereTentative = Tentative
        Tentative = int(input("Entrez un deuxième nombre pour savoir si vous êtes chaud ou froid (1-" + Str_valeurmax +") : "))

#sorti de while if true
NbrTentative= NbrTentative+1        
print("Bien ouej après", NbrTentative, "tentatives")