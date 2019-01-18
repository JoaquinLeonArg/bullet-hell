from pyglet.graphics import Batch
from pyglet.sprite import Sprite
from math import sin, cos
from constants import *
import pyglet

class Scene:
    def __init__(self, window):
        self.window = window
        self.keys = {}
        self.t = 0
    def exit(self): pass
    def draw(self): pass
    def update(self, dt):
        self.t += 1
        for key in (key for key in self.keys if self.keys[key]):
            self.keys[key] += 1
    def input(self, key, active):
        if key in self.keys:
            if active ^ self.keys[key]:
                self.keys[key] = int(active)
        else:
            self.keys[key] = int(active)
    def get_key(self, key):
        if key in keys:
            return keys[key]
        return 0

class GameObject:
    def __init__(self, game, x, y, image):
        self.game = game
        self.x = x
        self.y = y
        self.sprite = Sprite(image, x=x, y=y, batch=self.game.batch, group=G_MAIN_0)
    def draw(self):
        self.sprite.draw()
    def early_update(self, dt): pass
    def update(self, dt): pass
    def late_update(self, dt):
        self.sprite.position = self.x, self.y
    def destroy(self):
        self.sprite.batch = None

class Player(GameObject):
    def __init__(self, game, movespeed, focusspeed, image):
        super().__init__(game, WINDOW_SIZE['width']//2, 96, image)
        self.sprite.group = G_MAIN_1
        self.movespeed = movespeed
        self.focusspeed = focusspeed
        self.focused = False
    def input(self, key, time):
        if key is KEYS['up'] and time and self.y < WINDOW_SIZE['height'] - self.sprite.height//2:
            if self.focused:
                self.y += self.focusspeed
            else:
                self.y += self.movespeed
        elif key is KEYS['down'] and time and self.y > self.sprite.height//2:
            if self.focused:
                self.y -= self.focusspeed
            else:
                self.y -= self.movespeed
        elif key is KEYS['right'] and time and self.x < WINDOW_SIZE['width'] - self.sprite.width//2 - 160:
            if self.focused:
                self.x += self.focusspeed
            else:
                self.x += self.movespeed
        elif key is KEYS['left'] and time and self.x > self.sprite.width//2 + 160:
            if self.focused:
                self.x -= self.focusspeed
            else:
                self.x -= self.movespeed
        if key is KEYS['focus'] and time:
            self.focused = True
        if key is KEYS['focus'] and not time:
            self.focused = False

class Orb(GameObject):
    def __init__(self, game, image, player):
        super().__init__(game, player.x, player.y, image)
        self.sprite.group = G_MAIN_0
        self.target_x, self.target_y = player.x, player.y
        self.player = player
    def update(self, dt):
        super().update(dt)
        self.x = self.player.x + self.target_x
        self.y = self.player.y + self.target_y

class Overlay:
    #TODO: Implement other UI elements(HP, score, etc)
    def __init__(self, scene):
        self.scene = scene
        self.sprite_borders = Sprite(IMAGES['ui']['borders'], 0, 0, batch=self.scene.batch, group=G_FOREGROUND_2)

class Bullet(GameObject):
    def __init__(self, game, x, y, image, owner):
        super().__init__(x, y, image)
        self.sprite.group = G_MAIN_2
        self.owner = owner
        self.t = 0
    def check_hitbox(self, other):
        if distance(self.x, self.y, other.x, other.y) <= self.sprite.width:
            return True
        else:
            return False
    def update(self, dt):
        super().update(dt)
        self.t += 1

class Hitbox:
    pass

class Level:
    def __init__(self, game, events, time_limit):
        self.game = game
        self.events = events
        self.time_limit = time_limit
        self.t = 0
        self.active = True
    def update(self, dt):
        self.t += 1
        for e in self.events:
            if e['time'] is self.t:
                self.game.add_game_object(e['entity'](*e['args']))
        if self.t is self.time_limit:
            # TODO: Change level
            pass
    