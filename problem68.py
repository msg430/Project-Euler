import copy

class Ring:
    def __init__(self, a, size, addsTo):
        self.size = size
        self.outer = [-1]*size
        self.inner = [-1]*size
        self.populated = -1
        self.inner[0] = a
        self.left = list(range(1, size*2+1))
        self.left.remove(a)
        self.addsTo = addsTo

    def populate(self):
        self.populated += 1
        newOnes = []
        for a in self.left:
            for b in self.left:
                if a != b:
                    if a+b+self.inner[self.populated] == self.addsTo:
                        x = copy.deepcopy(self)
                        x.outer[self.populated] = a
                        x.inner[self.populated+1] = b
                        x.left.remove(a)
                        x.left.remove(b)
                        newOnes.append(x)
        return newOnes

    def lastOne(self):
        self.outer[self.size-1] = self.left[0]
        if (self.outer[self.size-1]+self.inner[self.size-1]+self.inner[0]) == self.addsTo:
            return True
        return False

    def printRing(self):
        print('outer:', self.outer)
        print('inner:', self.inner)

    def concatonation(self):
        lowestPlace = 0
        for k in range(1,self.size):
            if self.outer[k] < self.outer[lowestPlace]:
                lowestPlace = k
        list = []
        for k in range(size):
            list.append(self.outer[(lowestPlace+k) % size])
            list.append(self.inner[(lowestPlace + k) % size])
            list.append(self.inner[(lowestPlace + k + 1) % size])
        concat = ''
        for k in list:
            concat += str(k)
        length = len(concat)
        number = int(concat)
        return number, length


if __name__ == '__main__':

    size = 5

    stack = []
    for addsTo in range(6, (size*6)-2):
        for a in range(1,2*size+1):
            stack.append(Ring(a,size,addsTo))

    for k in range(size-1):
        nextStack = []
        for x in stack:
            nextStack.extend(x.populate())
        stack = nextStack.copy()

    nextStack = []
    for x in stack:
        if x.lastOne():
            nextStack.append(x)

    stack = []
    for x in nextStack:
        number, length = x.concatonation()
        if length == 16:
            stack.append(number)

    print(max(stack))
