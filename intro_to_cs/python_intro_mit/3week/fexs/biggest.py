def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    longest = 0
    longestKey = ''
    for key in aDict.keys():
        if len(aDict[key]) > longest:
            longestKey = key
    return longestKey



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

biggest(animals) # => 'd'
