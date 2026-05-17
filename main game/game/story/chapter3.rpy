label story_ch3_scene1:

    scene bg server:
        matrixcolor BrightnessMatrix(-0.2) * ContrastMatrix(0.95)
    show red_alert_overlay
    with flash

    play music audio.bgm_action fadeout 0.5 fadein 0.5
    play sound audio.sfx_warning

    bm "Alarm merah menyapu ruang server utama."
    bm "Suara benturan dari pintu besi membuat lantai bergetar."

    r "Sial! Sial! Mereka memotong jalur kita dari luar!"
    r "Enkripsi lapisan ketiga sudah jebol!"
    r "Pasukan bersenjata ada di lobi atas, dan mereka akan turun ke sini!"
    r "Tahan mereka selama mungkin!"

    play sound audio.sfx_impact

    bm "Suara tembakan terdengar dari tangga."
    bm "Gas air mata mulai merembes dari ventilasi, membuat layar monitor tampak kabur."

    show alya sick:
        xalign 0.18
        yalign 1.0
        zoom 0.48
        matrixcolor BrightnessMatrix(-0.18) * ContrastMatrix(0.85)
    with moveinleft

    a "Bumi... uhuk!"
    a "Datanya... apakah sudah..."

    show raka idle:
        xalign 0.82
        yalign 1.0
        zoom 0.52
        matrixcolor BrightnessMatrix(-0.18) * ContrastMatrix(0.85)
    with moveinright

    r "Tinggal 90%%!"
    r "Unduhan algoritma Seleksi Teladan butuh dua menit lagi untuk masuk ke hardisk portabel!"
    r "Kalau kucabut sekarang, filenya corrupt!"

    return

label story_ch3_scene2:

    show nisa normal:
        xalign 0.52
        yalign 1.0
        zoom 0.58
        matrixcolor BrightnessMatrix(-0.05) * ContrastMatrix(0.9)
    with fade

    n "Waktu kalian sudah habis."
    n "Tolong menyerahlah."
    n "Prosedur penahanan akan lebih lunak jika kalian tidak melawan."

    a "Nisa... apa yang..."
    a "Kau yang membawa mereka ke sini?"

    n "Aku menyelamatkan masa depan, Alya."
    n "Bumi, ikutlah denganku sekarang."
    n "Mereka memiliki perintah untuk tidak menembak kita berdua jika kau menyerahkan hardisk itu padaku."

    play sound audio.sfx_door_kick
    with flash

    bm "Pintu besi utama didobrak."
    bm "Bayangan pasukan keamanan dengan masker gas mulai terlihat di antara asap."

    return

label story_ch3_scene3:

    show item harddisk:
        xalign 0.5
        yalign 0.45
        zoom 0.22
    with moveinright

    r "BAWA DATANYA, BUMI!"
    r "Lari lewat jalur gorong-gorong!"

    a "Tinggalkan aku..."
    a "Sebarkan kebenarannya..."

    bm "Waktu membeku."
    bm "Pasukan merangsek masuk."
    bm "Nisa mengulurkan tangannya, menawarkan keselamatan palsu."
    bm "Raka bersiap menjadi tameng hidup."
    bm "Alya sekarat di lantai."
    bm "Di tanganku ada kebenaran yang bisa menghancurkan negara, tapi harganya adalah nyawa mereka."

    hide item harddisk
    with dissolve

    return

label story_ch3_choice:

    "KEPUTUSAN FINAL. APA YANG KAU LAKUKAN?"

    menu:
        "Angkat Alya dan lari tanpa hardisk":
            jump ch3_save_alya

        "Genggam hardisk, biarkan Raka menahan pintu":
            jump ch3_take_data

        "Gunakan kartu akses Nisa":
            if has_evidence:
                jump ch3_true_route
            else:
                bm "Tanganku meraba saku, tapi aku tidak punya kartu akses itu."
                bm "Tidak ada yang bisa kugunakan untuk menghentikan pasukan."
                jump ch3_take_data

        "Raih tangan Nisa dan serahkan hardisk":
            jump ch3_join_nisa

label ch3_save_alya:

    bm "Aku tidak bisa meninggalkannya."
    bm "Hardisk itu jatuh dari tanganku saat aku mengangkat tubuh Alya."

    if antidote_used_on == "alya":
        jump normal_ending
    else:
        jump bad_ending

label ch3_take_data:

    bm "Aku menggenggam hardisk itu sampai buku jariku memutih."
    bm "Kebenaran harus keluar, apa pun harganya."

    jump tragic_ending

label ch3_true_route:

    show item access_card_large:
        xalign 0.5
        yalign 0.42
        zoom 0.34
    with dissolve

    b "Komandan!"
    b "Sesuai Protokol Darurat Pasal 7, saya memegang otorisasi pembatalan operasi tingkat elit!"

    n "I-itu... dari mana kau..."
    n "Komandan, jangan dengarkan dia!"

    c "Tunggu."
    c "Itu akses level satu."
    c "Siapa target sebenarnya di ruangan ini?"

    b "Targetnya adalah dia!"
    b "Nisa adalah agen ganda yang mencoba menyabotase aset data kementerian."

    hide item access_card_large
    with dissolve

    jump true_ending

label ch3_join_nisa:

    bm "Aku melihat Alya yang batuk darah, lalu Raka yang masih memaksakan diri di depan monitor."
    bm "Lalu aku menatap statistik di layar yang berkedip."
    bm "Nisa benar. Kita tidak bisa menyelamatkan semua orang."

    b "Pastikan tidak ada data yang tersisa, Nisa."

    jump secret_ending

label chapter3:

    call story_ch3_scene1
    call story_ch3_scene2
    call story_ch3_scene3
    call story_ch3_choice

    return
