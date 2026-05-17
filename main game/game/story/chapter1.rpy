label story_ch1_intro:

    # =========================
    # SCENE SETUP
    # =========================
    scene bg apartment
    with fade
    $ renpy.music.set_volume(0.5, channel='music')
    play music audio.bgm_pianos fadein 1.0

    # MONOLOG BUMI (SLOW)
    bm "Pemerintah kita telah menghancurkan negara kita sendiri... "
    bm "HAM yang dulu mereka perjuangkan itu, kini telah mereka lupakan.."
    bm "Seleksi Teladan... mengharuskan kami untuk diseleksi agar dapat bekerja untuk pemerintah demi menjaga Indonesia tetap berjalan"
    bm "Tetapi, Upah kami hanya 1 botol oksigen per minggu yang bahkan hanya cukup 1 hari."


    scene bg basement:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.9)
    show light_glow_mask at flicker_light zorder 100:
        xpos -0.01
        zoom 1.2
    stop music
    play music bgm_basement
    $ renpy.music.set_volume(1.0, channel='music')
    with fade
    bm "Dunia ini sedang membusuk."
    bm "Udara di luar lebih pantas disebut racun."

    show dark zorder 101:
        alpha 0.6
    show antidote at center, zorder 102:
        ypos 0.7
    with dissolve

    bm "Di atas meja ini... hanya tersisa satu tabung penawar."
    hide dark
    hide antidote 
    with Dissolve(1.0)

    # ALYA MASUK (FAST)
    show alya sick at chara_left:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with moveinleft 

    $ renpy.music.set_volume(0.5, channel='audio')
    play audio girlcough
    a "Bumi... tadi ada protes di Sektor 4..."
    a "Mereka menembakkan gas saraf..."
    $ renpy.music.set_volume(0.3, channel='sound')
    play sound alyasick2
    a "Warga... mereka butuh suplai kita..."

    # RAKA MASUK (FAST)
    show raka idle at right, raka:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with moveinright

    r "Jangan gila woiii, Al!" 
    r "Kalau lu berikan tabung terakhir itu ke luar, lu yang mati lah malam ini!, gimana sih... Lagipula..."
    r "Filter udara ruangan kita mau jebol!"
    r "Gua juga butuh fokus untuk meretas sistem ventilasi pusat itu guys, tapi tangan gua tidak bisa berhenti gemetar karena racun ini."


    # NISA MASUK (SLOW)
    show nisa idle at center, nisa:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with fade

    n "Secara statistik, Alya, tindakanmu turun ke jalan hari ini murni bunuh diri."
    n "Bumi, tabung penawar itu harapan terakhir kita."
    n "Berikan pada Raka."
    n "Jika kita mati tercekik di rubanah ini, revolusi yang diteriakkan Alya tidak akan pernah terjadi."
    a "Nyawa manusia bukan sekadar aset LHOOOO, Nisa!"
    a "Jika kita membiarkan mereka mati malam ini, apa bedanya kita dengan pemerintah saat ini?"

    # MONOLOG BUMI (NORMAL)
    "Alya menatapku dengan mata memohon, meski paru-parunya hancur."
    "Raka menatap layarnya, tapi keringat dingin membanjiri pelipisnya, dia tetap bersikap seolah ini semua tidak apa- apa padahal dia sedang menderita."
    "Dan Nisa... dia hanya menatap tabung itu dengan perhitungan matematis."


    return

label story_ch1_choice:

    # SYSTEM PROMPT
    #play music audio.bgm_tense fadein 0.5
    show light_glow_mask at flashing, zorder 100:
        xpos -0.01
        zoom 1.2
    with Dissolve(0.5)
    "Aku harus memilih."

    menu:
        "Tidak ada waktu. Siapa yang kau selamatkan?!"
        "Suntikkan penawar ke Alya":
            $ antidote_used_on = "alya"
            jump ch1_result_alya

        "Berikan ke Raka":
            $ antidote_used_on = "raka"
            jump ch1_result_raka

        "Simpan penawar":
            $ antidote_used_on = None
            jump ch1_result_none


label ch1_result_alya:

    bm "Aku tidak akan mengorbankan nyawa demi angka."
    play sound alyasatisfied
    a "Terima kasih... Bumi..."
    show light_glow_mask:
        xalign 0.5
        matrixcolor BrightnessMatrix(0.0)
        linear 0.4 matrixcolor BrightnessMatrix(1.0)
        linear 0.4 zoom 6.0
    pause 1
    play sound sfx_bulb
    return


label ch1_result_raka:

    bm "Selesaikan retasanmu, Raka. Kita butuh jalan keluar"
    show light_glow_mask:
        xalign 0.5
        matrixcolor BrightnessMatrix(0.0)
        linear 0.4 matrixcolor BrightnessMatrix(1.0)
        linear 0.4 zoom 6.0
    pause 1
    play sound audio.sfx_bulb
    return


label ch1_result_none:

    bm "Belum saatnya digunakan."
    show light_glow_mask:
        xalign 0.5
        matrixcolor BrightnessMatrix(0.0)
        linear 0.4 matrixcolor BrightnessMatrix(1.0)
        linear 0.4 zoom 6.0
    pause 1
    play sound audio.sfx_bulb
    return

label chapter1:

    call story_ch1_intro
    call story_ch1_choice

    return