
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication


#setup alamt email pengirim dan penerima
email_pengirim = input(str("Akun gmail Pengirim: "))
email_password = input(str("Masukkan password : "))
email_penerima = input(str("Masukkan Email Tujuan: "))

#setup MIME
message = MIMEMultipart()
message['From'] = email_pengirim
message['To'] = email_penerima
message['Subject']=input(str("Subject Email: "))

#body email dari inputan
body_email = input(str("Isi Email: "))
message.attach(MIMEText(body_email,'plain'))
#body email dari baca file
nama_file = 'isi_email.txt'
message.attach(MIMEText(open(nama_file).read()))

#attachment
file_attach = MIMEApplication(open('data.txt','rb').read())
file_attach.add_header('Content-Disposition', 'attachment', filename='data.txt')
message.attach(file_attach)

#Setup SMTP Sessions
try:
    session = smtplib.SMTP_SSL('smtp.gmail.com',465)
    session.ehlo()
    session.login(email_pengirim, email_password)
    text = message.as_string()
    session.sendmail(email_pengirim,email_penerima, text)
    session.quit()
    print('Email terkirim, cek inbox tujuan')
except Exception as exception:
    print("Error: %s!\n\n" % exception)