class Dog:
    specie = "canis majoris"
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"message personnalisé de {self.name}"

    def __repr__(self):#official
        return "message personnalisézzz ({})".format(self.name)

    def bark(self):
        return "Bark of the Dog"




#object representation __str__
#iteration __len__, __getitem__, __reversed__



chien = Dog("Médor2")
print(chien.__repr__())


class Pug(Dog):
    def bark(self):
        return super().bark()

monChien = Pug("médor")


#polymorphisme, encapsulation,static method,class method,
#https://dbader.org/blog/python-dunder-methods