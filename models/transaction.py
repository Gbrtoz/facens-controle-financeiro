from utils.utils import Utils

class Transaction():
    def__init__(self, type=none, value=none, description):
        self.__type = type
        self.__value = value  
        self.__description = description

        self.__utils = Utils()

    def save(self):
        self.__utils.write_file(self.__type, self.__value, self.__description)

    def view(self):
        for line in self.__utils.read_file():
            print(line)