import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
    def config_file_write(self, filename, section, data):
        self.config[section] = data
        with open(filename, 'w') as configfile:
            self.config.write(configfile)
    def config_file_read(self, filename, section):
        self.config.read(filename)
        dic = {}
        for key in list(self.config[section]):
            dic[key] = self.config.get(section, key)
        return dic