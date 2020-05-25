from test_framework import generic_test

"""
count = 0
mask = 1
x & mask, if its 1 then increase the count
then we shift 1 bit to the right of x, x >>= 1
do this until x == 0
"""


def count_bits(x: int) -> int:
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count


"""
time O(n), n = size of the word, the # bits of x
as in python the integers are not bounded, so a 3 is 0b11, n = 2

space O(1)
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
