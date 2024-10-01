

letsgo = True
while(letsgo):
    t = input("taille cm")
    p = input("poids")
    """on peut calculer"""
    if(t.isdigit() and p.isdigit() ):
        t = int(t)
        p = int(p)
        t = t /100
        IMC = p/(t*t)
        print(IMC)
    else:
        print("recommencez")
