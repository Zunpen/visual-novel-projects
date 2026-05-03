label story_ch2_scene1:

    scene bg corridor
    with fade

    play music audio.bgm_main fadein 1.0

    # MONOLOG (SLOW → NORMAL)
    bm "Semenjak insiden virus itu 2 tahun lalu..."
    bm "Kami bahkan tidak tahu apa nama virus itu..."
    bm "Pemerintah dunia mengisolasi Indonesia..."

    bm "Bahkan wilayah perbatasan dikosongkan sejauh 30 km."
    bm "Siapa pun yang mencoba keluar... dieksekusi."

    bm "Virus ini menyebar lewat udara..."
    bm "Dan kini... pemerintah menggunakan itu untuk mengontrol kami."

    bm "Kami ingin menjadi harapan bangsa ini."
    bm "Pejuang keadilan..."

    return

label story_ch2_scene2:

    scene bg corridor
    with fade

    play music audio.bgm_tense fadein 1.0

    show nisa normal at center

    # SETUP SITUASI
    bm "Nisa meminta izin untuk memantau frekuensi radio keamanan."
    bm "Tapi... dia berdiri terlalu dekat dengan lorong keluar."

    bm "Aku mengikutinya dari bayang-bayang."

    n "...Ya. Titik koordinatnya di blok C."
    n "Pastikan unit ekstraksi hanya menargetkan ruang utama."
    n "Jangan sentuh lorong barat..."

    bm "Unit ekstraksi?"
    bm "Koordinat?"

    bm "Nisa... apa yang kau lakukan?"

    # TIMED CHOICE (5 DETIK)
    call screen timed_choice(
        [
            ("Geledah tas Nisa", Jump("ch2_search_bag")),
            ("Peringatkan Raka", Jump("ch2_warn_raka")),
            ("Konfrontasi Nisa", Jump("ch2_confront"))
        ],
        5.0,
        "ch2_timeout"
    )

    return

label ch2_timeout:

    bm "Aku ragu terlalu lama..."

    jump ch2_confront

label ch2_search_bag:

    $ has_evidence = True

    bm "Tanganku bergerak cepat membuka tasnya."
    bm "Di bawah dokumen hukum..."

    bm "Sebuah kartu akses militer elit."

    bm "Nisa... kau menjual kami."

    return

label ch2_warn_raka:

    bm "Aku tidak punya waktu."
    bm "Aku harus kembali sekarang."

    bm "Aku menyelinap dan mengikat Nisa sebelum dia bereaksi."

    # Shortcut langsung ke ending terbaik (sesuai flowchart)
    jump best_ending

label ch2_confront:

    show nisa normal at center

    bm "Siapa yang kau telepon tadi, Nis?"

    n "Bumi. Mengagetkan saja."
    n "Aku hanya menyadap frekuensi polisi sektor."

    bm "Dia berbohong."

    return

label chapter2:

    call story_ch2_scene1
    call story_ch2_scene2

    return