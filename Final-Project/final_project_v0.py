# AUTHOR: ADI

# sumber ilmu: 
# 1. https://realpython.com/python-send-email/
# 2. https://dbader.org/blog/python-send-email

# pada script ini,
# email akan dikirimkan dari server gmail dengan opsi: 'Less Secure Apps' bernilai: On. (https://myaccount.google.com/lesssecureapps) 
# untuk opsi yang lebih advanced: 
# anda bisa menggunakan access credentials untuk script python anda, menggunakan OAuth2 authorization framework, kunjungi link berikut: 
# (https://developers.google.com/gmail/api/quickstart/python)

# versi simple,
# pada script ini, 
# email akan dikirim ke email address penerima yang ada dalam file receiver_list_2.txt
# satu per satu
# file receiver_list_2.txt berisi data nama penerima, dan alamat email penerima
# email yang akan dikirim berupa plaintext dan akan diassembling secara manual


# import library yang akan digunakan
import csv
import os
import getpass
import locale
from datetime import datetime
import smtplib  # https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol


locale.setlocale(locale.LC_TIME, 'ID')


nama_file_daftar_email_address_target = 'receiver_list_2.txt' # file ini berisi daftar nama dan alamat email penerima


email_pengirim = 'alamat_email_pengirim@gmail.com' # ganti dengan alamat email pengirim 
your_email_password = None


# fungsi untuk membaca isi data dalam format csv
# untuk memudahkan proses pembacaan, kita memanfaatkan modul csv
# fungsi ini akan me-return list of tuple yang masing-masing tuple berisi data nama dan alamat email
def read_nama_dan_alamat_email_penerima(nama_file):
    with open(nama_file) as file:
        reader = csv.reader(file, delimiter=',')
        return [(nama, addr) for nama, addr in reader]


# fungsi untuk mengirim email 
# email akan diassembling secara manually 
# object server yang betipe SMTP dari modul smtplib akan digunakan untuk mengirim emailnya
# pada fungsi ini email akan dikirim dengan menggunakan service smtp dari gmail (smtp.gmail.com)
# dan menggunakan opsi: 'Less Secure Apps' bernilai: On. (https://myaccount.google.com/lesssecureapps) 
def send_email(list_data_penerima):
    subject = 'basic-python class'
    print('\nStart Kirim Email:')
    try:
        # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_pengirim, your_email_password)
        for nama, addr in list_data_penerima:
            recipient = addr
            pesan = f'Hi {nama}. Email ini dikirim secara otomatis via script python on {datetime.now():%A, %d %B %Y}'
            message = f'Subject: {subject}\n\n{pesan}'
            print(f'{" " * 4}Kirim Email Untuk: {nama.ljust(n)} ... ', end='')
            server.sendmail(email_pengirim, recipient, message)
            print("Done.")
        server.close()            
    except Exception as ex:
        print("Gagal")
        raise ex
    else:
        print('Proses Pengiriman Email Selesai.')


if __name__ == '__main__':
    # test skenario:
    # 1. program akan menampilkan alamat email pengirim.
    # 2. akan dibaca daftar nama penerima dan alamat email penerima yang akan dikirimi email. sumbernya dari file receiver_list_2.txt.
    #    pembacaan akan dilakukan dengan menggunakan fungsi read_nama_dan_alamat_email_penerima(...)
    #    fungsi ini akan mengembalikan data koleksi tuple dari nama penerima dan email address penerima dalam bentuk list .
    # 3. setelah dibaca, program akan menampilkan daftar nama penerima dan alamat email penerima ini .
    # 4. program kemudian akan meminta user untuk input password dari alamat email pengirim.
    #    password akan diinput via fungsi getpass(prompt).
    #    dengan fungsi ini, password yang diketik user tidak akan ditampilkan ke layar monitor.
    # 6. email akan mulai dikirim dengan memanggil fungsi send_email(...)
    #    email akan dikirim satu per satu, via looping 
    #    program akan menampilkan keterangan proses pengiriman email ke setiap data penerima yang ada 
    #    jika semua email sudah terkirim, program akan menampilkan pesan bahwa email sudah selesai dikirim.
    # 7. jika ada exception, akan ditampilkan error apa yang sedang terjadi (via try...except...)
    try:
        list_data_penerima = read_nama_dan_alamat_email_penerima(nama_file_daftar_email_address_target)
        n = max([len(nama) for nama, addr in list_data_penerima])
        os.system('cls')
        print('Script Python Kirim Email.')
        print('--------------------------')
        print(f'Alamat Email Pengirim: {email_pengirim}')
        print(f'Daftar Alamat Email Penerima:')    
        for no, email_addr in enumerate(list_data_penerima):
            nama, addr = email_addr
            print(f'{no+1:2}. {nama.ljust(n)} [{addr}]')        
        print()
        while True:
            your_email_password = getpass.getpass('Masukkan Password Alamat Email Pengirim ? ')
            if your_email_password != "":
                break
        # kirim email via fungsi send_email_with_attachment(...)
        send_email(list_data_penerima)
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
    
