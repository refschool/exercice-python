#BOOM !! Encapsulation https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes

#Encapsulation python style
class Utilisateur:
    def __init__(self,name):
        self.__secret = "Je suis privé"
        self.name=name
    def afficherName(self):
        print("Je m'appelle " + self.name)
    def afficherSecret(self):
        print("Le secret est " + self.__secret)


u = Utilisateur('Yvon')

#u.afficherSecret() #OK

#print(u.secret)  #AttributeError: 'Utilisateur' object has no attribute 'secret', Python change le nom de variable
# __ veut dire ne pas toucher à cette variable

print(u.__dict__) # on peut quand même voir à l'intérieur

# private variables don't really make sense in interpreted language
#let's not forget the main goal of Access Modifiers: To help users of code understand
# what is supposed to change and what is supposed not to