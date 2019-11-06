import math


def specialFactorial(number):
    number = str(number)
    summation = 0
    for k in number:
        summation += math.factorial(int(k))
    return summation


if __name__ == '__main__':

    limit = 9999999

    total = 0
    for k in range(3, limit):
        if specialFactorial(k) == k:
            total += k

    print(total)
    