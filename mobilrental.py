# import os

t_mobil = './database/t_mobil.txt'

list_status = [
    'Beroperasi',
    'Tak Beroperasi'
]

def clear_screen():
    print("\n" * 100)  # Biar keliatan bersih


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def get_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                data.append(line.strip().split(','))
        return data
    except FileNotFoundError:
        return []

def set_data(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(','.join(item) + '\n')

def sort_asc(arr, index):
    try:
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j][index] > arr[j + 1][index]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    except ValueError:
        return arr

def show_mobil():
    file_path = t_mobil
    data = sort_asc(get_data(file_path), 0)
    
    header = ['NO', 'MEREK', 'STATUS', 'PLAT NOMOR']
    print(f"{header[0]:<3} {header[1]:<20} {header[2]:<15} {header[3]}")
    print("-" * 60)
    if data:
        no = 1
        for row in data:
            print(f"{no:<3} {row[0]:<20} {row[1]:<15} {row[2]}")
            no += 1
    else:
        print("Tidak ada data!")


def add_mobil():
    print("Tambah Data Mobil")
    file_path = t_mobil
    data = get_data(file_path)
    merek = input('Masukkan Merek Mobil: ')
    print('Pilih Status: ')
    print(f"1. {list_status[0]}")
    print(f"2. {list_status[1]}")
    status = int(input('Masukkan Status: ')) - 1
    plat = input('Masukkan Plat Nomor: ')
    if status in [0, 1]:
        data.append([merek, list_status[status], plat])
        set_data(file_path, data)
    else:
        print("Gagal menambah data. Harap pilih status yang tersedia!")

def update_mobil():
    show_mobil()
    file_path = t_mobil
    data = get_data(file_path)
    if data:
        try:
            index = int(input('Masukkan ID Mobil (Nomor Urut): ')) - 1
            if 0 <= index < len(data):
                data[index][0] = input('Masukkan Merek Mobil Baru: ')
                print('Pilih Status Baru: ')
                print(f"1. {list_status[0]}")
                print(f"2. {list_status[1]}")
                status = int(input('Masukkan Status Baru: ')) - 1
                if status in [0, 1]:
                    data[index][1] = list_status[status]
                    data[index][2] = input('Masukkan Plat Nomor Baru: ')
                    set_data(file_path, data)
                    print("Data berhasil diubah!")
                else:
                    print("Status tidak valid!")
            else:
                print("ID tidak ditemukan.")
        except ValueError:
            print("Input tidak valid. Masukkan angka!")
    else:
        print("Tidak ada data untuk diubah.")


def delete_mobil():
    show_mobil()
    file_path = t_mobil
    data = get_data(file_path)
    if data:
        try:
            index = int(input('Masukkan ID Mobil (Nomor Urut): ')) - 1
            if 0 <= index < len(data):
                data.pop(index)
                set_data(file_path, data)
                print("Data berhasil dihapus!")
            else:
                print("ID tidak valid!")
        except ValueError:
            print("Input tidak valid. Masukkan angka!")
    else:
        print("Tidak ada data untuk dihapus.")


def search_mobil():
    file_path = t_mobil
    data = get_data(file_path)
    if data:
        merek = input('Masukkan Merek/Plat Nomor Mobil yang Dicari: ')
        header = ['NO', 'MEREK', 'STATUS', 'PLAT NOMOR']
        print(f"{header[0]:<3} {header[1]:<20} {header[2]:<15} {header[3]}")
        print("-" * 60)
        no = 1
        found = False
        for row in data:
            if merek.lower() in row[0].lower() or merek.lower() in row[2].lower():
                print(f"{no:<3} {row[0]:<20} {row[1]:<15} {row[2]}")
                no += 1
                found = True
        if not found:
            print("Data tidak ditemukan.")
    else:
        print("Tidak ada data!")


def show_menu():
    clear_screen()
    print("=== REM BRO ===")
    print("[1] Lihat Data Mobil")
    print("[2] Tambah Data Mobil")
    print("[3] Edit Data Mobil")
    print("[4] Hapus Data Mobil")
    print("[5] Cari Data Mobil")
    print("[0] Keluar")
    print("---------------------------")
    selected_menu = input("Pilih menu> ")
    if selected_menu == '1':
        clear_screen()
        show_mobil()
        back_to_menu()
    elif selected_menu == '2':
        clear_screen()
        add_mobil()
        back_to_menu()
    elif selected_menu == '3':
        clear_screen()
        update_mobil()
        back_to_menu()
    elif selected_menu == '4':
        clear_screen()
        delete_mobil()
        back_to_menu()
    elif selected_menu == '5':
        clear_screen()
        search_mobil()
        back_to_menu()
    elif selected_menu == '0':
        clear_screen()
        exit()
clear_screen()
show_menu()
