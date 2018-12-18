from pyglet.graphics import Batch
from pyglet.sprite import *
from constants import *

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class GameC(metaclass=Singleton):
    def __init__(self):
        self.level = 0
        self.score = 0
        self.player = None
        self.enemies = []
        self.bullets = []

        self.inputs = {key: False for key in list(KEYS.values())}
        self.inputs_timer = {key: 0 for key in list(KEYS.values())}

        self.batch_ui = Batch()
        self.batch_entities = Batch()
        self.sprites = {
            'border': Sprite(IMAGES['ui']['borders'], 0, 0, batch=self.batch_ui)
        }
    def on_update(self, delta_time):
        self.player.on_update(delta_time)
        for enemy in self.enemies:
            enemy.on_update(delta_time)
        for bullet in self.bullets:
            bullet.on_update(delta_time)
        if self.player:
            self.player.on_focus = self.inputs[KEYS['focus']]
        for key in [key for key in list(self.inputs.keys()) if self.inputs[key]]:
            if self.player:
                self.player.input_handler.execute(key, self.inputs_timer[key], delta_time)
            self.inputs_timer[key] += delta_time
    def on_draw(self):
        self.batch_entities.draw()
        self.batch_ui.draw()

class Entity:
    def __init__(self, x, y, image, behavior_handler):
        self.x, self.y = x, y
        self.sprite = Sprite(image, x, y, batch=GameC().batch_entities)
        if behavior_handler:
            self.behavior_handler = behavior_handler(self)
        else:
            self.behavior_handler = None
        self.visible = True
        self.vulnerable = False
        self.time_alive = 0
    def on_update(self, delta_time):
        self.time_alive += delta_time
        if self.behavior_handler:
            self.behavior_handler.execute(delta_time)
        self.sprite.position = self.x, self.y
    def on_damage(self):
        pass
    def on_death(self):
        self.sprite.batch = None
        GameC().pop(self)
    def on_collide(self, other):
        pass

class Player(Entity):
    def __init__(self, x, y, image, input_handler):
        super().__init__(x, y, image, None)
        self.input_handler = input_handler(self)
        self.on_focus = False
    def on_collide(self, other):
        if issubclass(Enemy) or issubclass(EnemyBullet):
            self.on_death()
    def on_update(self, delta_time):
        super().on_update(delta_time)

class Enemy(Entity):
    def __init__(self, x, y, image, behavior_handler, max_life):
        super().__init__(x, y, image, behavior_handler)
        self.max_life = max_life
        self.life = max_life

class Bullet(Entity):
    pass

class EnemyBullet(Bullet):
    pass

class PlayerBullet(Bullet):
    pass

class Handler:
    def __init__(self, parent):
        self.parent = parent

class InputHandler(Handler):
    def __init__(self, parent, move_speed, focus_speed):
        super().__init__(parent)
        self.move_speed = move_speed
        self.focus_speed = focus_speed
    def execute(self, key, timer, delta_time):
        pass

class BehaviorHandler(Handler):
    def execute(self, delta_time):
        pass