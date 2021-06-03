#instance, class and static method
"""
 static : takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
 Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

class:
Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

"""

class Dog():
    """  the state """
    ref = "123"
    def __init__(self,name):
        self.name = name
    """ instance method"""
    def run(self):
        print("run",self.name)
    """ class method """
    @classmethod
    def bark(cls):
        print("class method, bark",cls)
    """ static method """
    @staticmethod
    def eat(cls):
        print("static method, eat",cls)

chien  = Dog('medor')

Dog.bark()
Dog.eat()
chien.run()