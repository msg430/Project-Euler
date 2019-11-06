


def powerSum(number):
    string = str(number)
    sum = 0
    for k in string:
        sum += int(k)
    return sum


def checkAtIndex(inRoster, toCheck, index, found, jumps):
    if powerSum(toCheck[index]) == inRoster[index]:
        found.append(toCheck[index])
        print(len(found), ':', inRoster[index], 'has', toCheck[index])
    toCheck[index] *= inRoster[index]**jumps[index]


def getJumps(number):
    mod = number % 9
    if mod in [0, 1]:
        return 1
    if mod in [3, 6]:
        return 0
    if mod in [4, 7]:
        return 3
    if mod == 8:
        return 2
    return 6

if __name__ == '__main__':

    # inRoster = [2, 4, 5, 7, 8, 9]
    # toCheck = [128, 256, 15625, 2401, 512, 81]
    # jumps = [6, 3, 6, 3, 2, 1]
    # nextUp = 10
    # found = []
    # lowest = 81
    # lowestIndex = 5
    # length = 5
    # while len(found) < 30:
    #     if nextUp < lowest:
    #         # print('in here')
    #         inRoster.append(nextUp)
    #         toCheck.append(nextUp)
    #         jumps.append(getJumps(nextUp))
    #         length += 1
    #         checkAtIndex(inRoster, toCheck, length, found, jumps)
    #         if jumps[length] == 0:
    #             inRoster.pop()
    #             toCheck.pop()
    #             jumps.pop()
    #             length -= 1
    #         nextUp += 1
    #     else:
    #         checkAtIndex(inRoster, toCheck, lowestIndex, found, jumps)
    #         lowest = min(toCheck)
    #         lowestIndex = toCheck.index(lowest)


    # for k in range(2,25):
        # list = []
        # for j in range(20):
        #     list.append(powerSum(k**j))
        # print(list)


    # print(powerSum(23+230))
    # # print(19)

    # for k in range(2, 31):
    #     current = k
    #     j = 1
    #     while True:
    #         j += 1
    #         if powerSum(k**j)

#     first 10:
#         1 : 9 has 81
#         2 : 8 has 512
#         3 : 7 has 2401
#         4 : 17 has 4913
#         5 : 18 has 5832
#         6 : 26 has 17576
#         7 : 27 has 19683
#         8 : 22 has 234256
#         9 : 25 has 390625
#         10 : 28 has 614656


#   with jumps takes 3.550 seconds to get to 10
#   without takes 6.631 seconds
