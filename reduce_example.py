start_array = ['Hello', 'my', 'name', 'is', 'Freddie']

'''
Given an array of strings, I want a new string which is all the words repeated (i.e. printed twice)
'''

if __name__ == '__main__':
    result = ''
    for word in start_array:
        result += word
        result += word
    print(result)

