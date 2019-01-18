from pyglet.graphics import Batch
from pyglet.sprite import Sprite
from constants import *
from core import *

class MisuOrb(Orb):
    def __init__(self, game, player, id):
        super().__init__(game, IMAGES['bullets']['round'], player)
        self.id = id # -1 for left orb, 1 for right orb
    def update(self, dt):
        super().update(dt)
        if self.player.focused:
            self.target_x = 64*self.id
            self.target_y = 16
        else:
            self.target_x = 32*self.id
            self.target_y = 64

class MisuPlayer(Player):
    def __init__(self, game):
        super().__init__(game, 10, 6, IMAGES['player']['player1'])
        self.orbs = [MisuOrb(self.game, self, -1), MisuOrb(self.game, self, 1)]
        for orb in self.orbs:
            self.game.add_game_object(orb)