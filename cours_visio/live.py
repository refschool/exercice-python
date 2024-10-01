def test(liste,index):
    if isinstance(liste,list) == False:
        raise Exception("Veuillez entrer une liste")
    try:
        print(liste[index])
        print("si vous me lisez il n'y a pas eu de problème")
    except Exception as e:
        print("cast Exception : ",e)
    except TypeError:
        print("Je ne suis pas une chaine de caractères.. erreur déclenchée !")
    except IndexError:
        print("Je suis hors index...gros problème")





liste = [1,2,3]
index = "2"
test(liste,index)