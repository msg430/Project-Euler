import math

counter = 0


def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return False
    if number % 2 == 0:
        return False
    f = 3
    while f < math.sqrt(number) + 1:
        if number % f == 0:
            return False
        f += 2
    return True


def giveNext(number):
    number += 2
    switch = False
    while not switch:
        asWord = str(number)
        switch = True
        if asWord[0] == 1 or asWord[len(asWord)-1] == 1:
            number += 2
            switch = False
            continue
        if asWord[0] == 9 or asWord[len(asWord)-1] == 9:
            number += 2
            switch = False
            continue
        for i in asWord:
            if int(i) % 2 == 0:
                number += 2
                switch = False
                break
    return number


numbers = []
start = 9
while counter < 10:
    switcher = True
    start = giveNext(start)
    # start += 2
    while not isPrime(start):
        start = giveNext(start)
        # start += 2
    word = str(start)
    for i in range(0, len(word)):
        if not isPrime(int(word[0:i+1])):
            switcher = False
        if not isPrime(int(word[len(word)-i-1:len(word)+1])):
            switcher = False
    if switcher:
        numbers.append(start)
        counter += 1

print(sum(numbers)+23)


print(numbers)
