import csv
liste = [65,14,22,101,10,9,18,71]
liste = 0
def get_max(liste):
    try:
        #if not isinstance(liste,list):
        raise TypeError("erreur")
        max = liste[0]
        for x in liste:
            if(max < x):
                max = x
        return max
    except:
        print("except get_max")


def test(liste):
    try:
        return get_max(liste)
    except Exception as e:
        print(e)

test(liste)