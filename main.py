from abc import ABC, abstractmethod
import logging
from configparser import ConfigParser

# logging.basicConfig(filename='logging.log', level=logging.INFO, format='%(level_name)s : %(name)s : %(message)s')

class Parent(ABC):

    @abstractmethod
    def read(self):
        pass

    def write(self, content):
        pass

class FileHandling(Parent):
    logger = None
    def __init__(self, filename, out_filename):
        self.filename = filename
        self.out_filename = out_filename

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                file.close()
                self.logger.debug(f'File read for {self.filename} file')
                return content
        except FileNotFoundError:
            self.logger.error(f'FileNotFound filename:- {self.filename}')
            return None


    def write(self, content):
        with open(self.out_filename, 'w') as file:
            file.write(content)
            file.close()
            self.logger.debug(f'File Wrote to {self.out_filename} file')
        return 'File Wrote Successfully'

class StringManipulate(FileHandling):
    config_object = ConfigParser()
    def __init__(self, filename, out_filename):
        super().__init__(filename, out_filename)
        self.no_of_words_with_prefix_At = 0
        self.no_of_words_ending_with_ing = 0
        self.word_repeated_max = None
        self.list_of_palin = []
        self.list_of_unique_words = []
        self.counter_dict = {}
        self.status_of_output_file = None
        self.logger.debug(f'Created Object with {self.filename} '
                                f'and {self.out_filename} files and attributes are initialized')

    def __del__(self):
        self.logger.debug(f'Object Deleted for {self.filename} and {self.out_filename}')

    def file_to_list(self):
        content = self.read().replace(',', ' ').replace('.', ' ').strip().split()
        list_of_words = []
        for word in content:
            list_of_words.append(word)
        return list_of_words

    def print(self):
        self.logger.info(f'Filename:- {self.filename}')
        self.logger.info(f'No. of words with prefix \'At\':- {self.no_of_words_with_prefix_At}')
        self.logger.info(f'No. of words ending with \'ing\':- {self.no_of_words_ending_with_ing}')
        self.logger.info(f'The word repeated max:- {self.word_repeated_max}')
        self.logger.info(f'The List of Palindromes:- {self.list_of_palin}')
        self.logger.info(f'The list of Unique words:- {self.list_of_unique_words}')
        self.logger.info(f'Counter Dict:- {self.counter_dict}')
        self.logger.info(f'Status of New file:- {self.out_filename} {self.status_of_output_file}')

    def prefix_as_to(self):
        list_of_words = self.file_to_list()
        self.logger.debug(f'List of words in file has been returned')
        for word in list_of_words:
            if word[:2] == 'At':
                self.no_of_words_with_prefix_At += 1
        self.logger.debug(f'Count of words with prefix \'At\' has found')

    def ending_with_ing(self):
        list_of_words = self.file_to_list()
        self.logger.debug(f'List of words in file has been returned')
        for word in list_of_words:
            l = len(word)
            if word[l - 3:] == 'ing':
                self.no_of_words_ending_with_ing += 1
        self.logger.debug(f'Count of words ending \'ing\' was found')

    def word_max_repeat(self):
        list_of_words = self.file_to_list()
        self.logger.debug(f'List of words in file has been returned')
        from collections import Counter
        temp = Counter(list_of_words)
        self.word_repeated_max =  temp.most_common(1)[0][0]
        self.logger.debug(f'Max repeated word has found')

    def palindrome_words(self):
        list_of_words = self.file_to_list()
        self.logger.debug(f'List of words in file has been returned')
        for word in list_of_words:
            if word[::-1] == word:
                self.list_of_palin.append(word)
        self.logger.debug(f'List of palindromes were found')

    def find_unique_words(self):
        list_of_words = self.file_to_list()
        self.logger.debug(f'List of words in file has been returned')
        d = {}
        for i in list_of_words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] == 1:
                self.list_of_unique_words.append(i)
        self.logger.debug(f'List of unique words were found')

    def word_dict(self):
        list_of_words = self.file_to_list()
        self.logger.debug(f'List of words in file has been returned')
        for i in range(1, len(list_of_words) + 1):
            self.counter_dict[i] = list_of_words[i - 1]
        self.logger.debug(f'Counter word dict found')

    def splitting_words_based_vowels(self, content):
        import re
        from functools import reduce
        content = re.split('a|e|i|o|u|A|E|I|O|U', content)
        return reduce(lambda x, y: x + y, content)

    def capitalize_3rd_letter_of_a_word(self, content):
        from functools import reduce
        space = 1
        count = 0
        list_of_letters = []
        for i in content:
            count += 1
            if count / 3 == 1 and space == 1:
                space = 0
                list_of_letters.append(i.upper())
            else:
                list_of_letters.append(i)
            if i == ' ' or i == '\n':
                space = 1
                count = 0
        return reduce(lambda x, y: x + y, list_of_letters)

    def capitalize_5th_word(self, content):
        from functools import reduce
        space = 1
        list_of_letters = []
        for i in content.strip():
            if space == 5:
                space = 0
                list_of_letters.append(i.upper())
            else:
                list_of_letters.append(i)
            if i == ' ' or i == '\n':
                space += 1
        return reduce(lambda x, y: x + y, list_of_letters)

    def underscore_in_place_of_space(self, content):
        return content.replace(' ', '-')

    def semicolon_in_place_of_nextline(self, content):
        return content.replace('\n', ';')

    def creating_unique_file(self, content):
        return self.write(content)

    def new_file_with_actions(self):
        content = self.read()
        content = self.splitting_words_based_vowels(content)
        self.logger.debug(f'Split based on vowels')
        content = self.capitalize_3rd_letter_of_a_word(content)
        self.logger.debug(f'Capitalized 3rd letter of every word')
        content = self.capitalize_5th_word(content)
        self.logger.debug(f'Capitalized every 5th word')
        content = self.underscore_in_place_of_space(content)
        self.logger.debug(f'Replaced space with underscore')
        content = self.semicolon_in_place_of_nextline(content)
        self.logger.debug(f'Replaced newline with semicolon')
        self.status_of_output_file = self.creating_unique_file(content)
        self.logger.debug(f'Changed the Status of output file')

    def config_file(self):
        self.config_object[self.filename] = {
            "prefix": self.no_of_words_with_prefix_At,
            "suffix": self.no_of_words_ending_with_ing,
            "Max": self.word_repeated_max
        }
        with open('config.ini', 'w') as conf:
            self.config_object.write(conf)

def logger_func (name, format, filename, level):
    logger = logging.getLogger(name)
    formatter = logging.Formatter(format)
    filehandler = logging.FileHandler(filename)
    filehandler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(filehandler)
    return logger

def start(inp):
    StringManipulate.logger = logger_func(__name__, '%(levelname)s : %(name)s : %(asctime)s : %(message)s', 'logging.log',
                                               logging.DEBUG)
    for i in inp:
        obj = StringManipulate(i[0], i[1])
        if obj.read() is not None:
            obj.prefix_as_to()
            obj.ending_with_ing()
            obj.word_max_repeat()
            obj.palindrome_words()
            obj.find_unique_words()
            obj.word_dict()
            obj.new_file_with_actions()
            obj.config_file()
            obj.print()

n = int(input('Enter Number of Files:- '))
inp = []
for i in range(n):
    inp.append(input().split())
start(inp)