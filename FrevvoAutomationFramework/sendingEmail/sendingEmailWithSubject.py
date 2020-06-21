import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Send email with subject then need to import MIMEText & MIMEMultipart
# 1st turn on less secure app on your sender email address

sender = 'pratapkamal1983@gmail.com'
receiver = 'kamalpratap1985@gmail.com'
subject = 'Message with Subject import MIMEText & MIMEMultipart'
message = 'Sending email from python code, in which subject is also mentioned, to mention subject need to import MIMEText & MIMEMultipart'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

msg.attach(MIMEText(message,'plain'))
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender, 'Putun!@12')

server.sendmail(sender, receiver, text)
server.quit()
