"""  1-parcourir le texte ligne par ligne """


with open("lyrics.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def obtenir_dernier_mot(toto):
    print(toto)

for vers in lines:
    obtenir_dernier_mot(vers)