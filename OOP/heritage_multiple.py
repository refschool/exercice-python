
class Object:
    def __init__(self):
        pass
    def do(self):
        return "I exist"


class Kite(Object):
    def __init__(self,max_altitude):
        self.max_altitude = max_altitude
    def do(self):
        return "I fly"
    def getMaxAltitude(self):
        return self.max_altitude


class Surf(Object):
    def __init__(self,matter):
        self.matter = matter
    def do(self):
        return "I surf"
    def getMaxAltitude(self):
        return self.max_altitude

class KiteSurf(Surf,Kite):
    def __init__(self):
        pass

ks = KiteSurf()
print(ks.do())



