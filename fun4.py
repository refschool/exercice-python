#
liste1 = ['r','e','i','n']
liste2 = ['r','e','i','n']
liste3 = ['r','e','i','n']

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
                s.add((i,j,k,l))


for tuple in s:
    str = ''
    for x in tuple:
        str += liste1[x]
    print(str)