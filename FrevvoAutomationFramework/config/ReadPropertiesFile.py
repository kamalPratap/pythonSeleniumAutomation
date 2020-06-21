from configparser import ConfigParser

parser = ConfigParser()
parser.read('test.ini')

print(parser.sections())
print(parser.options('setting'))
print(parser.options('db'))
print(parser.options('files'))
print(parser.get('setting', 'secret_key'))

print(parser.get('files', 'staging_path'))

print('db' in parser)
print(parser.get('db', 'db_port'), type(parser.get('db', 'db_port')))
print(int(parser.get('db', 'db_port')))
print(parser.getint('db', 'db_port'), type(parser.get('db', 'db_port')))
