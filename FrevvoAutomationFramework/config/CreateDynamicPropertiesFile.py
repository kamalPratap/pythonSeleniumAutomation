from configparser import ConfigParser

config = ConfigParser()

config['setting'] = {
    'debug': 'true',
    'secret_key': '121212',
    'default_browser': 'Firefox',
    'log_path': 'C:/Users/kamal/Desktop/locales'
}

config['files'] = {
    'report_path': 'C:/Users/kamal/Desktop',
    'image_path': 'C:/Users/kamal/Desktop/locales',
    'url_path': 'http://localhost:8082/'
}

config['smtp'] = {
    'server': 'smtp.gmail.com',
    'port': '587'
}

config['email_address'] = {
    'from_email': 'pratapkamal1983@gmail.com',
    'password': 'Putun!@12',
    'to_email': 'kamalpratap1985@gmail.com',
    'subject': 'Message with Subject import MIMEText & MIMEMultipart'
}

with open('./configuration_file.ini', 'w') as f:
    config.write(f)