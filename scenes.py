from core import Scene, Overlay, GameObject, Player
from players import MisuPlayer
from backgrounds import CloudsBackground
from pyglet.text import Label
from pyglet.graphics import Batch, Group, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import key
from pyglet.gl import *
from pyglet import app
from constants import *
from math import sin
from draw import *

class SceneMainMenu(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.batch = Batch()
        self.menu = 0
        self.main_index = 0
        self.practice_index = 0
        self.config_index = 0
        self.t = 0

        self.background = Sprite(IMAGES['ui']['mainmenu_bg'], -15, -15)
        self.background.opacity = 100
        self.background2 = Sprite(IMAGES['ui']['mainmenu_bg2'], 0, 0, blend_src=774)
        self.left_sprite = Sprite(IMAGES['ui']['mainmenu_left'], 0, 0, batch=self.batch)
        self.left_sprite.opacity = 50

        # Main menu options:
        options_text = ['Start game', 'Practice', 'High scores', 'Config', 'Exit']
        self.main_options_shadow = [Label(text=options_text[i], font_name=MENU_FONT, color=(100, 100, 100, 100), font_size=22, x=199, y=401 - 32*i, batch=self.batch) for i in range(len(options_text))]
        self.main_options = [Label(text=options_text[i], font_name=MENU_FONT, font_size=22, x=200, y=400 - 32*i, batch=self.batch) for i in range(len(options_text))]

        # Practice options:
        options_text = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']
        self.practice_options_shadow = [Label(text=options_text[i], font_name=MENU_FONT, color=(100, 100, 100, 0), font_size=22, x=499, y=401 - 32*i, batch=self.batch) for i in range(len(options_text))]
        self.practice_options = [Label(text=options_text[i], font_name=MENU_FONT, font_size=22, x=500, y=400 - 32*i, color=(255,255,255,0), batch=self.batch) for i in range(len(options_text))]

        # Config options:
        options_text = ['SFX volume', 'BGM volume', 'Controls']
        self.config_options_shadow = [Label(text=options_text[i], font_name=MENU_FONT, color=(100, 100, 100, 0), font_size=22, x=499, y=401 - 32*i, batch=self.batch) for i in range(len(options_text))]
        self.config_options = [Label(text=options_text[i], font_name=MENU_FONT, font_size=22, x=500, y=400 - 32*i, color=(255,255,255,0), batch=self.batch) for i in range(len(options_text))]
    def draw(self):
        self.background.draw()
        self.background2.draw()
        self.batch.draw()
    def update(self, dt):
        super().update(dt)
        self.t += 1
        # Animate background:
        self.background.x = -15 + 11*sin(0.021*self.t)
        self.background.y = -15 + 10*sin(0.024*self.t)
        self.background2.opacity = 70 + 60*sin(0.01*self.t)
        # Manage input:
        if self.menu is 0: # Main menu
            if KEYS['up'] in self.keys and self.keys[KEYS['up']] is KEY_PRESSED and self.main_index > 0:
                self.main_index -= 1
            elif KEYS['down'] in self.keys and self.keys[KEYS['down']] is KEY_PRESSED and self.main_index < 4:
                self.main_index += 1
            elif KEYS['shoot'] in self.keys and self.keys[KEYS['shoot']] is KEY_PRESSED:
                if self.main_index is 0: # Start
                    self.window.change_scene(SceneGame)
                if self.main_index is 1: # Practice
                    self.menu = 2
                if self.main_index is 2: # Scores
                    pass
                if self.main_index is 3: # Config
                    self.menu = 4
                if self.main_index is 4: # Exit
                    app.exit()
        if self.menu is 2: # Practice menu
            if KEYS['up'] in self.keys and self.keys[KEYS['up']] is KEY_PRESSED and self.practice_index > 0:
                self.practice_index -= 1
            elif KEYS['down'] in self.keys and self.keys[KEYS['down']] is KEY_PRESSED and self.practice_index < 4:
                self.practice_index += 1
            elif KEYS['bomb'] in self.keys and self.keys[KEYS['bomb']] is KEY_PRESSED:
                self.menu = 0
                self.practice_index = 0
        if self.menu is 4: # Config menu
            if KEYS['up'] in self.keys and self.keys[KEYS['up']] is KEY_PRESSED and self.config_index > 0:
                self.config_index -= 1
            elif KEYS['down'] in self.keys and self.keys[KEYS['down']] is KEY_PRESSED and self.config_index < 2:
                self.config_index += 1
            elif KEYS['bomb'] in self.keys and self.keys[KEYS['bomb']] is KEY_PRESSED:
                self.menu = 0
                self.config_index = 0
        # Animate labels:
        for i in range(len(self.main_options)):
            l = self.main_options[i]
            s = self.main_options_shadow[i]
            if self.menu is 0 and l.color[3] < 255:
                l.color = (l.color[0], l.color[1], l.color[2], l.color[3] + 5)
            if self.menu is 0 and s.color[3] < 100:
                s.color = (s.color[0], s.color[1], s.color[2], s.color[3] + 5)
            if self.menu is not 0 and l.color[3] > 110:
                l.color = (l.color[0], l.color[1], l.color[2], l.color[3] - 5)
            if self.menu is not 0 and s.color[3] > 40:
                s.color = (s.color[0], s.color[1], s.color[2], s.color[3] - 5)
            if l.x < 210 and self.main_index == i:
                l.x += 1
            elif l.x > 200 and self.main_index != i:
                l.x -= 1
            if s.x > 189 and self.main_index == i:
                s.x -= 1
            elif s.x < 199 and self.main_index != i:
                s.x += 1
        for i in range(len(self.practice_options)):
            l = self.practice_options[i]
            s = self.practice_options_shadow[i]
            if self.menu is 2 and l.color[3] < 255:
                l.color = (l.color[0], l.color[1], l.color[2], l.color[3] + 5)
            if self.menu is 2 and s.color[3] < 100:
                s.color = (s.color[0], s.color[1], s.color[2], s.color[3] + 5)
            if self.menu is not 2 and l.color[3] > 0:
                l.color = (l.color[0], l.color[1], l.color[2], l.color[3] - 5)
            if self.menu is not 2 and s.color[3] > 0:
                s.color = (s.color[0], s.color[1], s.color[2], s.color[3] - 5)
            if l.x < 510 and self.practice_index == i:
                l.x += 1
            elif l.x > 500 and self.practice_index != i:
                l.x -= 1
            if s.x > 489 and self.practice_index == i:
                s.x -= 1
            elif s.x < 499 and self.practice_index != i:
                s.x += 1
        for i in range(len(self.config_options)):
            l = self.config_options[i]
            s = self.config_options_shadow[i]
            if self.menu is 4 and l.color[3] < 255:
                l.color = (l.color[0], l.color[1], l.color[2], l.color[3] + 5)
            if self.menu is 4 and s.color[3] < 100:
                s.color = (s.color[0], s.color[1], s.color[2], s.color[3] + 5)
            if self.menu is not 4 and l.color[3] > 0:
                l.color = (l.color[0], l.color[1], l.color[2], l.color[3] - 5)
            if self.menu is not 4 and s.color[3] > 0:
                s.color = (s.color[0], s.color[1], s.color[2], s.color[3] - 5)
            if l.x < 510 and self.config_index == i:
                l.x += 1
            elif l.x > 500 and self.config_index != i:
                l.x -= 1
            if s.x > 489 and self.config_index == i:
                s.x -= 1
            elif s.x < 499 and self.config_index != i:
                s.x += 1

class SceneGame(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.game_objects = []
        self.fx_bot_objects = []
        self.fx_top_objects = []
        self.batch = Batch()

        self.level_number = 0
        self.level = Level1()

        self.bg_manager = CloudsBackground()
        self.overlay = Overlay(self)

        self.player = MisuPlayer(self)
        self.game_objects.append(self.player)
    def draw(self):
        super().draw()
        self.bg_manager.draw()
        self.batch.draw()
    def update(self, dt):
        super().update(dt)
        self.bg_manager.update(dt)
        for e in self.game_objects + self.fx_bot_objects + self.fx_top_objects:
            e.early_update(dt)
            e.update(dt)
            e.late_update(dt)
        for key in self.keys:
            self.player.input(key, self.keys[key])
    def add_game_object(self, go):
        self.game_objects.append(go)
        go.sprite.batch = self.batch

class SceneGraphicsTest(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.batch = Batch()
        self.group0 = OrderedGroup(0)
        self.group1 = OrderedGroup(1)
        self.group2 = OrderedGroup(2)
        self.group_labels = OrderedGroup(5)
    def update(self, dt):
        super().update(dt)
        self.batch = Batch()
        # Image 1
        circle_arc(self.batch, 150, 570, 100, resolution=200, percentage=0.5*cos(self.t*0.01)+0.5, angle=pi)
        # Image 2
        circle_full(self.batch, 400, 570, 100, resolution=200, percentage=0.5, angle=int(self.t*0.01)*0.25*pi)
        # Image 4
        rectangle_line(self.batch, 870+30*cos(self.t*0.01), 480+20*cos((self.t+30)*0.005), 100+50*cos((self.t+105)*0.008), 100+40*cos((self.t+10)*0.018))
        # Image 5
        rectangle_filled(self.batch, 100, 200, 100, 100, color=(int(100*cos(self.t*0.01)+110), int(100*cos(self.t*0.02)+110), int(100*cos(self.t*0.03)+110), 255))
    def draw(self):
        super().draw()
        self.batch.draw()

class SceneBulletTest(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.bullets = [LinearBullet(IMAGES['bullets']['round'])]
        self.batch = Batch()
    def update(self, dt):
        super().update(dt)
        for bullet in self.bullets:
            bullet.sprite.batch = self.batch
            bullet.update()
            bullet.update_sprite()
    def draw(self):
        super().update()
        self.batch.draw()