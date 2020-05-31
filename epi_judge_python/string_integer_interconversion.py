from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    """
    Time O(n), n is the number of digits of x
    Space O(n)
    :param x:
    :return:
    """
    if x == 0:
        return '0'

    neg = False
    if x < 0:
        neg = True
        x *= -1

    res = x
    nums = []

    while res != 0:
        rem = res % 10
        res = res // 10
        nums.append(str(rem))

    if neg:
        nums.append('-')

    return ''.join(reversed(nums))


def string_to_int(s: str) -> int:
    if s[0] == '-' or s[0] == '+':
        neg = True if s[0] == '-' else False
        start = 1
    else:
        neg = False
        start = 0

    exp = 0
    sum_ = 0

    def get_int(s):
        """
        If we can't use int(s) we do it with a switch statement
        Time O(n), n is the length of s
        Space O(1)
        :param s:
        :return:
        """
        switch = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        return switch.get(s, 'default')
        # return int(s)

    for n in reversed(s[start:]):
        num = get_int(n)
        # ^ IS THE XOR BITWISE!!!
        # sum_ += num * (10 ^ exp)
        sum_ += num * (10 ** exp)
        exp += 1

    if neg:
        sum_ *= -1

    return sum_


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
