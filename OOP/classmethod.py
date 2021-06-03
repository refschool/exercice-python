#https://realpython.com/instance-class-and-static-methods-demystified/

class Dog():
    """
    static cannot see self no cls attribute
    class cannot
    """
    attr_de_classe = "attribut de classe"

    def __init__(self,name):
        self.name = name

    def instance_method(self):
       print("in the instance method",self)
    @classmethod
    def class_method(cls):
       print(cls.attr_de_classe)
    @staticmethod
    def static_method(self):
       print(self)


chien = Dog("médor")
chien.static_method("in the static method with a fake self argument")
chien.instance_method()

Dog.instance_method() #error
Dog.instance_method(chien) # works !!


#using classmethod as factory