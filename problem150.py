
def getValue():
    t = 0
    for k in range(1, 500501):
        t = (615949*t + 797807) % (2**20)
        yield t-(2**19)

def populate():
    getter = getValue()
    pyramid = []
    for n in range(1,1001):
        hold = []
        for k in range(n):
            hold.append(next(getter))
        pyramid.append(hold)
    return pyramid


def sumBeneath(pyramid, place, checks):
    height = len(pyramid)-place[0]
    least = pyramid[place[0]][place[1]]
    depth = 0
    summation = least
    while depth < height-1:
        depth += 1
        for k in range(depth+1):
            summation += pyramid[place[0]+depth][place[1]+k]
        checks += 1
        if summation < least:
            least = summation
    return least, checks


def testValues():
    hold = [15,-14,-7,20,-13,-5,-3,8,23,-26,1,-4,-5,-18,5,-16,31,2,9,28,3]
    for h in hold:
        yield h



if __name__ == '__main__':

    # pyramid = populate()
    #
    pyramid = [[15],[-14,-7],[20,-13,-5],[-3,8,23,-26],[1,-4,-5,-18,5],[-16,31,2,9,28,3]]

    # least = 273519
    # count = 0
    # checks = 0
    # while len(pyramid) > 0:
    #     print(count)
    #     print(checks)
    #     count += 1
    #     for j in range(count):
    #         hold, checks = sumBeneath(pyramid, (0, j), checks)
    #         if hold < least:
    #             least = hold
    #     pyramid.pop(0)
    #
    # print(least)

    # 7.025 to 10
    # 24.612 to 20

    # for k in range(len(pyramid)):
    #     print(k)
    #     for l in range(k+1):
    #         hold = sumBeneath(pyramid, (k,l))
    #         if hold < least:
    #             least = hold
    #
    # print(least)

    # getter = getValue()
    # limit = 1000
    # getter = testValues()
    # limit = 6




    # least = 2**20
    # tracker = []
    # for a in range(limit):
    #     print(a)
    #     row = []
    #     for b in range(a+1):
    #         row.append(next(getter))
    #     count = 0
    #     for t in tracker:
    #         count += 1
    #         for c in range(count):
    #             t[c] += sum(row[c:(a-count+2)+c])
    #             if t[c] < least:
    #                 least = t[c]
    #     tracker.append(row.copy())
    #     for r in row:
    #         if r < least:
    #             least = r
    #
    # print(least)

    pyramid = populate()

    # 4.808s to 990
    # 9.262 to 980
    # 12.696 to 970
    # 37.452 to 900

    least = 273519
    height = len(pyramid)
    while height > 0:
        print('height:', height)
        row = pyramid.pop()
        height -= 1
        running = []
        count = -1
        for r in range(len(row)):
            count += 1
            current = row[r]
            for h in range(count):
                current += pyramid[height-h-1][r-h-1]
                running[count-h-1] += current
                if running[count-h-1] < least:
                    least = running[count-h-1]
            running.append(row[r])
            if row[r] < least:
                least = row[r]

    print(least)
