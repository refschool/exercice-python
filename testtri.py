liste = []

if len(liste) == 0:
    print("kaput")
else:
    max = liste[0]
    for nombre in liste:

        if max > nombre:
            max = max
        if max < nombre:
            max = nombre

    print(max)

"""
if max > liste[0]:
    max = max
if max < liste[0]:
    max = liste[0]

print(max)

if max > liste[1]:
    max = max
if max < liste[1]:
    max = liste[1]

print(max)

if max > liste[2]:
    max = max
if max < liste[2]:
    max = liste[2]

print(max)
"""