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
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/1dc96f5a-9e5a-4250-9bb1-32e8f1f19693)

1. import mysql.connector, untuk menghubungkan program Python dengan database MySQL
2. from prettytable import PrettyTable, untuk membuat hasil tampilan program berbentuk tabel sehingga tampilan terlihat rapi dan terstruktur.

### B. Linked List
- class Node: fungsi ini class Node: Ini adalah kelas untuk merepresentasikan simpul atau node dalam linked list. Setiap simpul memiliki dua atribut: data, yang menyimpan data yang diinginkan, dan next, yang adalah referensi ke simpul berikutnya dalam linked list.
__init__(self, data): Ini adalah konstruktor kelas Node. Ketika sebuah objek Node dibuat, konstruktor ini dijalankan. Ini menginisialisasi data simpul dengan nilai yang diberikan dan mengatur next menjadi None (karena simpul baru belum ditautkan ke simpul lain).
- ![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/64906bc3-a937-43ac-98a1-534cc3f51206)

- class LinkedList: Ini adalah kelas untuk merepresentasikan linked list itu sendiri. Linked list memiliki satu atribut utama, yaitu head, yang merupakan referensi ke simpul pertama dalam linked list.
__init__(self): Ini adalah konstruktor kelas LinkedList. Ketika sebuah objek LinkedList dibuat, konstruktor ini dijalankan. Ini menginisialisasi head menjadi None, karena linked list awalnya kosong.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/00ef0ce6-ff7c-4483-aef6-a085483fdadf)

  
### C. Fungsi
- def append(self, data): Ini adalah metode untuk menambahkan data baru ke akhir linked list. Metode ini membuat sebuah simpul baru dengan data yang diberikan, kemudian menautkannya ke linked list. Jika linked list masih kosong (artinya head adalah None), simpul baru tersebut akan diatur sebagai head. Jika tidak, metode ini akan mencari simpul terakhir dalam linked list dan menautkan simpul baru tersebut ke simpul terakhir menggunakan atribut next.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/9f26da5b-85d5-4f18-bcf0-87ac5e974ded)

- def quicksort(arr, key=lambda x: x[0], reverse=False): Fungsi ini digunakan untuk mengurutkan array menggunakan algoritma quicksort. Fungsi ini memiliki parameter arr yang merupakan array yang akan diurutkan, key yang merupakan fungsi kunci untuk menentukan kriteria pengurutan (secara default pengurutan dilakukan berdasarkan elemen pertama dari tuple), dan reverse yang menentukan apakah pengurutan dilakukan secara ascending atau descending.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/b1cc8e74-81c3-4a1a-8101-5dbd910897ad)
  
- def jump_search(arr, x): Fungsi ini digunakan untuk mencari elemen dalam array menggunakan algoritma jump search. Fungsi ini memiliki parameter arr yang merupakan array yang akan dicari, dan x yang merupakan elemen yang ingin dicari.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/fa5a0e3b-4d4d-48d1-86ce-b695986f7b6a)
  
- def search_user_by_name(): Fungsi ini meminta input nama pengguna dari pengguna, kemudian mencari data pengguna berdasarkan nama pengguna yang dimasukkan. Jika data ditemukan, informasi pengguna ditampilkan. Jika tidak, pesan bahwa data tidak ditemukan akan ditampilkan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/312d4544-d262-4496-8411-10c435c0a5e4)

- def authenticate_admin(nama_admin): Fungsi ini digunakan untuk mengotentikasi admin berdasarkan nama admin yang diberikan. Fungsi ini akan melakukan pencarian di database untuk mencocokkan nama admin.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/f6f08b74-746a-47cb-9c8c-4bdde068e74a)

- def tambah_data_pengguna(): Fungsi ini meminta input data pengguna (ID pengguna, ID materi, nama pengguna, keterampilan, tujuan karier), kemudian menambahkan data tersebut ke database.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/73f19030-0e6a-4a4d-a2ef-e3836da7ab86)
  
- def tampilkan_data_pengguna(): Fungsi ini menampilkan seluruh data pengguna yang ada dalam database.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/c304165e-a2d1-4eed-952a-8949cc24e5d6)

- def update_data_pengguna(): Fungsi ini meminta input ID pengguna yang ingin diperbarui, kemudian memperbarui data pengguna berdasarkan input yang diberikan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/0dd14750-b1c5-4534-963b-df6f17db950b)

- def hapus_data_pengguna(): Fungsi ini meminta input ID pengguna yang ingin dihapus, kemudian menghapus data pengguna dari database.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/d9d6f75e-7953-405d-a9b1-7477ff52754a)

- def show_edit_tabel(): Fungsi ini menampilkan menu untuk mengedit tabel data pengguna.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/fbb96e94-a8cb-4656-aec8-74e775d39cf9)

- def choose_edit_tabel(): Fungsi ini meminta input pilihan dari pengguna dan memilih tindakan yang sesuai berdasarkan pilihan tersebut.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/ae32a74b-e7c3-478e-94b3-717fe94c3fb4)

- def authenticate_pengguna(nama_pengguna): Fungsi ini digunakan untuk mengotentikasi pengguna berdasarkan nama pengguna yang diberikan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/f1b07cc4-b3d4-46de-b768-a7c14eedae6b)

- def show_admin_menu(): Fungsi ini menampilkan menu untuk admin.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/f82ea851-f743-4e49-bbca-03d5b286fc70)

- def login_admin(): Fungsi ini meminta nama admin, kemudian melakukan proses login sebagai admin. Setelah login berhasil, menu admin akan ditampilkan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/28555a01-b5c6-4fec-878d-57a6fde33e4d)

- def show_training_method_menu(): Fungsi ini menampilkan menu untuk memilih metode pelatihan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/cd2bafb7-ab42-49b5-9d72-320a801339fa)

- def choose_training_method(): Fungsi ini meminta input pilihan metode pelatihan dari pengguna dan mengembalikan metode yang dipilih.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/66f8a29e-8592-41fd-a4b9-704d00e07988)

- def show_training_session_menu(): Fungsi ini menampilkan menu untuk memilih sesi pelatihan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/27fd5517-5255-4dce-8303-436a87307a3f)

- def choose_training_session(): Fungsi ini meminta input pilihan sesi pelatihan dari pengguna dan mengembalikan sesi yang dipilih.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/c66178fd-6065-4220-8c6b-15ad51774f4b)

- def show_user_menu(): Fungsi ini menampilkan menu untuk pengguna.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/70261ef7-fd2e-45b2-bf24-3d58290444f4)

- def show_learning_materials(): Fungsi ini menampilkan menu untuk memilih materi pembelajaran.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/1e4f06c1-3c91-4408-8d17-086a8b04e9c1)

- def show_training_day_menu(): Fungsi ini menampilkan menu untuk memilih hari pelatihan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/12bea675-a0bc-415f-9151-1d5d24dee9e6)

- def login_pengguna(): Fungsi ini digunakan untuk login sebagai pengguna. Setelah login berhasil, menu pengguna akan ditampilkan.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/cf3f98a5-a149-457e-bdf2-4aff3913d1a0)

- def main(): Fungsi utama yang menjalankan program. Pada fungsi ini, pengguna diminta untuk memilih apakah akan login sebagai admin atau pengguna, atau keluar dari program.
![image](https://github.com/PA-B23-KELOMPOK4/PA-B23-KELOMPOK4/assets/144610446/1c6af0b4-910d-4a49-b13f-7f6baa4e4822)

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

