label story_ch3_scene1:

    stop music fadeout 0.5
    play music bgm_tense fadein 1.0

    scene bg basement:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.9)
    show light_glow_mask at flicker_light zorder 100:
        xpos -0.01
        zoom 1.2
    show raka idle at center, raka, bounce_limited
    with fade
    #play music audio.bgm_tense fadein 0.5
    

    play sound ketik
    r "Sial! Sial! Mereka memotong jalur kita dari luar guysss, gimana iniii???!!!!, mati kita wokkk"
    r "Enkripsi lapisan ketiga udah jebol! Pasukan bersenjata ada di lobi atas, dan akan turun ke siniii, tolong tahan mereka selama mungkinnnn woiiii!"

    show alya sick at left, chara_left, slow_slide
    a "Bumi... uhuk! Datanya... apakah sudah"
    show raka idle at center, raka, jump
    r "90%%! Unduhan algoritma Seleksi Teladan butuh dua menit lagi untuk masuk ke harddisk portabel! Kalau kucabut sekarang, filenya corrupt!"

    return

label story_ch3_scene2:
    
    scene bg basement:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.9)
    show light_glow_mask at flicker_light zorder 100:
        xpos -0.01
        zoom 1.2
    show nisa idle at center, nisa
    with fade 
    stop sound
    play audio doorslam

    n "Waktu kalian habis. Tolong menyerahlah. Prosedur penahanan akan lebih lunak jika kalian tidak melawan."

    a "Nisa... apa yang... kau yang membawa mereka ke sini?!"

    n "Aku menyelamatkan masa depan, Alya. Bumi, ikutlah denganku sekarang. Mereka memiliki perintah untuk tidak menembak kita berdua jika kau menyerahkan harddisk itu padaku."
    play sound gasleak
    "Sial! Apa yang harus kulakukan? Kita terkepung dan gas sudah mulai masuk!"


    return

label story_ch3_scene3:

    show dark zorder 101:
        alpha 0.6
    show harddisk at center, zorder 102:
        ypos 0.7
    with dissolve

    r "BAWA DATANYA WOIIII, BUMI!"
    hide dark
    hide harddisk
    show gas zorder 101:
        alpha 0.2
    with dissolve

    r "MENDING LU LARI LEWAT JALUR GORONG-GORONG!"

    a "Tinggalkan aku... bumi... sebarkan kebenarannya..."

    "Waktu membeku."
    "Pasukan merangsek masuk. Nisa mengulurkan tangannya menawarkan keselamatan palsu. Raka bersiap menjadi tameng hidup. Alya sekarat di lantai."
    "Di tanganku ada kebenaran yang bisa menghancurkan negara, tapi harganya adalah nyawa mereka."

    return

label story_ch3_choice:
    
    show gas:
        alpha 0.4
    with dissolve

    "Keputusan final. Apa yang kau lakukan?"

    menu:
        "Selamatkan Alya":
            jump ch3_save_alya

        "Ambil data dan lari":
            jump ch3_take_data

        "Gunakan kartu akses Nisa":
            if has_evidence:
                jump ch3_true_route
            else:
                "Aku tidak punya apa-apa untuk melawan mereka..."
                jump ch3_take_data

        "Ikut Nisa":
            jump ch3_join_nisa

label ch3_save_alya:

    bm "Aku tidak bisa meninggalkannya."

    if antidote_used_on == "alya":
        jump normal_ending
    else:
        jump bad_ending

label ch3_take_data:

    bm "Kebenaran lebih penting dari segalanya."
    stop music fadeout 0.5
    stop audio fadeout 0.5
    stop sound fadeout 0.5
    scene dark
    with Dissolve(1.0)
    play sound doorslam
    pause 0.5
    play sound running
    play sound gunshot
    pause 2.0

    jump tragic_ending


label ch3_true_route:
    show dark zorder 101:
        alpha 0.6
    show access card at center, zorder 102:
        ypos 0.7
    with dissolve

    bm "Aku punya ini."

    jump true_ending

label ch3_join_nisa:

    bm "Ini satu-satunya cara bertahan."

    jump secret_ending

label chapter3:

    call story_ch3_scene1 from _call_story_ch3_scene1
    call story_ch3_scene2 from _call_story_ch3_scene2
    call story_ch3_scene3 from _call_story_ch3_scene3
    call story_ch3_choice from _call_story_ch3_choice

    return