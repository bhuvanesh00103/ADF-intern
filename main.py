def file_to_list(filename):
    list_of_words = []
    with open(filename, 'r') as f:
        for line in f:
            for word in line.replace(',', ' ').replace('.', ' ').strip().split():
                list_of_words.append(word)
        f.close()
    return list_of_words

def prefix_as_To(list_of_words):
    count = 0
    for word in list_of_words:
        if word[:2] == 'At':
            count += 1
    return count

#The method 'prefix_as_To_using_startswith' can also used for finding prefix
def prefix_as_To_using_startswith(list_of_words):
    count = 0
    for word in list_of_words:
        if word.startswith('At',0,len(word)):
            count += 1
    return count

def ending_with_ing(list_of_words):
    count = 0
    for word in list_of_words:
        l = len(word)
        if word[l-3:] == 'ing':
            count += 1
    return count

#The method 'ending_with_ing_using_endswith' can also used for finding suffix
def ending_with_ing_using_endswith(list_of_words):
    count = 0
    for word in list_of_words:
        l = len(word)
        if word.endswith('ing'):
            count += 1
    return count

def word_max_repeat(list_of_words):
    from collections import Counter
    temp = Counter(list_of_words)
    return temp.most_common(1)[0][0]

def palindrome_words(list_of_words):
    list_of_palin = []
    for word in list_of_words:
        if word[::-1] == word:
            list_of_palin.append(word)
    return list_of_palin

def find_unique_words(list_of_words):
    d = {}
    for i in list_of_words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    list_of_unique_words = []
    for i in d:
        if d[i] == 1:
            list_of_unique_words.append(i)
    return list_of_unique_words

#the below method can also used to find unique words
def find_unique_words_using_set(list_of_words):
    return [i for i in set(list_of_words)] #But it will return unordered list

def word_dict(list_of_words):
    dict ={}
    for i in range(1,len(list_of_words)+1):
        dict[i]=list_of_words[i-1]
    return dict

def splitting_words_based_vowels(content):
    import re
    from functools import reduce
    content = re.split('a|e|i|o|u|A|E|I|O|U', content)
    return reduce(lambda x, y: x + y, content)

'''def capitalize_3rd_letter_of_a_word(content):
    from functools import reduce
    list_of_words = content.split()
    content=[]
    for i in range(len(list_of_words)):
        if len(list_of_words[i])>2:
            content.append(list_of_words[i][:2] + list_of_words[i][2].upper() + list_of_words[i][3:])
        else:
            content.append(list_of_words[i])
    return reduce(lambda x, y: x + y, content)'''

def capitalize_3rd_letter_of_a_word(content):
    from functools import reduce
    space = 1
    count=0
    list_of_letters = []
    for i in content:
        count+=1
        if count/3 == 1 and space == 1:
            space=0
            list_of_letters.append(i.upper())
        else:
            list_of_letters.append(i)
        if i == ' ' or i == '\n':
            space=1
            count=0
    return reduce(lambda x, y: x + y, list_of_letters)

def capitalize_5th_word(content):
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

def underscore_in_place_of_space(content):
    return  content.replace(' ','-')

def semicolon_in_place_of_nextline(content):
    return  content.replace('\n',';')

def creating_unique_file(content):
    flag = 0
    try:
        with open('output', 'x') as f:
            f.close()
    except:
        flag = 1
        print('File Already Exists')
    finally:
        with open('output', 'w') as f:
            f.write(content)
            f.close()
    return 'Wrote in Existing file' if flag else 'Wrote in New file'

def new_file_with_actions(filename):
    with open(filename,'r') as f:
        content = f.read()
        f.close()
        #i.Split the words based on the vowels
        content = splitting_words_based_vowels(content)

        #ii.Capitalize 3rd letter of every word
        content = capitalize_3rd_letter_of_a_word(content)

        #iii.Capitalize all characters of every 5th word in the file.
        content = capitalize_5th_word(content)

        #iv.Use – in place of blank space
        content = underscore_in_place_of_space(content)

        #v.Use ; (semi-colon) for new line.
        content = semicolon_in_place_of_nextline(content)

        #vi.Output file name should be generated with unique name.
        return  creating_unique_file(content)

filename = input(f'Enter the filename:- ')
list_of_words = file_to_list(filename)

#a.Print the number of words having prefix with “To” in the input file.
no_of_words_with_prefix_At = prefix_as_To(list_of_words)
print(f'a.\nNumber of words with prefix \'At\' is: {no_of_words_with_prefix_At}')

#b.Print the number of words ending with “ing” in the input file.
no_of_words_ending_with_ing = ending_with_ing(list_of_words)
print(f'b.\nNumber of words ending with \'ing\' is: {no_of_words_ending_with_ing}')

#c.Print the word that was repeated maximum number of times.
word_repeated_max = word_max_repeat(list_of_words)
print(f'c.\nThe word \'{word_repeated_max}\' was repeated maximum number of times')

#d.Print the palindrome present in the file.
list_of_palin = palindrome_words(list_of_words)
print(f'd.\nList of Palindrome in the file :- {list_of_palin}')

#e.Convert all words into unique list and print in command line
list_of_unique_words = find_unique_words(list_of_words)
print(f'e.\nunique list of words :- {list_of_unique_words}')

#f.Create a Word dict with Key as counter index and value as the words present in file and print them on screen.
counter_dict = word_dict(list_of_words)
print(f'f.\nWord dict :- {counter_dict}')

#g.Write new file with following actions
file_res = new_file_with_actions(filename)
print(f'g.\n{file_res}')