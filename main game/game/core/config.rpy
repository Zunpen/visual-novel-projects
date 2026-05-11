## variables.rpy - Definisi atau List Config Game

"""
Contoh pendefinisian :
define fade_scene = Fade(0.5, 1.0, 0.5)
Contoh call untuk script utama (script.rpy) :
scene bg basement
with fade_scene
"""

transform flicker:
    matrixcolor BrightnessMatrix(0.0) 
    
    linear 0.05 matrixcolor BrightnessMatrix(-0.2)
    linear 0.05 matrixcolor BrightnessMatrix(0.0)
    
    pause (renpy.random.uniform(1.5, 5.0))
    linear 0.05 matrixcolor BrightnessMatrix(-0.15)
    linear 0.05 matrixcolor BrightnessMatrix(0.0)
    repeat

transform chara_left:
    zoom 0.9
    yalign -0.3
    xalign 0.2
    
transform chara_middle:
    zoom 0.9
    yalign -0.3

transform chara_right:
    zoom 1.1
    yalign -0.1

transform flicker_light:
    alpha 0.3
    matrixcolor BrightnessMatrix(-0.7) 
    matrixcolor ContrastMatrix(1.2)

    linear 0.05 matrixcolor BrightnessMatrix(-0.8)
    linear 0.05 matrixcolor BrightnessMatrix(-0.2)
    
    pause (renpy.random.uniform(2.0, 5.0))

    linear 0.05 matrixcolor BrightnessMatrix(-0.8)
    linear 0.05 matrixcolor BrightnessMatrix(-0.2)
    repeat

define config.layers = [ 'master', 'lighting', 'transient', 'screens', 'overlay' ]