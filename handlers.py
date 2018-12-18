from constants import *
from main_classes import InputHandler, BehaviorHandler

class PlayerInputHandler(InputHandler):
    def execute(self, key, timer, delta_time):
        if self.parent.on_focus:
            if key == KEYS['up'] and self.parent.y + self.focus_speed*delta_time < MAX_Y:
                self.parent.y += self.focus_speed*delta_time
            elif key == KEYS['down'] and self.parent.y - self.focus_speed*delta_time > MIN_Y:
                self.parent.y -= self.focus_speed*delta_time
            if key == KEYS['left'] and self.parent.x + self.focus_speed*delta_time > MIN_X:
                self.parent.x -= self.focus_speed*delta_time
            elif key == KEYS['right'] and self.parent.x - self.focus_speed*delta_time < MAX_X:
                self.parent.x += self.focus_speed*delta_time
        else:
            if key == KEYS['up'] and self.parent.y + self.move_speed*delta_time < MAX_Y:
                self.parent.y += self.move_speed*delta_time
            elif key == KEYS['down'] and self.parent.y - self.move_speed*delta_time > MIN_Y:
                self.parent.y -= self.move_speed*delta_time
            if key == KEYS['left'] and self.parent.x + self.move_speed*delta_time > MIN_X:
                self.parent.x -= self.move_speed*delta_time
            elif key == KEYS['right'] and self.parent.x - self.move_speed*delta_time < MAX_X:
                self.parent.x += self.move_speed*delta_time

class Player1Input(PlayerInputHandler):
    def __init__(self, parent):
        super().__init__(parent, 1500, 1000)