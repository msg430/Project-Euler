

def powerSum(number, power):
    digits = list(str(number))
    sum = 0
    for k in digits:
        sum += pow(int(k), power)
    return sum




if __name__ == '__main__':

    power = 5

    number = 9
    x = 1
    while True:
        if powerSum(number, power) < pow(10, x):
            break
        number = 10*number+9
        x += 1

    works = []
    for k in range(2, pow(10,x)):
        if powerSum(k, power) == k:
            works.append(k)

    print(works)
    print(sum(works))

    # print(powerSum(999999,4))