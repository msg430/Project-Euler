

def getDivisors(number):
    divisors = []
    for d in range(1,int(number/2)+1):
        if number % d == 0:
            divisors.append(d)
    return divisors


if __name__ == '__main__':

    upperLimit = 10000
    divisorSums = [0]
    for k in range(1, upperLimit):
        divisorSums.append(sum(getDivisors(k)))

    totalSum = 0
    for k in range(1, upperLimit):
        if divisorSums[k] >= upperLimit:
            holder = sum(getDivisors(divisorSums[k]))
            if holder == k:
                totalSum += k
            continue
        if divisorSums[divisorSums[k]] == k:
            if divisorSums[k] == k:
                continue
            # print(k)
            totalSum += k

    print(totalSum)