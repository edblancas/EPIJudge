from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
   s = 0
    e = len(A) - 1
    first_ocurr = -1
    while s <= e:
        mid = (s + e) // 2
        if k < A[mid]:
            e = mid - 1
        elif k > A[mid]:
            s = mid + 1
        else:
            first_ocurr = mid
            e = mid - 1

    return first_ocurr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
