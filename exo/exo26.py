import csv
with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv

f = open('../test.csv', 'r')
for line in f.readlines():
    liste = line.split(',')
    print(liste[1], liste[0], liste[2], liste[3])

"""    ['Yvon', 'Huynh', '45', 'Toulouse\n']
    ['Jean', 'Dupont', '34', 'Paris\n']
    ['Fabien', 'Martin', '35', 'Lyon\n']
    ['Elodie', 'Cartier', '33', 'Tours\n']
    faire la phrase : yvon huynh a 45 ans et vit à toulouse

    """