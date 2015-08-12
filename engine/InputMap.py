__author__ = 'Michel Llorens'
__email__ = "mllorens@dcc.uchile.cl"
import curses

_keys = {
    "down": "down",
    "up": "up",
    "left": "left",
    "right": "right",
    "enter": "enter",
    'q': 'quit',
    'i': 'log_up',
    'k': 'log_down',
    'j': 'log_left',
    'l': 'log_right',
    1: 'it_1',
    2: 'it_2',
    3: 'it_3',
    4: 'it_4',
    'y': 'yes',
    'n': 'no',
    'm': 'map'
}

def change_key(old_key, new_key):
    _keys[new_key] = _keys[old_key]
    del _keys[old_key]

def key(value):
    if value in _keys:
        return _keys[value]
    return None