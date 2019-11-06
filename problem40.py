if __name__ == '__main__':

    counter = 0
    currentNumber = 0
    searchingFor = [1, 10, 100, 1000, 10000, 100000, 1000000]
    jump = 1
    jumpStop = 10
    nextStop = searchingFor.pop(0)
    found = []
    halt = True
    while halt:
        while currentNumber < jumpStop-1:
            counter += jump
            currentNumber += 1
            if counter >= nextStop:
                found.append(int(str(currentNumber)[jump-(counter-nextStop)-1]))
                try:
                    nextStop = searchingFor.pop(0)
                except IndexError:
                    halt = False
                    break
        jump += 1
        jumpStop *= 10

    h = 1
    for k in found:
        h *= k
    print(h)



