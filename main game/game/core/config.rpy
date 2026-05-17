## variables.rpy - Definisi atau List Config Game

"""
Contoh pendefinisian :
define fade_scene = Fade(0.5, 1.0, 0.5)
Contoh call untuk script utama (script.rpy) :
scene bg basement
with fade_scene
"""


define config.layers = [ 'master', 'lighting', 'transient', 'screens', 'overlay' ]
init python:
    renpy.music.register_channel("sound2", "sound", loop=False)