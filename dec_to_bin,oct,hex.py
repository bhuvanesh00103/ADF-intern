def dec_to_bin(n):
    return  bin(n)[2:]

def dec_to_oct(n):
    return oct(n)[2:]

def dec_to_hex(n):
    return hex(n)[2:]

n = int(input('Enter the Number: '))
print(dec_to_bin(n))
print(dec_to_oct(n))
print(dec_to_hex(n))