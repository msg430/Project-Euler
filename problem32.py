def recursor(left):
    if not left:
        yield []
    else:
        for k in left:
            leftCopy = left.copy()
            leftCopy.remove(k)
            r = recursor(leftCopy)
            for each in r:
                yield [str(k)] + each


if __name__ == '__main__':

    works = set()
    recurs = recursor(list(range(1, 10)))
    for h in recurs:
        a = int(''.join(h[0]))
        b = int(''.join(h[1:4]))
        c = int(''.join(h[4:9]))
        if a*b == c:
            print(a, '*', b, '=', c)
            works.add(c)

        a = int(''.join(h[0]))
        b = int(''.join(h[1:5]))
        c = int(''.join(h[5:9]))
        if a * b == c:
            print(a, '*', b, '=', c)
            works.add(c)

        a = int(''.join(h[0:2]))
        b = int(''.join(h[2:4]))
        c = int(''.join(h[4:9]))
        if a * b == c:
            print(a, '*', b, '=', c)
            works.add(c)

        a = int(''.join(h[0:2]))
        b = int(''.join(h[2:5]))
        c = int(''.join(h[5:9]))
        if a * b == c:
            print(a, '*', b, '=', c)
            works.add(c)


    works = list(works)
    print(sum(works))