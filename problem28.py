


if __name__ == '__main__':

    size = 1001

    summation = 1
    currentlyAt = 1
    gap = 1
    for k in range(int(size/2)):
        for h in range(4):
            currentlyAt += gap+1
            summation += currentlyAt
        gap += 2

    print(summation)

