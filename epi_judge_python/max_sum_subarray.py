from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    max_sum = 0
    max_seen = 0
    for n in A:
        max_seen = max(n, max_seen + n)
        max_sum = max(max_sum, max_seen)
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
