## assets.rpy - Definisi atau List assets pada game

"""
Contoh code :
define audio.bgm_main = "audio/main_theme.mp3"
define audio.bgm_tense = "audio/tense.mp3"
define audio.bgm_sad = "audio/sad.mp3"
image bg basement = "assets/bg/basement.png"
image bg corridor = "assets/bg/hall.png"
image alya sick = "assets/chara/alya/alya_sick.png"
"""

## Define images
image light_overlay = Solid("#fff3c040")

## Define bg
image bg placeholder = Transform("assets/bg/basement.png", xysize=(1920, 1080))
image bg basement = Transform("assets/bg/basement.png", xysize=(1920, 1080))
image bg broadcast = Transform("assets/bg/broadcast.png", xysize=(1920, 1080))
image bg corridor = Transform("assets/bg/hall.png", xysize=(1920, 1080))
image bg hall = Transform("assets/bg/hall.png", xysize=(1920, 1080))
image bg office = Transform("assets/bg/office_best_ending.png", xysize=(1920, 1080))
image bg office_bad = Transform("assets/bg/office_bad_ending.png", xysize=(1920, 1080))
image bg office_best = Transform("assets/bg/office_best_ending.png", xysize=(1920, 1080))
image bg sewer = Transform("assets/bg/tunnel.png", xysize=(1920, 1080))
image bg tunnel = Transform("assets/bg/tunnel.png", xysize=(1920, 1080))
image bg server = Transform("assets/bg/server.png", xysize=(1920, 1080))
image light_glow_mask = Transform("assets/bg/light_source.png", xysize=(1920, 1080))

## Define character
image alya sick = "assets/chara/alya/alya_sick.png"
image alya idle   = "assets/chara/alya/base_alya.png"
image raka idle = "assets/chara/raka/base_raka.png"
image raka normal = "assets/chara/raka/base_raka.png"
image nisa idle = "assets/chara/nisa/base_nisa.png"
image nisa normal = "assets/chara/nisa/base_nisa.png"

## Define ui
image choice idle = "assets/ui/choice_idle.png"
image choice hover = "assets/ui/choice_hover.png"
image ui main_menu_bg = "assets/ui/BackgroundMainMenu.png"
image ui textbox = "assets/ui/textbox.png"
image ui textbox_dark = "assets/ui/textbox_dark.png"
image ui dialog_dark = "assets/ui/DIalogTextBox_DarkVersion.png"
image ui option_dialog = "assets/ui/OptionDialog_New.png"
image ui chosen_dialog = "assets/ui/ChosenDialog_New.png"
image ui start = "assets/ui/start.png"
image ui start_hover = "assets/ui/BTN__Start.png"
image ui load = "assets/ui/load.png"
image ui load_hover = "assets/ui/BTN_LoadGame.png"
image ui quit = "assets/ui/quit.png"
image ui settings = "assets/ui/SettingsSmall.png"
image ui info = "assets/ui/InfoSmall.png"
image ui volume = "assets/ui/VolumeSmall.png"
image ui back_to_menu = "assets/ui/BackToMenuSmall.png"
image item access_card = "assets/ui/AccessCard_600.png"
image item access_card_large = "assets/ui/AccessCard_850.png"
image item harddisk = "assets/ui/Harddisk_600.png"
image item harddisk_large = "assets/ui/Harddisk_850.png"
image item syringe = "assets/ui/Suntikan_600.png"
image item syringe_large = "assets/ui/Suntikan_850.png"

## Unused
image bg basement_dark = Transform("assets/bg/basement_dark.png", xysize=(1920, 1080))
image bg basement_bright = Transform("assets/bg/basement.png", xysize=(1920, 1080))
