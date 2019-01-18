from pyglet.sprite import Sprite
from pyglet.graphics import Batch
from constants import *

class CloudsBackground:
    def __init__(self):
        self.batch = Batch()
        self.clouds = [Sprite(IMAGES['backgrounds']['clouds'], x=0, y=0, batch=self.batch, group=G_BACKGROUND_2),
                        Sprite(IMAGES['backgrounds']['clouds'], x=-1280, y=0, batch=self.batch, group=G_BACKGROUND_2),
                        Sprite(IMAGES['backgrounds']['clouds'], x=0, y=720, batch=self.batch, group=G_BACKGROUND_2),
                        Sprite(IMAGES['backgrounds']['clouds'], x=-1280, y=720, batch=self.batch, group=G_BACKGROUND_2)]
        self.grass = [Sprite(IMAGES['backgrounds']['grass'], x=0, y=0, batch=self.batch, group=G_BACKGROUND_1),
                        Sprite(IMAGES['backgrounds']['grass'], x=0, y=720, batch=self.batch, group=G_BACKGROUND_1)]
    def draw(self):
        self.batch.draw()
    def update(self, dt):
        for s in self.clouds:
            s.x += 0.1
            s.y -= 5
            if s.x > 1280:
                s.x -= 1280*2
            if s.y < -720:
                s.y += 720*2
        for s in self.grass:
            s.y -= 9
            if s.y < -720:
                s.y += 720*2