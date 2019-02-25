import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText #(_maintype, _subtype, **_params)
from email.mime.base import MIMEBase #(_text[, _subtype[, _charset]])
from email import encoders #is especially true for image/* and text/* type messages containing binary data.


fromaddr = "sender mail_id"
toaddr = "receiver mail_id"


msg = MIMEMultipart()# instance of MIMEMultipart

msg['From'] = fromaddr# storing the senders email address

msg['To'] = toaddr# storing the receivers email address

msg['Subject'] = "Subject of the Mail"# storing the subject

body = "DATA file"# string to store the body of the mail

msg.attach(MIMEText(body, 'plain'))# attach the body with the msg instance

filename = "outfile.xlsx"
attachment = open("/home/pardise/Desktop/pycham/outfile.xlsx","rb")# open the file to be sent

p = MIMEBase('application', 'octet-stream')# instance of MIMEBase and named as p

p.set_payload((attachment).read())# To change the payload into encoded form

encoders.encode_base64(p)# encode into base64

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)# attach the instance 'p' to instance 'msg'

s = smtplib.SMTP('smtp.gmail.com', 587)# creates SMTP session

s.starttls()# start TLS for security

# Authentication
s.login(fromaddr, "passw")

text = msg.as_string()# Converts the Multipart msg into a string

s.sendmail(fromaddr, toaddr, text)# sending the mail

s.quit()# terminating the session
