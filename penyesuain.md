Iya, ada beberapa asset/definisi yang kurang atau belum rapi:

- `bg corridor` dipakai di chapter 2 sebelumnya, tapi belum didefinisikan di `core/assets.rpy`. Aku sementara ganti ke `assets/bg/hall.jpeg`.
- `nisa normal` dipakai di chapter 2 sebelumnya, tapi belum ada image definition. Yang tersedia adalah `nisa idle`, jadi aku pakai itu.
- `audio.bgm_main`, `audio.bgm_tense`, `audio.bgm_sad` belum benar-benar didefinisikan di `core/audio.rpy`; sekarang masih berada di dalam komentar contoh. Karena itu aku pakai path langsung ke file `.wav`.
- BGM yang tersedia baru 3: `Calm`, `Action`, `Tension`. Untuk mood seperti sedih, misterius, ambience drone, atau ending emosional, aset khususnya belum ada.
- Beberapa background tersedia tapi belum didefinisikan sebagai image Ren’Py di `core/assets.rpy`, misalnya `hall.jpeg`, `server.jpeg`, `office.jpeg`, `sewer.jpeg`, `broadcast.jpeg`.

Untuk chapter 2 sekarang aman karena aku pakai asset yang benar-benar ada. Tapi biar project lebih rapi, nanti bagusnya kita rapikan `core/assets.rpy` dan `core/audio.rpy` supaya script bisa pakai nama seperti `bg corridor`, `audio.bgm_tense`, dll.