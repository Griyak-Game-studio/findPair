import pygame
from pygame import color
from pygame.locals import *
from .ImageLoader import ImageLoader


class FruitTale(pygame.sprite.Sprite):
    il = ImageLoader()

    def __init__(self, img, name, coord=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.hidden_img = self.il.getImage('question.png')
        self.shown_img = img
        self.image = self.hidden_img
        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.image.set_colorkey((0, 0, 0))
        self.size = self.width, self.height = self.image.get_size()
        self.name = name
        self.isLoked = False
        self.x, self.y = coord

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def __ne__(self, other):
        if isinstance(other, FruitTale):
            return self.name != other.name

    def setCoord(self, coord):
        self.x, self.y = coord
        self.rect.center = coord

    def lock(self):
        self.isLoked = True
        self.image = self.shown_img

    def unlock(self):
        self.isLoked = False
        self.image = self.hidden_img

    def reverse(self):
        if self.image is self.shown_img:
            self.image = self.hidden_img
        else:
            self.image = self.shown_img
        #self.image.set_colorkey(BLACK)
        #self.shown_img, self.hidden_img = self.hidden_img, self.shown_img

    def isHit(self, coord):
        x, y = coord
        return self.rect.collidepoint(x, y)


    def update(self):
        #self.reverse()
        pass


class Score():
    def __init__(self, coord = (0, 0), size= 18):
        #pygame.Surface.__init__(self)
        font_name = pygame.font.match_font('arial')
        self.size = size
        self.coord = coord
        self.font = pygame.font.Font(font_name, size)
        self.surf = None
        self.rect = None

    def update(self, text):
        self.surf = self.font.render("Найдено пар: " + text, True, (0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.midtop = self.coord
        #return (self.surf, self.rect)