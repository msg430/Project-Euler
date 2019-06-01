file = open("poker.txt")


# flush is 1 if it is a flush, 0 otherwise
# straight is 0 if it is not a straight, and is the highest card number if it is a straight
# containsPair is 0 if it contains some pair, is the number of the high card otherwise
# hasQuad is 0 of there is no quad, and is the value of the quad if there is one
# triple is 0 if there is none, and is the value of the triple if there is one
# fullHouse is 0 if there is no full house, and is the value of the pair if there is one
class Hand:
    def __init__(self, line):
        self.card = []
        for i in range(0, 5):
            self.card.append(convert(line[3*i]))
        self.flush = 1
        for i in range(1, 5):
            if line[3*i+1] != line[1]:
                self.flush = 0
                break
        self.card.sort()
        self.straight = 1
        for i in range(1, 5):
            if self.card[i] != self.card[i-1]+1:
                self.straight = 0
                break
        if self.straight == 1:
            self.straight = self.card[4]
        self.containsPair = self.card[4]
        for i in range(1, 5):
            if self.card[i] == self.card[i-1]:
                self.containsPair = 0
                break

    def more(self):
        self.amounts = dict()
        for i in range(2,15):
            self.amounts[i] = 0
        for i in self.card:
            self.amounts[i] = self.amounts[i] + 1
        self.hasQuad = 0
        for i in range(2, 15):
            if self.amounts[i] == 4:
                self.hasQuad = i
                for j in range(2, 15):
                    if self.amounts[j] == 1:
                        self.high = j
                        break
                return

        self.triple = 0;
        self.fullHouse = 0;
        for i in range(2, 15):
            if self.amounts[i] == 3:
                self.triple = i
                for j in range(2, 15):
                    if self.amounts[j] == 2:
                        self.fullHouse = j
                        return
                for j in reversed(range(2, 15)):
                    if self.amounts[j] == 1:
                        self.high = j
                        break
                for j in reversed(range(2, self.high)):
                    if self.amounts[j] == 1:
                        self.secondHigh = j
                        return

        self.lowPair = 0
        for i in reversed(range(2, 15)):
            if self.amounts[i] == 2:
                self.pair = i
                break
        for i in reversed(range(2, 15)):
            if self.amounts[i] == 1:
                self.high = i
                break
        for i in reversed(range(2, self.pair)):
            if self.amounts[i] == 2:
                self.lowPair = i
                return
        for i in reversed(range(2,self.high)):
            if self.amounts[i] == 1:
                self.secondHigh = i
                break
        for i in reversed(range(2,self.secondHigh)):
            if self.amounts[i] == 1:
                self.thirdHigh = i
                return


def convert(string):
    if string[0].isdigit():
        return int(string[0])
    if string[0] == 'T':
        return 10
    if string[0] == 'J':
        return 11
    if string[0] == 'Q':
        return 12
    if string[0] == 'K':
        return 13
    if string[0] == 'A':
        return 14


def giveNumber(hand):
    if hand.flush == 1:
        if hand.straight == 14:
            return 9
        if hand.straight != 0:
            return 8
        return 5
    if hand.straight != 0:
        return 4
    if hand.containsPair != 0:
        return 0
    hand.more()
    if hand.hasQuad != 0:
        return 7
    if hand.fullHouse != 0:
        return 6
    if hand.triple != 0:
        return 3
    if hand.lowPair != 0:
        return 2
    return 1


counter = 0


while 1:
    nextLine = file.readline()
    if not nextLine:
        break
    a = Hand(nextLine[0:14])
    aScore = giveNumber(a)
    b = Hand(nextLine[15:29])
    bScore = giveNumber(b)

    if aScore > bScore:
        counter += 1
        continue
    if aScore < bScore:
        continue
    if aScore == 8:
        if a.straight > b.straight:
            counter += 1
        continue
    if aScore == 7:
        if a.hasQuad > b.hasQuad:
            counter += 1
            continue
        if a.hasQuad == b.hasQuad:
            if a.high > b.high:
                counter += 1
        continue
    if aScore == 6:
        if a.triple > b.triple:
            counter += 1
            continue
        if a.triple < b.triple:
            continue
        if a.fullHouse > b.fullHouse:
            counter += 1
        continue
    if aScore == 5 or aScore == 4:
        if a.containsPair > b.containsPair:
            counter += 1
        continue
    if aScore == 3:
        if a.triple > b.triple:
            counter += 1
            continue
        if a.triple < b.triple:
            continue
        if a.high > b.high:
            counter += 1
            continue
        if a.high < b.high:
            continue
        if a.secondHigh > b.secondHigh:
            counter += 1
        continue
    if aScore == 2:
        if a.pair > b.pair:
            counter += 1
            continue
        if a.pair < b.pair:
            continue
        if a.lowPair > b.lowPair:
            counter += 1
            continue
        if a.lowPair < b.lowPair:
            continue
        if a.high > b.high:
            counter += 1
        continue
    if aScore == 1:
        if a.pair > b.pair:
            counter += 1
            continue
        if a.pair < b.pair:
            continue
        if a.high > b.high:
            counter += 1
            continue
        if a.high < b.high:
            continue
        if a.secondHigh > b.secondHigh:
            counter += 1
            continue
        if a.secondHigh < b.secondHigh:
            continue
        if a.thirdHigh > b.thirdHigh:
            counter += 1
        continue
    if aScore == 0:
        for i in reversed(range(0, 5)):
            if a.card[i] > b.card[i]:
                counter += 1
                break
            if a.card[i] < b.card[i]:
                break

print(counter)
