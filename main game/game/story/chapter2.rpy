<<<<<<< HEAD
label story_ch2_scene1:

    scene dark
    pause 3.0
    scene bg corridor dark with Dissolve(1.2)
    pause 2.0
    show bg corridor with Dissolve(5.0)

    # play music audio.placeholder fadein 1.0 (Suara drone patroli terdengar samar dari kejauhan. Musik berubah menjadi misterius/tegang)

    # MONOLOG (SLOW → NORMAL)
    "Semenjak insiden virus itu 2 tahun lalu..."
    "Kami bahkan tidak tahu apa nama virus itu..."
    "Pemerintah dunia mengisolasi Indonesia..."

    "Bahkan wilayah perbatasan dikosongkan sejauh 30 km."
    "Info yang kami dapatkan bahwa menurut penelitian virus ini dapat bertahan dan menyebar lewat udara, bahkan menempuh jarak 25 km dari saat keluar dari tubuh manusia…"
    "Pemerintah yang tugasnya mempersatukan kita, malah memecah belah kita, mereka menggunakan segala cara untuk bertahan… bahkan dengan menginjak injak kami yang dibawah…"
    "Sialan."
    "Kalau begini, apakah hak kami sebagai manusia hanya gurauan belaka?"
    "Lihat saja, kami akan memperjuangkan apa yang menjadi hak kami dari pemerintah yang sudah tidak mengenal ideologinya sendiri."
    return

label story_ch2_scene2:


    #play music audio.bgm_tense fadein 1.0

    show nisa idle at center:
        yalign 0.5
        zoom 0.09
        matrixcolor BrightnessMatrix(-0.80) * ContrastMatrix(0.20)
    with fade

    # SETUP SITUASI
    "Nisa meminta izin untuk memantau frekuensi radio keamanan."
    "Sebagai ahli hukum yang sangat taat prosedur, seharusnya dia menghindari area dekat pintu keluar karena risiko patroli."
    "Tapi dia justru berdiri di sana"

    bm "Firasatku tidak enak."
    "Perlahan, aku melangkah mendekatinya."
    show nisa idle at center:
        yalign 0.6
        zoom 0.3
        matrixcolor BrightnessMatrix(-0.80) * ContrastMatrix(0.20)
    with fade
    "Apa itu?"
    "Itu tidak terlihat seperti radio kelompok"

    n "...Ya. Titik koordinatnya di blok C."
    n "Pastikan unit ekstraksi hanya menargetkan ruang utama."
    n "Jangan sentuh lorong barat..., Aku akan memastikan datanya tertahan."

    bm "Unit ekstraksi?"
    bm "Koordinat?"
    "(Nisa baru saja memutuskan jalur komunikasi.)"
    "(Dia memasukkan alat itu ke dalam tas hitamnya yang diletakkan di atas tong kosong, lalu berjalan sebentar ke ujung lorong untuk mengecek jendela.)"

    show nisa idle at center:
        yalign 0.5
        zoom 0.09
        matrixcolor BrightnessMatrix(-0.80) * ContrastMatrix(0.20)
    with fade

    if antidote_used_on == None:
        bm "Sial!"

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

    "Tanganku bergerak cepat membuka tasnya."
    show dark zorder 101:
        alpha 0.6
    show access card at center, zorder 102:
        ypos 0.7
    with dissolve

    "Di bawah dokumen hukum, aku menemukan kartu akses militer tingkat elit"

    hide dark
    hide access 
    with Dissolve(1.0)
    bm "Nisa... kau menjual kami."

    return

label ch2_warn_raka:

    $ best_route = 1
    bm "Aku tidak punya waktu."
    bm "Aku harus cepat bertindak."
    bm "Sekarang waktunya."
    show nisa idle at center:
        yalign 0.6
        zoom 0.3
        matrixcolor BrightnessMatrix(-0.80) * ContrastMatrix(0.20)
    with Dissolve(1.0)
    pause 2.0
    show nisa idle at center, nisa:
        ypos -0.1
        zoom  0.8
        matrixcolor BrightnessMatrix(-0.60) * ContrastMatrix(0.20)
    with dissolve
    pause 2.0
    hide nisa idle
    with fade
    #play sound audio.sfx_choke
    play sound audio.sfx_clothes

    n "Ap..!"
    n "Bumi!"
    n "Keparat... Apa yang kau lakuk-"
    # Shortcut langsung ke ending terbaik (sesuai flowchart)
    jump best_ending

label ch2_confront:

    show nisa idle at center:
        yalign 0.6
        zoom 0.3
        matrixcolor BrightnessMatrix(-0.80) * ContrastMatrix(0.20)
    with Dissolve(1.0)
    pause 2.0
    show nisa idle at center, nisa:
        ypos -0.1
        zoom  0.8
        matrixcolor BrightnessMatrix(-0.60) * ContrastMatrix(0.20)
    with dissolve
    pause 2.0
    show nisa idle at center, nisa:
        ypos -0.1
        zoom 0.8
        matrixcolor BrightnessMatrix(-0.80)
    show nisa idle at jump:
        ypos -0.1
        linear 0.2 matrixcolor BrightnessMatrix(-0.2)


    bm "Siapa yang kau telepon tadi, Nis?"
    n "Bumi... "
    n "Mengagetkan saja."
    n "Aku hanya menyadap frekuensi polisi sektor. Ada pergerakan di atas."

    return

label chapter2:

    call story_ch2_scene1
    call story_ch2_scene2

=======
label story_ch2_scene1:

    scene bg corridor
    with fade

    # play music audio.placeholder fadein 1.0 (Suara drone patroli terdengar samar dari kejauhan. Musik berubah menjadi misterius/tegang)

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

    scene bg corridor
    with fade

    play music audio.bgm_tense fadein 1.0

    show nisa normal at center

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

    show nisa normal at center

    bm "Siapa yang kau telepon tadi, Nis?"

    n "Bumi. Mengagetkan saja."
    n "Aku hanya menyadap frekuensi polisi sektor."

    bm "Dia berbohong."

    return

label chapter2:

    call story_ch2_scene1
    call story_ch2_scene2

>>>>>>> 9cb7361821f62c8560ade3094d67531a5ef54315
    return