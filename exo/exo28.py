#class Personne

class Personne :
    def __init__(self,nom,prenom,mail):
        self.nom=nom
        self.prenom=prenom
        self.mail=mail
    def saluer (self) :
        return "Bonjour, comment allez-vous" + self.prenom + self.nom


people1= Personne("HENRY","Jean-joseph","henry_jj@yahoo.fr")

print("methode methode de class : ")
print (people1.saluer())



