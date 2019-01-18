from pyglet.gl import *
from pyglet.graphics import vertex_list, vertex_list_indexed, Group
from math import sin, cos, pi

def circle_arc(batch, x, y, r, resolution=100, color=(255, 255, 255, 255), percentage=1, angle=0, group=None):
    """Adds a vertex list representing a circumference arc to a batch.
    Keyword arguments:
    resolution -- number of lines to form the circle, if it would be full(see percentage) (default 100)
    color -- color of the lines (default (255, 255, 255) or white)
    percentage -- percentage of the circumference to be drawn, between 0 and 1, 1 meaning full (default 1)
    angle -- angle to start the arc, between 0 and 1, 0 meaning to start right, clockwise (default 0)
    group -- group to which the vertex group is added, None for new group (default None)"""
    if not group:
        group = Group()
    points = []
    colors = []
    points_count = int(resolution*percentage+1)
    for i in range(points_count):
        points += [x + r*cos(i*2*pi/resolution + angle), y + r*sin(i*2*pi/resolution + angle)]
        colors += [*color]
    return batch.add(points_count, GL_LINE_STRIP, group, ('v2f', points), ('c4B', colors))

def circle_full(batch, x, y, r, resolution=100, color=(255, 255, 255, 255), percentage=1, angle=0, group=None):
    """Adds a vertex list representing a filled circle to a batch.
    Keyword arguments:
    resolution -- number of lines to form the circle (default 100)
    color -- color of the lines (default (255, 255, 255) or white)
    percentage -- percentage of the circumference to be drawn, between 0 and 1, 1 meaning full (default 1)
    angle -- angle to start the arc, between 0 and 1, 0 meaning to start right, clockwise (default 0)
    group -- group to which the vertex group is added, None for new group (default None)"""
    if not group:
        group = Group()
    points = [x, y]
    colors = [*color]
    points_count = int(resolution*percentage)
    for i in range(points_count+1):
        points += [x + r*cos(i*2*pi/resolution + angle), y + r*sin(i*2*pi/resolution + angle)]
        colors += [*color]
    return batch.add(points_count+2, GL_TRIANGLE_FAN, group, ('v2f', points), ('c4B', colors))

def rectangle_line(batch, x, y, width, height, color=(255, 255, 255, 255), group=None):
    """Adds a vertex list representing rectangular perimeter to a batch.
    Keyword arguments:
    color -- color of the lines (default (255, 255, 255) or white)
    group -- group to which the vertex group is added, None for new group (default None)"""
    if not group:
        group = Group()
    points = [x, y, x+width, y, x+width, y+height, x, y+height, x, y]
    colors = []
    for i in range(5):
        colors += [*color]
    return batch.add(5, GL_LINE_STRIP, group, ('v2f', points), ('c4B', colors))
    
def rectangle_filled(batch, x, y, width, height, color=(255, 255, 255, 255), group=None):
    """Adds a vertex list representing a filled rectangle perimeter to a batch.
    Keyword arguments:
    color -- color of the lines (default (255, 255, 255) or white)
    group -- group to which the vertex group is added, None for new group (default None)"""
    if not group:
        group = Group()
    points = [x, y, x+width, y, x+width, y+height, x, y+height, x, y]
    colors = []
    for i in range(5):
        colors += [*color]
    return batch.add(5, GL_TRIANGLE_FAN, group, ('v2f', points), ('c4B', colors))

def rectangle_filled_vertgrad(batch, x, y, width, height, color_top=(255, 255, 255, 255), color_bot=(0, 0, 0, 0), group=None):
    """Adds a vertex list representing a filled rectangle perimeter to a batch.
    Keyword arguments:
    color -- color of the lines (default (255, 255, 255) or white)
    group -- group to which the vertex group is added, None for new group (default None)"""
    if not group:
        group = Group()
    points = [x, y, x+width, y, x+width, y+height, x, y+height, x, y]
    colors = []
    for i in range(5):
        colors += [*color]
    return batch.add(5, GL_TRIANGLE_FAN, group, ('v2f', points), ('c4B', colors))