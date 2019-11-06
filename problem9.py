def doit():
    for i in range(1, 500):
        for j in range(i, 500):
            if (i*i+j*j) == (1000-i-j)*(1000-i-j):
                print(i)
                print(j)
                print(1000-i-j)
                print(i*j*(1000-i-j))
                return


doit()
