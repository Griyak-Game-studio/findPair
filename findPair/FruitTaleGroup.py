import pygame
import numpy as np
import random as rand
import math
from .FruitTale import FruitTale
from .FruitTaleFabric import FruitTaleFabric
from .ImageLoader import ImageLoader

class FruitTaleGroup:

    def __init__(self):
        self.il = ImageLoader()
        self.fabrics = (FruitTaleFabric(self.il.getImage('apple.png'), 'apple'),
                   FruitTaleFabric(self.il.getImage('bananas.png'), 'bananas'),
                   FruitTaleFabric(self.il.getImage('grapes.png'), 'grapes'),
                   FruitTaleFabric(self.il.getImage('lemon.png'), 'lemon'),
                   FruitTaleFabric(self.il.getImage('peach.png'), 'peach'),
                   FruitTaleFabric(self.il.getImage('pineapple.png'), 'pineapple'),
                   FruitTaleFabric(self.il.getImage('strawberry.png'), 'strawberry'),
                   FruitTaleFabric(self.il.getImage('watermelon.png'), 'watermelon'))
        self.N = len(self.fabrics)

    def generateGroup(self, numPairs):
        pairs = []
        if numPairs < 0:
            return pairs
        need = math.floor(self.N/2)
        cols = numPairs % need
        rows = math.floor(numPairs / need)
        for i in range(0, numPairs):
            pairs.append(self.fabrics[i % self.N].getTale())
            pairs.append(self.fabrics[i % self.N].getTale())
        rand.shuffle(pairs)
        return pairs

        result = []
        for i in range(0, rows):
            temp = []
            for j in range(0, need):
                temp.append(pairs.pop(0))
            result.append(temp)
        temp = []
        for i in range(0, cols):
            temp.append(pairs.pop(0))
        result.append(temp)
        return result
