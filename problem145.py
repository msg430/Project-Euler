import multiprocessing as mp
import queue





def printNumber(list):
    string = ''
    for k in list:
        string += str(k)
    return string


def addANumber(number, n, j):
    sum = 0
    hold = number.copy()
    if n == 1:
        for k in range(1, 10):
            sum += doTheThing(hold + [k], j+n)
    else:
        for k in range(0, 10):
            sum += addANumber(hold + [k], n-1, j+1)
    return sum


def doTheThing(number, l):
    holdover = 0
    for k in range(l):
        if ((number[k] + number[l-1-k]) + holdover) % 2 == 0:
            return 0
        if ((number[k] + number[l-1-k]) + holdover) > 9:
            holdover = 1
        else:
            holdover = 0
    return 1


def threadProcess(k, length):
    sum = 0
    # h = length-1
    # h = 3
    # sum += addANumber([k], h, 1)
    for h in range(1, length):
        sum += addANumber([k], h, 1)
    resultsQueue.put(sum)
    return


if __name__ == '__main__':


    resultsQueue = mp.Queue()


    # for upperLimit = 10000000: 1.400 seconds just to produce next ones
    #                       and  11.125 seconds for all
    upperLimit = 100000000
    # for upperLimit = 1000000: 1.148 seconds for all


    sum = 0
    length = len(str(upperLimit))-1

    threads = []
    for k in range(1, 10):
        threads.append(mp.Process(target=threadProcess, args=(k, length)))

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    sum = 0
    for x in range(1, 10):
        sum += resultsQueue.get()

    print(sum)

    # get  when just do length 9