

def cancel(number, place):
    asString = str(number)
    asString = asString[(place+1) % 2]
    if int(asString) == 0:
        return -1
    return int(asString)



if __name__ == '__main__':

    for a in range(10,100):
        for b in range(a+1,100):
            hold = a/b
            x = cancel(a,0)/cancel(b,1)
            y = cancel(a,1)/cancel(b,0)
            if hold == x or hold == y:
                print((a,b))




    # (16/64)
    # (19/95)
    # (26/65)
    # (49/98)