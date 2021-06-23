def dec_to_bin(n):
    if n >= 0:
        return bin(n)[2:]
    return bin(n)[0] + bin(n)[3:]

def dec_to_oct(n):
    if n>=0:
        return oct(n)[2:]
    return oct(n)[0]+oct(n)[3:]

def dec_to_hex(n):
    if n >= 0:
        return hex(n)[2:]
    return hex(n)[0] + hex(n)[3:]

dec = input('Enter the dec Number: ')
try:
    for i in dec:
        if int(i) not in range(0,10):
            raise Exception
except Exception:
    print('Character are not allowed')
else:
    dec = int(dec)
    bin = dec_to_bin(dec)
    oct = dec_to_oct(dec)
    hex = dec_to_hex(dec)
    print('Binary Number: ', bin)
    print('Octal Number: ', oct)
    print('HexaDec Number: ', hex)