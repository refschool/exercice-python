
class Dog:
    """  encapsulation private protected public """
    __race = "labrador"
    def __init__(self,name):
        self.name = name
    def saluer(self):
        print(f"je m'appelle {self.name} {self.__race}")


chien1 = Dog("médor")

chien1.saluer()
print(Dog.__race)