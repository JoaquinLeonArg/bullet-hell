from pyglet.window.key import *
from pyglet.image import load

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

IMAGES = {
    'ui': {
        'borders': load('resources/graphics/ui/borders.png')
    },
    'bullets': {

    },
    'player': {
        'player1': load('resources/graphics/player/player1.png')
    },
    'enemies': {

    }
}

MIN_X = 150 + int(IMAGES['player']['player1'].width*0.5)
MIN_Y = 20
MAX_X = 1130 - int(IMAGES['player']['player1'].width*1.5)
MAX_Y = 700 - IMAGES['player']['player1'].height