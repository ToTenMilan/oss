def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = a
    while test >= 1:
        test -= 1
        if a % test== 0 and b % test == 0:
            return test

    return 1
