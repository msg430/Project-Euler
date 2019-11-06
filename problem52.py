def listEquality(list1, list2):
    for k in range(len(list1)):
        if list1[k] != list2[k]:
            return False
    return True


def check(inputNumber):
    digits = list(str(inputNumber))
    digits.sort()
    for x in range(1, 7):
        compare = list(str(inputNumber*x))
        compare.sort()
        if not listEquality(compare, digits):
            return False
    return True


if __name__ == '__main__':

    halt = True
    zeros = 1
    while halt:
        zeros += 1
        upper = 10 ** zeros
        print(upper)
        realUpper = int(upper/6)
        for k in range(10**(zeros-1)+1, realUpper+1):
            if check(k):
                print(k)
                halt = False
                break
