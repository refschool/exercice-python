try :
    liste = [1,2,5,3]
    print(liste[6])
except IndexError:
    print("L'index 6 n'est pas présent")
print("Je suis encore vivant")




"""t = input("entrez un  nombre ")
try:
    t = int(t)
    print(t + 2)
except ValueError:
    print("erreur sur la valeur")
except Exception:
    print("Erreur générale")"""