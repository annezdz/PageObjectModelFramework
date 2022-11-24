from configparser import ConfigParser


def read_config(section, key):
    config = ConfigParser()
    config.read('..\\configurationData\\config.ini')
    return config.get(section, key)


