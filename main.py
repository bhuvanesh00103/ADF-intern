from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def read(self):
        pass

    def write(self, content):
        pass

class FileHandling(Parent):

    def __init__(self, filename, outfilename):
        self.filename = filename
        self.outfilename = outfilename

    def read(self):
        with open(self.filename, 'r') as file:
            content = file.read()
            file.close()
            return content

    def write(self, content):
        with open(self.outfilename, 'w') as file:
            file.write(content)
            file.close()
        return 'File Wrote Successfully'

class StringManipulate(FileHandling):

    def __init__(self, filename, outfilename):
        super().__init__(filename, outfilename)
        self.no_of_words_with_prefix_At = 0
        self.no_of_words_ending_with_ing = 0
        self.word_repeated_max = None
        self.list_of_palin = []
        self.list_of_unique_words = []
        self.counter_dict = {}
        self.status_of_output_file = None

    def __del__(self):
        print('Object Deleted')

    def file_to_list(self):
        content = self.read().replace(',', ' ').replace('.', ' ').strip().split()
        list_of_words = []
        for word in content:
            list_of_words.append(word)
        return list_of_words

    def print(self):
        print(self.no_of_words_with_prefix_At)
        print(self.no_of_words_ending_with_ing)
        print(self.word_repeated_max)
        print(self.list_of_palin)
        print(self.list_of_unique_words)
        print(self.counter_dict)
        print(self.status_of_output_file)

    def prefix_as_to(self):
        list_of_words = self.file_to_list()
        for word in list_of_words:
            if word[:2] == 'At':
                self.no_of_words_with_prefix_At += 1

    def ending_with_ing(self):
        list_of_words = self.file_to_list()
        for word in list_of_words:
            l = len(word)
            if word[l - 3:] == 'ing':
                self.no_of_words_ending_with_ing += 1

    def word_max_repeat(self):
        list_of_words = self.file_to_list()
        from collections import Counter
        temp = Counter(list_of_words)
        self.word_repeated_max =  temp.most_common(1)[0][0]

    def palindrome_words(self):
        list_of_words = self.file_to_list()
        for word in list_of_words:
            if word[::-1] == word:
                self.list_of_palin.append(word)

    def find_unique_words(self):
        list_of_words = self.file_to_list()
        d = {}
        for i in list_of_words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] == 1:
                self.list_of_unique_words.append(i)

    def word_dict(self):
        list_of_words = self.file_to_list()
        for i in range(1, len(list_of_words) + 1):
            self.counter_dict[i] = list_of_words[i - 1]

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
        content = self.capitalize_3rd_letter_of_a_word(content)
        content = self.capitalize_5th_word(content)
        content = self.underscore_in_place_of_space(content)
        content = self.semicolon_in_place_of_nextline(content)
        self.status_of_output_file = self.creating_unique_file(content)
obj = StringManipulate('input','output')
obj.prefix_as_to()
obj.ending_with_ing()
obj.word_max_repeat()
obj.palindrome_words()
obj.find_unique_words()
obj.word_dict()
obj.new_file_with_actions()
obj.print()