<<<<<<< HEAD
## assets.rpy - Definisi atau List assets pada game

"""
Contoh code :
define audio.bgm_main = "audio/main_theme.mp3"
define audio.bgm_tense = "audio/tense.mp3"
define audio.bgm_sad = "audio/sad.mp3"
image bg basement = "assets/bg/basement.png"
image bg corridor = "assets/bg/corridor.png"
image alya sick = "assets/sprites/alya_sick.png"
"""

## Define audio
define audio.sfx_bulb = "assets/audio/bulb.mp3"
define audio.sfx_clothes = "assets/audio/clothes_rustle.mp3"

## Define images
image light_overlay = Solid("#fff3c040")
image dark = Solid("#000000")
image access card = "assets/images/AccessCard_600.png"
image harddisk = "assets/images/Harddisk_600.png"
image antidote = "assets/images/Suntikan_600.png"

## Define bg
image bg basement = "assets/bg/basement.png"
image bg basement_dark = "assets/bg/basement_dark.png"
image bg corridor = "assets/bg/corridor.png"
image bg broadcast = "assets/bg/broadcast.png"
image bg sewer = Movie(
    play="assets/bg/sewer.webm",
    loop=True,
)
image bg office = Movie(
    play="assets/bg/office.webm",
    loop=True,
)
image light_glow_mask = "assets/bg/light_source.png"
image bg corridor dark = "assets/bg/corridor_dark.png"

## Define character
image alya sick = "assets/chara/alya/alya_sick.png"
image alya idle = "assets/chara/alya/base_alya.png"
image alya think = "assets/chara/alya/alya_think.png"
image raka idle = "assets/chara/raka/base_raka.png"
image nisa idle = "assets/chara/nisa/base_nisa.png"
image nisa smile = "assets/chara/nisa/nisa_smile.png"
image bumi idle = "assets/chara/bumi/base_bumi.png" 
image bumi regret = "assets/chara/bumi/bumi_menyesal.png"
image bumi serius = "assets/chara/bumi/bumi_serius.png"

## Define ui
image choice idle = "assets/ui/choice_idle.png"
image choice hover = "assets/ui/choice_hover.png"

## Unused
=======
## assets.rpy - Definisi atau List assets pada game

"""
Contoh code :
define audio.bgm_main = "audio/main_theme.mp3"
define audio.bgm_tense = "audio/tense.mp3"
define audio.bgm_sad = "audio/sad.mp3"
image bg basement = "assets/bg/basement.png"
image bg corridor = "assets/bg/corridor.png"
image alya sick = "assets/sprites/alya_sick.png"
"""

## Define audio

## Define images
image light_overlay = Solid("#fff3c040")

## Define bg
image bg basement = "assets/bg/basement.png"
image light_glow_mask = "assets/bg/light_source.png"

## Define character
image alya sick = "assets/chara/alya/alya_sick.png"
image alya idle   = "assets/chara/alya/base_alya.png"
image raka idle = "assets/chara/raka/base_raka.png"
image nisa idle = "assets/chara/nisa/base_nisa.png"

## Define ui
image choice idle = "assets/ui/choice_idle.png"
image choice hover = "assets/ui/choice_hover.png"

## Unused
image bg basement_dark = "assets/bg/basement_dark.png"
>>>>>>> 9cb7361821f62c8560ade3094d67531a5ef54315
image bg basement_bright = "assets/bg/basement.png"