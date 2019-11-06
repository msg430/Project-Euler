import math


def isPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for d in range(3,int(math.sqrt(number))+1,2):
        if number % d == 0:
            return False
    return True

if __name__ == '__main__':

    mult = 1
    limit = 1000000
    k = 1
    while True:
        k += 1
        if isPrime(k):
            mult *= k
            print(k)
            if mult > limit:
                mult = int(mult/k)
                break
    print(mult)
    l = int(limit/mult)
    print(l)
    result = l*mult
    print(result)
