from os import system
from sys import platform


list_kontak = []


def clear_screen():
    if platform == 'win32':
        system('cls') 
    else:
        system('clear') 
    

def get_string(prompt):
    while True:
        string = input(f'{prompt} ? ')
        if string.strip() != '':
            return string


def print_list_kontak():
    print('Daftar Kontak:')
    print('==============\n')
    for nama, telp in list_kontak:
        print(f'Nama: {nama}\nNo Telepon: {telp}\n')
        
        
def insert_new_kontak():
    nama = get_string('Nama')
    telp = get_string('No. Telepon')
    return (nama, telp)


clear_screen()


print('Selamat Datang !\n')


while True:
    
    print('--- menu ---')
    print('1. Daftar Kontak')    
    print('2. Tambah Kontak')    
    print('3. Keluar')    

    menu = input('\nPilih Menu: ')

    clear_screen()

    if menu == '1':
        print_list_kontak()
    elif menu == '2':
        print('Tambah item kontak baru:')
        list_kontak.append(insert_new_kontak())
        print('\nKontak berhasil ditambahkan.\n')
    elif menu == '3':
        print('Program Selesai, Sampai Jumpa!\n')
        break
    else:
        print('Menu tidak tersedia.\n')
    
    system('pause')
    
    clear_screen()






    




