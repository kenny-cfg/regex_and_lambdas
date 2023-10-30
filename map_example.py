start_array = [1, 2, 3, 5, 7]

'''
Want to transform each of these numbers in the array by doubling them
'''


if __name__ == '__main__':
    new_array = list(map(lambda num: num * 2, start_array))
    print(new_array)
    new_array_with_comprehension = [num * 2 for num in start_array]
    print(new_array_with_comprehension)

    '''
    The old way:
    
    new_array = []
    for entry in start_array:
        new_array.append(entry * 2)
    print(new_array)
    '''
