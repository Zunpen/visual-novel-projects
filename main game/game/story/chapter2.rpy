label story_ch2_scene1:

    scene expression "assets/bg/hall.jpeg"
    with fade

    play music "assets/audio/bgm/SFX_BGM_Calm.wav" fadein 1.0

    # MONOLOG (SLOW → NORMAL)
    bm "Semenjak insiden virus itu 2 tahun lalu..."
    bm "Kami bahkan tidak tahu apa nama virus itu..."
    bm "Pemerintah dunia mengisolasi Indonesia..."

    bm "Bahkan wilayah perbatasan dikosongkan sejauh 30 km."
    bm "Info yang kami dapatkan bahwa menurut penelitian virus ini dapat bertahan dan menyebar lewat udara, bahkan menempuh jarak 25 km dari saat keluar dari tubuh manusia…"
    bm "Pemerintah yang tugasnya mempersatukan kita, malah memecah belah kita, mereka menggunakan segala cara untuk bertahan… bahkan dengan menginjak injak kami yang dibawah…"
    bm "Sialan."
    bm "Kalau begini, apakah hak kami sebagai manusia hanya gurauan belaka?"
    bm "Lihat saja, kami akan memperjuangkan apa yang menjadi hak kami dari pemerintah yang sudah tidak mengenal ideologinya sendiri."
    return

label story_ch2_scene2:

    scene expression "assets/bg/hall.jpeg"
    with fade

    play music "assets/audio/bgm/SFX_BGM_Tension.wav" fadeout 0.5 fadein 1.0

    show nisa idle at center

    # SETUP SITUASI
    "(Nisa meminta izin untuk memantau frekuensi radio keamanan.)"
    "(Sebagai ahli hukum yang sangat taat prosedur, seharusnya dia menghindari area dekat pintu keluar karena risiko patroli.)"

    bm "Firasatku tidak enak."
    "(Perlahan, aku melangkah mendekatinya.)"
    "(Apa itu?)"
    "Itu tidak terlihat seperti radio kelompok"

    n "...Ya. Titik koordinatnya di blok C."
    n "Pastikan unit ekstraksi hanya menargetkan ruang utama."
    n "Jangan sentuh lorong barat..., Aku akan memastikan datanya tertahan."

    bm "Unit ekstraksi?"
    bm "Koordinat?"
    "(Nisa baru saja memutuskan jalur komunikasi.)"
    "(Dia memasukkan alat itu ke dalam tas hitamnya yang diletakkan di atas tong kosong, lalu berjalan sebentar ke ujung lorong untuk mengecek jendela.x)"

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

    show nisa idle at center

    bm "Siapa yang kau telepon tadi, Nis?"

    n "Bumi. Mengagetkan saja."
    n "Aku hanya menyadap frekuensi polisi sektor."

    bm "Dia berbohong."

    return

label chapter2:

    call story_ch2_scene1
    call story_ch2_scene2

    return
