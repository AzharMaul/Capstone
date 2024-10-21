from tabulate import tabulate

daftar_buku = {'Id_buku' : ['B001', 'B002', 'B003', 'B004', 'B005', 'B006', 'B007', 'B008', 'B009'],
               'Judul_buku' : ['Atomic Habit', 
                               'The ABC Murders', 
                               'Dumb Witness', 
                               'The Death of Expertise', 
                               'How to Kill a Mockingbird', 
                               'Dunia Sophie',
                               'Kamus Bahasa Jepang',
                               'Kamus Bahasa Jerman',
                               'Basic Maths For Dummies'],
               'Author' : ['James Clear', 'Agatha Christie', 'Agatha Christie', 'Tom Nichols', 'Harper Lee', 'Jostein Gaarder', 'Naruto',
                           'Manuel Neuer', 'Colin Beveridge'],
                'Genre' : ['Non Fiksi', 'Fiksi', 'Fiksi', 'Non Fiksi', 'Fiksi', 'Fiksi', 'Non Fiksi', 'Non Fiksi', 'Non Fiksi'],
               'Sub_Genre' : ['Self Improvement', 'Novel', 'Novel', 'Hukum', 'Novel', 'Filsafat', 'Bahasa', 'Bahasa', 'Pelajaran'],
               'Status' : ['Tersedia', 'Tersedia', 'Dipinjam', 'Tersedia', 'Tersedia', 'Dipinjam', 'Dipinjam', 'Dipinjam', 'Tersedia']
               }

daftar_member = {'Id_member' : ['member01', 'member02', 'member03', 'member04', 'member05', 'member06'],
                 'Nama' : ['Putra Manggala', 'Muhammad Ali', 'Haidar Syahid', 'Alia Fatiha', 'Zahra Nur Alia', 'Visha Aghni Fradana'],
                 'Nomor_hp' : ['081230408976', '085912378946', '081320409876', '085951425888', '085951425899', '085951427699' ],
                 'E-mail' : ['manggala@gmail.com', 'ali.muhammad@gmail.com', 'haidar.syahid@gmail.com', 'alfatiha@gmail.com', 'araraneeh@gmail.com', 
                             'tuyulbotak@gmail.com'],
                 'Alamat' : ['Jalan Sumatra no. 7', 'Jalan Bogor no 17', 'Jl. Sudirman no. 2', 'Jl. Kampus no. 3', 'Jalan Bogor no. 19', 
                             'Jl. Ir. Juanda no. 14']
                 }

daftar_peminjaman = {'Id_Pinjam' : ['BP01', 'BP02', 'BP03', 'BP04'],
                     'Id_member' : ['member04', 'member06', 'member02', 'member03'],
                     'Nama_Peminjam' : ['Alia Fatiha', 'Visha Aghni Fradana', 'Muhammad Ali', 'Haidar Syahid'],
                     'ID_buku' : ['B003', 'B006', 'B007', 'B008'], 
                     'Judul_buku' : ['Dumb Witness', 'Dunia Sophie', 'Kamus Bahasa Jepang', 'Kamus Bahasa Jerman'],
                     'Tanggal_peminjaman' : ['2024-10-17','2024-10-20', '2024-10-18', '2024-10-25'],
                     'Tanggal_pengembalian' : ['2024-10-30', '2024-11-2', '2024-10-28', '2024-11-5']}

user = ''
def login():
    global user
    while True:
        user = input("Login : ")
        if user.lower() == 'admin123':
            print("\nLogin sebagai Admin berhasil!")
            menu_admin()
            break
        elif user.lower() in daftar_member['Id_member']:
            print(f"\nLogin sebagai Member berhasil!\n")
            menu_member()
            break
        elif user.lower() == 'tamu' :
            print('Anda login sebagai tamu')
            menu_member()
        else:
            print("Login gagal! Masukkan 'admin123' atau ID Member yang valid.")

def main_menu():
    print('==== Selamat Datang di Library.py ====')
    print("Silakan login untuk melanjutkan")
    login()

def menu_admin():
    print('==== Sistem Peminjaman Buku Perpustakaan ====\n')
    print('==== Selamat Datang di Library.py ====')
    
    while True:
        print('''
Main Menu : 1. Data Buku
            2. Data Member
            3. Data Peminjaman 
            4. Tambah Buku 
            5. Update Buku 
            6. Hapus Buku   
            7. Pinjam Buku 
            8. Perpanjang Peminjaman Buku
            9. Pengembalian Buku
            10. Daftar Member 
            11. Update Member
            12. Hapus Member
            12. Exit Program
''')
        
        pilihan = input('Pilih Menu : ')
        
        if pilihan == '1' :
            data_buku()
            continue
        elif pilihan == '2' :
            data_member()
            continue
        elif pilihan == '3' :
            data_peminjaman()
            continue
        elif pilihan == '4' :
            tambah_buku()
            continue
        elif pilihan == '5' :
            update_buku()
            continue
        elif pilihan == '6' :
            hapus_buku()
            continue
        elif pilihan == '7' :
            pinjam_buku()
            continue
        elif pilihan == '8' :
            perpanjang_pinjaman()
            continue
        elif pilihan == '9' :
            pengembalian_buku()
            continue
        elif pilihan == '10' :
            tambah_member()
            continue
        elif pilihan == '11' :
            update_member()
            continue
        elif pilihan == '12' :
            hapus_member()
            continue
        elif pilihan == '13' :
            exit = input('Anda yakin mau keluar ( ya (Keluar) / tidak (Kembali ke Main Menu) ): ').strip().lower()
            if exit == 'ya' :
                print('Exit Program...')
                print('Terima kasih sudah berkunjung di Library.py')
                break
            elif exit == 'tidak' :
                print('Kembali ke Main Menu...')
                continue
            else :
                print('Pilihan tidak valid')
        else :
            print('Pilihan tidak valid')
            continue

def menu_member():
    print('==== Sistem Peminjaman Buku Library.py ====')
    
    while True:
        print('''
Main Menu : 1. Data Buku
            2. Data Member 
            3. Data Peminjaman
            4. Pinjam Buku
            5. Perpanjang Peminjaman Buku
            6. Pengembalian Buku
            7. Daftar Member 
            8. Exit Program
''')
        
        pilihan = input('Pilih Menu : ')
        
        if pilihan == '1' :
            data_buku()
            continue
        elif pilihan == '2' :
            data_member()
            continue
        elif pilihan == '3' :
            data_peminjaman()
            continue
        elif pilihan == '4' :
            pinjam_buku()
            continue
        elif pilihan == '5' :
            perpanjang_pinjaman()
            continue
        elif pilihan == '6' :
            pengembalian_buku()
            continue
        elif pilihan == '7' :
            tambah_member()
            continue
        elif pilihan == '8' :
            exit = input('Anda yakin mau keluar ( ya (Keluar) / tidak (Kembali ke Main Menu) ): ').strip().lower()
            if exit == 'ya' :
                print('Exit Program...')
                print('Terima kasih sudah berkunjung di Library.py')
                break
            elif exit == 'tidak' :
                print('Kembali ke Main Menu...')
                continue
            else :
                print('Pilihan tidak valid')
        else :
            print('Pilihan tidak valid')
            continue

def menu_tamu():
    print('==== Sistem Peminjaman Buku Library.py ====')
    
    while True:
        print('''
Main Menu : 1. Data Buku
            2. Data Member 
            3. Data Peminjaman
            4. Daftar Member 
            5. Login Sebagai Member 
            6. Exit Program
''')
        
        pilihan = input('Pilih Menu : ')
        
        if pilihan == '1' :
            data_buku()
            continue
        elif pilihan == '2' :
            data_member()
            continue
        elif pilihan == '3' :
            data_peminjaman()
            continue
        elif pilihan == '4' :
            tambah_member()
            continue
        elif pilihan == '5' :
            login()
            continue
        elif pilihan == '6' :
            exit = input('Anda yakin mau keluar ( ya (Keluar) / tidak (Kembali ke Main Menu) ): ').strip().lower()
            if exit == 'ya' :
                print('Exit Program...')
                print('Terima kasih sudah berkunjung di Library.py')
                break
            elif exit == 'tidak' :
                print('Kembali ke Main Menu...')
                continue
            else :
                print('Pilihan tidak valid')
        else :
            print('Pilihan tidak valid')
            continue

# =================================== READ =========================================
# Fungsi untuk menampilkan daftar buku
def tampilkan_daftar_buku():
    print("Daftar Buku:")
    print(tabulate(daftar_buku, headers='keys', tablefmt='grid'))

def cari_buku():
    while True:
        kata_kunci = input("Masukkan kata kunci pencarian (Ketik 'kembali' untuk kembali ke menu): ").strip().lower()
        
        # Cek apakah pengguna ingin kembali ke menu sebelumnya
        if kata_kunci == 'kembali':
            break

        hasil_pencarian = []
        
        # Mencari buku di semua kriteria
        for i in range(len(daftar_buku['Id_buku'])):
            match = False  # Flag untuk mendeteksi kecocokan
            for key in daftar_buku:
                # Pengecualian khusus untuk genre "fiksi" agar tidak mencocokkan dengan "non-fiksi"
                if key == 'Genre' and kata_kunci == "fiksi" and "non-fiksi" in daftar_buku[key][i].lower():
                    continue  # Jika kata kunci adalah "fiksi" dan genre adalah "non-fiksi", lewati
                elif kata_kunci in str(daftar_buku[key][i]).lower():
                    match = True
                    break  # Menghentikan loop setelah menemukan kecocokan di satu atribut
            if match:
                hasil = {key: daftar_buku[key][i] for key in daftar_buku}
                hasil_pencarian.append(hasil)

        # Menampilkan hasil pencarian
        if hasil_pencarian:
            print('Hasil Pencarian:')
            print(tabulate(hasil_pencarian, headers='keys', tablefmt='grid'))
        else:
            print('Buku tidak ditemukan dengan kata kunci tersebut.')

def data_buku():
    while True:
        print('''Menu:
    1. Tampilkan Daftar Buku
    2. Cari Buku
    3. Kembali ke Menu Utama
''')
        input_user = input('Pilih Menu: ')
        
        if input_user == '1':
            tampilkan_daftar_buku()
        elif input_user == '2':
            cari_buku()
        elif input_user == '3':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Fungsi untuk menampilkan daftar member perpustakaan
def tampilkan_daftar_member():
    print("Daftar Member:")
    print(tabulate(daftar_member, headers='keys', tablefmt='grid'))

def cari_data_member():
    print("=== Cari Data Member ===")
    cari = input("Masukkan ID Member atau Nama Member: ").strip().lower()
    
    # Mencari data member
    hasil_cari = {
        'Id_member': [],
        'Nama': [],
        'Nomor_hp': [],
        'E-mail': [],
        'Alamat': []
    }
    
    for i in range(len(daftar_member['Id_member'])):
        if cari in daftar_member['Id_member'][i].lower() or cari in daftar_member['Nama'][i].lower():
            hasil_cari['Id_member'].append(daftar_member['Id_member'][i])
            hasil_cari['Nama'].append(daftar_member['Nama'][i])
            hasil_cari['Nomor_hp'].append(daftar_member['Nomor_hp'][i])
            hasil_cari['E-mail'].append(daftar_member['E-mail'][i])
            hasil_cari['Alamat'].append(daftar_member['Alamat'][i])

    # Menampilkan hasil pencarian
    if hasil_cari['Id_member']:
        print("\nHasil Pencarian Member:")
        print(tabulate(hasil_cari, headers='keys', tablefmt='grid'))
    else:
        print("Tidak ada member yang ditemukan.")

def data_member():
    while True:
        print('''\n=== Kelola Data Member ===
Menu:
    1. Tampilkan Seluruh Data Member
    2. Cari Data Member
    3. Kembali ke Menu Utama
''')
        input_user = input('Pilih Menu: ').strip()

        if input_user == '1':
            tampilkan_daftar_member()  # Tampilkan semua member
        elif input_user == '2':
            cari_data_member()  # Cari member berdasarkan ID atau nama
        elif input_user == '3':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Fungsi untuk menampilkan daftar peminjaman buku
def tampilkan_daftar_peminjaman():
    print("Daftar Peminjaman:")
    print(tabulate(daftar_peminjaman, headers='keys', tablefmt='grid'))

def cari_data_peminjaman():
    print("=== Cari Data Peminjaman ===")
    cari = input("Masukkan ID Peminjaman, Nama Peminjam, atau Judul Buku: ").strip().lower()
    
    # Mencari data peminjaman
    hasil_cari = {
        'Id_Pinjam': [],
        'Id_member': [],
        'Nama_Peminjam': [],
        'ID_buku': [],
        'Judul_buku': [],
        'Tanggal_peminjaman': [],
        'Tanggal_pengembalian': []
    }
    
    for i in range(len(daftar_peminjaman['Id_Pinjam'])):
        if (cari in daftar_peminjaman['Id_Pinjam'][i].lower() or 
            cari in daftar_peminjaman['Nama_Peminjam'][i].lower() or 
            cari in daftar_peminjaman['Judul_buku'][i].lower()):
            hasil_cari['Id_Pinjam'].append(daftar_peminjaman['Id_Pinjam'][i])
            hasil_cari['Id_member'].append(daftar_peminjaman['Id_member'][i])
            hasil_cari['Nama_Peminjam'].append(daftar_peminjaman['Nama_Peminjam'][i])
            hasil_cari['ID_buku'].append(daftar_peminjaman['ID_buku'][i])
            hasil_cari['Judul_buku'].append(daftar_peminjaman['Judul_buku'][i])
            hasil_cari['Tanggal_peminjaman'].append(daftar_peminjaman['Tanggal_peminjaman'][i])
            hasil_cari['Tanggal_pengembalian'].append(daftar_peminjaman['Tanggal_pengembalian'][i])

    # Menampilkan hasil pencarian
    if hasil_cari['Id_Pinjam']:
        print("\nHasil Pencarian Peminjaman:")
        print(tabulate(hasil_cari, headers='keys', tablefmt='grid'))
    else:
        print("Tidak ada data peminjaman yang ditemukan.")

def data_peminjaman():
    while True:
        print('''\n=== Kelola Data Peminjaman ===
Menu:
    1. Tampilkan Seluruh Data Peminjaman
    2. Cari Data Peminjaman
    3. Kembali ke Menu Utama
''')
        input_user = input('Pilih Menu: ').strip()

        if input_user == '1':
            tampilkan_daftar_peminjaman() 
        elif input_user == '2':
            cari_data_peminjaman() 
        elif input_user == '3':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# =============================== CREATE ====================================
# Fungsi untuk menambahkan buku ke daftar buku
def tambah_buku():
    while True:
        tampilkan_daftar_buku()
        print('''
Menu :
    1. Tambah Buku
    2. Kembali ke Main Menu
''')
        input_user = input('Pilih Menu: ')
        if input_user == '1':
            print("\n=== Tambah Buku Baru ===")
            while True:    
                # Membuat ID member baru secara otomatis
                buku_number = len(daftar_buku['Id_buku']) + 1
                id_buku = f"B{buku_number:03d}"
                print(f"ID buku baru: {id_buku}")
                
                # Meminta input dari pengguna untuk data member baru
                Judul = input("Masukkan Judul Buku: ").strip().title()
                Author = input("Masukkan Penulis Buku: ").strip().title()
                Genre = input("Masukkan Genre Buku: ").strip().title()
                Sub_Genre = input("Masukkan Sub-Genre Buku: ").strip().title()
                Status = input("Masukkan Status Buku: ").strip().title()

                buku_baru = {'Id_buku' : [],
                    'Judul_buku' : [],
                    'Author' : [],
                    'Genre' : [],
                    'Sub_Genre' : [],
                    'Status' : []
                    }

                # Menambahkan data member baru ke dalam dictionary daftar_member
                buku_baru['Id_buku'].append(id_buku)
                buku_baru['Judul_buku'].append(Judul)
                buku_baru['Author'].append(Author)
                buku_baru['Genre'].append(Genre)
                buku_baru['Sub_Genre'].append(Sub_Genre)
                buku_baru['Status'].append(Status)

                print(tabulate(buku_baru, headers='keys', tablefmt='grid'))

                input_admin = input("\nSimpan data buku baru? (y/n): ").strip().lower()

                if input_admin == 'y' :
                    # Menambahkan data member baru ke dalam dictionary daftar_member
                    daftar_buku['Id_buku'].append(id_buku)
                    daftar_buku['Judul_buku'].append(Judul)
                    daftar_buku['Author'].append(Author)
                    daftar_buku['Genre'].append(Genre)
                    daftar_buku['Sub_Genre'].append(Sub_Genre)
                    daftar_buku['Status'].append(Status)

                    print("\nBuku baru berhasil ditambahkan!")

                elif input_admin == 'n' :
                    print('\nPenambahan dibatalkan!')

                print(tabulate(daftar_buku, headers='keys', tablefmt='grid'))

                # Konfirmasi apakah ingin menambah member lagi
                tambah_lagi = input("\nApakah Anda ingin menambahkan buku? (y/n): ").strip().lower()
                if tambah_lagi != 'y':
                    print("\nKembali ke Menu")
                    break
        elif input_user == '2' :
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
        else :
            print('Pilihan tidak valid!')

# Fungsi untuk mendaftar member perpustakaan
def tambah_member():
    while True:
        print('''
Menu :
    1. Daftar Member
    2. Kembali ke Main Menu
''')
        input_user = input('Pilih Menu: ')
        if input_user == '1':
            print("\n=== Tambah Member Baru ===")
            while True:
                input_user = input('Masukkan angka ID (1 manual / 2 otomatis): ')

                if input_user == '1':
                    while True:
                        input_ID = input('Masukkan 2 digit angka untuk ID : ')
                        if input_ID.isdigit() and len(input_ID) == 2:
                            id_member = f"member{input_ID}"
                        else:
                            print('Input tidak valid! Harap masukkan 2 digit angka.')
                            continue
                        if id_member in daftar_member['Id_member']:
                            print('ID member sudah terdaftar, harap ganti dengan angka lain.')
                            continue
                        else:
                            print(f"ID member baru: {id_member}")
                            break

                elif input_user == '2':
                    # Membuat ID member baru secara otomatis
                    member_number = len(daftar_member['Id_member']) + 1
                    id_member = f"member{member_number:02d}"
                    print(f"ID member baru: {id_member}")
                else:
                    print('Pilihan tidak valid! Silakan pilih 1 atau 2.')
                    continue

                # Meminta input dari pengguna untuk data member baru
                nama = input("Masukkan nama member: ").strip().title()

                # Validasi nomor handphone
                while True:
                    nomor_hp = input("Masukkan nomor handphone member (hanya angka): ").strip()
                    if nomor_hp.isdigit() and 10 <= len(nomor_hp) <= 13:
                        break
                    else:
                        print("Nomor handphone tidak valid! Harap masukkan nomor yang benar (10-13 digit angka).")

                # Validasi email
                while True:
                    email = input("Masukkan email member: ").strip()
                    if "@" in email and "." in email and len(email) > 5:
                        break
                    else:
                        print("Format email tidak valid! Harap masukkan email dengan format yang benar (contoh: nama@email.com).")

                alamat = input("Masukkan alamat member: ").strip().title()

                # Data member baru
                member_baru = {'Id_member': [id_member],
                               'Nama': [nama],
                               'Nomor_hp': [nomor_hp],
                               'E-mail': [email],
                               'Alamat': [alamat]}

                print(tabulate(member_baru, headers='keys', tablefmt='grid'))

                input_user = input('Simpan data member baru? (ya/tidak): ').strip().lower()

                if input_user == 'ya':
                    # Menambahkan data member baru ke dalam dictionary daftar_member
                    daftar_member['Id_member'].append(id_member)
                    daftar_member['Nama'].append(nama)
                    daftar_member['Nomor_hp'].append(nomor_hp)
                    daftar_member['E-mail'].append(email)
                    daftar_member['Alamat'].append(alamat)

                    print("\nMember baru berhasil ditambahkan!")
                elif input_user == 'tidak':
                    print('\nPenambahan member dibatalkan!')
                else:
                    print("Pilihan tidak valid! Data member tidak disimpan.")

                # Tampilkan daftar member yang diperbarui
                print(tabulate(daftar_member, headers='keys', tablefmt='grid'))

                # Konfirmasi apakah ingin menambah member lagi
                tambah_lagi = input("\nApakah Anda ingin menambahkan member lagi? (ya/tidak): ").strip().lower()
                if tambah_lagi != 'ya':
                    print("\nKembali ke Menu")
                    break

        elif input_user == '2':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
        else:
            print('Pilihan tidak valid! Silakan coba lagi.')

# Fungsi untuk memastikan format tanggal valid
def format_tanggal(tanggal):
    list_tanggal = tanggal.split('-')
    return len(list_tanggal) == 3 and all(i.isdigit() for i in list_tanggal) and len(list_tanggal[0]) == 4 and len(list_tanggal[1]) == 2 and len(list_tanggal[2]) == 2

# Fungsi untuk menghitung tanggal pengembalian dengan memperhatikan overflow tanggal
def hitung_tanggal(tahun, bulan, hari):
    jumlah_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Tambahkan 14 hari ke tanggal peminjaman
    hari += 14
    
    # Jika jumlah hari melebihi batas dalam bulan tersebut, sesuaikan tanggal dan bulan
    while hari > jumlah_hari[bulan - 1]:
        hari -= jumlah_hari[bulan - 1]
        bulan += 1
        if bulan > 12:  # Jika bulan melebihi Desember, naikkan ke tahun berikutnya
            bulan = 1
            tahun += 1
    
    return f"{tahun}-{bulan:02d}-{hari:02d}"

def tanggal_hari_ini():
    while True:
        today_date = input("Masukkan tanggal hari ini (yyyy-mm-dd): ").strip()
        if format_tanggal(today_date):
            return today_date
        else:
            print("Format tanggal tidak valid. Gunakan format yyyy-mm-dd.")

def cek_id_member(id_member):
    if id_member not in daftar_member['Id_member']:
        print("ID member tidak valid. Silakan coba lagi.")
        return None
    else:
        return daftar_member['Nama'][daftar_member['Id_member'].index(id_member)]

def cek_id_buku(input_buku):
    if input_buku not in daftar_buku['Id_buku']:
        print("ID buku tidak ditemukan. Silakan coba lagi.")
        return None
    index_buku = daftar_buku['Id_buku'].index(input_buku)
    if daftar_buku['Status'][index_buku].lower() != 'tersedia':
        print("Buku tidak tersedia untuk dipinjam. Silakan pilih buku lain.")
        return None
    return index_buku

def pinjam_buku():
    while True:
        print('''
Menu :
    1. Pinjam Buku
    2. Kembali ke Main Menu
''')
        input_user = input('Pilih Menu: ')
        if input_user == '1':
            ke_menu = False
            while not ke_menu:
                print("\n=== Peminjaman Buku ===")

                # Menampilkan daftar buku yang tersedia dalam bentuk tabel
                buku_tersedia = [i for i, status in enumerate(daftar_buku['Status']) if status.lower() == 'tersedia']
                if not buku_tersedia:
                    print("Tidak ada buku yang tersedia untuk dipinjam saat ini.")
                    return

                daftar_buku_tersedia = {key: [daftar_buku[key][i] for i in buku_tersedia] for key in daftar_buku}
                print("\nDaftar Buku Tersedia:")
                print(tabulate(daftar_buku_tersedia, headers='keys', tablefmt='grid'))

                # Minta ID member
                id_member = input("\nMasukkan ID member Anda: ").strip().lower()
                nama_peminjam = cek_id_member(id_member)
                if not nama_peminjam:
                    continue

                # Minta input ID buku yang ingin dipinjam
                input_buku = input("\nMasukkan ID buku yang ingin dipinjam: ").strip().upper()
                index_buku = cek_id_buku(input_buku)
                if index_buku is None:
                    continue

                # Menampilkan detail buku yang dipilih
                buku_dipilih = {key: [daftar_buku[key][index_buku]] for key in daftar_buku}
                print("\nBuku yang Anda pilih:")
                print(tabulate(buku_dipilih, headers='keys', tablefmt='grid'))

                # Meminta input tanggal hari ini dari pengguna
                today_date = tanggal_hari_ini()
                tahun, bulan, hari = map(int, today_date.split('-'))

                # Menghitung tanggal pengembalian
                tanggal_pengembalian = hitung_tanggal(tahun, bulan, hari)

                # Konfirmasi peminjaman
                while True:
                    konfirmasi = input(f"Konfirmasi peminjaman buku '{buku_dipilih['Judul_buku'][0]}' oleh {nama_peminjam} (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        daftar_buku['Status'][index_buku] = 'Dipinjam'

                        # Menambahkan data ke daftar peminjaman
                        id_peminjaman_baru = f"BP{len(daftar_peminjaman['Id_Pinjam']) + 1:02d}"
                        daftar_peminjaman['Id_Pinjam'].append(id_peminjaman_baru)
                        daftar_peminjaman['Id_member'].append(id_member)
                        daftar_peminjaman['Nama_Peminjam'].append(nama_peminjam)
                        daftar_peminjaman['ID_buku'].append(input_buku)
                        daftar_peminjaman['Judul_buku'].append(buku_dipilih['Judul_buku'][0])
                        daftar_peminjaman['Tanggal_peminjaman'].append(today_date)
                        daftar_peminjaman['Tanggal_pengembalian'].append(tanggal_pengembalian)

                        print(f"Buku '{buku_dipilih['Judul_buku'][0]}' berhasil dipinjam oleh {nama_peminjam}.")
                        print(f"Harap dikembalikan sebelum tanggal {tanggal_pengembalian}.")
                        
                        ke_menu = True
                        break
                    elif konfirmasi == 'n':
                        print("Peminjaman dibatalkan.")
                        ke_menu = True
                        break
                    else:
                        print('Pilihan tidak valid!')

        elif input_user == '2':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            else:
                print('Pilihan tidak valid!')

# ====================================== UPDATE =============================================
# Fungsi untuk Update data buku
def update_buku():
    while True:
        print("\n--- Menu Update Data Buku ---")
        print("1. Update Data Buku")
        print("2. Kembali ke Main Menu")

        pilihan = input("Pilih Menu: ")

        if pilihan == '1':
            kriteria = input("Masukkan ID atau Judul Buku yang ingin diupdate: ")

            # Cek ID Buku
            if kriteria.upper() in [id_buku.upper() for id_buku in daftar_buku['Id_buku']]:
                index = [id_buku.upper() for id_buku in daftar_buku['Id_buku']].index(kriteria.upper())
            # Cek Judul Buku
            elif kriteria.lower() in [judul.lower() for judul in daftar_buku['Judul_buku']]:
                index = [judul.lower() for judul in daftar_buku['Judul_buku']].index(kriteria.lower())
            else:
                print("ID atau Judul Buku tidak ditemukan. Silakan coba lagi.")
                continue

            print("\nData Buku yang akan diupdate:")
            for key in daftar_buku:
                print(f"{key}: {daftar_buku[key][index]}")

            kolom = input("Masukkan nama kolom yang ingin diupdate (Judul_buku/Author/Genre/Sub_Genre/Status) atau ketik 'Cancel' untuk membatalkan: ").capitalize()
            if kolom == 'Cancel':
                print("Proses update dibatalkan.")
                continue  # Kembali ke awal loop untuk menampilkan menu
            elif kolom in daftar_buku:
                new_value = input(f"Masukkan nilai baru untuk {kolom}: ")
                daftar_buku[kolom][index] = new_value
                print("Data buku berhasil diupdate.")
            else:
                print("Field tidak valid. Silakan coba lagi.")

        elif pilihan == '2':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

# Fungsi untuk Update Data Member
def update_member():
    while True:
        print("\n--- Menu Update Data Member ---")
        print("1. Update Data Member")
        print("2. Kembali ke Main Menu")

        pilihan = input("Pilih Menu: ")

        if pilihan == '1':
            kriteria = input("Masukkan ID atau Nama Member yang ingin diupdate: ")

            if kriteria in daftar_member['Id_member']:
                index = daftar_member['Id_member'].index(kriteria)
            elif kriteria in daftar_member['Nama']:
                index = daftar_member['Nama'].index(kriteria)
            else:
                print("ID atau Nama Member tidak ditemukan. Silakan coba lagi.")
                continue

            print("\nData Member yang akan diupdate:")
            for key in daftar_member:
                print(f"{key}: {daftar_member[key][index]}")

            kolom = input("Masukkan nama field yang ingin diupdate (Nama/Nomor_hp/E-mail/Alamat) atau ketik 'Cancel' untuk membatalkan: ").capitalize()
            if kolom == 'Cancel':
                print("Proses update dibatalkan.")
                continue  # Kembali ke awal loop untuk menampilkan menu
            elif kolom in daftar_member:
                new_value = input(f"Masukkan nilai baru untuk {kolom}: ")
                daftar_member[kolom][index] = new_value
                print("Data member berhasil diupdate.")
            else:
                print("Field tidak valid. Silakan coba lagi.")

        elif pilihan == '2':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

# Fungsi untuk update / perpanjang peminjaman buku
def perpanjang_pinjaman():
    while True:
        # Tampilkan daftar peminjaman
        tampilkan_daftar_peminjaman()

        print(
            '''
 Menu :
    1. Perpanjang Pinjaman Buku
    2. Kembali ke Main Menu
''')

        pilihan = input('Pilih Menu: ')

        if pilihan == '1':
            while True:
                id_pinjaman = input("\nMasukkan ID Peminjaman yang ingin diperpanjang: ").strip().upper()

                if id_pinjaman in daftar_peminjaman['Id_Pinjam']:
                    index = daftar_peminjaman['Id_Pinjam'].index(id_pinjaman)

                    # Meminta input tanggal perpanjang dan memvalidasinya
                    tanggal_perpanjang = tanggal_hari_ini()
                    tahun, bulan, hari = map(int, tanggal_perpanjang.split('-'))

                    # Hitung tanggal pengembalian baru (14 hari dari tanggal perpanjang)
                    tanggal_pengembalian_baru = hitung_tanggal(tahun, bulan, hari)

                    print(f"Tanggal peminjaman baru: {tanggal_perpanjang}")
                    print(f"Tanggal pengembalian baru: {tanggal_pengembalian_baru}")

                    input_user = input('Simpan perpanjang pinjaman buku? (ya/tidak): ')
                    if input_user == 'ya':
                        # Update tanggal peminjaman di daftar peminjaman dengan tanggal perpanjang
                        daftar_peminjaman['Tanggal_peminjaman'][index] = tanggal_perpanjang
                        # Update tanggal pengembalian di daftar peminjaman dengan tanggal pengembalian baru
                        daftar_peminjaman['Tanggal_pengembalian'][index] = tanggal_pengembalian_baru
                        print(f"Peminjaman dengan ID {id_pinjaman} berhasil diperpanjang.\n")
                        break
                    else :
                        print('Perpanjang peminjaman dibatalkan!\n')
                        break
                else:
                    print("ID Peminjaman tidak ditemukan.")
                    continue
        elif pilihan == '2':
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print('Pilihan tidak valid! Silakan coba lagi.')

# ================================== DELETE =============================================
def hapus_buku():
    while True:
        print("\n=== Delete Data Buku ===")
        print("1. Delete Buku")
        print("2. Kembali ke Main Menu")
        
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            input_buku = input("Masukkan ID atau Judul Buku yang ingin dihapus: ")

            # Pastikan input minimal 4 karakter
            if len(input_buku) < 4:
                print("Masukkan minimal 4 karakter untuk pencarian.")
                continue

            input_buku_lower = input_buku.lower()

            # Cek ID buku
            found = False
            for index, id_buku in enumerate(daftar_buku['Id_buku']):
                if id_buku.lower() == input_buku_lower:
                    # Tampilkan data yang akan dihapus
                    print("\nData Buku yang akan dihapus:")
                    for key in daftar_buku:
                        print(f"{key}: {daftar_buku[key][index]}")
                    
                    # Konfirmasi hapus data
                    konfirmasi = input("Apakah Anda yakin ingin menghapus buku ini? (ya/tidak): ").lower()
                    if konfirmasi == 'ya':
                        for key in daftar_buku.keys():
                            daftar_buku[key].pop(index)
                        print(f"Buku dengan ID '{input_buku}' berhasil dihapus.")
                    else:
                        print("Penghapusan buku dibatalkan.")
                    found = True
                    break
            
            if found:
                continue

            # Cek Judul buku
            found = False
            for index, judul_buku in enumerate(daftar_buku['Judul_buku']):
                if input_buku_lower in judul_buku.lower(): 
                    # Tampilkan data yang akan dihapus
                    print("\nData Buku yang akan dihapus:")
                    for key in daftar_buku:
                        print(f"{key}: {daftar_buku[key][index]}")
                    
                    # Konfirmasi hapus data
                    konfirmasi = input("Apakah Anda yakin ingin menghapus buku ini? (ya/tidak): ").lower()
                    if konfirmasi == 'ya':
                        for key in daftar_buku.keys():
                            daftar_buku[key].pop(index)
                        print(f"Buku dengan Judul '{judul_buku}' berhasil dihapus.")
                    else:
                        print("Penghapusan buku dibatalkan.")
                    found = True
                    break

            if not found:
                print(f"Buku dengan ID atau Judul '{input_buku}' tidak ditemukan.")
        
        elif pilihan == "2":
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def hapus_member():
    while True:
        print("\n=== Delete Data Member ===")
        print("1. Delete Member")
        print("2. Kembali ke Main Menu")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            input_member = input("Masukkan ID atau Nama Member yang ingin dihapus: ")
            if input_member in daftar_member['Id_member']:
                index = daftar_member['Id_member'].index(input_member)
                # Tampilkan data yang akan dihapus
                print("\nData Member yang akan dihapus:")
                for key in daftar_member:
                    print(f"{key}: {daftar_member[key][index]}")
                
                # Konfirmasi hapus data
                konfirmasi = input("Apakah Anda yakin ingin menghapus member ini? (ya/tidak): ").lower()
                if konfirmasi == 'ya':
                    for key in daftar_member.keys():
                        daftar_member[key].pop(index)
                    print(f"Member dengan ID '{input_member}' berhasil dihapus.")
                else:
                    print("Penghapusan member dibatalkan.")
            elif input_member in daftar_member['Nama']:
                index = daftar_member['Nama'].index(input_member)
                # Tampilkan data yang akan dihapus
                print("\nData Member yang akan dihapus:")
                for key in daftar_member:
                    print(f"{key}: {daftar_member[key][index]}")
                
                # Konfirmasi hapus data
                konfirmasi = input("Apakah Anda yakin ingin menghapus member ini? (ya/tidak): ").lower()
                if konfirmasi == 'ya':
                    for key in daftar_member.keys():
                        daftar_member[key].pop(index)
                    print(f"Member dengan Nama '{input_member}' berhasil dihapus.")
                else:
                    print("Penghapusan member dibatalkan.")
            else:
                print(f"Member dengan ID atau Nama '{input_member}' tidak ditemukan.")
        
        elif pilihan == "2":
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def pengembalian_buku():
    while True:
        print("\n=== Pengembalian Buku ===")
        print("1. Kembalikan Buku")
        print("2. Lihat Data Peminjaman")
        print("3. Kembali ke Main Menu")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            input_pengembalian = input("Masukkan ID Peminjaman, Judul Buku, atau Nama Peminjam: ")

            # Memeriksa panjang input
            if len(input_pengembalian) < 5:
                print("Masukkan minimal 5 karakter untuk pencarian.")
                continue
            
            # Cek ID Peminjaman
            if input_pengembalian.upper() in daftar_peminjaman['Id_Pinjam']:
                index = daftar_peminjaman['Id_Pinjam'].index(input_pengembalian.upper())
                for key in daftar_peminjaman.keys():
                    daftar_peminjaman[key].pop(index)
                print(f"Buku dengan ID Peminjaman '{input_pengembalian}' berhasil dikembalikan.")

            else:
                found = False

                # Cek Judul Buku
                for index, judul_buku in enumerate(daftar_peminjaman['Judul_buku']):
                    if input_pengembalian.lower() in judul_buku.lower():  # Ubah menjadi lowercase
                        for key in daftar_peminjaman.keys():
                            daftar_peminjaman[key].pop(index)
                        print(f"Buku dengan Judul '{judul_buku}' berhasil dikembalikan.")
                        found = True
                        break
                
                # Cek Nama Peminjam
                if not found:
                    for index, nama_peminjam in enumerate(daftar_peminjaman['Nama_Peminjam']):
                        if input_pengembalian.lower() in nama_peminjam.lower():
                            for key in daftar_peminjaman.keys():
                                daftar_peminjaman[key].pop(index)
                            print(f"Buku yang dipinjam oleh '{nama_peminjam}' berhasil dikembalikan.")
                            found = True
                            break

                if not found:
                    print(f"Peminjaman dengan ID, Judul, atau Nama '{input_pengembalian}' tidak ditemukan.")

        elif pilihan == "2":
            tampilkan_daftar_peminjaman()
            continue
        elif pilihan == "3":
            if user == 'admin123':
                menu_admin()
                break
            elif user in daftar_member['Id_member']:
                menu_member()
                break
            elif user == 'tamu':
                menu_tamu()
                break
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

main_menu()