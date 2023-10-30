import re

my_str = "Nano Degree is fun"
regex = "Nano\s\w+\s"


if __name__ == '__main__':
    matched = re.match(regex, my_str)
    print(matched)
    print(matched.span())
    print(matched.group())