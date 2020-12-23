from .FruitTale import FruitTale

class FruitTaleFabric:

    def __init__(self, img, type):
        self.img = img
        self.type = type

    def getTale(self):
        return FruitTale(self.img, self.type)