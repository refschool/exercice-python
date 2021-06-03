"""# 1er cas de sortie 0 tour
pic_suivant([2,3],3)

# 1er cas de sortie 1 tour
pic_suivant([2,4],0)

# 2eme cas de sortie 0 tour
pic_suivant([9,8],0) #

# 2eme cas de sortie 1 tour
pic_suivant([8,9],0)
"""
def pic_suivant(L,i):
    j = i
    while j < len(L) -1 and L[j] < L[j+1]:
        j = j + 1
    return j


L = [1,6,2,3,7,5,0,4,6,8]
sL = [4,6,8]


def fond_suivant(L,i):
    j = i
    while j < len(L) -1 and L[j] > L[j+1]:
        j = j + 1
    return j

def sous_liste_alternee(L):
    LR = [L[0]]
    montee = L[0] < L[1]
    i=0
    while i < len(L) - 1:
        if montee:
            i = pic_suivant(L, i)
        else:
            i = fond_suivant(L, i)
        LR.append(L[i])
        montee = not(montee)
    return LR

res = sous_liste_alternee([3,1,10,8,4,5,6,7,0,3,4])



'A1affrDg'

def test_lg(str):
    if len(str) >= 6:
        return True
    return False


def test_maj(char):
    if 65 <= ord(char) <= 90:
        return True
    return False

def test_min(char):
    if 97 <= ord(char) <= 122:
        return True
    return False


def test_initiale(str):
    if(test_maj(str[0])):
        return True
    return False

print(test_initiale('Abc2def'))
def test_chiffre(c):
    pass

def test_1chiffre(str):
    for c in str:
        if(test_chiffre(c)):
            return True
    return False

# 97 et 122 minuscule
# 65 et 90 majuscule
print(ord('A'))
def remplacement(str):
    mot = ''
    for c in str:
        if not(test_maj(c) or test_min(c) or c.isdigit()):
            mot = mot + 'a'
        else:
            mot = mot + c
    return mot

print(remplacement('Axx1xx#?'))

float('20.15a')