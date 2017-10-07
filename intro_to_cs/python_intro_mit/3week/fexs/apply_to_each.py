testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

applyToEach(testList, abs) # => [1, 4, 8, 9]

def addOne(e):
    return e + 1

applyToEach(testList, addOne) # => [2, -3, 9, -8]

def sqr(e):
    return e ** 2

applyToEach(testList, sqr) # => [1, 16, 64, 81]
