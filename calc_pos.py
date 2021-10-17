# Import
from const import WINDOW_WIDTH, WINDOW_HEIGHT

def calc_pos(x, y, z):
    if z <= 0:
        z = 0.00001
    return [(x / z) + (WINDOW_WIDTH / 2), (y / z) + (WINDOW_HEIGHT / 2)]