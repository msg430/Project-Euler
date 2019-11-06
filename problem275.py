def sidePoss(number, maxPoss):
    yield 0, 0, []
    for k in range(1, number+1):
        positions = [k]
        length = 1
        yield sideScore(positions), k, positions
        halt = True
        while halt:
            print(positions)
            for l in reversed(range(length)):
                if positions[l] > 1:
                    if l == length-1:
                        positions.append(1)
                        positions[l] -= 1
                        length += 1
                    else:
                        positions[l] -= 1
                        positions[l+1] += 1
                    h = sideScore(positions)
                    if h > maxPoss:
                        halt = False
                        break
                    yield h, k, positions
                    break
                if l == 0:
                    halt = False
                    break


def sideScore(side):
    total = 0
    for k in range(len(side)):
        total += (k+1)*side[k]
    return total


def sideMoves(positions, bottom, top):

    current = positions.copy()
    this = current.pop(0)
    if len(current) == 0:
        low = max(bottom+1-this, 1)
        high = top
        return high-low+1
    total = 0
    for k in range(-this+1, top-bottom+1):
        if bottom + k > 0:
            total += sideMoves(current, bottom+k, this+bottom+k-1)
    return total


def recursor(allowed, used, left, spent):
    if left == 0:
        yield sorted(list(used))
    else:
        hold = allowed.copy()
        noGo = spent.copy()
        left -= 1
        for k in allowed:
            hold.remove(k)
            noGo.add(k)
            thisH = set(hold)
            if k-1 > 0:
                if k-1 not in used:
                    if k - 1 not in noGo:
                        thisH.add(k-1)
            if k+1 not in used:
                if k+1 not in noGo:
                    thisH.add(k+1)
            nextLevel = recursor(thisH, used.union({k}), left, noGo)
            for n in nextLevel:
                yield n


def thisColumn(prior, number):
    rec = recursor(prior, set(), number, set())
    for r in rec:
        yield r


def newSideMoves(positions, prior):

    current = positions.copy()
    this = current.pop(0)
    if len(current) == 0:
        col = thisColumn(prior, this)
        count = 0
        for c in col:
            count += 1
        return count
    count = 0
    col = thisColumn(prior, this)
    for possibility in col:
        count += newSideMoves(current, possibility)
    return count


def sub(highest, left, lowest):
    if left == 0:
        yield []
    else:
        for r in range(lowest, highest-left+2):
            level = sub(highest, left-1, r+1)
            for l in level:
                yield [r]+l


def chooseMiddle(number, n, left, right, highest):
    # highest = n
    chosen = [1]
    giver = sub(highest, number-1, 2)
    for g in giver:
        yield chosen + g


def leftRightCheck(side, center, otherSide):
    needToClear = []
    good = []
    for block in center[0]:
        if block in side:
            good.append(block)
            continue
        if len(center) > 1:
            if block in center[1]:
                good.append(block)
                continue
        if len(center) == 1:
            if block in otherSide:
                good.append(block)
                continue
        needToClear.append(block)

    caught = True
    while caught:
        caught = False
        for need in needToClear:
            if (need + 1 in good) or (need - 1 in good):
                good.append(need)
                caught = True
                needToClear.remove(need)
                break

    if len(needToClear) > 0:
        return False
    return True


def giveNextColumns(left, middle, right, lpeak, rpeak):
    leftGiver = sub(lpeak, left, 1)
    rightGiver = sub(rpeak, right, 1)
    rights = []
    for rig in rightGiver:
        rights.append(rig)
    for lef in leftGiver:
        for rig in rights:
            if leftRightCheck(lef, middle, rig):
                rev = middle.copy()
                rev.reverse()
                if leftRightCheck(rig, rev, lef):
                    yield [lef] + middle + [rig]


def giveLastColumns(left, middle, right, n):
    using = []
    sides = [left,right]
    if left > 0:
        using.append(0)
    if right > 0:
        using.append(1)
    inner = [[], []]
    for u in using:
        inner[u] = middle[(len(middle)-1)*u].copy()
    width = len(middle)
    good = [(int(width/2), 1)]
    caught = True
    while caught:
        caught = False
        for c in range(width):
            for h in middle[c]:
                if (c, h) not in good:
                    for a in [-1, 1]:
                        if ((c + a, h) in good) or ((c, h + a) in good):
                            good.append((c, h))
                            caught = True
                            break
    bad = [[], []]
    for u in using:
        for h in middle[u*(width-1)]:
            if (u*(width-1), h) not in good:
                bad[u].append(h)
    if len(bad[0]) > 0 and len(bad[1]) > 0:
        if right < 3 and left < 3:
            return []
    mins = [1, 1]
    maxs = [0,0]
    for u in using:
        mins[u] = max(min(inner[u])-sides[u]+1,1)
        maxs[u] = max(inner[u])+sides[u]-1
    possible = []
    leftGiver = sub(maxs[0], left, mins[0])
    for l in leftGiver:
        rightGiver = sub(maxs[1], right, mins[1])
        for r in rightGiver:
            if checkConnection([l] + middle + [r], int((width+2)/2), n):
                possible.append([l]+middle+[r])
    # for p in possible:
    #     print(possible)
    #     printPoly(p, int((width+2)/2))
    return possible


def sideCheck(side, centre):
    needToClear = []
    good = []
    for block in side:
        if block in centre:
            good.append(block)
        else:
            needToClear.append(block)
    caught = True
    while caught:
        caught = False
        for need in needToClear:
            if (need + 1 in good) or (need - 1 in good):
                good.append(need)
                caught = True
                needToClear.remove(need)
                break
    if len(needToClear) > 0:
        return False
    return True


def printPoly(polyomino, centre):
    print('--------')
    # print(polyomino)
    width = len(polyomino)
    height = 0
    for c in polyomino:
        height = max(height, max(c))
    # print(height, width)
    for h in reversed(range(1,height+1)):
        # print(h)
        for c in polyomino:
            # row = ''
            if h in c:
                print('0', end='')
                # row = row + '0'
            else:
                # row = row + ' '
                print(' ', end='')
        print(' ')
            # print(row)
    # row = ''
    for r in range(centre):
        print(' ', end='')
        # row += ' '
    print('0')
    # print(row)


def calculatePeaks(left, right, middle):
    thisLeft = left.copy()
    thisLeft.reverse()
    polyomino = thisLeft + [middle] + right
    centre = len(thisLeft)
    peaks = []
    for k in range(len(polyomino)):
        # print(' ')
        # print(k)
        if k < centre:
            side = -1
        elif k == centre:
            side = 0
        else:
            side = 1
        # print(side)
        if side != 0:
            peak = 1
            c = centre
            while polyomino[c] > 1:
                peak += max(polyomino[c]-2, 0)
                c += -side
                if c == len(polyomino) or c == -1:
                    break
            if peak != 1:
                peak += 1
            else:
                peak = polyomino[centre]
            # print(peak, 'after moving opposite')
            c = centre + side
            while c != k:
                peak += polyomino[c]-1
                c += side
            # if polyomino[c] == 1:
            #     peaks.append(peak+1)
            #     continue
            # print(peak, 'after moving across')
            # print(c)
            # print(polyomino)
            while polyomino[c] > 1:
                # print('her')
                peak += max(polyomino[c]-2, 0)
                c += side
                if c == len(polyomino) or c == -1:
                    break
            if polyomino[k] > 1:
                peak += 1
            peaks.append(peak)
        else:
            if polyomino[k] == 1:
                peaks.append(1)
                continue
            left = centre
            while polyomino[left] > 1:
                left -= 1
                if left == -1:
                    break
            left += 1
            right = centre
            while polyomino[right] > 1:
                right += 1
                if right == len(polyomino):
                    break
            r = 0
            for h in range(centre + 1, right):
                r += max(polyomino[h] - 2, 0)
            l = 0
            for h in range(left, centre):
                l += max(polyomino[h] - 2, 0)
            if polyomino[centre] == 2:
                peak = 2
                peaks.append(peak+max(l, r))
            else:
                # print(l, r)
                peak = polyomino[centre] + l + r
                peaks.append(peak)
    return peaks


def doTheThing(n, left, right, middle):
    peaks = calculatePeaks(left, right, middle)
    # print(peaks)
    lPeaks = peaks[0:len(left)]
    lPeaks.reverse()
    rPeaks = peaks[len(left)+1:]
    symmetries = False
    if left == right:
        symmetries = True
    centreColumn = len(left)
    length = max(len(left), len(right))
    mid = chooseMiddle(middle, n, left, right, peaks[centreColumn])
    forNext = []
    for m in mid:
        # print(m)
        mids = [[m]]
        useLeft = left.copy()
        useRight = right.copy()
        useLPeak = lPeaks.copy()
        useRPeak = rPeaks.copy()
        for b in range(length):
            nextUp = []
            try:
                l = useLeft.pop(0)
                lpeak = useLPeak.pop(0)
            except IndexError:
                l = 0
                lpeak = 0
            try:
                r = useRight.pop(0)
                rpeak = useRPeak.pop(0)
            except IndexError:
                r = 0
                rpeak = 0
            for mi in mids:
                if b == length-1:
                    nextUp.extend(giveLastColumns(l, mi, r, n))
                    # print(nextUp)
                else:
                    giver = giveNextColumns(l, mi, r, lpeak, rpeak)
                    for g in giver:
                        nextUp.append(g)
                    # print(g)
            # print(nextUp)
            mids = nextUp.copy()
            # print(len(nextUp))
        forNext = mids + forNext
    outPut = []
    for m in forNext:
        hold = []
        for column in m:
            if column != []:
                hold.append(column)
        outPut.append(hold)
    pre = []
    for o in outPut:
        left = o[0]
        middle = o[1]
        if sideCheck(left, middle):
            right = o[len(o) - 1]
            middle = o[len(o) - 2]
            if sideCheck(right, middle):
                pre.append(o)
    if not symmetries:
        count = 0
        for p in pre:
            if checkConnection(p, centreColumn, n):
                count += 1
        return count
    else:
        mirrors = 0
        final = []
        for p in pre:
            if checkConnection(p, centreColumn, n):
                final.append(p)
        count = 0
        for f in final:
            great = False
            for h in range(length):
                if f[h] != f[2*length-h]:
                    great = True
                    count += 1
                    break
            if not great:
                mirrors += 1
        count = int(count/2)+mirrors
        return count


def checkConnection(polyomino, centre, n):
    # print(polyomino)
    good = [(centre, 1)]
    counter = 1
    caught = True
    while caught:
        caught = False
        for c in range(len(polyomino)):
            for h in polyomino[c]:
                if (c, h) not in good:
                    for a in [-1, 1]:
                        if ((c+a, h) in good) or ((c, h+a) in good):
                            good.append((c, h))
                            caught = True
                            counter += 1
                            break
    if counter == n:
        return True
    return False


def newGenerator(n):
    maxBlocks = int((n-1)/2)
    maxScore = int(maxBlocks*(maxBlocks+1)/2)
    maxBlocks = 0
    for r in range(1, n):
        maxBlocks += 1
        if maxBlocks > (n-1-r)*(n-r)/2:
            maxBlocks -= 1
            break
    peaks = []
    for k in range(1, int((n+1)/2)):
        high = int(k*(k-1)/2)
        r = 0
        while high + (r*k) <= (n-k-r)*(n-k-r+1)/2:
            r += 1
        r -= 1
        if r == 0:
            break
        peaks.append(r)
    combos = combinations(peaks)
    for c in combos:
        if c[len(c)-1] == 0:
            c.pop()
        blocks = sum(c)
        if blocks > maxBlocks:
            continue
        hold = sideScore(c)
        if hold > maxScore:
            continue
        yield hold, blocks, c


def combinations(tops):
    try:
        currentTop = tops.pop(0)
        deeper = combinations(tops)
        yield [0]
        for rest in deeper:
            for k in range(1, currentTop+1):
                yield [k] + rest
    except IndexError:
        yield []


if __name__ == '__main__':
    n = 15

    hold = 1
    while True:
        if hold*(hold+1) > n:
            hold -= 1
            break
        hold += 1

    maxe = int(hold*(hold+1)/2)
    if n-(hold*(hold+1)) > 1:
        maxe += (n-(hold*(hold+1))-1)
    maxPoss = int(0.5+(n-1)/2)
    maxPoss = int(maxPoss*(maxPoss+1)/2)

    bins = dict()
    side = newGenerator(n)
    for s in side:
        score, blocks, positions = s
        if blocks == 0:
            continue
        if score in bins:
            bins[score].append((blocks, positions.copy()))
        else:
            bins[score] = [(blocks, positions.copy())]

    highestScore = max(bins.keys())

    # print(bins)

    totalSum = 1
    for h in bins.keys():
        # print(h, 'of', highestScore)
        length = len(bins[h])
        for l in range(length):
            left = bins[h][l]
            for w in range(l, length):
                right = bins[h][w]
                print(left, right)
                middle = n - left[0] - right[0]
                # print(' ')
                # print(left[1], right[1], middle)
                # print(calculatePeaks(left[1], right[1], middle))
                if middle < 1:
                    continue
                add = doTheThing(n, left[1], right[1], middle)
                print(add)
                # print(' ')
                totalSum += add
    print(totalSum)

    # a = [3]
    # print(doTheThing(15, a, a, 9))
    # a = [1, 1]
    # b = [3]
    # print(doTheThing(10, b, a, 5))
    # 95