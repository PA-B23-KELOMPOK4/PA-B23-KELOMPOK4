# PLATFORM MIRIN
---------------------------------------------------------------------------------------------------------
## DESKRIPSI PROGRAM
> Platform Pelatihan dan Pengembangan Keterampilan (MIRIN) dibuat untuk memberikan akses mudah dan terjangkau kepada pelatihan yang relevan dengan kebutuhan pasar tenaga kerja saat ini. Tujuannya adalah membantu individu meningkatkan keterampilan mereka sesuai dengan perkembangan industri dan teknologi. MIRIN menawarkan fleksibilitas belajar dan inklusivitas akses, memungkinkan individu dari berbagai latar belakang dan lokasi untuk mengakses materi pembelajaran terkini sesuai jadwal dan preferensi mereka sendiri. Melalui evaluasi efektivitasnya, MIRIN bertujuan untuk memberikan wawasan bagi pengembang platform edukasi dan pelatihan serta pemangku kepentingan dalam ekosistem ketenagakerjaan.

> Platform Pelatihan dan Pengembangan Keterampilan (MIRIN) menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Struktur data ini digunakan untuk mengelola informasi terkait platform MIRIN. Selain itu, MIRIN  menggunakan database lokal untuk menyimpan data pengguna, data platform, dan data administrator, memungkinkan pengguna mengakses informasi platform dan materi pembelajaran dengan mudah  serta menyimpan pengaturan akun  tanpa kehilangan data.

## STRUKTUR PROJECT
## Flowchart ##

![WhatsApp Image ](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144861672/229b47e5-871c-4b40-87e7-4095a6f1c917)

![WhatsApp Image ](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144861672/e248410a-d23d-4cf0-8d9d-269467bd78f3)

![WhatsApp Image ](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144861672/df79aaf2-f01e-49e7-99de-ea71a4216817)


### A. Library
1. import mysql.connector, untuk menghubungkan program Python dengan database MySQL
2. from prettytable import PrettyTable, untuk membuat hasil tampilan program berbentuk tabel sehingga tampilan terlihat rapi dan terstruktur.
### B. Linked List
- class Node
- class LinkedList
### C. Fungsi
- def append
- def quicksort
- def jump_search
- def search_user_by_name
- def authenticate_admin
- def tambah_data_pengguna
- def tampilkan_data_pengguna
- def update_data_pengguna
- def hapus_data_pengguna
- def show_edit_tabel
- def choose_edit_tabel
- def authenticate_pengguna
- def show_admin_menu
- def login_admin
- def show_training_method_menu
- def choose_training_method
- def show_training_session_menu
- def choose_training_session
- def show_user_menu
- def show_learning_materials
- def show_training_day_menu
- def login_pengguna
  
## FITUR
Adapun fitur fitur yang terdapat dalam program platform mirin yaitu:
- Login sebagai admin
- Login sebagai pengguna
- Menambahkan data pengguna
- Menampilkan data pengguna
- Menghapus data pengguna
- Mengupdate data pengguna
- Megurutkan data pengguna
- Search data pengguna
- Menampilkan dan memilih materi pembelajran
- Menampilkan dan memilih metode pelatihan
- Menampilkan dan memilih hari pelatihan
- Menampilkan dan memilih sesi pelatihan
- Menampilkan hasil jadwal pelatihan pengguna

## FUNGSIONALITAS
> User melakukan login terlebih dahulu untuk masuk ke dalam program, dengan cara memasukkan nama user yang sesuai. User dapat memilih dua pilihan login yaitu login sebagai admin atau login sebagai pengguna, user juga dapat keluar dari program dengan memilih menu keluar. Penjelasan terkait fungsionalitas 2 jenis user tersebut yaitu:

**1. Admin**
- Menambah, Admin memiliki akses untuk menambah data pengguna baru ke dalam database
- Menampilkan, Admin memiliki akses untuk melihat semua data pengguna yang ada didalam database
- Menghapus, Admin memiliki akses untuk menghapus data pengguna dari database
- Mengupdate, Admin memiliki akses untuk memperbarui data pengguna di database
- Mengurutkan, Admin dapat melakukan pengurutan data pengguna berdasarkan nama
- Searching, Admin dapat mencari data pengguna yang diinginkan berdasarkan nama

**2. Pengguna**
- Memilih, pengguna dapat memilih materi pembelajaran, metode pelatihan, hari pelatihan, dan sesi pelatihan sesuai dengan kterampilan yang ingin ditingkatkan oleh pengguna
- Menampilkan, pengguna dapat melihat menu terlebih dahulu sebelum melakukan inputan pilihan dan dapat melihat jadwal yang telah dipilih oleh pengguna

