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
- class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  fungsi ini class Node: Ini adalah kelas untuk merepresentasikan simpul atau node dalam linked list. Setiap simpul memiliki dua atribut: data, yang menyimpan data yang diinginkan, dan next, yang adalah referensi ke simpul berikutnya dalam linked list.
__init__(self, data): Ini adalah konstruktor kelas Node. Ketika sebuah objek Node dibuat, konstruktor ini dijalankan. Ini menginisialisasi data simpul dengan nilai yang diberikan dan mengatur next menjadi None (karena simpul baru belum ditautkan ke simpul lain).
- class LinkedList
- class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
  class LinkedList: Ini adalah kelas untuk merepresentasikan linked list itu sendiri. Linked list memiliki satu atribut utama, yaitu head, yang merupakan referensi ke simpul pertama dalam linked list.
__init__(self): Ini adalah konstruktor kelas LinkedList. Ketika sebuah objek LinkedList dibuat, konstruktor ini dijalankan. Ini menginisialisasi head menjadi None, karena linked list awalnya kosong.
append(self, data): Ini adalah metode untuk menambahkan data baru ke akhir linked list. Metode ini membuat sebuah simpul baru dengan data yang diberikan, kemudian menautkannya ke linked list. Jika linked list masih kosong (artinya head adalah None), simpul baru tersebut akan diatur sebagai head. Jika tidak, metode ini akan mencari simpul terakhir dalam linked list dan menautkan simpul baru tersebut ke simpul terakhir menggunakan atribut next.
- 
### C. Fungsi
- def append
- def quicksort(arr, key=lambda x: x[0], reverse=False): Fungsi ini digunakan untuk mengurutkan array menggunakan algoritma quicksort. Fungsi ini memiliki parameter arr yang merupakan array yang akan diurutkan, key yang merupakan fungsi kunci untuk menentukan kriteria pengurutan (secara default pengurutan dilakukan berdasarkan elemen pertama dari tuple), dan reverse yang menentukan apakah pengurutan dilakukan secara ascending atau descending.
  
- def jump_search(arr, x): Fungsi ini digunakan untuk mencari elemen dalam array menggunakan algoritma jump search. Fungsi ini memiliki parameter arr yang merupakan array yang akan dicari, dan x yang merupakan elemen yang ingin dicari.
  
- def search_user_by_name(): Fungsi ini meminta input nama pengguna dari pengguna, kemudian mencari data pengguna berdasarkan nama pengguna yang dimasukkan. Jika data ditemukan, informasi pengguna ditampilkan. Jika tidak, pesan bahwa data tidak ditemukan akan ditampilkan.
  
- def authenticate_admin(nama_admin): Fungsi ini digunakan untuk mengotentikasi admin berdasarkan nama admin yang diberikan. Fungsi ini akan melakukan pencarian di database untuk mencocokkan nama admin.
  
- def tambah_data_pengguna(): Fungsi ini meminta input data pengguna (ID pengguna, ID materi, nama pengguna, keterampilan, tujuan karier), kemudian menambahkan data tersebut ke database.
  
- def tampilkan_data_pengguna(): Fungsi ini menampilkan seluruh data pengguna yang ada dalam database.
  
- def update_data_pengguna(): Fungsi ini meminta input ID pengguna yang ingin diperbarui, kemudian memperbarui data pengguna berdasarkan input yang diberikan.
  
- def hapus_data_pengguna(): Fungsi ini meminta input ID pengguna yang ingin dihapus, kemudian menghapus data pengguna dari database.
  
- def show_edit_tabel(): Fungsi ini menampilkan menu untuk mengedit tabel data pengguna.
  
- def choose_edit_tabel(): Fungsi ini meminta input pilihan dari pengguna dan memilih tindakan yang sesuai berdasarkan pilihan tersebut.
  
- def authenticate_pengguna(nama_pengguna): Fungsi ini digunakan untuk mengotentikasi pengguna berdasarkan nama pengguna yang diberikan.
  
- def show_admin_menu(): Fungsi ini menampilkan menu untuk admin.
  
- def login_admin(): Fungsi ini meminta nama admin, kemudian melakukan proses login sebagai admin. Setelah login berhasil, menu admin akan ditampilkan.
  
- def show_training_method_menu(): Fungsi ini menampilkan menu untuk memilih metode pelatihan.
  
- def choose_training_method(): Fungsi ini meminta input pilihan metode pelatihan dari pengguna dan mengembalikan metode yang dipilih.
  
- def show_training_session_menu(): Fungsi ini menampilkan menu untuk memilih sesi pelatihan.
  
- def choose_training_session(): Fungsi ini meminta input pilihan sesi pelatihan dari pengguna dan mengembalikan sesi yang dipilih.
  
- def show_user_menu(): Fungsi ini menampilkan menu untuk pengguna.

- def show_learning_materials(): Fungsi ini menampilkan menu untuk memilih materi pembelajaran.
  
- def show_training_day_menu(): Fungsi ini menampilkan menu untuk memilih hari pelatihan.
  
- def login_pengguna(): Fungsi ini digunakan untuk login sebagai pengguna. Setelah login berhasil, menu pengguna akan ditampilkan.

- def main(): Fungsi utama yang menjalankan program. Pada fungsi ini, pengguna diminta untuk memilih apakah akan login sebagai admin atau pengguna, atau keluar dari program.
  
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

