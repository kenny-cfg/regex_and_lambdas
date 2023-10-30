start_array = [1, 2, 3, 5, 6, 7, 9, 10]

'''
Get an array of all the elements that are even
'''


def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    new_array = list(filter(lambda element: element % 2 == 0, start_array))
    new_array_again = list(filter(is_even, start_array))
    print(new_array)
    print(new_array_again)
    '''
    The naive way:
    new_array = []
    for element in start_array:
        if element % 2 == 0:
            new_array.append(element)
    print(new_array)
    '''
