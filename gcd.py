def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a, b = input('Enter the Numbers:').split()
a, b = int(a), int(b)
res = gcd(a, b)
print('Gcd for',a,'and',b,'is:',res)