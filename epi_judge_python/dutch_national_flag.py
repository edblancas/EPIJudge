import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition_book(pivot_index: int, A: List[int]) -> None:
    piv = A[pivot_index]
    # equals_idx is the one to compare
    smaller_idx, equals_idx = 0, 0
    larger_idx = len(A) - 1

    # this need to be <= because we need to inspect the larger index also
    # cause the larger_idx is the next to be placed, so its not compared
    # already
    # while equals_idx < larger_idx:
    while equals_idx <= larger_idx:
        if A[equals_idx] < piv:
            A[smaller_idx], A[equals_idx] = A[equals_idx], A[smaller_idx]
            smaller_idx += 1
            equals_idx += 1
        elif A[equals_idx] > piv:
            A[larger_idx], A[equals_idx] = A[equals_idx], A[larger_idx]
            larger_idx -= 1
        else: # A[equals_idx] == piv
            equals_idx += 1


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # swap the pivot to the last position
    A[-1], A[pivot_index] = A[pivot_index], A[-1]
    # 1st pass to put all the elems <= in the left and the elems > in the right
    #   and get the new position of the pivot
    p = sort_pivot(A, 0, len(A) - 1, lambda e1, e2: e1 > e2)
    # 2nd pass to put all the elems < the piv in the left and the elems == in the
    #   right
    sort_pivot(A, 0, p, lambda e1, e2: e1 >= e2)


def sort_pivot(array, start, piv_idx, comp) -> int:
    while start < piv_idx:
        if comp(array[start], array[piv_idx]):
            piv_tmp = array[piv_idx]
            array[piv_idx] = array[start]
            piv_prev = array[piv_idx - 1]
            array[piv_idx - 1] = piv_tmp
            if start < piv_idx - 1:
                array[start] = piv_prev
            piv_idx -= 1
        else:
            start += 1

    return piv_idx


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
