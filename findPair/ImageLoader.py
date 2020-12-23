import os
import pygame

class ImageLoader:
    def getImage(self, nme):
        img_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img')
        file_folder = os.path.join(img_folder, nme)
        img = pygame.Surface((50, 50))
        img.fill((128, 128, 128))
        if os.path.isfile(file_folder):
            img = pygame.image.load(file_folder).convert()
        return img


