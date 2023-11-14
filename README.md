## Getting Started

1. Buka command prompt lalu masuk ke direktori yang diinginkan
2. Clone repositori program aplikasi back end di GitHub https://github.com/diskuskuy/diskuskuy-be pada branch develop (merupakan branch yang paling up to date) menggunakan command:

`git clone https://github.com/diskuskuy/diskuskuy-be`

3. Masuk ke dalam folder proyek diskuskuy-be kemudian buat virtual environment menggunakan command:

`python -m venv [nama-folder-virtual-environment]`

4. Aktifkan virtual environment menggunakan command:

`[nama-folder-virtual-environment]\scripts\activate.bat`

5. Instalasi requirements di dalam requirements.txt menggunakan command:

`pip install -r requirements.txt`

6. Buka text editor, lalu ganti konfigurasi basis data di diskuskuy_be/settings.py sesuai kebutuhan. Di bawah ini merupakan contoh konfigurasi basis data untuk terhubung dengan basis data di server PostgreSQL:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': [nama_basis_data],
        'USER': [user],
        'PASSWORD': [password],
        'HOST': [IP address host],
        'PORT': [port],
    }
}`

Nilai ENGINE dapat disesuaikan dengan SQL server yang digunakan. Sedangkan nilai NAME, USER, PASSWORD, HOST, PASSWORD, HOST, dan PORT disesuaikan dengan basis data yang akan digunakan. HOST dan PORT disesuaikan dengan basis data yang digunakan. Jika ingin terhubung ke basis data pada server yang dijalankan di mesin yang sama, maka nilai HOST menjadi `127.0.0.1` dan nilai PORT menjadi port server postgreSQL, umumnya 5432. Jika ingin terhubung ke basis data di server cloud, maka nilai HOST dan PORT menjadi host dan port dari basis data tersebut. Untuk nilai NAME, USER, dan PASSWORD, diisi dengan data user, password, dan nama basis data yang dibuat di server.

7. Lakukan migrasi basis data menggunakan command:

`python manage.py makemigrations`

`python manage.py migrate`

8. Jalankan program aplikasi back end dengan command:

`python3 manage.py runserver`

Server back end akan berjalan pada port 8000. dengan url `http://127.0.0.1:8000`. Aplikasi back end dapat digunakan sendiri atau dipanggil dari aplikasi front end.
