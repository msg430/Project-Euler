

def loopLength(number):
    start = 1
    used = [1]
    while True:
        while start < number:
            start *= 10
            used.append(0)
        used.pop()
        start = start % number
        if start == 0:
            return -1
        if start in used:
            return len(used) - used.index(start)
        used.append(start)




if __name__ == '__main__':

    longest = 0
    longestObtained = 0
    for d in range(1, 1000):
        print('trying', d)
        hold = loopLength(d)
        if hold > longest:
            longest = hold
            longestObtained = d
            print(d, 'has length', hold)
    print(longest)
    print(longestObtained)
    #
    # print(loopLength(89))