from pyglet.graphics import Batch
from pyglet.window import Window
from pyglet import app, clock
from scenes import *
from constants import WINDOW_SIZE
import pyglet

class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.set_size(WINDOW_SIZE['width'], WINDOW_SIZE['height'])
        clock.schedule_interval(self.update, 1/60)
        self.fps_display = clock.ClockDisplay()
        self.scene = SceneMainMenu(self)
        self.set_vsync(True)
    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.fps_display.draw()
    def on_key_press(self, key, mod):
        self.scene.input(key, True)
    def on_key_release(self, key, mod):
        self.scene.input(key, False)
    def update(self, dt):
        self.scene.update(dt)
    def change_scene(self, scene):
        self.scene.exit()
        self.scene = scene(self)

if __name__ == '__main__':
    window = MainWindow()
    app.run()