#https://www.freecodecamp.org/news/python-property-decorator/
class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price #protected because one underscore

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price

maison  = House(300000)

maison.price = 30.
print(maison.price)

print(maison)