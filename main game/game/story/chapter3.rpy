label story_ch3_scene1:

    scene bg basement
    with flash

    play music audio.bgm_tense fadein 0.5

    r "Sial! Mereka memotong jalur kita!"
    r "Pasukan bersenjata sudah masuk!"

    a "Bumi... uhuk... datanya..."

    r "90%! Aku butuh waktu!"

    return

label story_ch3_scene2:

    show nisa normal at center
    with fade

    n "Waktu kalian habis."

    a "Nisa... kau yang membawa mereka?!"

    n "Aku menyelamatkan masa depan."

    n "Bumi, ikutlah denganku."

    return

label story_ch3_scene3:

    r "BAWA DATANYA, BUMI!"
    r "LARI!"

    a "Tinggalkan aku..."

    bm "Waktu membeku."
    bm "Semua pilihan ada di tanganku."

    return

label story_ch3_choice:

    "APA YANG KAU LAKUKAN?"

    menu:
        "Selamatkan Alya":
            jump ch3_save_alya

        "Ambil data dan lari":
            jump ch3_take_data

        "Gunakan kartu akses Nisa":
            if has_evidence:
                jump ch3_true_route
            else:
                "Aku tidak punya apa-apa untuk melawan mereka..."
                jump ch3_take_data

        "Ikut Nisa":
            jump ch3_join_nisa

label ch3_save_alya:

    bm "Aku tidak bisa meninggalkannya."

    if antidote_used_on == "alya":
        jump normal_ending
    else:
        jump bad_ending

label ch3_take_data:

    bm "Kebenaran lebih penting dari segalanya."

    jump tragic_ending


label ch3_true_route:

    bm "Aku tidak sendirian kali ini."

    jump true_ending

label ch3_join_nisa:

    bm "Ini satu-satunya cara bertahan."

    jump secret_ending

label chapter3:

    call story_ch3_scene1
    call story_ch3_scene2
    call story_ch3_scene3
    call story_ch3_choice

    return