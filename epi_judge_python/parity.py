from test_framework import generic_test

"""
1 if the # of 1's is odd, otherwise 0

10 = 0b1010 -> 0
14 = 0b1110 -> 1

1st approach:
count the 1's with a 1 mask, x & mask and increase the count
shift to the right 1 bit of x
do until x == 0
return int(count % 2 == 1) 
"""


def parity(x: int) -> int:
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return int(count % 2 == 1)


"""
time O(n), n = size of the x word in binary
space constant O(1)
"""

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
