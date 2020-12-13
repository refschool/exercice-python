class UtilisateurOld:
    def __init__(toto,name,age):
        toto.name = name
        toto.age = age
    def afficherNom(self):
       print("Je m'appelle " + self.name)


class Utilisateur:
    def __init__(toto,name,age):
        toto.name = name
        toto.age = age
    def afficherNom(self):
       print("Je m'appelle " + self.name)


class Administrateur(Utilisateur):
    def resetSysteme(self):
        print("Je reset le système")

a = Administrateur("Buck Rodgers", 33)

a.name = 'Huynh'
a.afficherNom()

a.resetSysteme()
