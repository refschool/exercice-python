from random import randint
""" generation d'un  texte"""
seed = "abcdefghijklmnopqrstuvwxyz "
length = 2000
manuscrit = ""
while(len(manuscrit) < length):
    """ bien fait de mettre un len(seed) -1 car on a  ajouté un espace après"""
    i = randint(0,len(seed)-1)
    manuscrit += seed[i]


""" insertion du message à coder"""
message = "https://formapedia.com/fort-knox.jpg        "
last=0
for lettre in message:
    manuscrit = list(manuscrit)
    manuscrit[last] = lettre
    manuscrit = ''.join(manuscrit)
    last = last + 11

print(manuscrit)