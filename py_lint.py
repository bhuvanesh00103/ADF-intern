"""
Required module's are imported.
"""
import logging
from configparser import ConfigParser
import re
from functools import reduce
from collections import Counter

class FileHandling():
    '''class FileHandling'''
    logger = None
    def __init__(self, filename, out_filename):
        self.filename = filename
        self.out_filename = out_filename

    def read(self):
        """Reads the file"""
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                file.close()
                self.logger.debug(self.filename)
                return content
        except FileNotFoundError:
            self.logger.error(self.filename)
            return None


    def write(self, content):
        """Write into file"""
        with open(self.out_filename, 'w') as file:
            file.write(content)
            file.close()
            self.logger.debug('File Wrote to', self.out_filename, 'file')
        return 'File Wrote Successfully'

class StringManipulate(FileHandling):
    '''class StringManipulate'''
    config_object = ConfigParser()
    def __init__(self, filename, out_filename):
        super().__init__(filename, out_filename)
        self.no_of_prefix_at = 0
        self.no_of_words_ending_with_ing = 0
        self.word_repeated_max = None
        self.list_of_palin = []
        self.list_of_unique_words = []
        self.counter_dict = {}
        self.status_of_output_file = None
        self.logger.debug('Created Object with files and attributes are initialized')

    def file_to_list(self):
        """Return list of words"""
        content = self.read().replace(',', ' ').replace('.', ' ').strip().split()
        list_of_words = []
        for word in content:
            list_of_words.append(word)
        return list_of_words

    def print(self):
        """Prints"""
        self.logger.info(self.filename)
        self.logger.info(self.no_of_prefix_at)
        self.logger.info(self.no_of_words_ending_with_ing)
        self.logger.info(self.word_repeated_max)
        self.logger.info(self.list_of_palin)
        self.logger.info(self.list_of_unique_words)
        self.logger.info(self.counter_dict)
        self.logger.info(self.status_of_output_file)

    def prefix_as_to(self):
        """Return count of prefix present"""
        list_of_words = self.file_to_list()
        self.logger.debug('List of words in file has been returned')
        for word in list_of_words:
            if word[:2] == 'At':
                self.no_of_prefix_at += 1
        self.logger.debug('Count of words with prefix \'At\' has found')
        return self.no_of_prefix_at

    def ending_with_ing(self):
        """Return count of suffix present"""
        list_of_words = self.file_to_list()
        self.logger.debug('List of words in file has been returned')
        for word in list_of_words:
            length = len(word)
            if word[length - 3:] == 'ing':
                self.no_of_words_ending_with_ing += 1
        self.logger.debug('Count of words ending \'ing\' was found')
        return self.no_of_words_ending_with_ing

    def word_max_repeat(self):
        """Return max repeat word"""
        list_of_words = self.file_to_list()
        self.logger.debug('List of words in file has been returned')
        temp = Counter(list_of_words)
        self.word_repeated_max = temp.most_common(1)[0][0]
        self.logger.debug('Max repeated word has found')
        return self.word_repeated_max

    def palindrome_words(self):
        """Return list of palindrome."""
        list_of_words = self.file_to_list()
        self.logger.debug('List of words in file has been returned')
        for word in list_of_words:
            if word[::-1] == word:
                self.list_of_palin.append(word)
        self.logger.debug('List of palindromes were found')
        return self.list_of_palin

    def find_unique_words(self):
        """Return list of unique words."""
        list_of_words = self.file_to_list()
        self.logger.debug('List of words in file has been returned')
        dict1 = {}
        for i in list_of_words:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in dict1:
            if dict1[i] == 1:
                self.list_of_unique_words.append(i)
        self.logger.debug('List of unique words were found')
        return self.list_of_unique_words

    def word_dict(self):
        """Return counter word dict"""
        list_of_words = self.file_to_list()
        self.logger.debug('List of words in file has been returned')
        for i in range(1, len(list_of_words) + 1):
            self.counter_dict[i] = list_of_words[i - 1]
        self.logger.debug('Counter word dict found')
        return self.counter_dict

    def capitalize_3rd_letter_of_a_word(self, content):
        """Return modified content"""
        print(self.no_of_prefix_at)
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
            if i in (' ', '\\n'):
                space = 1
                count = 0
        return reduce(lambda x, y: x + y, list_of_letters)

    def capitalize_5th_word(self, content):
        """Return modified content"""
        print(self.no_of_prefix_at)
        space = 1
        list_of_letters = []
        for i in content.strip():
            if space == 5:
                space = 0
                list_of_letters.append(i.upper())
            else:
                list_of_letters.append(i)
            if i in (' ', '\\n'):
                space += 1
        return reduce(lambda x, y: x + y, list_of_letters)

    def creating_unique_file(self, content):
        """Write into file"""
        return self.write(content)

    def new_file_with_actions(self):
        """Creates new file with some Actions"""
        content = self.read()
        content = re.split('a|e|i|o|u|A|E|I|O|U', content)
        content = reduce(lambda x, y: x + y, content)
        self.logger.debug('Split based on vowels')
        content = self.capitalize_3rd_letter_of_a_word(content)
        self.logger.debug('Capitalized 3rd letter of every word')
        content = self.capitalize_5th_word(content)
        self.logger.debug('Capitalized every 5th word')
        content = content.replace(' ', '-')
        self.logger.debug('Replaced space with underscore')
        content = content.replace('\n', ';')
        self.logger.debug('Replaced newline with semicolon')
        self.status_of_output_file = self.creating_unique_file(content)
        self.logger.debug('Changed the Status of output file')

    def config_file(self):
        """Creates config file"""
        self.config_object[self.filename] = {
            "prefix": self.no_of_prefix_at,
            "suffix": self.no_of_words_ending_with_ing,
            "Max": self.word_repeated_max
        }
        with open('config.ini', 'w') as conf:
            self.config_object.write(conf)

def logger_func(name, format1, filename, level):
    """Return logger object"""
    logger = logging.getLogger(name)
    formatter = logging.Formatter(format1)
    filehandler = logging.FileHandler(filename)
    filehandler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(filehandler)
    return logger

StringManipulate.logger = logger_func(__name__, '%(levelname)s : %(name)s : %(asctime)s : %(message'
                                                ')s', 'logging.log', logging.DEBUG)