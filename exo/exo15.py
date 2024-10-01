try:
    liste = [1,2,5,3]
    x= int(input('entrez un chiffre:'))
    print(liste[x])
except IndexError:
    print('index hors liste')
except ValueError as e:
    print('Entrez un chiffre !',e)

"""
#transmission d'exception    

def test(a):
    if a== 5:
        raise Exception("Exception de Test")

def main(a):
    try:
        test(a)
    except Exception as e:
        print("exception",e)
main(5)
    
    """