filename = input('Enter the filename:- ')
with open(filename,'r') as f:
    for line in f:
        print(line)