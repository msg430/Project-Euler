import math

def ps(n, h, dictionary):
    if h == 0:
        return 1
    if h == 1:
        return p(n, dictionary)
    value = p(n, dictionary)
    for k in range(1, h):
        value -= ps(n-k, k, dictionary)
    return value


def p(n, dictionary):
    if n in dictionary:
        return dictionary.get(n)
    summation = 0
    for h in range(0, int(n/2)+1):
        summation += ps(n-h, h, dictionary)
    dictionary[n] = summation
    return summation


if __name__ == '__main__':

    dictionary = dict()

    print(p(3, dictionary))
