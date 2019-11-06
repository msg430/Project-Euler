

def fibb():
    low = 1
    high = 1
    yield low
    yield high
    while True:
        hold = high
        high = low + high
        low = hold
        yield high

if __name__ == '__main__':

    lookingFor = 1000

    f = fibb()
    count = 0
    while True:
        count += 1
        string = str(next(f))
        if len(string) >= lookingFor:
            print(string)
            print(count)
            break