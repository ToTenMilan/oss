def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if char == aStr :
        return True
    elif len(aStr) == 0:
        return False
    else:
        while len(aStr) > 1:
            middle = len(aStr) // 2
            if char == aStr[middle]:
                return True
            elif char < aStr[middle]:
                return isIn(char, aStr[:middle])
            elif char > aStr[middle]:
                return isIn(char, aStr[(middle+1):])
        return False
