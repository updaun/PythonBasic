import configparser

config = configparser.ConfigParser()
config.sections()

config.read('file_handing/log/example.cfg')
config.sections()

for key in config['SectionOne']:
    print(key)

print(config['SectionOne']["status"])
