



class CouteauSuisse:
    def __init__(self,numeroSerie):
        """ constructeur     """
        self.numeroSerie = numeroSerie
        print("Dans le constructeur")
    def couper(self):
        print(self.numeroSerie,"Je coupe")
    def tirer_bouchon(self):
        print("Je retire le bouchon")

#objet      #class
mon_couteau = CouteauSuisse(123)
mon_couteau.couper()

class CouteauSuisseUSB(CouteauSuisse):
    def stockerData(self):
        print("Je stocke des données")

couteau_usb = CouteauSuisseUSB(54312346544)

print("*****")
prix = 12
def foo():
    global prix
    prix = 10

foo()
print(prix)