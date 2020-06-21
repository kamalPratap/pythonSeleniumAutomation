import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Send email with subject then need to import MIMEText & MIMEMultipart
# 1st turn on less secure app on your sender email address

sender = 'pratapkamal1983@gmail.com'
receiver = 'kamalpratap1985@gmail.com'
subject = 'Message with Subject import MIMEText & MIMEMultipart'
message = 'Sending email from python code, in which subject is also mentioned, to mention subject need to import MIMEText & MIMEMultipart  https://www.youtube.com/watch?v=bXRYJEKjqIM'
password = 'Putun!@12'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

msg.attach(MIMEText(message,'plain'))

filename = 'sendingEmailWithAttachment.py'
attachment = open(filename,'rb')

part = MIMEBase('application','octet_stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender, password)

server.sendmail(sender, receiver, text)
server.quit()