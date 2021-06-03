L3 = ["le", "loup", "est", "un", "loup", "pour",
"le", "loup"]

L2 = ["l’", "homme", "est", "un", "loup", "pour",
"l’", "homme"]

L1 = ["et", "jamais", "je", "ne", "pleure", "et", "jamais",
"je", "ne", "ris"]

L4 = ["un", "homme", "vit", "une", "couleuvre"]
L5 = ["vous", "pleurates", "ma", "mort", "helas", "trop",
"peu", "certaine"]


def occurence(liste):
    annuaire = {}
    """construction du dico"""
    for mot in liste:
        if mot in annuaire:
            annuaire[mot] += 1
        else:
            annuaire[mot] = 1

    return annuaire


def hapax(liste):
    unique = set()
    annuaire = occurence(liste)
    for cle in annuaire:
        if annuaire[cle] == 1:
            unique.add(cle)
    return unique

def frequences(liste):
    annuaire = occurence(liste)
    total_mot = len(liste)
    for cle in annuaire:
        annuaire[cle] = round(annuaire[cle] / total_mot * 100,1)
    return annuaire


def union_frequences(D1, D2, l1, l2):
    """ DFreq * DFreq * int * int -> DFreq
    Hypothese: l1 >= 0 and l2 >= 0 and l1 + l2 > 0"""
    # D : DFreq
    D = dict()
    # e1 : str
    for e1 in D1:
        D[e1] = D1[e1] * l1 / (l1 + l2)
    # e2 : str
    for e2 in D2:
        if e2 in D:
            D[e2] = D[e2] + D2[e2] * l2 / (l1 + l2)
        else:
            D[e2] = D2[e2] * l2 / (l1 + l2)
    return D


def compare(dicoD,dicoA):
    score = 0
    for mot in dicoD:
        if mot in dicoA:
            score += abs(dicoD[mot] - dicoA[mot])
        else:
            score += 100

    return score




def compare(D1, D2):
    """ DFreq * DFreq -> float """
    # score: float
    score = 0
    for (m1,f1) in D1.items():
        if m1 in D2:
            score = score + abs(f1 - D2[m1])
        else:
            score = score + 100
    return score



dicoLaFontaine = {"homme": 30, "loup": 20, "agneau": 10, "cigale": 10,
"fourmi": 10, "renard":10, "couleuvre": 10}
dicoRacine = {"helas": 50, "appas": 10, "transport": 10, "mort" : 10 ,
"coeur": 20}

f4 = frequences(L4)
print(compare(f4,dicoLaFontaine))