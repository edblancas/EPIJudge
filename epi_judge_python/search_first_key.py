from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    """
    [1, 1, 3, 4, 5, 6, 6, 9]
    10 -> -1
    1 -> 0

    6 -> 5
    len = 8
    mid = 8 // 2 = 4
    mid = (5 + 8) // 2 = 6
    return 5

    [1, 1, 1]
    1 -> 0
    len = 3
    mid = 3 // 2 = 1
    if a[mid] == elem_search:
        while mid >= 0 and a[mid] == elem_search:
            mid -= 1
        return mid

    :param A:
    :param k:
    :return:

    start = 0
    end = 7, 2, 0
    mid = 3, 1, 0
    """

    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if k > A[mid]:
            start = mid + 1
        elif k < A[mid]:
            end = mid - 1
        else:
            while mid > 0 and A[mid-1] == k:
                mid -= 1
            return mid
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
