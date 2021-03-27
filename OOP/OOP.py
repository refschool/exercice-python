from datetime import date
today = date.today()


client1 = {'nom':'Dupont','age':42,'point_fidelite':150}
client2 = {'nom':'Toto','age':32,'point_fidelite':100}

client2['point_fidelite'] += 20

print(client2['point_fidelite'])

# ce qu'on veut faire
#print(client2.afficher_point_fidelite())


class Client:
    attr_de_classe = "equivalent static"

    def __init__(self, nom, age,pf = None,birthday = None):
        """fonction constructeur"""
        self.nom = nom
        self.age = age
        self.point_fidelite = pf
        self.birthday = birthday
    def add_point_fidelite(self,pf):
        self.point_fidelite += pf
    def remove_point_fidelite(self,pf):
        self.point_fidelite -= pf
    def set_name(self,new_name):
        """ setter """
        self.nom = new_name
    def get_name(self):
        """ getter """
        return self.nom




print(Client.attr_de_classe)












class ClientVIP(Client):
    def __init__(self, nom, age,pf,birthday,cagnotte):
        """fonction constructeur"""
        self.nom = nom
        self.age = age
        self.point_fidelite = pf
        self.birthday = birthday
        self.cagnotte = cagnotte
    def add_cagnotte(self,montant):
        self.cagnotte += montant
    def remove_cagnotte(self,montant):
        self.cagnotte -= montant


"""
client3 = Client("Durand",44,20,'2021-03-27')
nom = client3.get_name()
print("nom=",nom) # Durand



client4 = ClientVIP("Gros",65,420,'2021-03-27',12.3)
"""

class Geeks:
     def __init__(self):
          self._age = 0

     # using property decorator
     # a getter function
     @property
     def age(self):
         print("getter method called")
         return self._age

     # a setter function
     @age.setter
     def age(self, a):
         if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
         print("setter method called")
         self._age = a

mark = Geeks()

mark.age = 19

print(mark.age)

