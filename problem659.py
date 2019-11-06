import math

def divisors(number):
    divisors = []
    if number % 2 == 0:
        divisors.append(2)
        number = int(number/2)
        while number % 2 == 0:
            number = int(number / 2)
    d = 3
    halt = True
    while halt:
        halt = False
        for d in range(3,int(math.sqrt(number)+1),2):
            if number % d == 0:
                divisors.append(d)
                halt = True
                number = int(number/d)
                while number % d == 0:
                    number = int(number / d)
                break
        if number == 1:
            break
    if number > 1:
        divisors.append(number)
    return divisors

if __name__ == '__main__':

    # for k in range(1,100):
    #     print(k, divisors(4*(k**2)+1))

    k = 97
    n = 97**2*2
    print((n**2)+(k**2))
    print(((n**2)+(k**2)) % (2*n+1))
    