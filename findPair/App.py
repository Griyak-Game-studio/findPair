import pygame
from .ImageLoader import ImageLoader
from .FruitTale import FruitTale
from .FruitTale import Score
from .FruitTaleFabric import FruitTaleFabric as ftf
from .FruitTaleGroup import FruitTaleGroup as ftg
from .Game import Game
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class App:
    FPS = 30
    def __init__(self):
        self._running = True
        self.screen = None
        self.clock = None
        self.all_sprites = None
        self.il = ImageLoader()
        self.size = self.width, self.height = 800, 650
        self.tales = []

    def on_init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.tales = ftg().generateGroup(6)
        for tale in self.tales:
            self.all_sprites.add(tale)
        self._running = True
        self.game = Game(self.tales)

        cols = 4
        rows = math.ceil(len(self.tales) / cols)
        dist = 30
        x_indent = 100
        y_indent = 150
        for i, tale in enumerate(self.tales):
            w, h = tale.size
            x = x_indent + (i % cols) * (dist + w)
            y = y_indent + math.floor(i / cols) * (dist + h)
            tale.setCoord((x, y))

        self.score = Score(coord=(self.width/2, 10))
        self.score.update(str(self.game.getScore()))
        self.screen.blit(self.score.surf, self.score.rect)


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            '''for tale in self.all_sprites:
                if isinstance(tale, FruitTale) and tale.isHit((x, y)):
                    tale.reverse()
            '''
            self.game.taleHit(event.pos)

    def on_logic(self):
        self.game.matchCheck()

    def on_loop(self):
        self.all_sprites.update()

    def on_render(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)

        self.score.update(str(self.game.getScore()))
        self.screen.blit(self.score.surf, self.score.rect)
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.clock.tick(self.FPS)

        while (self._running):
            self.on_logic()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()