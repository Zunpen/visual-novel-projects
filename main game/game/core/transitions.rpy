transform flash_light:
    # Menggunakan additive blending agar sangat cerah
    additive 1.0 
    alpha 0.0
    # Muncul seketika
    linear 0.1 alpha 1.0
    # Menghilang perlahan
    linear 1.0 alpha 0.0

transform flicker:
    matrixcolor BrightnessMatrix(0.0) 
    
    linear 0.05 matrixcolor BrightnessMatrix(-0.2)
    linear 0.05 matrixcolor BrightnessMatrix(0.0)
    
    pause (renpy.random.uniform(1.5, 5.0))
    linear 0.05 matrixcolor BrightnessMatrix(-0.15)
    linear 0.05 matrixcolor BrightnessMatrix(0.0)
    repeat

transform chara_left:
    zoom 0.9
    yalign -0.3
    xalign 0.2
    
transform nisa:
    zoom 0.9
    yalign -0.3

transform raka:
    zoom 1.1
    yalign -0.1

transform flicker_light:
    alpha 0.3
    matrixcolor BrightnessMatrix(-0.7) 
    matrixcolor ContrastMatrix(1.2)

    linear 0.05 matrixcolor BrightnessMatrix(-0.8)
    linear 0.05 matrixcolor BrightnessMatrix(-0.2)
    
    pause (renpy.random.uniform(2.0, 5.0))

    linear 0.05 matrixcolor BrightnessMatrix(-0.8)
    linear 0.05 matrixcolor BrightnessMatrix(-0.2)
    repeat

transform slow_slide:
    xpos -1.0
    linear 2.0 xpos 0.1

transform jump:
    linear 0.1 yoffset -50
    linear 0.1 yoffset 0

transform bounce:
    subpixel True
    block:
        easein .2 yoffset -20
        easeout .2 yoffset 0
        repeat

transform bounce_limited:
    subpixel True
    # Animasi akan berjalan berulang...
    block:
        easein .2 yoffset -20
        easeout .2 yoffset 0
        repeat
    # ...sampai waktu 3.0 detik tercapai
    time 2.0
    # Setelah 3 detik, paksa kembali ke posisi normal
    linear 0.1 yoffset 0

transform flashing:
    # Set kondisi awal (Hanya jalan sekali di awal)
    alpha 0.3
    matrixcolor ContrastMatrix(1.2)
    matrixcolor BrightnessMatrix(-0.2) 

    block:
        # Denyut Pertama (Sirine)
        linear 0.5 matrixcolor BrightnessMatrix(0.6)  # Naik ke terang
        linear 0.5 matrixcolor BrightnessMatrix(-0.2) # Turun ke gelap (sama dengan awal)
        
        # Jeda dalam kondisi gelap
        pause 1.0
        
        # Denyut Kedua
        linear 0.5 matrixcolor BrightnessMatrix(0.6)  # Naik ke terang
        linear 0.5 matrixcolor BrightnessMatrix(-0.2) # Turun ke gelap (sama dengan awal)
        
        # Kembali ke atas block (mengulang dari Brightness -0.7)
        repeat

transform littlezoom:
    xpos -0.0005
    xalign 0.1
    zoom 1.0
    linear 5.0 zoom 1.01
    pause 5.0
    linear 5.0 zoom 1.0
    repeat
define blink = Fade(0.1, 0.1, 0.4, color="#000000") 

define heavy_blink = Fade(0.5, 0.3, 0.8, color="#000000")
