import smtplib

# Send email without subject
# 1st turn on less secure app on your sender email address

sender = 'pratapkamal1983@gmail.com'
receiver = 'kamalpratap1985@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender, 'Putun!@12')

message = 'Test email from python'
server.sendmail(sender, receiver, message)
server.quit()
