import time
def prime(n):
    if n==2 or n==3:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
n = int(input('Enter the End Number:'))
for i in range(2,n+1):
    if prime(i):
        print(i)
    time.sleep(5)