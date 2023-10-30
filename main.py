def plus_two(num):
    return num + 2


plus_two_lambda = lambda num: num + 2


if __name__ == '__main__':
    result = plus_two(5)
    print(result)
    result_with_lambda = plus_two_lambda(5)
    print(result_with_lambda)
