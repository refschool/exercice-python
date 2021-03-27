def repetition(c,k):
    phrase = ""
    for i in range(1,k+1):
        phrase += c
    return phrase


def alterne(c):
    if c == "0":
        return "1"
    else:
        return "0"

def demyst(liste):
    chaine = ''
    c = "0"
    for i in liste:
        chaine += repetition(c,i)
        c = alterne(c)

    return chaine



liste = [3, 2, 1, 3]
print(demyst(liste))