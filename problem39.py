import math


if __name__ == '__main__':

    most = 0
    mostObtained = 0
    found = []
    limit = 1000

    primitives = []
    dictionary = dict()

    for n in range(1, int(math.sqrt(limit)/2)):
        for m in range(n+1, 1+int(limit/2)):
            if m % 2 == 1 and n % 2 == 1:
                continue
            if math.gcd(n, m) > 1:
                continue
            a = (m**2)-(n**2)
            b = 2*m*n
            c = m**2+(n**2)
            print((a, b, c))
            k = 1
            while k*(a+b+c)<limit +1:
                if k*(a+b+c) in dictionary:
                    dictionary[k*(a+b+c)] += 1
                else:
                    dictionary[k*(a+b+c)] = 1
                k += 1



    print(dictionary)

    max = 0
    obtained = 0
    for k in dictionary.keys():
        if dictionary[k] > max:
            max = dictionary[k]
            obtained = k

    print((obtained, max))
