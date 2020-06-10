from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    ptr_a, ptr_b = 0, 0
    r = []
    while ptr_a < len(A) and ptr_b < len(B):
        if A[ptr_a] == B[ptr_b]:
            # if (ptr_a == 0 and ptr_b == 0) or \
            #         (ptr_a > 0 and A[ptr_a - 1] != B[ptr_b]) or \
            #         (ptr_b > 0 and B[ptr_b - 1] != A[ptr_a]):
            if ptr_a == 0 or A[ptr_a] != A[ptr_a - 1]:
                r.append(A[ptr_a])
            ptr_a += 1
            ptr_b += 1
        elif A[ptr_a] < B[ptr_b]:
            ptr_a += 1
        else:
            ptr_b += 1

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
