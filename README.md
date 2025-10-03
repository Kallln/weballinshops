Link pws: https://ahmad-haikal41-weballinshops.pbp.cs.ui.ac.id/
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1) Sebelum membuat proyek django, saya melakukan beberapa hal terlebih dahulu, yaitu membuat python env dulu dengan python -m venv env, lalu menjalankannya dengan env\Scripts\activate di dalam direktori proyek. Setelahnya, saya membuat requirements yang dibutuhkan dalam proyek django di dalam requirements.txt dan akan dijalankan dengan pip install -r requirements.txt. Terakhir, baru saya menjalankan proyek django dengan nama weballinshops melalui perintah "django-admin startproject weballinshops ."
    2) Pada direktori proyek, saya menjalankan virtual environment dan membuat aplikasi main pada direktori proyek dengan perintah "python manage.py startapp main" yang akan membuat direktori aplikasi baru, yaitu main. Hal yang harus dilakukan selanjutnya adalah menghubungkan aplikasi ke proyek, melalui settings.py dalam proyek weballinshops, dan di dalamnya tambahkan 'main' di variabel INSTALLED_APPS sehingga aplikasi sekarang sudah terhubung.
    3) Proses routing diawali dengan menambahkan beberapa kode di urls.py dalam direktori aplikasi main, seperti berikut:
        from django.urls import path
        from main.views import show_main
        app_name = 'main'
        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
    Setelahnya, kita juga perlu mengubah urls.py yang ada di direktori proyek weballinshops, dengan menambahkan impor include dari django.urls dan menambah perintah "path('', include('main.urls'))" pada variabel urlpatterns
    4) Dalam pembuatan model, saya membuat Product(models.model) pada file models.py yang ada di dalam direktori main, lalu menambahkan atribut seperti berikut:
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        thumbnail = models.URLField(blank=True, null=True)
        category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
        is_featured = models.BooleanField(default=False)
    Lalu, saya membuat dan melakukan migrasi karena untuk mengupdate perubahan pada model.
    5) Pada aplikasi main, di file views.py saya membuat fungsi yang nantinya ditampilkan ke template html
    ![views.py image](https://drive.google.com/uc?export=view&id=1-X7BrnZG__Fv0vQOLGgcpzl_5nCR5FIz)
    ![html image](https://drive.google.com/uc?export=view&id=1JAW3It7bD8_Z9HjRuMM7ybqAzHxN0iYA)
    6) Saya membuat routing pada urls.py dalam aplikasi main, seperti berikut
    ![urls.py image](https://drive.google.com/uc?export=view&id=1rkq-2MLXXlmHPxYAD0bJTbnbAH3axgxF) sehingga nantinya akan memetakan fungsi yang dibuat ke views.py
    7) Saya melakukan deployment ke pws dengan melakukan beberapa perintah berikut:
        git remote add pws <link-pws>
        git branch -M master
        git add .
        git commit -m "Deployment PWS"
        git push origin master
        git push pws master


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan](https://drive.google.com/uc?export=view&id=1b9EqrhcNlfw85E5f-YzLo_EDmnvrMRaL)
Penjelasan:
     1) Pengguna mengakses url suatu web, hal ini akan melakukan request pada URLS. 
     2) URLS akan meneruskan request dari pengguna, ke views
     3) Views.py akan memroses request dari pengguna dan menampilkan hasil requestnya berupa html. Selain itu, views.py juga dapat mengakses models untuk memenuhi request dari pengguna.
     4) models.py secara sederhana dapat dikatakan sebagai database tempat ditentukannya struktur suatu aplikasi.
     5) html, tampilan yang nantinya akan dilihat oleh pengguna
     refrensi: https://medium.com/@sundaram.2911/an-introduction-to-django-b17b51e3a7dc

3. Jelaskan peran settings.py dalam proyek Django!
Peran settings.py adalah sebagai tempat utama mengatur proyek django. Di dalam file tersebut, kita mengatur database, informasi dasar mengenai konfigurasi proyek seperti hosts yang dapat menjalankan proyek django

4. Bagaimana cara kerja migrasi database di Django?
migrasi database di Django bekerja dengan menghubungkan model pada models.py dan database aplikasi. Ketika pengembang membuat model baru ataupun mengubah model yang sudah ada perlu dilakukan "makemigrations" untuk membuat berkas migrasi yang berisi perubahan yang belum diaplikasikan ke basis data. Kemudian perintah "migrate" untuk mengaplikasikan perubahan model yang ada di dalam berkas migrasi ke dalam basis data.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Memiliki dokumentasi yang jelas, komunitasnya luas, pola MTV yang ada di dalamnya, dan skalabilitasnya yang baik.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
tutorial 1 memiliki tutorial yang sangat jelas sehingga mudah untuk diikuti, dan penjelasan tiap langkahnya memberi pemahaman yang baik mengenai Django.

TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? 
Data delivery menjadi penting karena berguna untuk memberikan informasi yang tepat mengenai data yang kita buat supaya akurat sesuai dengan kriteria yang kita inginkan, memberikan kemudahan mengakses data ketika kita membutuhkannya, dan memudahkan untuk mendeteksi saat terjadi error.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, lebih baik JSON dibandingkan dengan XML karena efektifitas dan simplisitas yang diprioritaskan JSON. JSON lebih populer dibandingkan XML karena JSON memberika fleksibilitas yang lebih baik dari XML, lebih compact, dan lebih mudah untuk ditulis dan dibaca oleh pengembang.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method .is_valid() pada objek form adalah untuk memvalidasi data, dan me-return boolean saat datanya valid. Method ini penting supaya form yang dibuat sesuai dengan aturan di dalam forms.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dibutuhkan untuk melindungi platform yang kita buat dari serangan CSRF. Jika tidak terdapat csrf_token akan menyebabkan platform kita menjadi lebih rentan dari serangan CSRF. Penyerang akan mengecoh user atau browser dengan membuat HTTP request kepada web yang rentan pada CSRF melalui malicious site, karena kerentanan tersebut penyerang akan mendapat kredensial pengguna lainnya yang seharusnya tidak terjadi jika terdapat csrf.

5. Step-step pengerjaan Tugas 2:
    1) Sebelum membuat 4 fungsi views, Buat forms.py terlebih dahulu yang meng-import Product dari models, dan ModelForm dari Django, lalu buat form baru dengan nama ProductForm. Di dalamnya, buat variabel Model = Product dan fields yang disesuaikan dengan atribut-atribut yang ada di model Product. Berpindah ke views, dari django.shortcuts import render, redirect, get_object_or_404, import Product dari models dan ProductForm dari forms. Kemudian, buatlah 4 fungsi views, sebagai berikut:
    ![alt text](https://drive.google.com/uc?export=view&id=1230ACSsus-E1nGrC1nWF57xxF8yPpnjF)
    
    2) Lakukan Routing ke tiap fungsi yang sudah dibuat dengan mengimportnya fungsi-fungsi tersebut ke views.  Tambahkan 4 path pada urlpaterns di views, seperti berikut: 
    		path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'), 
    3) Pada main.html yang berada di dalam direktori main/templates tambahkan kode berikut: 
            <a href="{% url 'main:create_product' %}">
            <button>+ Add Product</button>
            </a>
    kode tersebut akan memunculkan tombol “Add” yang akan memindahkan user ke halaman form. Selain itu, tambahkan kode berikut:
            {% for product in product_list %}
            <div>
            <h2><a href="{% url 'main:show_product' product.id %}">{{ product.title }}</a></h2>

            <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
                <b>Featured</b>{% endif %} | <i>{{ product.created_at|date:"d M Y H:i" }}</i> 
                </p>

            {% if product.thumbnail %}
            <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
            <br />
            {% endif %}

            <p>{{ product.content|truncatewords:25 }}...</p>

            <p><a href="{% url 'main:show_product' product.id %}"><button>Read More</button></a></p>
            </div>

            <hr>
            {% endfor %}
    Kode tersebut melakukan iterasi pada semua produk yang ada di dalam product_list, lalu memunculkan semua produk dengan judul, kategorinya, dan lain-lain. Tombol “Detail” akan men-direct user ke detail produk yang dipilihnya.

    4) Halaman form untuk menambahkan objek pada aplikasi sebelumnya dilakukan di file baru dalam direktori yang sama dengan main.html, bernama create_product.html. Halaman ini lah yang akan dibuka ketika user mengklik tombol “Add”.
        ![alt text](https://drive.google.com/uc?export=view&id=1s9AyQEtz64J_XvPG2zSeY41pdwHP8LPD)
    5) Halaman yang menampilkan detail setiap data produk yang ada, file product_detail.html ada di direktori yang sama dengan create_product.html
    ![alt text](https://drive.google.com/uc?export=view&id=1TXiGre-2RcbAX60OV56K09a0uE8MB2Nl)

    6. Tutorial 2 sangat membantu dalam mengerjakan tutorial 2, penjelasannya juga mudah dipahami

Postman
- XML
![XML](https://drive.google.com/uc?export=view&id=1wsw2twV4qQetoTk-9QkSuNMejph6NtrO)
- JSON
![JSON](https://drive.google.com/uc?export=view&id=161Ud3-F6G8sNfKrbLEHohtV85iTU_teD) 
- XML by ID
![XML by ID](https://drive.google.com/uc?export=view&id=1WvVHgCQirORgF6HTWPUJ2vwGvq5A5ljM)  
- JSON by ID
![JSON by ID](https://drive.google.com/uc?export=view&id=1V3ad9V7NhLKP2QLmt3u_MVR6gdKxMcIW)

Tugas 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Sebuah form class yang disediakan Django dan berguna untuk autentikasi user supaya dapat melakukan proses login. 
    Kelebihan:
    - built-in dan dapat langsung dipakai
    - terintegrasi langsung dengan auth yang ada dalam Django
    - memiliki validasi keamanan bawaan, yaitu memeriksa kecocokan username dengan password, mengetahui aktif tidaknya suatu akun, dan memberikan pesan error saat login tidak berhasil dilakukan.
    - mudah untuk dikostumisasi
    Kekurangan:
    - terbatas pada username dan password
    - tidak ada keamanan tambahan, seperti captcha, 2FA. Hal-hal tersebut haruus ditambahkan sendiri.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi memeriksa user login sebagai siapa, sedangkan otorisasi memberikan akses tertentu tergantung pada user yang login. Django menyediakan Authentication Framework untuk memverifikasi user. Selain itu, terdapat model user bawaan, login & logout, dan form & view. Django punya sistem permission yang melekat pada modelnya sehingga bisa memeriksa akses apa saja yang boleh dilakukan suatu user.

3.  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan Cookie: 
    1) Pengguna tidak perlu melakukan login berulang kali ketika mengakses halaman yang berbeda dari aplikasi web yang sama
    2) Tidak membebani server
    3) Mudah untuk digunakan, hanya perlu melakukan set header Set-Cookie dan browser otomatis mengirimkannya pada request selanjutnya.
Kekurangan Cookie:
    1) Kapasitas yang terbatas
    2) Keamanannya yang rentan sehingga mudah dicuri
    3) tidak cocok untuk menyimpan data yang sensitif

Kelebihan Session:
    1) Lebih aman, karena data yang sensitif tidak diterima oleh client
    2) Memiliki kapasitas yang tidak terbatas
    3) Dapat dikontrol oleh server
    4) Sulit untuk dimanipulasi client
Kekurangan Session:
    1) Beban server yang lebih berat
    2) Ketergantungan pada mekanisme Session
    3) Butuh penyimpanan tambahan

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Secara default tidak otomatis aman, ada beberapa risiko-risiko yang perlu diperhatikan, seperti pencurian cookie, XSS, dan CSRF. Django menangani hal-hal tersebut dengan HttpOnly Flag, Secure Flag, SameSite Attribute, CSRF protection.

5. Berikut ini cara saya mengimplementasi checklist di atas:
    1) Pada views.py, saya membuat fungsi register, login, logout, dan saya lakukan routing pada tiap-tiap fungsi tersebut. Setelahnya di dalam main/templates, saya membuat register.html yang akan menampilkan pembuatan akun, login.html untuk login user, dan menambahkan tombol logout di main.html. Kemudian supaya halaman main dan detail hanya bisa diakses oleh user yang sudah login, saya tambahakan decorator login_required di fungsi show_main dan show_product.
     
    2) Saya membuat 2 akun yang berbeda dan membuat 3 produk baru.
    ![Akun 1](https://drive.google.com/uc?export=view&id=1qKspyHLqKw9u8ficNCVOVkEN3HN0eA0a)
    ![Akun 2](https://drive.google.com/uc?export=view&id=14e8erx8cA6qa54dftqkWONoWQk0HCkAH)

    3) pada Models.py import User, dan tambahkan User di model Product. Kemudian makemigrations dan migrate. Kemudian di fungsi create_product tambahakan request.user pada product_entry  dan show_main tambahkan filter produk yang disesuaikan dengan user yang login. Tambahkan juga tombol filter di main.html, lalu product.user.username di product_detail.html

    4) Pada main.html tambahkan kode berikut:
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        <h5>User yang sedang login: {{ user }}</h5>

Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    Urutannya sebagai berikut:
    1) inline styles, contohnya <h1 style="color: pink;"> (Highest priority, override selector lainnya)
    2) Id selectors, contohnya #navbar dengan weight 1-0-0 (Second highest priority)
    3) Classes, attribute selectors and pseudo-classes. Contohnya .test, [type="text"], :hover dengan weight 0-1-0 (Third highest priority)
    4) Elements and pseudo-elements, contohnya h1, ::before, ::after dengan weight 0-0-1 (Low priority)
    5) Universal selector and :where(), weight 0-0-0 (no priority)
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Karena memberikan konsistenitas, pengalaman penggunaan yang dapat dinikmati oleh user, dan biaya lebih murh dibanding membuat versi tiap perangkat yang berbeda. Contoh responsive: medium. youtube. Alasannya bisa dipakai semua perangkat dengan nyaman. Contoh ysng belum: web-web pemerintah yang lama. Alasannya karena dibuat saat penggunaan lintas perangkat belum diprioritaskan.
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    - Padding: mengosongkan area di sekitar konten (transparan)
    - Border: garis tepian yang membungkus konten dan padding-nya
    - Margin: mengosongkan area di sekitar border (transparan)
    Untuk implementasinya menggunakan px, dan jika ingin sisi tertentu spesifik right, left, bottom, top.
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox merupakan metode layouting satu dimensi dan berbasis pada content (item) itu sendiri yang dapat dikatakan sebagai item terkecil dari layout. Bagus untuk perataan tiap elemen, yaitu memposisikan elemen yang lebih kecil  atau detail.
- Grid adalah memodelkan layout sebagai baris dan kolom (row and column) sehingga dalam pembuatan layout nya kita baca sebagai dua dimensi, yaitu row (kiri-kanan) dan column (atas-bawah). Digunakan untuk mengatur gambar yang besar dan untuk layout yang dua dimensi.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    1) Menambahkan fungsi di views, lakukan routing di urls.py, dan tambahkan pada main.html
    2) Tambahkan cdn tailwind di base.html, load static di tiap file html di main/templates dan buat card_product, buat folder static di root, lalu buat css/global.css dan image/no_image.png. Selain itu, buat navbar.html di root/templates.
    Berikan style di global.css (ini opsional), dan di tiap-tiap file-file html yang ada dalam main/templates