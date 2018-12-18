from pyglet.window import Window
from pyglet import event, clock, app
from main_classes import GameC
from constants import WINDOW_SIZE
from content import player1

global SCREEN
global APP

SCREEN = Window(WINDOW_SIZE['width'], WINDOW_SIZE['height'])

class ApplicationManager:
    def __init__(self, manager):
        self.manager = manager()
        self.manager.player = player1()
    def send_update(self, delta_time):
        self.manager.on_update(delta_time)
    def send_draw(self):
        SCREEN.clear()
        self.manager.on_draw()
        SCREEN.flip()
    def send_input(self, key, status):
        if key in list(self.manager.inputs.keys()):
            self.manager.inputs[key] = status

def game_loop(delta_time):
    APP.send_update(delta_time)

@SCREEN.event
def on_draw():
    APP.send_draw()

@SCREEN.event
def on_key_press(symbol, _):
    APP.send_input(symbol, True)

@SCREEN.event
def on_key_release(symbol, _):
    APP.send_input(symbol, False)

APP = ApplicationManager(GameC)

if __name__ == "__main__":
    APP = ApplicationManager(GameC)
    clock.schedule(game_loop)
    app.run()