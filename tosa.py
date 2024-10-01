"""
POO fondmentaux
class => def test()
Les concepts fondamentaux:


Héritage : une classe peut hériter d'une autre et ajouter de nouvelle fonctions
Encapsulation
poly-morphisme
Abstraction

"""
#definition
class Program():
    def __test(self):
        print("Je teste le programme")
    def test2(self):
        self.__test()
class ProgramReseau(Program):
    def test3(self):
        print("Je teste le programme réseau")

prog = Program()


