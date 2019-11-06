

def concatonate(number, n):
    output = ''
    for k in range(1, n+1):
        output = output + str(number*k)
    return output


def checkPandigital(number):
    if len(number) < 9:
        return False
    number = set(list(number))
    if '0' in number:
        return False
    if len(number) < 9:
        return False
    return True


if __name__ == '__main__':

    works = []
    for n in range(2, 10):
        k = 1
        while True:
            current = concatonate(k, n)
            if len(current) > 9:
                break
            if checkPandigital(current):
                works.append(int(current))
            k += 1

    print(max(works))