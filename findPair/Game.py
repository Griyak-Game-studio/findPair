from .FruitTale import FruitTale
import pygame

class Game:

    def __init__(self, tales):
        self.points = 0
        self.tales = tales
        self.stack = []

    def taleHit(self, coord):
        x, y = coord
        for tale in self.tales:
            if isinstance(tale, FruitTale) and tale.isHit(coord) and not tale.isLoked:
                if len(self.stack) == 0 or (len(self.stack) == 1 and not self.stack[0] is tale):
                    self.stack.append(tale)
                    tale.lock()
                    #time.sleep(1)

    def matchCheck(self):
        if len(self.stack) > 1:
            pygame.time.delay(700)
            if self.stack[0].getName() == self.stack[1].getName():
                self.points += 1
                print(self.points)
            else:
                self.stack[0].unlock()
                self.stack[1].unlock()
            self.stack.clear()
        #time.sleep(100)

    def getScore(self):
        return self.points