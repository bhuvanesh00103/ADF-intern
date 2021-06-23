try:
    f = open("input.txt", "w")
except:
    print('Not Able Create input file')
else:
    content = '''When the villagers heard the cry, they came running up the hill to drive the wolf away.
    But, when they arrived, they saw no wolf. The boy was amused when seeing their angry faces.
    Once, there was a boy who became bored when he watched over the village sheep grazing on the hillside.
    Later, the boy saw a real wolf sneaking around his flock. Alarmed, he jumped on his feet and cried out as loud as he could.
    But the villagers thought he was fooling them again, and so they didn’t come to help.
    At sunset, the villagers went looking for the boy who hadn’t returned with their sheep. When they went up the hill, they found him weeping.
    An old man went to comfort the boy. As he put his arm around him, he said, Nobody believes a liar, even when he is telling the truth.
    '''
    f.write(content)
    f.close()

def convert_to_list(f):
    l = []
    for i in f:
        for j in i.replace(',',' ').replace('.',' ').split():
            l.append(j)
    return l

def find_unique_words(l):
    d = {}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    l = []
    for i in d:
        if d[i]==1:
            l.append(i)
    return l

def sort_by_word_length(l):
    l.sort(key=len)
    return l

try:
    f = open("input.txt", "r")
except:
    print('FileNotFoundError')
else:
    list_of_words = convert_to_list(f)
    f.close()
    list_of_unique_words = find_unique_words(list_of_words)
    list_of_sorted_words = sort_by_word_length(list_of_unique_words)
    try:
        f = open("output.txt", "a")
    except:
        print('File Not Able to create/append')
    else:
        for i in list_of_sorted_words:
            f.write(i + str(len(i)) + '\n')
        f.close()