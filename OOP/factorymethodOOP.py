class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        """ trick to use the constructor method"""
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

""" factory method """
"""Flagging a method as a static method is not just a hint that a method won’t modify class 
or instance state — this restriction is also enforced by the Python runtime.

Techniques like that allow you to communicate clearly about parts of your 
class architecture so that new development work 
is naturally guided to happen within these set boundaries"""

"""
Because the circle_area() method is completely independent from the rest of the class it’s much easier to test.
"""

print(Pizza.margherita())