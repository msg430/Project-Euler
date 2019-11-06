import math


def primeFactors(number):
    factors = []
    while True:
        switch = True
        for k in range(2, int(math.sqrt(number)+1)):
            if number % k == 0:
                factors.append(k)
                number = int(number/k)
                while number % k == 0:
                    number = int(number/k)
                switch = False
                break
        if switch:
            break
    if number != 1:
        factors.append(number)
    return len(factors)



if __name__ == '__main__':

    sequenceLength = 4

    around = list(range(-sequenceLength+1, sequenceLength))
    around.remove(0)
    # print(around)
    # around.insert(2,0)
    # print(around)
    # print(around[0:3])
    #
    test = 0
    halt = True
    while halt:
        test += sequenceLength
        if primeFactors(test) == sequenceLength:
            holder = []
            for k in around:
                if primeFactors(test+k) == sequenceLength:
                    holder.append(1)
                else:
                    holder.append(0)
            if sum(holder) < sequenceLength-1:
                continue
            holder.insert(sequenceLength-1,1)
            for j in range(sequenceLength+1):
                if sum(holder[j:j+sequenceLength]) == sequenceLength:
                    print(test-sequenceLength+1+j)
                    halt = False
                    break
