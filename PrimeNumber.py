import time
def prime(n):
    if n==2 or n==3:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input('Enter the End Number:'))
try:
    if n<2:
        raise Exception
except Exception:
    print('End Number should greater than 1')
else:
    for i in range(2, n + 1):
        if prime(i):
            if i!=n:
                time.sleep(5)
            print(i)