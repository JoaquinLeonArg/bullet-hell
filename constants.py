from pyglet.window.key import *
from pyglet.image import load
from pyglet.graphics import OrderedGroup

WINDOW_SIZE = {
    'width': 1280,
    'height': 720
}

KEYS = {
    'up': UP,
    'down': DOWN,
    'left': LEFT,
    'right': RIGHT,
    'focus': LSHIFT,
    'shoot': Z,
    'bomb': X,
}

KEY_PRESSED = 2

IMAGES = {
    'ui': {
        'borders': load('resources/graphics/ui/borders.png'),
        'mainmenu_bg': load('resources/graphics/ui/mainmenu_bg.png'),
        'mainmenu_bg2': load('resources/graphics/ui/mainmenu_bg2.png'),
        'mainmenu_left': load('resources/graphics/ui/mainmenu_left.png')
    },
    'bullets': {
        'round': load('resources/graphics/bullets/round.png')
    },
    'player': {
        'player1': load('resources/graphics/player/player1.png')
    },
    'enemies': {

    },
    'backgrounds': {
        'clouds': load('resources/graphics/backgrounds/clouds.png'),
        'grass': load('resources/graphics/backgrounds/grass.png')
    }
}

MENU_FONT = 'Calibri'

# Layers
G_BACKGROUND_0 = OrderedGroup(5)
G_BACKGROUND_1 = OrderedGroup(6)
G_BACKGROUND_2 = OrderedGroup(7)
G_BACKGROUND_3 = OrderedGroup(8)

G_MAIN_0 = OrderedGroup(10)
G_MAIN_1 = OrderedGroup(11)
G_MAIN_2 = OrderedGroup(12)
G_MAIN_3 = OrderedGroup(13)

G_FOREGROUND_0 = OrderedGroup(15)
G_FOREGROUND_1 = OrderedGroup(16)
G_FOREGROUND_2 = OrderedGroup(17)
G_FOREGROUND_3 = OrderedGroup(18)


# Set anchor points
IMAGES['player']['player1'].anchor_x, IMAGES['player']['player1'].anchor_y = IMAGES['player']['player1'].width // 2, IMAGES['player']['player1'].height // 2

IMAGES['bullets']['round'].anchor_x, IMAGES['bullets']['round'].anchor_y = IMAGES['bullets']['round'].width // 2, IMAGES['bullets']['round'].height // 2