"""liste = ['*','***','*****','*******','*','*']

espaces = [3,2,1,0,3,3]

for i in range(len(liste)):
    texte = ' ' * espaces[i] + liste [i]
    print(texte)"""


liste = ['*','***','*****','*******','*','*']

for i in range(len(liste)):
    print(liste[i].center(len(liste)+1))