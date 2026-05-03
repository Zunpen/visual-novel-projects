label normal_ending:

    scene bg sewer
    with fade

    play music audio.bgm_sad fadein 1.0

    bm "Hardisk itu hancur..."

    a "Bumi... datanya hilang..."
    a "Raka... mati sia-sia..."

    b "Aku tidak bisa kehilangan semuanya..."

    bm "Kami selamat..."
    bm "Tapi dunia ini tetap sama."

    return

label bad_ending:

    scene bg sewer
    with fade

    play music audio.bgm_sad fadein 1.0

    bm "Aku terlambat..."

    a "Terlambat... Bumi..."

    bm "Alya mati di pelukanku."

    bm "Raka mati."
    bm "Semua hancur."

    return

label tragic_ending:

    scene bg broadcast
    with fade

    play music audio.bgm_tense fadein 1.0

    bm "Aku berlari tanpa henti."

    bm "Hardisk ini... adalah segalanya."

    bm "Siaran berhasil dibajak."

    bm "Kebenaran tersebar."

    b "Tugas kita selesai..."

    bm "Kami menang..."
    bm "Tapi tidak ada yang tersisa untuk melihatnya."

    return

label true_ending:

    scene bg basement
    with flash

    play music audio.bgm_main fadein 1.0

    b "Komandan! Aku memegang otorisasi elit!"

    n "Itu mustahil!"

    bm "Pasukan ragu."

    b "Targetnya adalah Nisa!"

    bm "Kesempatan itu cukup."

    bm "Kami kabur."

    scene bg broadcast
    with fade

    r "Data siap disiarkan."

    a "Kita berhasil..."

    bm "Kebenaran akhirnya terbuka."

    return

label secret_ending:

    scene bg basement
    with fade

    play music audio.bgm_sad fadein 1.0

    bm "Aku memilih logika."

    r "Bumi...? Apa yang kau lakukan?"

    a "Bumi... jangan..."

    n "Keputusan yang tepat."

    bm "Aku menyerahkan hardisk itu."

    scene bg office
    with fade

    bm "Dua tahun kemudian..."

    n "Kita harus mengurangi populasi."

    b "Lakukan."

    bm "Aku menyelamatkan dunia..."

    bm "Dengan kehilangan kemanusiaanku."

    return

label best_ending:

    scene bg broadcast
    with fade

    play music audio.bgm_main fadein 1.0

    bm "Rezim runtuh."

    if antidote_used_on == "alya":

        show alya sick
        a "Dengarkan aku semua!"
        a "Jangan hancurkan fasilitas penawar!"

        bm "Alya memimpin revolusi."

    elif antidote_used_on == "raka":

        show raka normal
        r "Aku sudah menyebarkan rumus penawar!"

        bm "Raka membebaskan dunia dari ketergantungan."

    bm "Kami menang."

    b "Ayo kita pulang."

    return