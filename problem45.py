

def triangle():
    n = 1
    while True:
        n += 1
        yield int(n*(n+1)/2)

def pentago():
    n = 1
    while True:
        n += 1
        yield int(n*(3*n-1)/2)

def hexagon():
    n = 1
    while True:
        n += 1
        yield int(n*(2*n-1))


if __name__ == '__main__':

    t = triangle()
    p = pentago()
    h = hexagon()
    tri = next(t)
    hex = next(h)
    pent = next(p)

    while True:

        hex = next(h)
        while tri < hex:
            tri = next(t)
        while pent < hex:
            pent = next(p)
        if hex == tri:
            if tri == pent:
                # break
                print(tri)
                # break