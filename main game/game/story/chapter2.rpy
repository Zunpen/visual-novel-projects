label story_ch2_scene1:

    scene bg hall
    with fade

    play music "assets/audio/bgm/SFX_BGM_Calm.wav" fadein 1.0

    # First-person monologue. Bumi is not shown here so the hallway stays readable.
    bm "Semenjak insiden virus itu 2 tahun lalu..."
    bm "Kami bahkan tidak tahu apa nama virus itu..."
    bm "Pemerintah dunia mengisolasi Indonesia..."

    bm "Bahkan wilayah perbatasan dikosongkan sejauh 30 km."
    bm "Katanya, menurut penelitian, virus ini dapat bertahan dan menyebar lewat udara hingga 25 km dari tubuh manusia."
    bm "Pemerintah yang tugasnya mempersatukan kita malah memecah belah kita."
    bm "Mereka menggunakan segala cara untuk bertahan... bahkan dengan menginjak-injak kami yang di bawah."
    bm "Sialan."
    bm "Kalau begini, apakah hak kami sebagai manusia hanya gurauan belaka?"
    bm "Lihat saja, kami akan memperjuangkan apa yang menjadi hak kami dari pemerintah yang sudah tidak mengenal ideologinya sendiri."

    return

label story_ch2_scene2:

    scene bg hall
    with fade

    play music "assets/audio/bgm/SFX_BGM_Tension.wav" fadeout 0.5 fadein 1.0

    show nisa idle:
        xalign 0.72
        yalign 1.0
        zoom 0.58
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)

    bm "Setelah ketegangan tadi, Nisa meminta izin untuk memantau frekuensi radio keamanan di lorong depan."
    bm "Sebagai ahli hukum yang sangat taat prosedur, seharusnya dia menghindari area dekat pintu keluar karena risiko patroli."
    bm "Tapi dia justru berdiri di sana."
    bm "Aku mengikutinya dari bayang-bayang."

    show expression "assets/chara/bumi/bumi_serius.png" as bumi:
        xalign 0.12
        yalign 1.0
        zoom 0.48
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)
    with fade

    bm "Firasatku tidak enak."
    bm "Perlahan, aku melangkah mendekatinya."
    bm "Apa itu?"
    bm "Itu tidak terlihat seperti radio kelompok."

    n "...Ya. Titik koordinatnya di blok C."
    n "Pastikan unit ekstraksi hanya menargetkan ruang utama."
    n "Jangan sentuh lorong barat... Aku akan memastikan datanya tertahan."

    bm "Unit ekstraksi?"
    bm "Koordinat?"
    bm "Nisa baru saja memutuskan jalur komunikasi."
    bm "Dia memasukkan alat itu ke dalam tas hitamnya yang diletakkan di atas tong kosong, lalu berjalan sebentar ke ujung lorong untuk mengecek jendela."

    if antidote_used_on == "none":
        bm "Aku kaget... tanpa sadar penawar itu terlepas dari genggamanku."

    bm "Nisa... apa yang kau lakukan?"

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

    show expression "assets/chara/bumi/bumi_serius.png" as bumi:
        xalign 0.12
        yalign 1.0
        zoom 0.48
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)

    bm "Aku ragu terlalu lama..."

    jump ch2_confront

label ch2_search_bag:

    $ has_evidence = True

    show expression "assets/chara/bumi/bumi_serius.png" as bumi:
        xalign 0.12
        yalign 1.0
        zoom 0.48
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)

    bm "Tanganku bergerak cepat membuka ritsleting tasnya."
    bm "Di bawah tumpukan dokumen hukum..."
    bm "Sebuah kartu akses militer tingkat elit."
    bm "Lambang kementerian terukir di sana."
    bm "Nisa... kau menjual kami."

    return

label ch2_warn_raka:

    show expression "assets/chara/bumi/bumi_serius.png" as bumi:
        xalign 0.12
        yalign 1.0
        zoom 0.48
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)

    bm "Aku tidak punya waktu."
    bm "Aku harus kembali sekarang."
    bm "Aku menyelinap ke belakang Nisa dan mengikatnya sebelum dia bereaksi."
    bm "Setelah itu, aku kabur bersama Raka dan Alya."

    jump best_ending

label ch2_confront:

    show nisa idle:
        xalign 0.72
        yalign 1.0
        zoom 0.58
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.8)

    bm "Siapa yang kau telepon tadi, Nis?"

    n "Bumi. Mengagetkan saja."
    n "Aku hanya mencoba menyadap frekuensi polisi sektor."
    n "Ada pergerakan di atas."

    bm "Dia berbohong."

    return

label chapter2:

    call story_ch2_scene1
    call story_ch2_scene2

    return
