from random import randrange
class File:
    def __init__(self):
        self.data = []

    def emfiler(self,element):
        self.data.append(element)
        return self.data

L = File()
file_client = L.emfiler(L,1)

duree_total = 0


class Test:
    def __init__(self):
        pass
    def saluer(self):
        print("Hello")