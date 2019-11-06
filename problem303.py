def digitCheck(number):
    number = list(str(number))
    for k in number:
        if k not in ['0','1','2']:
            return False
    return True


def newDoThing(n):
    length = len(str(n))
    jump = 10**length
    works = []
    nextP = [([], 0)]

    halt = True
    while halt:
        pattern = nextP.copy()
        nextP = []
        for k in range(1, jump):
            hold = str(n * k)
            hold = hold[len(hold) - length:len(hold)]
            prior = -1
            for p in pattern:
                if p[1] == prior:
                    continue
                if digitCheck(p[1] + n * k):
                    halt = False
                    works.append([k]+p[0])
                if digitCheck(p[1] + int(hold)):
                    a = str(n * k + p[1])
                    a = a[:len(a) - length]
                    if a == '':
                        a = 0
                    else:
                        a = int(a)
                    nextP.append(([k] + p[0], a))
                    prior = p[1]
            if not halt:
                break

    finalized = []
    for p in works:
        hold = ''
        for l in p:
            l = str(l)
            while len(l) < length:
                l = '0' + l
            hold = hold + l
        finalized.append(int(hold))
    return min(finalized)


if __name__ == '__main__':

    summation = 0
    limit = 10000
    for n in range(1, limit+1):
        print(n)
        summation += newDoThing(n)

    print(summation)