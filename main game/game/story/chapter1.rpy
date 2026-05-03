label story_ch1_intro:

    # =========================
    # SCENE SETUP
    # =========================
    scene bg basement
    with fade

    play music audio.bgm_main fadein 1.0

    # MONOLOG BUMI (SLOW)
    bm "Dunia ini sedang membusuk."
    bm "Udara di luar lebih pantas disebut racun."
    bm "Di atas meja ini... hanya tersisa satu tabung penawar."

    # ALYA MASUK (FAST)
    show alya sick at left
    with moveinleft

    a "Bumi... protes di Sektor 4 tadi..."
    a "Mereka menembakkan gas saraf..."
    a "Warga... mereka butuh suplai kita..."

    # RAKA MASUK (FAST)
    show raka normal at right
    with moveinright

    r "Jangan gila, Al!"
    r "Kalau kau berikan tabung terakhir itu ke luar, kau yang mati malam ini!"
    r "Filter udara ruangan kita mau jebol!"
    r "Aku butuh fokus untuk meretas sistem ventilasi pusat!"


    # NISA MASUK (SLOW)
    show nisa normal at center
    with fade

    n "Secara statistik, Alya, tindakanmu hari ini adalah bunuh diri."
    n "Bumi, tabung penawar itu harapan terakhir kita."
    n "Berikan pada Raka."
    a "Nyawa manusia bukan sekadar aset, Nisa!"
    a "Jika kita membiarkan mereka mati, kita tidak ada bedanya dengan pemerintah itu!"

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

    bm "Selesaikan retasanmu, Raka."
    r "Pilihan yang logis."
    return


label ch1_result_none:

    bm "Belum saatnya digunakan."
    n "Keputusan yang... menarik."
    return

label chapter1:

    call story_ch1_intro
    call story_ch1_choice

    return