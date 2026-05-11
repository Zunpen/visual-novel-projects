label story_ch1_intro:

    # =========================
    # SCENE SETUP
    # =========================
    scene bg placeholder
    with fade

    play music audio.bgm_main fadein 1.0

    # MONOLOG BUMI (SLOW)
    bm "Pemerintah kita telah menghancurkan negara kita sendiri... "
    bm "HAM yang dulu mereka perjuangkan itu, kini telah mereka lupakan.."
    bm "Seleksi Teladan... mengharuskan kami untuk diseleksi agar dapat bekerja untuk pemerintah demi menjaga Indonesia tetap berjalan"
    bm "Tetapi, Upah kami hanya 1 botol oksigen per minggu yang bahkan hanya cukup 1 hari."

    scene bg basement:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.9)
        zoom 1.2
    show light_glow_mask at flicker_light zorder 100:
        xpos -0.01
        zoom 1.2
    with fade
    bm "Dunia ini sedang membusuk."
    bm "Udara di luar lebih pantas disebut racun."
    bm "Di atas meja ini... hanya tersisa satu tabung penawar."

    # ALYA MASUK (FAST)
    show alya sick at chara_left:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with moveinleft

    a "Bumi... protes di Sektor 4 tadi..."
    a "Mereka menembakkan gas saraf..."
    a "Warga... mereka butuh suplai kita..."

    # RAKA MASUK (FAST)
    show raka idle at right, chara_right:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with moveinright

    r "Jangan gila, Al!"
    r "Kalau kau berikan tabung terakhir itu ke luar, kau yang mati malam ini!"
    r "Filter udara ruangan kita mau jebol!"
    r "Aku butuh fokus untuk meretas sistem ventilasi pusat, tapi tanganku tidak bisa berhenti gemetar karena racun ini."


    # NISA MASUK (SLOW)
    show nisa idle at center, chara_middle:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with fade

    n "Secara statistik, Alya, tindakanmu hari ini adalah bunuh diri."
    n "Bumi, tabung penawar itu harapan terakhir kita."
    n "Berikan pada Raka."
    n "Jika kita mati tercekik di rubanah ini, revolusi yang diteriakkan Alya tidak akan pernah terjadi."
    a "Nyawa manusia bukan sekadar aset, Nisa!"
    a "Jika kita membiarkan mereka mati malam ini, apa bedanya kita dengan pemerintah saat ini?"

    # MONOLOG BUMI (NORMAL)
    bm "Alya menatapku dengan mata memohon..."
    bm "Raka berusaha tetap fokus meski tubuhnya gemetar..."
    bm "Dan Nisa... hanya melihat ini sebagai perhitungan."

    bm "Aku harus memilih."

    return

label story_ch1_choice:

    # SYSTEM PROMPT
    play music audio.bgm_tense fadein 0.5

    "WAKTU MENIPIS. SIAPA YANG KAU SELAMATKAN?"

    menu:
        "Suntikkan penawar ke Alya":
            $ antidote_used_on = "alya"
            jump ch1_result_alya

        "Berikan ke Raka":
            $ antidote_used_on = "raka"
            jump ch1_result_raka

        "Simpan penawar":
            $ antidote_used_on = "none"
            jump ch1_result_none

label ch1_result_alya:

    bm "Aku tidak akan mengorbankan nyawa demi angka."
    a "Terima kasih... Bumi..."
    return


label ch1_result_raka:

    bm "Selesaikan retasanmu, Raka. Kita butuh jalan keluar"
    return


label ch1_result_none:

    bm "Belum saatnya digunakan."
    return

label chapter1:

    call story_ch1_intro
    call story_ch1_choice

    return