label normal_ending:

    scene bg sewer:
        matrixcolor BrightnessMatrix(-0.2) * ContrastMatrix(0.9)
    with fade

    play music audio.bgm_sad fadein 1.0

    show alya idle:
        xalign 0.5
        yalign 1.0
        zoom 0.52
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.85)
    with dissolve

    bm "Hardisk itu terlepas dari tanganku saat aku mengangkat tubuh Alya."
    bm "Aku melihat sepatu pasukan menginjak benda itu hingga hancur."
    bm "Di belakang kami, suara tembakan meredam teriakan Raka."
    bm "Aku tidak pernah menoleh lagi."

    a "Bumi... datanya hancur..."
    a "Raka... mati sia-sia..."
    a "Kenapa kau membawaku dan membiarkannya mati di sana?"

    b "Aku tidak bisa kehilangan kalian semua dalam satu malam."
    b "Kau butuh hidup untuk memimpin pergerakan ini, Al."

    a "Memimpin apa tanpa bukti?"
    a "Tanpa data itu, Nisa menang."
    a "Pemerintah menang."

    bm "Kami selamat."
    bm "Fisik Alya pulih karena penawar itu, tapi api di dalam dirinya padam."
    bm "Tanpa bukti algoritma Seleksi Teladan, massa perlahan kembali tunduk pada jam kerja pemerintah."
    bm "Kami bertahan hidup di bawah tanah, tapi sekadar bernapas bukanlah kehidupan."

    centered "NORMAL ENDING - Gema yang Pudar"

    return

label bad_ending:

    scene bg sewer:
        matrixcolor BrightnessMatrix(-0.35) * ContrastMatrix(0.85)
    with fade

    play music audio.bgm_sad fadein 1.0

    show alya sick:
        xalign 0.5
        yalign 1.0
        zoom 0.48
        matrixcolor BrightnessMatrix(-0.55) * ContrastMatrix(0.75)
    with dissolve

    bm "Hardisk itu hancur diinjak pasukan."
    bm "Suara tembakan merenggut nyawa Raka di ruang server."
    bm "Aku memapah Alya sekuat tenaga menyusuri gorong-gorong, tapi tubuhnya semakin dingin."

    a "Terlambat, Bumi..."
    a "Kau merelakan data Raka..."
    a "Dan kau membiarkanku mati tanpa membawa kebenaran apa pun..."

    b "Tidak, Al."
    b "Kumohon, jangan tutup matamu."

    a "Ini semua... sia-sia..."

    hide alya
    with fade

    bm "Hening."
    bm "Gorong-gorong ini menjadi makamnya."
    bm "Raka tewas. Alya mati di pelukanku. Nisa mengkhianati kami."
    bm "Keputusan-keputusanku yang setengah hati menghancurkan segalanya."
    bm "Pemerintah kini berkuasa mutlak, dan aku hanya tersisa sebagai bayangan yang menunggu dihapus dari sistem."

    centered "BAD ENDING - Tirani Tanpa Wajah"

    return

label tragic_ending:

    scene bg broadcast:
        matrixcolor BrightnessMatrix(-0.1) * ContrastMatrix(1.05)
    with fade

    play music audio.bgm_tense fadein 1.0

    show item harddisk_large:
        xalign 0.5
        yalign 0.42
        zoom 0.26
    with dissolve

    bm "Aku berlari tanpa henti."
    bm "Di kepalaku, suara pintu besi yang didobrak dan jeritan Alya terus berputar."
    bm "Tanganku mencengkeram hardisk ini hingga jariku memutih."
    bm "Ini harga dari sebuah kebenaran."

    bm "Aku menancapkan hardisk itu ke panel kontrol."
    bm "Loading bar bergerak: 80%%... 90%%... 100%%."

    play sound audio.sfx_warning

    bm "Siaran berhasil dibajak."
    bm "Di seluruh negeri, layar-layar menampilkan data Seleksi Teladan."
    bm "Angka-angka itu membuktikan bahwa jutaan nyawa sengaja dikorbankan."

    hide item harddisk_large
    with dissolve

    bm "Sirene meraung dari luar gedung pemancar."
    bm "Langkah kaki pasukan militer terdengar mendekat."
    bm "Di kejauhan, massa mulai turun ke jalan dengan kemarahan murni."

    b "Tugas kita selesai, Al, Raka."

    play sound audio.sfx_gunshot
    with flash

    bm "Revolusi menang."
    bm "Sistem Harmonisasi dihancurkan keesokan harinya."
    bm "Namun tidak ada satu pun dari Kelompok Resonansi yang tersisa untuk melihat fajar baru."

    centered "TRAGIC ENDING - Martir Terakhir"

    return

label true_ending:

    scene bg server:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.95)
    show red_alert_overlay
    with flash

    play music audio.bgm_main fadein 1.0

    show item access_card_large:
        xalign 0.5
        yalign 0.42
        zoom 0.32
    with dissolve

    b "Komandan! Sesuai Protokol Darurat Pasal 7, saya memegang otorisasi pembatalan operasi tingkat elit!"

    n "I-itu... dari mana kau..."
    n "Komandan, jangan dengarkan dia!"

    c "Tunggu."
    c "Itu akses level satu."
    c "Kami hanya menerima perintah dari pemegang akses."

    b "Targetnya adalah Nisa!"
    b "Dia agen ganda yang mencoba menyabotase aset data kementerian."

    n "Tidak!"
    n "Aku yang memanggil kalian!"

    hide item access_card_large
    with dissolve

    bm "Kebingungan melanda pasukan."
    bm "Aku menendang panel server utama dan memicu sistem pemadam api."
    bm "Asap putih menyembur ke seluruh ruangan."

    b "Raka, Alya, sekarang!"

    scene bg broadcast
    with fade

    show raka normal:
        xalign 0.78
        yalign 1.0
        zoom 0.52
    show alya idle:
        xalign 0.22
        yalign 1.0
        zoom 0.5
    with dissolve

    r "Data siap disiarkan."
    a "Kita berhasil..."
    a "Kau sudah merencanakan ini, Bum?"

    b "Hanya memperhatikan hal-hal yang tidak kalian perhatikan."

    bm "Negara ini tidak hancur dalam semalam, tapi kebohongannya runtuh malam ini."
    bm "Besok, kami akan menghadapi dunia yang baru."
    bm "Masih rusak, masih beracun, tapi kali ini kami akan memperbaikinya bersama-sama."

    centered "TRUE ENDING - Resonansi Sempurna"

    return

label secret_ending:

    scene bg server:
        matrixcolor BrightnessMatrix(-0.25) * ContrastMatrix(0.85)
    with fade

    play music audio.bgm_sad fadein 1.0

    show nisa normal:
        xalign 0.58
        yalign 1.0
        zoom 0.58
    show item harddisk:
        xalign 0.35
        yalign 0.45
        zoom 0.18
    with dissolve

    bm "Aku melihat Alya yang batuk darah, lalu Raka yang terjebak di depan monitor."
    bm "Lalu aku menatap statistik di layar yang berkedip."
    bm "Nisa benar."
    bm "Kita tidak bisa menyelamatkan semua orang."

    r "Bumi...?"
    r "Apa yang kau lakukan?"

    a "Bumi... kumohon..."

    n "Kau membuat keputusan yang logis, Bumi."
    n "Komandan, amankan dua pemberontak ini."

    b "Pastikan tidak ada data yang tersisa, Nisa."

    scene bg office
    with fade

    hide item harddisk

    bm "Dua tahun kemudian."
    bm "Ruang kantor kementerian terasa terlalu bersih untuk dunia yang masih membusuk di luar."

    show nisa normal:
        xalign 0.65
        yalign 1.0
        zoom 0.56
    with dissolve

    n "Bumi, kuota Seleksi Teladan untuk Distrik 7 bulan ini sudah keluar."
    n "Kita harus mengurangi 15%% lagi populasi di sana agar cadangan penawar sektor utama tetap aman."

    b "Lakukan."
    b "Algoritma tidak pernah bohong demi kesejahteraan mayoritas."

    bm "Kami hidup."
    bm "Negara stabil."
    bm "Tapi setiap malam, yang kudengar hanyalah batuk Alya dan makian Raka."
    bm "Aku menyelamatkan umat manusia dengan kehilangan kemanusiaanku sendiri."

    centered "SECRET ENDING - Rasionalitas Dingin"

    return

label best_ending:

    scene bg broadcast:
        matrixcolor BrightnessMatrix(0.05) * ContrastMatrix(1.05)
    with fade

    play music audio.bgm_main fadein 1.0

    show raka normal:
        xalign 0.82
        yalign 1.0
        zoom 0.5
    show alya idle:
        xalign 0.18
        yalign 1.0
        zoom 0.5
    with dissolve

    bm "Layar-layar raksasa di seluruh negeri menampilkan kebenaran."
    bm "Rezim runtuh dari dalam."
    bm "Militer menurunkan senjata setelah menyadari kebohongan pemerintah."
    bm "Kami menang."

    if antidote_used_on == "alya":

        a "Buka jalur audionya, Raka."
        a "Biar aku yang bicara pada mereka."

        r "Panggung milikmu, Sang Orator."

        a "Saudara-saudaraku, kalian telah melihat kebenarannya!"
        a "Jangan biarkan amarah membakar kota kita."
        a "Ambil alih fasilitas penawar, jangan hancurkan."

        bm "Karena penawar itu, suara Alya kembali kuat."
        bm "Ia menghentikan massa dari anarki dan memimpin revolusi secara tertib."

    elif antidote_used_on == "raka":

        r "Bumi, kau tahu kenapa aku butuh fokus penuh tadi?"
        r "Aku tidak hanya membajak data korupsi mereka."
        r "Aku juga menyebarkan cetak biru mesin pembuat penawar ke server universitas dan rumah sakit rakyat."

        a "Dasar gila..."

        bm "Keputusanku memberikan penawar pada Raka membuahkan hasil yang tidak ternilai."
        bm "Ia menghancurkan monopoli oksigen dan memberi rakyat cara untuk bertahan."

    else:

        a "Kita berhasil..."
        r "Belum sempurna, tapi ini awal."

        bm "Tidak ada yang mendapat penawar malam itu."
        bm "Namun data tersiar, Nisa tertangkap, dan rakyat akhirnya tahu siapa musuh mereka."

    scene bg office_best
    with fade

    bm "Fajar menyingsing dari balik kaca ruang siaran."
    bm "Udara di luar mungkin masih butuh waktu bertahun-tahun untuk pulih."
    bm "Namun pagi ini, untuk pertama kalinya, masa depan tidak terasa seperti hukuman."

    b "Ayo kita pulang."
    b "Ada dunia yang harus kita perbaiki."

    centered "BEST ENDING - Harapan Baru"

    return
