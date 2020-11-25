# AUTHOR: ADI

# sumber ilmu: 
# 1. https://www-freecodecamp-org.cdn.ampproject.org/v/s/www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/amp/?usqp=mq331AQFKAGwASA%3D&amp_js_v=0.1#amp_tf=From%20%251%24s&aoh=16060386440567&referrer=https%3A%2F%2Fwww.google.com&ampshare=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fsend-emails-using-code-4fcea9df63f%2F
# 2. https://realpython.com/python-send-email/

# pada script ini,
# email akan dikirimkan dari server gmail dengan opsi: 'Less Secure Apps' bernilai: On. (https://myaccount.google.com/lesssecureapps) 
# untuk opsi yang lebih advanced: 
# anda bisa menggunakan access credentials untuk script python anda, menggunakan OAuth2 authorization framework, kunjungi link berikut: 
# (https://developers.google.com/gmail/api/quickstart/python)



# import library yang akan digunakan
import os
import getpass
import smtplib  # https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
from email.mime.multipart import MIMEMultipart # https://docs.python.org/3/library/email.mime.html#module-email.mime
from email.mime.text import MIMEText # https://docs.python.org/3/library/email.mime.html#module-email.mime
from email.mime.application import MIMEApplication # https://docs.python.org/3/library/email.mime.html#module-email.mime
from email.mime.image import MIMEImage # https://docs.python.org/3/library/email.mime.html#module-email.mime


nama_file_daftar_email_address_target = 'receiver_list.txt' # file ini berisi daftar alamat email penerima


email_pengirim = 'emailpengirim@gmail.com' # ganti dengan alamat email anda 


# nama file contoh untuk sample file attachment
sample_nama_file_pdf = 'python_file_tutorialpoint.pdf'
sample_nama_file_image = 'wonderful_indonesia.jpg'
sample_nama_file_text = 'final_project.py'


# flag untuk attach atau tidak masing-masing jenis file attachment di atas
# pertanyaaan akan diajukan dibagian main (bagian bawah script ini)
# block bagian if __name__ == '__main__':
attach_file_pdf = False
attach_file_image = False
attach_file_text = False


isi_pesan_email = \
   'Ini adalah sample body message.\nAnda Bisa Ubah Isi Pesan Email Sesuai dengan yang anda inginkan\n\nthanks.\n\nRgds\nAdi'


# fungsi untuk membaca isi file dan mengembalikan hasil pembacaan sebagai sebuah object list 
def read_file_target_email_address(nama_file):
    with open(nama_file, 'r') as file:
        contents = file.readlines()
    return [item.strip() for item in contents]    


# fungsi untuk mengirim email 
# object msg yang bertipe MIMEMultipart dari modul email akan digunakan untuk konstruksi email (from, to, subject, body, attachment)
# object server yang betipe SMTP dari modul smtplib akan digunakan untuk mengirim emailnya
# pada fungsi ini email akan dikirim dengan menggunakan service smtp dari gmail (smtp.gmail.com)
# dan menggunakan opsi: 'Less Secure Apps' bernilai: On. (https://myaccount.google.com/lesssecureapps) 
def send_email_with_attachment(list_data_penerima:list, your_email_password:str):

    # konstruksi email yang akan dikirim 
    # set up object msg sebagai MIMEMultipart
    msg = MIMEMultipart()
    
    # set up alamat email pengirim
    msg['From'] = email_pengirim
    
    # set up alamat email penerima
    # karena alamat email penerima lebih dari satu, setiap alamat email akan dipisahkan dengan tanda koma 
    msg['To'] = ','.join(list_data_penerima)
    
    # set up subject email
    msg['Subject'] = 'indonesia.ai kelas basic-python'
    
    # set up isi pesan email 
    body = isi_pesan_email
        
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
    
    # konstruksi object smtplib.SMTP, disini, digunakan smtpnya gmail (smtp.gmail.com, port 587)
    # object ini akan digunakan untuk mengirimkan emailnya
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # set up secure connection via tls dengan memanggil starttls()
    server.starttls()
    # server.set_debuglevel(1)
    # login ke gmail
    server.login(email_pengirim, your_email_password) 
    # kirim emailnya 
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    # test skenario:
    # 1. program akan menampilkan alamat email pengirim.
    # 2. akan dibaca daftar alamat email yang akan dikirimi email. sumbernya dari file receiver_list.txt.
    #    pembacaan akan dilakukan dengan menggunakan fungsi read_file_target_email_address(...)
    #    fungsi ini akan mengembalikan data koleksi email address penerima dalam bentuk list .
    # 3. setelah dibaca, program akan menampilkan daftar alamat email penerima ini .
    # 4. program akan menanyakan opsi, apakah mau kirim file attachment atau tidak.
    #    attachment ada 3 sample, dalam bentuk pdf, image dan text.
    #    program akan bertanya satu per satu ingin mengikutkan file attachment sample ini atau tidak .
    # 5. program kemudian akan meminta user untuk input password dari alamat email pengirim.
    #    password akan diinput via fungsi getpass(prompt).
    #    dengan fungsi ini, password yang diketik user tidak akan ditampilkan ke layar monitor.
    # 6. email akan mulai dikirim dengan memanggil fungsi send_email_with_attachment(...)
    # 7. jika sukses, program akan menampilkan pesan bahwa email sudah selesai dikirim.
    #    jika gagal, akan ditampilkan error apa yang sedang terjadi (via try...except...)
    try:
        list_data_penerima = read_file_target_email_address(nama_file_daftar_email_address_target)
        os.system('cls')
        print('Script Python Kirim Email.')
        print('--------------------------')
        print(f'Alamat Email Pengirim: {email_pengirim}')
        print(f'Daftar Alamat Email Penerima:')    
        for no, email_addr in enumerate(list_data_penerima):
            print(f'{no+1:2}. {email_addr}')        
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
        print('\nEmail Sedang Dikirim ...')
        send_email_with_attachment(list_data_penerima, your_email_password)        
        print('Proses Pengiriman Email Selesai.')
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
    
