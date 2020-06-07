from typing import List

from test_framework import generic_test

from heapq import heapify, heappush, heappop
import heapq


def merge_sorted_arrays_(sorted_arrays: List[List[int]]) -> List[int]:
    """
    [-1, 0], [-2]
    :param sorted_arrays:
    :return:
    """
    h = [(a[0], i, 0) for i, a in enumerate(sorted_arrays)]
    heapify(h)
    r = []
    while h:
        try:
            c = heappop(h)
            r.append(c[0])
            heappush(h, (sorted_arrays[c[1]][c[2] + 1], c[1], c[2] + 1))
        except:
            pass
    return r


def merge_sorted_arrays_refactor(sorted_arrays: List[List[int]]) -> List[int]:
    """
    [-1, 0], [-2]
    :param sorted_arrays:
    :return:
    """
    h = [(a[0], i, 0) for i, a in enumerate(sorted_arrays)]
    heapify(h)
    r = []
    while h:
        try:
            elem, idx_arr, pos_elem = heappop(h)
            r.append(elem)
            heappush(h, (sorted_arrays[idx_arr][pos_elem + 1],
                         idx_arr,
                         pos_elem + 1))
        except:
            pass
    return r


def merge_sorted_arrays_book(sorted_arrays: List[List[int]]) -> List[int]:
    array_iterators = [iter(curr_array) for curr_array in sorted_arrays]
    h = []
    r = []
    # the list is automatically heapify if we use heappush as below
    # heapify(h)
    for idx_array, iter_array in enumerate(array_iterators):
        elem = next(iter_array, None)
        if elem is not None:
            heappush(h, (elem, idx_array))
    while h:
        min_elem, idx_array = heappop(h)
        r.append(min_elem)
        next_elem = next(array_iterators[idx_array], None)
        if next_elem is not None:
            heappush(h, (next_elem, idx_array))

    return r


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
