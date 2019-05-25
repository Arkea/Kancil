# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kancil", who_color="#fd680d")
define b1 = Character("Baya", who_color="#0ea605")
define b2 = Character("Boyo", who_color="#34cd0b")
define h = Character("Harimau", who_color="#ffaa00")
define p = Character("Pak Tani", who_color="#2591f6")
define a = Character("Ireng", who_color="#020b31")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg hutan

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show kancil

    # These display lines of dialogue.

    # k "Halo."

    # Tes transisi bg

    # show bg sungai with dissolve
    # hide kancil

    # show kancil

    # k "Ini baru percobaan ya."

    # k "Ini untuk ngetes percabangan"

    "Pada suati hari yang cerah, terdengar suara kicauan burung saling bersahut-sahutan."

    "Dengan mata si kancil yang masih sayup-sayup dia bangun dari tidurnya."

    k "alangkah  indahnya pagi ini"

    "Si Kancil pun keluar dari sarangnya, berniat untuk jalan-jalan sambil menikmati udara segar dan indahnya matahari terbit."

    "Ketika sedang berjalan-jalan Si Kancil merasa lapar, Si kancil pun berniat untuk mencari makan."

    "Si kancil befikir kemana dia akan mencari makan."

    "Setelah berfikir akhirnya dia memutuska untuk pergi ke......"

    jump choice

label choice:

    menu:
        "Setelah berfikir akhirnya dia memutuska untuk pergi ke......"

        "Kebun pak tani":
            jump tani

        "Di hutan":
            jump hutan

label tani:

    "Ketika dalam perjalanan ke kebun pak tani, ternyata dia harus melewati sebuah sungai."

    "Si Kancil pun memikirkan ide bagaimana cara untuk melewati sungai tersebut."

    "Si kancil yang cerdas ini pun tidak kehilangan akal."

    " Si Kancil..."

    k "Buaya...buaya... ayo keluaaaaar... Aku punya makanan untukmu...!!"

    "Si Kancil berteriak sambil melompat kegirangan kepada buaya-buaya yang banyak tinggal di sungai yang dalam itu."

    "Buaya...buaya... ayo keluar... mau daging segar tidaaaak?"

    "Setelah kancil berteriak sekali lagi, Tak lama kemudian seekor buaya muncul dari dalam air"

    b1 "Bruaaar... siapa yang teriak siang-siang begini... mengganggu tidurku saja."

    b2 "Hei Kancil, diam kau... kalau tidak aku makan nanti kamu."

    k "Wah... bagus kalian mau keluar, mana buaya yang lain?"

    k "Kalau cuma dua ekor masih sisa banyak nanti makanannya ini. Ayo keluar semuaaa...!"

    "Teriak kancil"

    b1 "Ada apa Kancil sebenarnya, ayo cepat katakan"

    k "Begini buaya, maaf kalau aku mengganggu tidurmu, tapi aku akan bagi-bagi daging segar buat buaya-buaya di sungai ini."

    k "Makanya kalian harus keluar semua untuk menghabiskan daging-daging segar ini."

    "Mendengar bahwa mereka akan dibagikan daging segar, buaya-buaya itu segera memanggil teman-temannya untuk keluar semua."

    b1 "Hei, teman-teman semua, ada makanan gratis nih! Ayo kita keluaaaar...!"

    "Baya sebagai pemimpin dari buaya itu berteriak memberikan komando."

    "Tak berapa lama, bermunculanlah buaya-buaya dari dalam air."

    k "Nah, sekarang aku harus menghitung dulu ada berapa buaya yang datang, ayo kalian para buaya segera baris berjajar hingga ke tepi sungai di sebelah sana"

    k "Nanti aku akan menghitung satu persatu."

    "Tanpa berpikir panjang, buaya-buaya itu segera mengambil posisi, berbaris berjajar dari tepi sungai satu ke tepi sungai lainnya, sehingga membentuk seperti jembatan."

    k "Oke, sekarang aku akan mulai menghitung"

    k "Satuuu..."

    "Kancil melompat ke punggung buaya pertama, sambil berteriak"

    k "Duaaaa... tigaaaa..."

    "Begitu seterusnya sambil terus meloncat dari punggung buaya yang satu ke buaya lainnya. Hingga akhirnya si Kancil sampai di seberang sungai."

    k "{i}Mudah sekali ternyata.{/i}"

    "Begitu sampai di seberang sungai, Kancil berbalik dan berkata..."

    "Hai buaya-buaya bodoh, sebetulnya tidak ada daging segar yang akan aku bagikan. Tidakkah kau lihat bahwa aku tidak membawa sepotong daging pun?"

    "Sebenarnya aku hanya ingin menyeberangi sungai ini, dan aku butuh jembatan untuk lewat. Kalau begitu saya ucapkan terima kasih pada kalian, dan mohon maaf kalau aku mengerjai kalian"

    b1 "Haaaa..."

    b1 "Huaaaaaahh...!!"

    b2 "sialan... Kancil nakal, ternyata kita cuma dibohongi."

    b1 "Awas kau kancil ya.. kalau ketemu lagi saya makan kamu"

    "Si Kancil segera berlari menghilang di balik pepohonan meninggalkan buaya yang geram dan menuju kebun Pak Tani untuk mencari ketimun makanan kesukaannya."

    "Si Kancil pun berhasil mencuri ketimun di kebun petani."

    "Pagi yang sangat cerah."
    
    "Matahari bersinar dengan indah."
    
    "Pak Tani bersiap-siap pergi ke ladang dengan sangat gembira dengan memanggul pacul."

    p "Aku akan pergi ke ladang untuk memeriksa kebun timunku, mungkin saja besok sudah bisa dipanen."
    
    "Sesampainya di kebun timun Pak Tani sangat terkejut."

    "Buah timun di kebunnya banyak yang rusak."
    p "Aduh siapa yang berani merusak buah timunku ini. Mengapa harus dirusak? Aku bukan petani yang pelit, jika ada orang yang mau timunku ambil saja. Tapi tidak untuk dirusak"

    "Dengan hati muram Pak Tani pulang ke rumah."

    "Ia menduga-duga hewan apakah yang suka makan mentimun."
    
    p "{i}Pasti hewan yang merusak dan mencuri kebun mentimun ku adalah si Kancil{/i}"

    "Pak Tani mencari akal untuk menjebak si Kancil."

    "Pak Tani akhirnya berhasil mencari akal untuk menjebak si Kancil dengan membuat orang-orangan yang di beri pelekat sangat kuat."

    "Menjelang sore orang-orangan itu sudah selesai dibuat dan dibawa ketengah kebun timun untuk dipasang."
    
    p "{i}Aku tahu kancil hewan yang sangat cerdik, dia bisa melakukan apa saja untuk mencuri timunku{/i}"

    "Ternyata dugaan Pak Petani benar, malam harinya Kancil datang untuk mengambil mentimun."

    "Kancil tertawa melihat orang-orangan yang di buat Pak Tani."

    k "Haha.. hanya orang-orangan, siapa takut?"

    "Kancil hanya melewati orang-orangan itu dan memakan timun yang muda-muda."

    "Tak banyak yang di makan si Kancil. Hanya 3 buah timun ia sudah merasa kenyang."

    "Ia juga tidak merusak timun yang lainnya."

    "Setelah makan timun. Kancil menghampiri orang-orangan yang dibuat Pak Tani"

    "Karena sifat jail si Kancil. Ia pukul orang-orangan itu dengan kaki depannya."

    k "Aduh… kenapa melekat seperti ini? Kaki ku tidak dapat di gerakkan!"

    k "Hei orang-orangan jelek. Lepaskan kakiku. Kalau tidak, akan kupukul lagi kau!"

    "Kancil memukul orang-orangan itu dengan kaki yang satu lagi."
    
    "\*Plak!\*"

    "Kini kedua kakinya menempel erat pada baju orang-orangan itu."
    
    "Pelekat yang di pasang Pak Petani di baju orang-orangan itu sangat kuat. Kancil tak bisa melepaskan diri. Sekuat tenaga ia berusaha tetapi tidak berhasil. Semalaman Kancil menangis."

    "Pagi harinya Pak Tani datang."

    p "Ku tangkap kau Kancil. Dasar biang kerok."

    p "Kau boleh mengambil makan timunku Cil. Tapi tidak untuk merusak buah yang lain."

    k "Ampun Pak Tani. Bukan aku yang merusak timunmu, aku hanya makan 2-3 buah timun. Dan perutku sudah merasa sangat kenyang."

    "Pak Tani tidak percaya dengan perkataan si Kancil. Leher si Kancil di ikat dan di seret Pak Tani ke rumahnya."

    "Sesampainya di rumah Pak Tani, Kancil langsung diletakkan di dalam kurungan ayam."
    
    "Anjing hitam peliharaan Pak tani heran melihat kancil sedang di kurung"
    
    p "Kancil . Batu ini sangat kuat. Kau tak dapat meloloskan diri dari sini. Aku akan pergi sebentar ke pasar untuk membeli bumbu sate."

    k "Ampunilah aku Pak Tani, jangan sate aku. Dagingku pahit dan tidak enak."

    "Pak tani pergi meninggalkan si Kancil yang merengek meminta ampun."

    "Pada saat Pak Tani pergi ke pasar untuk membeli bumbu sate, anjing peliharaan Pak Tani datang menghampiri kurungan si Kancil."

    "Anjing hitam itu bernama Ireng."

    a "Kenapa kau di kurung?"
    
    k "Apa kau tak tau Reng?"

    a "Katakan ada apa sebenernya Cil?"

    k "Begini Reng, aku ini akan di jadikan menantu oleh Pak Tani. Mangkannya Pak Tani pergi ke pasar untuk membeli makanan yang lezat-lezat untukku calon menantunya."

    a "Hah..? Kamu itu tidak pantas Cil, badan mu kecil. Lebih baik aku saja yang menjadi menantu Pak Tani. Aku sudah bertahun-tahun menjadi peliharaannya"

    k "Tapi Pak Tani sudah memilih aku Reng. Sudah sana pergilah kau Ireng!"
    
    "Si Ireng menggerang marah"

    a "Cil, kalau kau tidak mau aku gantikan sekarang juga batu yang ada di atas kurangan itu akan aku dorong dan lehermu akan ku gigit sampai putus."

    k "Wah.. Jangan gitu dong!"

    a "Mau apa tidak?"

    k "Baik-baik aku turuti keinginanmu."

    "Si Ireng mendorong batu hingga terjatuh, kurungan itu terbuka dan Kancil keluar dari kurungannya. Lalu Ireng menggantikkan Kancil masuk ke dalam kurungan."

    k "Selamat Ireng, sebentar lagi kau akan menjadi menantu Pak Tani."
    
    "Setelah itu Kancil berlari sekuat tenaga meninggalkan si ireng."

    "Sesaat kemudian Pak Tani datang."

    "Ia sangat kaget melihat Kancil yang berada di kurungan berubah menjadi Ireng anjing peliharannya."
    
    a "Hormat saya calon mertua."
    
    p "Calon Mertua katamu? Hey kamu kemanakan si Kancil."

    a "Sudah pergi ke hutan Pak Tani!"

    p "Kau sungguh-sungguh mau menjadi menantuku?"

    a "Benar sekali tuan"
    return

label hutan:

    "Ketika seadang mencari makan du hutan, tiba-tiba Kancil dikagetkan dengan suara auman di depannya."

    "Ternyata itu adalah suara seekor Harimau yang sedang kelaparan."

    h "Auuumm!!"

    h "Hari ini nasibku baik sekali, perutku sedang keroncongan eeh sekarang ketemu Kancil sebagai makan siangku."
    
    h "Hei Kancil... bersiap-siaplah, karena hari ini kau akan aku makan!!"

    k "Eeiit...tunggu dulu Harimau. Kalau kamu mau memakanku, kamu akan kehilangan rahasia sabuk sang dewa."

    k "Siapa yang memakainya, maka dia akan bisa terbang dan kuat seperti dewa."

    k "Kamu mau nggak bisa terbang dan kuat seperti dewa? Dan kalau kamu memakainya, kamu juga pasti akan menjadi raja hutan yang selama ini kamu idam-idamkan!!"

    h "Benar nih Cil..!!"
    
    h "Kalau begitu kamu tidak akan aku makan, tapi kamu harus memberitahu dimana sabuk dewa itu?"
    
    k "Benar dong...!! Sekarang ayo kamu ikut aku ke batu besar dipinggir sungai dekat rumpun bambu di selatan hutan"

    "Si kancil dan harimau pun segera berjalan menuju pinggir sungai di selatan hutan."

    "Sesampainya disana, tampak sebuah benda berwarna coklat hitam melingkar di sebuah batu besar menyerupai sebuah sabuk."

    h "Aummmmmm!!"

    "Sang Harimau mengaum panjang, bergerak hendak menerjang benda itu."

    k "Tunggu dulu Harimau!!"

    k "Kalau kamu mau mengambil sabuk dewa tersebut, kamu harus berjalan mundur ke arah sabuk tersebut dan jangan sekali-kali menengok ke belakang agar dewa pemilik sabuk itu tidak mengetahui kedatanganmu, kalau ketahuan bisa gawat nanti...!!!"

    h "Benar juga katamu ,Cil!! Habis sabuknya besar sekali sih, aku sudah tidak sabar untuk memakai sabuk itu"

    k "Oke Harimau!! Sekarang kamu berjalan mundur ke arah sabuk itu. Tapi sebelum itu, aku hitung dulu yah, sekalian mau sembunyi, soalnya dewa pasti memarahiku kalau melihatku!!"

    h "Cepat hitung, Cil!! Aku sudah tidak sabar nih...!!!"

    k "Oke, aku hitung ya!!"

    k ".....1,2,3...."

    h "Sudah belum?"

    k "Belum!!!"

    "Teriak Kancil sambil berlari, dia meneruskan menghitung sampai dengan 10 sambil terus berlari sampai dirinya tidak kelihatan"

    "Tanpa berpikir panjang, sang Harimau berjalan mundur menuju ke arah benda yang menyerupai sabuk tersebut."

    "Dan ketika tubuhnya memasuki kedalam lingkaran tersebut, tiba-tiba benda tersebut bergerak melilit tubuh sang Harimau."

    "Sang Harimau tampak senang, karena pikirannya sabuk tersebut sedang bereaksi memberikan kekuatan pada tubuhnya."

    "Namun, lilitan itu semakin lama semakin kuat dan membuat Harimau kesakitan."

    "Alangkah kagetnya sang Harimau ketika dihadapannya muncul kepala ular piton raksasa"

    "Harimau berteriak minta tolong, namun teriakan minta tolongnya itu sia-sia karena ular piton itu terlalu besar dan lilitannya terlalu kuat."

    "Pada akhirnya sang Harimau itu mati di makan ular piton dengan tulang-tulang yang remuk."

    "Adapun sang Kancil yang nyawanya terselamatkan karena kecerdikannya memulai petualangan barunya di hutan belantara."

    return
