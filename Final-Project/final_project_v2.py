# AUTHOR: ADI

# sumber ilmu: 
# 1. https://www-freecodecamp-org.cdn.ampproject.org/v/s/www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/amp/?usqp=mq331AQFKAGwASA%3D&amp_js_v=0.1#amp_tf=From%20%251%24s&aoh=16060386440567&referrer=https%3A%2F%2Fwww.google.com&ampshare=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fsend-emails-using-code-4fcea9df63f%2F
# 2. https://realpython.com/python-send-email/

# pada script ini,
# email akan dikirimkan dari server gmail dengan opsi: 'Less Secure Apps' bernilai: On. (https://myaccount.google.com/lesssecureapps) 
# untuk opsi yang lebih advanced: 
# anda bisa menggunakan access credentials untuk script python anda, menggunakan OAuth2 authorization framework, kunjungi link berikut: 
# (https://developers.google.com/gmail/api/quickstart/python)

# versi alternatif,
# pada script ini, 
# email akan dikirim ke email address penerima yang ada dalam file receiver_list_2.txt
# satu per satu
# file receiver_list_2.txt berisi data nama penerima, dan alamat email penerima


# import library yang akan digunakan
import csv
import os
import getpass
import locale
from datetime import datetime
import smtplib  # https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
from email.mime.multipart import MIMEMultipart # https://docs.python.org/3/library/email.mime.html#module-email.mime
from email.mime.text import MIMEText # https://docs.python.org/3/library/email.mime.html#module-email.mime
from email.mime.application import MIMEApplication # https://docs.python.org/3/library/email.mime.html#module-email.mime
from email.mime.image import MIMEImage # https://docs.python.org/3/library/email.mime.html#module-email.mime


locale.setlocale(locale.LC_TIME, 'ID')


nama_file_daftar_email_address_target = 'receiver_list_2.txt' # file ini berisi daftar nama dan alamat email penerima


email_pengirim = 'alamat_email_pengirim@gmail.com' # ganti dengan alamat email pengirim 
your_email_password = None


# nama file contoh untuk sample file attachment
sample_nama_file_pdf = 'python_file_tutorialpoint.pdf'
sample_nama_file_image = 'wonderful_indonesia.jpg'
sample_nama_file_text = 'final_project_v0.py'


# flag untuk attach atau tidak masing-masing jenis file attachment di atas
# pertanyaaan akan diajukan dibagian main (bagian bawah script ini)
# block bagian if __name__ == '__main__':
attach_file_pdf = False
attach_file_image = False
attach_file_text = False


# fungsi untuk membaca isi data dalam format csv
# untuk memudahkan proses pembacaan, kita memanfaatkan modul csv
# fungsi ini akan me-return list of tuple yang masing-masing tuple berisi data nama dan alamat email
def read_nama_dan_alamat_email_penerima(nama_file):
    with open(nama_file) as file:
        reader = csv.reader(file, delimiter=',')
        return [(nama, addr) for nama, addr in reader]


# fungsi untuk mengirim email 
# object msg yang bertipe MIMEMultipart dari modul email akan digunakan untuk konstruksi email (from, to, subject, body, attachment)
# object server yang betipe SMTP dari modul smtplib akan digunakan untuk mengirim emailnya
# pada fungsi ini email akan dikirim dengan menggunakan service smtp dari gmail (smtp.gmail.com)
# dan menggunakan opsi: 'Less Secure Apps' bernilai: On. (https://myaccount.google.com/lesssecureapps) 
def send_email_with_attachment(list_data_penerima):
    
    # konstruksi object smtplib.SMTP, disini, digunakan smtpnya gmail (smtp.gmail.com, port 587)
    # object ini akan digunakan untuk mengirimkan emailnya
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # set up secure connection via tls dengan memanggil starttls()
    server.starttls()
    # server.set_debuglevel(1)
    # login ke gmail
    server.login(email_pengirim, your_email_password) 
    
    for nama_penerima, alamat_email_penerima in list_data_penerima:

        # konstruksi email yang akan dikirim 
        # set up object msg sebagai MIMEMultipart
        msg = MIMEMultipart()
        
        # set up alamat email pengirim
        msg['From'] = email_pengirim
        
        # set up alamat email penerima
        # karena alamat email penerima lebih dari satu, setiap alamat email akan dipisahkan dengan tanda koma 
        msg['To'] = alamat_email_penerima
        
        # set up subject email
        msg['Subject'] = 'indonesia.ai kelas basic-python'
        
        # set up isi pesan email 
        sekarang = datetime.now()
        body = f'Hi, {nama_penerima}\nIni adalah contoh isi pesan pada body email.\n\nNb.Email ini dikirimkan pada hari: {sekarang:%A, %d %B %Y - %H:%M:%S}'
            
        # attach isi pesan email ini ke dalam object msg (MIMEMultipart)
        # disini di set up sebagai pesan dalam format/bentuk plain text 
        msg.attach(MIMEText(body, 'plain'))

        # attach pdf
        if attach_file_pdf:
            # konstruksi lampiran yang berjenis pdf menggunakan object MIMEApplication
            # pertama, buka filenya (mode binary), read, dan jadikan sebagai object MIMEApplication
            # kedua, set header lampirannya
            # attach file lampiran tsb ke email yang sedang dikonstruksi
            lampiran1 = MIMEApplication(open(sample_nama_file_pdf, 'rb').read())
            lampiran1.add_header('Content-Disposition', 'attachment', filename=sample_nama_file_pdf)
            msg.attach(lampiran1)
        
        # attach image
        if attach_file_image:
            # konstruksi lampiran yang berjenis image menggunakan object MIMEImage
            # pertama, buka filenya (mode binary), read, dan jadikan sebagai object MIMEImage
            # kedua, set header lampirannya
            # attach file lampiran tsb ke email yang sedang dikonstruksi
            fp = open(sample_nama_file_image, 'rb')
            lampiran2 = MIMEImage(fp.read())
            lampiran2.add_header('Content-Disposition', 'attachment', filename=sample_nama_file_image)
            fp.close()
            msg.attach(lampiran2)

        # attach text file
        if attach_file_text:
            # konstruksi lampiran yang berjenis text menggunakan object MIMEText
            # pertama, buka filenya, read, dan jadikan sebagai object MIMEText
            # kedua, set header lampirannya
            # attach file lampiran tsb ke email yang sedang dikonstruksi
            lampiran3 = MIMEText(open(sample_nama_file_text, 'r').read())
            lampiran3.add_header('Content-Disposition', 'attachment', filename=sample_nama_file_text)
            msg.attach(lampiran3)

        print(f'{" " * 4}Kirim Email Untuk: {nama_penerima.ljust(n)} ... ', end='')
        try:
            # kirim emailnya 
            server.send_message(msg)
            print('Done.')
        except Exception as e:
            print('Gagal')
            raise e
        
    server.quit()


if __name__ == '__main__':
    # test skenario:
    # 1. program akan menampilkan alamat email pengirim.
    # 2. akan dibaca daftar nama penerima dan alamat email penerima yang akan dikirimi email. sumbernya dari file receiver_list_2.txt.
    #    pembacaan akan dilakukan dengan menggunakan fungsi read_nama_dan_alamat_email_penerima(...)
    #    fungsi ini akan mengembalikan data koleksi tuple dari nama penerima dan email address penerima dalam bentuk list .
    # 3. setelah dibaca, program akan menampilkan daftar nama penerima dan alamat email penerima ini .
    # 4. program akan menanyakan opsi, apakah mau kirim file attachment atau tidak.
    #    attachment ada 3 sample, dalam bentuk pdf, image dan text.
    #    program akan bertanya satu per satu ingin mengikutkan file attachment sample ini atau tidak .
    # 5. program kemudian akan meminta user untuk input password dari alamat email pengirim.
    #    password akan diinput via fungsi getpass(prompt).
    #    dengan fungsi ini, password yang diketik user tidak akan ditampilkan ke layar monitor.
    # 6. email akan mulai dikirim dengan memanggil fungsi send_email_with_attachment(...)
    #    email akan dikirim satu per satu, via looping 
    #    program akan menampilkan keterangan proses pengiriman email ke setiap data penerima yang ada 
    # 7. jika semua email sudah terkirim, program akan menampilkan pesan bahwa email sudah selesai dikirim.
    #    jika gagal, akan ditampilkan error apa yang sedang terjadi (via try...except...)
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
            ans = input('Kirim Sample Attachment File PDF [y/n] ? ').lower()
            if (ans in {'y', 'n'}):
                break
        attach_file_pdf = True if ans == 'y' else False
        print()
        while True:
            ans = input('Kirim Sample Attachment File Image [y/n] ? ').lower()
            if (ans in {'y', 'n'}):
                break
        attach_file_image = True if ans == 'y' else False
        print()
        while True:
            ans = input('Kirim Sample Attachment File Text [y/n] ? ').lower()
            if (ans in {'y', 'n'}):
                break
        attach_file_text = True if ans == 'y' else False
        print()
        while True:
            your_email_password = getpass.getpass('Masukkan Password Alamat Email Pengirim ? ')
            if your_email_password != "":
                break
        # kirim email via fungsi send_email_with_attachment(...)
        print('\nStart Kirim Email:')
        send_email_with_attachment(list_data_penerima)
        print('Proses Pengiriman Email Selesai.')
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
    
