label normal_ending:
    stop music fadeout 0.5
    play music bgm_sewer fadein 1.0

    scene bg sewer
    with fade
    play sound sewerrun
    play audio hdd_drop
    "Hardisk itu terlepas dari tanganku"
    "Aku tidak sempat mengambilnya kembali, mereka terlalu dekat!"
    bm "Sial, mereka menghancurkannya!" 

    play audio gunshot
    stop sound fadeout 2.0
    "Raka...!"
    scene bg sewer
    show alya sick at center, nisa
    with fade
    play music bgm_normalending fadein 1.0
    a "Bumi... datanya hancur..."
    a "Raka gimanaa... apa yang baru saja kau lakukan?"
    a "Kenapa kau membawaku dan membiarkannya mati di sana?!"
    bm "Aku tidak bisa kehilangan kalian semua dalam satu malam. Kau butuh hidup untuk memimpin pergerakan ini, Al."
    a "Apa maknanya, bumi!"
    show alya sick at jump
    a "APA!"
    a "Kita tidak punya bukti apa-apa..."
    a "Tanpa data itu, kematian raka sia-sia!"
    a "Nisa menang, Bumi..."
    a "Pemerintah menang..."

    scene dark
    with Dissolve(2.0)
    stop music fadeout 0.5
    play music bgm_aftermath fadein 1.0
    bm "Kami selamat..."
    "Fisik Alya pulih berkat penawar itu, namun api di dalam jiwanya telah padam."
    "Tanpa bukti algoritma itu, massa di jalanan perlahan kembali menjadi zombi yang patuh pada jam kerja pemerintah."
    "Sesekali, aku melihat Nisa di siaran televisi, berbicara tentang 'harmoni' dengan seragam kementeriannya."
    "Kami bertahan hidup di bawah tanah, mengumpulkan sisa-sisa perlawanan."

    bm "Tapi di dunia ini, sekadar bernapas bukanlah sebuah kehidupan. Ini hanyalah gema dari perlawanan yang telah lama mati."

    "Normal Ending - Gema yang Pudar"
    scene dark
    with Dissolve(2.0)

    return

label bad_ending:

    stop music fadeout 0.5
    play music bgm_sewer fadein 1.0

    scene bg sewer
    with fade

    #play music audio.bgm_sad fadein 1.0

    play sound sewerrun
    play audio hdd_drop
    "Hardisk itu terlepas dari tanganku"
    "Aku tidak sempat mengambilnya kembali, mereka terlalu dekat!"
    bm "Sial, mereka menghancurkannya!"
    play audio gunshot
    stop sound fadeout 2.0
    "Raka...!"
    
    scene bg sewer
    show alya sick at center, nisa
    with fade

    "Aku memapah Alya sekuat tenaga menyusuri gorong-gorong ini, tapi badannya terasa semakin dingin."

    bm "Alya! Bertahanlah!"

    if antidote_used_on == None:
        bm "Kita hampir sampai di titik aman. Aku... aku masih menyimpan penawarnya"
        "Sial! Aku lupa kalau antidotenya jatuh sebelum kami melakukan pelarian"


    a "Terlambat... Bumi..."
    a "Kau... merelakan data Raka..."
    a "Kau juga membiarkanku mati tanpa membawa kebenaran apa pun..."
    bm "Tidak, Al, kumohon, jangan tutup matamu!"
    show alya sick:
        linear 2.0 blur 20
    show bg sewer:
        linear 2.0 blur 50
    $ renpy.say(a, "...Kauu..., ini semua sia-sia...", interact=False)
    pause 2.0
    window hide 
    with dissolve


    scene bg sewer
    with blink
    "Hening.."
    "Tak kusangka, gorong-gorong ini menjadi tempat terakhirnya"
    "Aku memeluk tubuhnya yang tak bernyawa"
    "Hardisk hancur"
    if antidote_used_on == None:
        bm "Antidote terakhir terjatuh di basement itu."
    "Raka tewas"
    "Alya mati di pelukanku."
    "Nisa mengkhianati kami."
    "Keputusan-keputusanku yang setengah hati telah menghancurkan segalanya."

    scene dark
    with Dissolve(2.0)
    stop music fadeout 1.0
    play music bgm_aftermath fadein 2.0
    "Aku adalah satu-satunya yang tersisa. "
    "Aku bersembunyi seperti tikus, sendirian, dihantui rasa bersalah yang mencabik-cabik kewarasan."
    "Pemerintah kini berkuasa mutlak tanpa ada lagi yang berani melawan."
    "Mereka telah menjadi tirani tanpa wajah, dan aku hanyalah hantu yang menunggu giliran untuk dihapus dari sistem."

    "Bad Ending - Tirani Tanpa Wajah" 

    scene dark
    with Dissolve(2.0)
    return

label tragic_ending:

    stop music fadeout 0.5
    play audio running
    play music bgm_broadcast fadein 1.0
    scene bg broadcast
    with Fade(0.5, 2.0, 0.5)

    #play music audio.bgm_tense fadein 1.0
    play audio broadcasterror2 fadein 2.0
    "Aku berlari tanpa henti."
    "Di kepalaku, suara pintu besi yang didobrak dan jeritan Alya terus berputar seperti kaset rusak."
    "Tanganku mencengkeram hardisk ini hingga jariku memutih. Ini harganya. Ini harga dari sebuah kebenaran."
    stop audio fadeout 1.0
    $ renpy.music.set_volume(0.5, channel='sound')
    play sound broadcasterror1
    "Siaran berhasil dibajak."
    "Di seluruh penjuru negara, layar-layar menampilkan rahasia menjijikkan pemerintah."
    "Angka-angka yang membuktikan bahwa jutaan nyawa sengaja dilenyapkan."

    bm "Kebenaran akhirnya tersebar." 
    stop sound fadeout 1.0

    play sound protest fadein 2.0
    play sound2 doorslam loop
    "Massa mulai turun ke jalan. "
    "Kali ini bukan dengan petisi, tapi dengan kemarahan murni."
    "Revolusi akhirnya meledak."
    stop sound2
    play audio doorslam

    bm "Tugas kita selesai, Al, Raka."
    scene dark
    play audio gunshot
    stop sound fadeout 1.0
    with heavy_blink
  
    
    stop music fadeout 0.5
    play music bgm_aftermath fadein 1.0

    "Revolusi menang."
    "Sistem Harmonisasi dihancurkan keesokan harinya."
    "Namun, tidak ada orang Kelompok Resonansi kami yang tersisa untuk melihat fajar baru tersebut."
    "Kami semua menjadi martir untuk dunia yang tidak akan pernah kami tinggali."
    "Tragic Ending - Martir Terakhir"
    scene dark
    with Dissolve(2.0)

    return

label true_ending:

    stop music fadeout 0.5
    play music bgm_broadcast fadein 1.0
    scene bg basement:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.9)
    show light_glow_mask at flicker_light zorder 100:
        xpos -0.01
        zoom 1.2
    show nisa smile at center, nisa
    with fade

    #play music audio.bgm_main fadein 1.0


    n "Sudah berakhir, Bumi. Serahkan hardisk itu."
    bm "Heh."
    hide nisa smile
    show nisa idle at center, nisa
    show dark zorder 101:
        alpha 0.6
    show access card at center, zorder 102:
        ypos 0.7
    with dissolve
    bm "Komandan! Sesuai Protokol Darurat Pasal 7, saya memegang otorisasi pembatalan operasi tingkat elit!"
    hide dark
    hide access card
    with dissolve 

    show nisa at jump
    n "I-itu... dari mana kau... Komandan, jangan dengarkan dia! Rebut hardisknya"

    c "Tunggu. Itu akses level 1. Kami hanya menerima perintah dari pemegang akses. Siapa target sebenarnya di ruangan ini?"

    bm "Targetnya adalah dia!"
    bm "Dia adalah agen ganda yang mencoba menyabotase aset data kementerian."
    bm "Tangkap dia sekarang atau kalian semua akan dieksekusi atas tuduhan pembangkangan!"

    show nisa at jump
    n "Tidak!"
    n "Dia berbohong!"
    n "Aku yang memanggil kalian!"

    "Kesempatan!"

    bm "Raka, Alya, SEKARANG!"
    play sound doorslam
    play sound2 running
    scene bg broadcast
    show raka idle at center, raka
    with Fade(0.5, 2.0, 0.5)

    stop music fadeout 0.5
    play music bgm_trueending fadein 1.0
    show raka at bounce_limited


    r "Hah! Ha ha.. Hahaha!"
    r "Militer tu kocak banget dah itu pasti masih sibuk menginterogasi Nisa di markas kosong!"

    show alya idle at left, chara_left
    with dissolve
    play audio alyaquestioning
    a "Kau... kau sudah merencanakan ini, Bum?"
    scene bg broadcast
    hide alya idle
    hide raka idle
    show bumi idle at center, raka
    with heavy_blink


    bm "Hanya memperhatikan hal-hal yang tidak kalian perhatikan."

    scene dark
    with dissolve

    "Negara ini tidak hancur dalam semalam, tapi kebohongannya telah runtuh."
    "Besok, kami akan menghadapi dunia yang baru."
    "Biarlah tidak sempurna, rusak, atau apapun itu"
    "Tapi kali ini... kami akan memperbaikinya bersama-sama"

    "True Ending - Resonansi Sempurna"
    scene dark
    with Dissolve(2.0)

    return

label secret_ending:

    stop music fadeout 0.5
    play music bgm_broadcast fadein 1.0
    scene bg basement:
        matrixcolor BrightnessMatrix(-0.15) * ContrastMatrix(0.9)
    show light_glow_mask at flicker_light zorder 100:
        xpos -0.01
        zoom 1.2
    with fade

    #play music audio.bgm_sad fadein 1.0

    "Aku melihat ke arah Alya yang batuk darah, lalu ke arah Raka yang terjebak di kursi rodanya."
    "Lalu, aku menatap statistik di layar monitor yang berkedip."
    show nisa smile at center, nisa
    with heavy_blink
    "Nisa benar."
    "Kita tidak bisa menyelamatkan semua orang."
    "Idealisme hanyalah racun manis yang membunuh perlahan."

    r "Bumi...? Apa yang lu lakukan WOIIII?, JANGAN BILANG!" 
    r "Setelah semua yang kita laluin, LU KHIANATIN KITA?! CEPAT! Bawa itu lari!"

    a "Bumi... jangan... kumohon."

    n "Kau membuat keputusan yang logis, Bumi."
    n "Komandan, amankan dua pemberontak ini. Eksekusi sesuai prosedur."
    bm "Pastikan tidak ada data yang tersisa, Nisa."

    
    play music bgm_secretending fadein 2.0
    scene bg office
    show nisa idle at center, nisa
    with fade   

    n "Bumi, kuota Seleksi Teladan untuk Distrik 7 bulan ini sudah keluar."
    n "Kita harus mengurangi 15%% lagi populasi di sana agar cadangan penawar sektor utama tetap aman."

    bm "Lakukan. Algoritma tidak pernah bohong demi kesejahteraan mayoritas."
    hide nisa idle with dissolve
    "Kami hidup. Negara stabil. Harmoni tercapai, setidaknya itu yang dikatakan pemerintahan ini kepada kami yang bekerja untuknya."
    "Tapi setiap malam, saat aku menutup mata, yang kudengar hanyalah suara batuk Alya dan makian Raka yang menggema di kepalaku."
    "Aku menyelamatkan umat manusia... dengan kehilangan kemanusiaanku sendiri."
    "Secret Ending - Rasionalitas Dingin"
    scene dark
    with Dissolve(2.0)
    return

label best_ending:
    stop music fadeout 0.5
    scene bg broadcast
    with fade

    play music audio.bgm_bestending fadein 1.0

    "Layar-layar raksasa di seluruh penjuru kota kini menampilkan kebenaran."
    "Rezim telah runtuh dari dalam."
    "Komandan militer memerintahkan pasukannya untuk mengamankan fasilitas penawar, bukan untuk elit, tapi untuk dibagikan."
    "Kami menang. Tapi bagaimana kami melangkah dari sini, tak kusangka akan ditentukan oleh apa yang terjadi di rubanah itu beberapa jam yang lalu..."

    if antidote_used_on == "alya":

        show alya idle at center, nisa
        a "Buka jalur audionya, Raka. Biar aku yang bicara pada mereka."
        show raka idle at raka:
            xpos -0.2
            linear 0.4 xalign -0.15
        r "Panggung milik lu nih, Sang Orator terbaik bangsa ini."
        show raka idle at raka:
            linear 0.4 xalign -0.4
        play audio walkie
        a "Saudara-saudaraku! Kalian telah melihat kebenarannya!"
        a "Tapi dengarkan aku—jangan biarkan amarah membakar kota kita!"
        a "Jika kalian menghancurkan fasilitas pemerintah, kita akan kehilangan mesin pembuat penawar!"
        a "Bergeraklah dengan tertib! Ambil alih, jangan hancurkan!"

        "Karena Alya dalam kondisi fisik prima, suaranya menggelegar penuh karisma, menghentikan massa dari anarki berdarah."
        "Revolusi terjadi secara damai dan terstruktur."
        "Ia bukan lagi sekadar martir yang sakit-sakitan, melainkan pemimpin sah dari dunia yang baru ini."

    elif antidote_used_on == "raka":

        scene bg broadcast
        show raka idle at center, raka, bounce_limited
        with blink
        play sound ketik
        r "Hahaha! Bumi, lu tahu gak kenapa aku butuh fokus penuh tadi?! gua gak hanya hack data korupsi mereka cuy!"
        show alya sick at nisa:
            xpos -0.2
            linear 0.4 xalign -0.15
        play sound alyaquestioning
        a "Lalu apa yang kau retas, dasar gila?"
        show alya sick at nisa:
            linear 0.4 xalign -0.4
        r "Gua hack juga source code dari mesin pembuat penawar itu lek!"
        r "Gua berhasil dapat blueprint-nya! Selama ini tuh orang mengunci rumusnya agar kita bergantung pada pabrik kementerian."
        r "Sekarang? Gua dah menyebarkan rumus pembuatan penawar ini ke semua server universitas dan rumah sakit rakyat!"
        r "Kita bisa meraciknya sendiri!. Iya gua tau gua jago banget emang, dan gak ada yang lebih jago dari gua, thank you guys"

        "Keputusanku memberikan penawar pada Raka membuahkan hasil yang tak ternilai."
        "Dengan otak jeniusnya yang bekerja 100%%, ia tidak hanya menghancurkan monopoli pemerintah, tapi memberikan kami kunci untuk memproduksi napas kami sendiri. Monopoli oksigen telah resmi berakhir."

    scene bg broadcast
    show bumi idle at center, raka
    with fade
    stop sound fadeout 0.5
    "Udara di luar mungkin masih butuh waktu bertahun-tahun untuk pulih."
    "Tantangan membangun ulang negara yang hancur ini ada di depan mata."
    "Namun pagi ini, saat aku melihat teman-temanku berdiri di sampingku menatap matahari terbit..."
    bm "Ayo kita pulang."
    bm "Ada dunia yang harus kita perbaiki."
    "Best Ending - Harapan Baru"
    scene dark
    with Dissolve(2.0)
    return