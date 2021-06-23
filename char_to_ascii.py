ch = input('Enter the Character: ')
try:
    if len(ch) != 1:
        raise Exception
except Exception:
    print('error - single character only accepted')
else:
    print(ord(ch))