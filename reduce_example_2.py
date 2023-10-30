from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]
print(numbers)


if __name__ == '__main__':
    result = reduce(lambda a, b: a + b, numbers)
    print(result)