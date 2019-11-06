def firstDigitCheck(number):
    if number > 9:
        print('problem')
        return -1
    if number in [1,2,6]:
        return 3
    if number in [3,7,8]:
        return 5
    if number in [4,5,9]:
        return 4
    return 0


def numberCheck(number):
    number = int(number)
    if number > 99:
        print('problem')
        return 0
    count = 0
    if number > 19:
        tensDigit = int(str(number)[0])
        if tensDigit in [2,3,8,9]:
            count += 6
        elif tensDigit in [4,5,6]:
            count += 5
        else:
            count += 7
        count += firstDigitCheck(number % 10)
        return count
    if number < 10:
        return firstDigitCheck(number)
    if number in [11,12]:
        return 6
    if number in [13, 14, 18, 19]:
        return 8
    if number in [15, 16]:
        return 7
    if number == 17:
        return 9
    return 3


def lettersUsed(number):
    count = 0
    string = str(number)
    if len(string) == 4:
        return 8 + 3
    if len(string) > 2:
        count += numberCheck(string[0]) + 7
        string = string[1:]
        if string == '00':
            return count
        while string[0] == '0':
            string = string[1:]
    if count > 0:
        count += 3
    count += numberCheck(string)
    return count


if __name__ == '__main__':

    summation = 0
    limit = 1000
    for k in range(1, limit + 1):
        summation += lettersUsed(k)

    print(summation)