try:
    index = input("Entrez un index")
    print(type(index))
    liste = [1, 2, 5, 3]
    print(liste[int(index)])
except IndexError:
    print('devinez quelle exception a été levée?')
except TypeError:
    print('Convertissez en int index')
except Exception:
    print("Exception générale")
