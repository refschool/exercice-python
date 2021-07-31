class Taxable():
    def __init__(self,prix):
        self.TVA = 0.196
        self.prix = prix
    def getPrixHT(self):
        return self.prix
    def getPrixTTC(self):
        return self.prix * ( 1 + self.TVA)
    def getTVA(self):
        return self.TVA

class ProduitTaxable(Taxable):

    def __init__(self,prix):
        self.prix = prix
        self.TVA = 0.2



class ProduitTauxReduitTaxable(Taxable):

    def __init__(self,prix):
        self.prix = prix
        self.TVA = 0.055


BarreChocolatee = ProduitTaxable(5)

TamponHygienique = ProduitTauxReduitTaxable(3)


print(BarreChocolatee.getTVA())
print(TamponHygienique.getPrixTTC())
