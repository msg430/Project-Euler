
class ack:
    def __init__(self):
        self.dictionary = dict()

    def call(self, m, n):
        print(m, n)
        if (m, n) in self.dictionary:
            return self.dictionary[(m, n)]
        if m == 2:
            return (3+n*2) % (14**8)
        if m == 3:
            hold = 1
            for l in range(n):
                hold = (hold * 2) % (14**8)
            return (5+(2**3)*(hold-1)) % (14**8)
            # return (5+(2**3)*(2**n-1)) % (14**8)
        if n > m:
            for k in range(1, n):
                self.call(m, k)
        if m == 0:
            a = n+1
        elif n == 0:
            a = self.call(m-1, 1)
        else:
            a = self.call(m-1, self.call(m, n-1))
        self.dictionary[(m, n)] = a
        return a % (14**8)


if __name__ == '__main__':

    acker = ack()
    n = 4
    print(acker.call(3, 804023037))
    # print(' ')
    # print(5+(2**3)*(2**n-1))

    # (4,1) = (3,(4,0)) = (3,(3,1))
    # (4,2) = (3,(4,1)) = (3,(3,(3,1)))
    # (4,3) = (3,(4,2)) = (3,(3,(3,(3,1))))
