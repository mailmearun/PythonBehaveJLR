from configparser import ConfigParser

config = ConfigParser()
config.read(r'.\config.ini')


class ReadConfig:

    @staticmethod
    def getValue(key, value):
        return config.get(key, value)
