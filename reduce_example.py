from functools import reduce

start_array = ['Hello', 'my', 'name', 'is', 'Freddie']

'''
Given an array of strings, I want a new string which is all the words repeated (i.e. printed twice)
'''


def reduction(current, next):
    return current + next + next


if __name__ == '__main__':
    result = reduce(reduction, start_array, 'Hello')
    print(result)
    '''
    This is the naive way:
    result = ''
    for word in start_array:
        result += word
        result += word
    print(result)
    '''

