## assets.rpy - Definisi atau List assets pada game


#Contoh code :
#define audio.bgm_main = "audio/main_theme.mp3"
#define audio.bgm_tense = "audio/tense.mp3"
#define audio.bgm_sad = "audio/sad.mp3"
#image bg basement = "assets/bg/basement.png"
#image bg corridor = "assets/bg/corridor.png"
#image alya sick = "assets/sprites/alya_sick.png"


## Define audio
define audio.sfx_bulb = "assets/audio/bulb.mp3"
define audio.sfx_clothes = "assets/audio/clothes_rustle.mp3"
define audio.bgm_basement = "assets/audio/basement.wav"
define audio.bgm_broadcast = "assets/audio/broadcast.wav"
define audio.bgm_pianos = "assets/audio/pianos.wav"
define audio.bgm_sewer = "assets/audio/sewer.wav"
define audio.bgm_tense = "assets/audio/tense.mp3"
define audio.bgm_hallway = "assets/audio/hallway.wav"
define audio.bgm_bestending = "assets/audio/best_ending.mp3"
define audio.bgm_aftermath = "assets/audio/aftermath.mp3"
define audio.bgm_normalending = "assets/audio/normal_ending.mp3"
define audio.bgm_secretending = "assets/audio/secret_ending.wav"
define audio.bgm_trueending = "assets/audio/true_ending.mp3"
define audio.girlcough = "assets/audio/sfx/SFX_GirlCough.mp3"
define audio.gasleak = "assets/audio/sfx/SFX_GasLeak.mp3"
define audio.gunshot = "assets/audio/sfx/SFX_HELLFIREGUNSHOT.mp3"
define audio.ketik = "assets/audio/sfx/SFX_Ketik.mp3"
define audio.warn = "assets/audio/sfx/SFX_Warning.mp3"
define audio.doorslam = "assets/audio/sfx/door_slam.mp3"
define audio.sewerrun = "assets/audio/sfx/sewerrun.mp3"
define audio.electricalhum = "assets/audio/sfx/SFX_ElectricalHum.mp3"
define audio.hdd_drop = "assets/audio/sfx/hdd_drop.wav"
define audio.unzip = "assets/audio/sfx/unzips.mp3"
define audio.running = "assets/audio/sfx/running.mp3"
define audio.broadcasterror1 = "assets/audio/sfx/broadcast_error1.wav"
define audio.broadcasterror2 = "assets/audio/sfx/broadcast_error2.wav"
define audio.protest = "assets/audio/sfx/protest.mp3"
define audio.walkie = "assets/audio/sfx/walkie.mp3"

## Define images
image gas = Solid("#9a9a9a")
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
image bg apartment = Movie(
    play="assets/bg/apart.webm",
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

##Bonue - Define Voice
define audio.alyasatisfied = "assets/audio/SE/alya_satisfied.mp3"
define audio.alyasick1 = "assets/audio/SE/alya_sick.mp3"
define audio.alyasick2 = "assets/audio/SE/alya_sick2.mp3"
define audio.nisasurprised = "assets/audio/SE/nisa_surprised.wav"
define audio.alyaquestioning = "assets/audio/SE/alyaquestioning.mp3"

## Unused
image bg basement_bright = "assets/bg/basement.png"