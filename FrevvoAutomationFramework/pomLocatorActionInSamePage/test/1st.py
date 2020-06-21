from configparser import ConfigParser

parser = ConfigParser()
parser.read('../../config/configuration_file.ini')
print(parser.get('files', 'url_path'))