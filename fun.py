from pprint import pprint
liste = ['t','e','d','e','i']


""" abc,acb,bac,bca,cab,cba  3!"""
s = set()
for i in range(0,5):
    for j in range(0,5):
        if(j == i):
            continue
        for k in range(0,5):
            if(k in [i,j]):
                continue
            for l in range(0,5):
                if(l in [i,j,k]):
                    continue
                for m in range(0,5):
                    if(m in [i,j,k,l]):
                        continue
                    s.add((i,j,k,l,m))

mots = []
for tuple in s:
    str = ''
    for x in tuple:
        str += liste[x]
    mots.append(str)
mots.sort()
pprint(mots)