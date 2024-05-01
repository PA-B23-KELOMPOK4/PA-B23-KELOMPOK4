import mysql.connector
from prettytable import PrettyTable


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mirin"
)

mycursor = mydb.cursor()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

# Fungsi quicksort untuk pengurutan data
def quicksort(arr, key=lambda x: x[0], reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x) < key(pivot)]
    center = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]
    if reverse:
        return quicksort(right, key, reverse) + center + quicksort(left, key, reverse)
    else:
        return quicksort(left, key, reverse) + center + quicksort(right, key, reverse)
    
def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n)-1][1].lower() < x.lower():  
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev][1].lower() < x.lower():  
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev][1].lower() == x.lower():  
        return prev
    return -1

def search_user_by_name():
    nama_pengguna = input("Masukkan nama pengguna: ")
    try:
        mycursor.execute("SELECT * FROM pengguna WHERE nama_pengguna = %s", (nama_pengguna,))
        result = mycursor.fetchone()
        if result:
            print("------------------------")
            print("Data pengguna ditemukan:")
            print("------------------------")
            table = PrettyTable(["ID Pengguna", "ID materi", "Nama pengguna", "Tujuan Karier"])
            table.add_row(result[0:4])
            print(table)
        else:
            print("------------------------------")
            print("Data pengguna tidak ditemukan.")   
            print("------------------------------") 
    except Exception as e:
        print("Error:", e)   
    
# Fungsi untuk melakukan autentikasi admin
def authenticate_admin(nama_admin):
    try:
        mycursor.execute("SELECT * FROM admin WHERE nama_admin = %s", (nama_admin,))
        result = mycursor.fetchone()
        return result is not None
    except Exception as e:
        print("Error:", e)
        return False
     
# Fungsi untuk menambahkan pengguna
def tambah_data_pengguna():
    try:
        id_pengguna = int(input("ID Pengguna: "))
        id_materi = int(input("ID Materi: "))
        nama_pengguna = input("Nama pengguna: ")
        keterampilan = input("Keterampilan: ")
        tujuan_karier = input("Tujuan karier: ")

        # Memeriksa apakah input sesuai dengan tipe data yang diharapkan
        if not (isinstance(id_pengguna, int) and isinstance(id_materi, int)):
            raise ValueError("ID Pengguna dan ID Materi harus berupa bilangan bulat.")
        if not nama_pengguna.replace(" ", "").isalpha():
            raise ValueError("Nama pengguna hanya boleh berisi huruf.")
        if not (keterampilan.replace(" ", "").isalpha() and tujuan_karier.replace(" ", "").isalpha()):
            raise ValueError("Keterampilan dan tujuan karier hanya boleh berisi huruf.")

        query = "INSERT INTO pengguna (id_pengguna, id_materi, nama_pengguna, keterampilan, tujuan_karier) VALUES (%s, %s, %s, %s, %s)"
        values = (id_pengguna, id_materi, nama_pengguna, keterampilan, tujuan_karier)

        mycursor.execute(query, values)
        mydb.commit()
        print("-----------------------------------")
        print("Data pengguna berhasil ditambahkan!")
        print("-----------------------------------")

        # Setelah menambahkan data pengguna, tampilkan data pengguna
        tampilkan_data_pengguna()

    except Exception as e:
        print("Error:", e)
        mydb.rollback()




# Fungsi untuk menampilkan data pengguna
def tampilkan_data_pengguna():
    try:
        mycursor.execute("SELECT * FROM pengguna")
        results = mycursor.fetchall()
        if results:
            table = PrettyTable()
            table.field_names = ["ID Pengguna", "iD materi" ,"Nama Pengguna", "Keterampilan", "Tujuan Karier"]
            for row in results:
                table.add_row(row[0:5])  
            
            print("--------------")
            print("Data Pengguna:")
            print("--------------")
            print(table)
        else:
            print("------------------------")
            print("Tidak ada data pengguna.") 
            print("------------------------") 

    except Exception as e:
        print("Error:", e)

# Fungsi untuk mengupdate data pengguna
def update_data_pengguna():
    try:
        id_pengguna = int(input("Masukkan ID pengguna yang ingin diperbarui: "))
        nama_pengguna_baru = input("Masukkan nama pengguna baru: ")
        id_materi_baru = int(input("Masukkan ID Materi baru: "))
        keterampilan_baru = input("Masukkan keterampilan baru: ")
        tujuan_karier_baru = input("Masukkan tujuan karier baru: ")

        if not id_materi_baru.isdigit():
            raise ValueError("Nama pengguna, Keterampilan dan tujuan karier hanya boleh berisi huruf.")

        query = "UPDATE pengguna SET nama_pengguna = %s, Id_materi = %s, keterampilan = %s, tujuan_karier = %s WHERE id_pengguna = %s"
        values = (nama_pengguna_baru, id_materi_baru, keterampilan_baru, tujuan_karier_baru, id_pengguna)


        mycursor.execute(query, values)
        mydb.commit()
        print("----------------------------------")
        print("Data pengguna berhasil diperbarui!")
        print("----------------------------------")
    except Exception as e:
        print("Error:", e)
        mydb.rollback()

# Fungsi untuk menghapus data pengguna
def hapus_data_pengguna():
    try:
        id_pengguna = int(input("Masukkan ID pengguna yang ingin dihapus: "))
        query = "DELETE FROM pengguna WHERE id_pengguna = %s"
        values = (id_pengguna,)
        mycursor.execute(query, values)
        mydb.commit()
        print("-------------------------------")
        print("Data pengguna berhasil dihapus!")
        print("-------------------------------")
    except Exception as e:
        print("Error:", e)
        mydb.rollback()


def show_edit_tabel():
    print("=================================")
    print("|Silahkan pilih menu edit tabel:|")
    print("=================================")
    print("| 1. Tambah data pengguna       |")
    print("| 2. Tampilkan data pengguna    |")
    print("| 3. Update data pengguna       |")
    print("| 4. Hapus data pengguna        |")
    print("| 5. Keluar                     |")
    print("=================================")

def choose_edit_tabel():
    while True:
        show_edit_tabel()
        edit_choice = input("Masukkan pilihan metode: ")
        if edit_choice == "1":
            print("----------------------------------")
            print("Anda memilih Tambah data pengguna.")
            print("----------------------------------")
            tambah_data_pengguna()
            return "Tambah"  
        elif edit_choice == "2":
            print("-------------------------------------")
            print("Anda memilih Tampilkan data pengguna.")
            print("-------------------------------------")
            tampilkan_data_pengguna()
            return "Tampilkan"  
        elif edit_choice == "3":
            print("---------------------------------")
            print("Anda memilih update data pengguna")
            print("---------------------------------")
            update_data_pengguna()
        elif edit_choice == "4":
            print("--------------------------------")
            print("Anda memilih hapus data pengguna")
            print("--------------------------------")
            hapus_data_pengguna()
            return "hapus"
        elif edit_choice == "5":
            print("--------------------------")
            print("kembali ke menu sebelumnya")
            print("--------------------------")
            return None  
        else:
            print("---------------------------------------------------------")
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
            print("---------------------------------------------------------")

# Autentikasi pengguna
def authenticate_pengguna(nama_pengguna):
    try:
        mycursor.execute("SELECT * FROM pengguna WHERE nama_pengguna = %s", (nama_pengguna,))
        result = mycursor.fetchone()
        return result is not None
    except Exception as e:
        print("Error:", e)
        return False

def show_admin_menu():
    print("===============================")
    print("|        Menu Admin:          |")
    print("===============================")
    print("|    1. Edit Tabel            |")
    print("|    2. Cek Data Pengguna     |")
    print("|    3. Sorting Nama Pengguna |")
    print("|    4. Search Nama Pengguna  |") 
    print("|    5. Logout                |")
    print("===============================")

# Fungsi untuk menampilkan menu admin
def login_admin():
    try:
        nama_admin = input("Nama admin: ")
        if authenticate_admin(nama_admin):
            print("-----------------------------")
            print("Login berhasil sebagai admin.")
            print("-----------------------------")
            while True:
                show_admin_menu()
                choice = input("Masukkan pilihan: ")
                if choice == "1":
                    chosen_action = choose_edit_tabel()
                    if chosen_action == "Tambah":
                        print("------------------------------------------")
                        print("Anda memilih untuk menambah data pengguna.")
                        print("------------------------------------------")
                    elif chosen_action == "Tampilkan":
                        print("---------------------------------------------")
                        print("Anda memilih untuk menampilkan data pengguna.")
                        print("---------------------------------------------")
                    elif chosen_action == "hapus":
                        print("-------------------------------------------")
                        print("Anda memilih untuk menghapus data pengguna.")
                        print("-------------------------------------------")
                    elif chosen_action == "Cari":
                        search_user_by_name()  
                elif choice == "2":
                    tampilkan_data_pengguna()
                    print("------------------------------------------")
                    print("Anda memilih untuk mengecek data pengguna.")
                    print("------------------------------------------")
                elif choice == "3":
                    # Pengurutan nama pengguna
                    print("----------------------------------------------------")
                    print("|                    Pengurutan                    |")
                    print("----------------------------------------------------")
                    print("|    1. Urutkan nama pengguna secara ascending     |")
                    print("|    2. Urutkan nama pengguna secara descending    |")
                    print("----------------------------------------------------")
                    sorting_choice = input("Pilih opsi pengurutan: ")
                    if sorting_choice in ("1", "2"):
                        ascending = sorting_choice == "1"

                        mycursor.execute("SELECT nama_pengguna FROM pengguna")
                        users = mycursor.fetchall() 

                        sorted_users = quicksort(users, key=lambda x: x[0].lower(), reverse=not ascending)

                        table = PrettyTable(["Nama Pengguna"])
                        for user in sorted_users:
                            table.add_row([user[0]])
                        print("-----------------")
                        print("Hasil pengurutan:")
                        print("-----------------")
                        print(table)
                        show_admin_menu
                    else:
                        print("Pilihan tidak valid.")
                elif choice == "4":
                    print("-----------------------------------------")
                    print("Anda memilih untuk mencari nama pengguna.")
                    print("-----------------------------------------")
                    search_user_by_name()  
                elif choice == "5":
                    print("Logout")
                    break
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Login gagal. Periksa kembali nama admin Anda.")
    except EOFError:
        print("---------------------------------------------------------")
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        print("---------------------------------------------------------")


def show_training_method_menu():
    print("Silahkan pilih Metode Pelatihan:")
    table = PrettyTable(["Nomor", "Metode Pelatihan"])
    table.add_row(["1", "Offline"])
    table.add_row(["2", "Online"])
    table.add_row(["3", "Kembali"])
    print(table)


def choose_training_method():
    while True:
        show_training_method_menu()
        method_choice = input("Masukkan pilihan metode: ")
        if method_choice == "1":
            print("Anda memilih pelatihan offline.")
            return "Offline"  
        elif method_choice == "2":
            print("Anda memilih pelatihan online.")
            return "Online"  
        elif method_choice == "3":
            print("Kembali ke menu sebelumnya...")
            return None  
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

def show_training_session_menu():
    sessions = {
        "1": "Sesi pagi (08.00-10.00)",
        "2": "Sesi siang (13.00-15.00)",
        "3": "Sesi malam (19.00-21.00)",
        "4": "Kembali"
    }

    print("Silahkan pilih Sesi Pelatihan:")
    table = PrettyTable(["Nomor", "Sesi Pelatihan"])
    for key, value in sessions.items():
        table.add_row([key, value])
    print(table)


def choose_training_session():
    while True:
        show_training_session_menu()
        session_choice = input("Masukkan pilihan sesi pelatihan: ")
        if session_choice == "1":
            print("Anda memilih sesi pagi (08.00-10.00).")
            return "Sesi pagi (08.00-10.00)"  
        elif session_choice == "2":
            print("Anda memilih sesi siang (13.00-15.00).")
            return "Sesi siang (13.00-15.00)"  
        elif session_choice == "3":
            print("Anda memilih sesi malam (19.00-21.00).")
            return "Sesi malam (19.00-21.00)"  
        elif session_choice == "4":
            print("Kembali ke menu sebelumnya")
            return None  
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

def show_user_menu():
    print("------------------------------------")
    print("|          Menu Pengguna:          |")
    print("------------------------------------")
    print("|  1. Tampilkan Materi Pembelajaran|")
    print("|  2. Logout                       |")
    print("------------------------------------")

from prettytable import PrettyTable

def show_learning_materials():
    materials = {
        "1": "Desain grafis ui/ux",
        "2": "Pemrograman",
        "3": "Kemampuan interpersonal",
        "4": "Analisis data",
        "5": "Database",
        "6": "Kembali"
    }

    print("Materi Pembelajaran:")
    table = PrettyTable(["Nomor", "Materi"])
    for key, value in materials.items():
        table.add_row([key, value])
    print(table)

    while True:
        choice = input("Masukkan pilihan: ")
        if choice in materials:
            if choice != "6":
                return materials[choice]
            else:
                return None
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")



def show_training_day_menu():
    days = {
        "1": "Senin",
        "2": "Selasa",
        "3": "Rabu",
        "4": "Kamis",
        "5": "Jum'at",
        "6": "Kembali"
    }

    print("Silahkan masukkan pilihan hari pelatihan:")
    table = PrettyTable(["Nomor", "Hari Pelatihan"])
    for key, value in days.items():
        table.add_row([key, value])
    print(table)


    while True:
        choice = input("Masukkan pilihan hari pelatihan: ")
        if choice in days:
            if choice != "6":  
                return days[choice]  
            else:
                return None  
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

def login_pengguna():
    nama_pengguna = input("Nama Pengguna: ")
    try:
        if authenticate_pengguna(nama_pengguna):
            print("Login berhasil sebagai pengguna.")
            while True:
                show_user_menu()  
                choice = input("Masukkan pilihan: ")
                if choice == "1":
                    materi = show_learning_materials() 
                    if materi is not None:
                        metode = choose_training_method()  
                        if metode is not None:
                            hari = show_training_day_menu()  
                            if hari is not None:
                                sesi = choose_training_session()  
                                if sesi is not None:
                                    table = PrettyTable()
                                    table.field_names = ["Nama Pengguna", "Materi", "Metode Pelatihan", "Hari Pelatihan", "Sesi Pelatihan"]
                                    table.add_row([nama_pengguna, materi, metode, hari, sesi])
                                    print("Pilihan Pelatihan:")
                                    print(table)
                                    break
                elif choice == "2":
                    print("Logout...")
                    break
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Login gagal. Periksa kembali nama pengguna Anda.")
        print("Terima kasih sudah menggunakan Mirin.")
    except EOFError:
            print("---------------------------------------------------------")
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
            print("---------------------------------------------------------")

# Fungsi utama
def main():
    while True:
        print("==============================================")
        print("|     SELAMAT DATANG DI PLATFORM MIRIN!      |")
        print("==============================================")
        print("|            1. Admin                        |")
        print("|            2. Pengguna                     |")
        print("|            3. Keluar                       |")
        print("==============================================")
        try:
            login_choice = input("Pilih opsi login: ")
        except EOFError:
            print("---------------------------------------------------------")
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
            print("---------------------------------------------------------")
            continue

        if login_choice == "1":
            login_admin()
        elif login_choice == "2":
            login_pengguna()
        elif login_choice == "3": 
            print("----------------------------------------------")  
            print("Terima kasih telah menggunakan platform Mirin!")
            print("----------------------------------------------")
            break
        else:
            print("--------------------")
            print("Pilihan tidak valid.")
            print("--------------------")

main()


