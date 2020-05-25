import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
3, 1, 2, 4, 7, 8 -> 2, 4, 8, 3, 1, 7
e              o
8, 1, 2, 4, 7, 3 -> 8, 1, 2, 4, 7, 3 -> 8, 1, 2, 4, 7, 3 -> 8, 4, 2, 1, 7, 3 -> e == o
   e           o       e        o          e     o                e  o
o is even? true then swap to e place and advance
e cause even num is in place, the o stays in the
same place cause we don't know if it's even or odd

o is even? false is odd, this is in place so move o

when e == o we finish
"""


def even_odd(A: List[int]) -> None:
    # TODO - you fill in here.
    e = 0
    o = len(A) - 1
    while e < o:
        if A[o] % 2 == 0:
            A[o], A[e] = A[e], A[o]  # this way we don't need a temp var
            e += 1
        else:
            o -= 1
    return


"""
Tips:
- Beware of the o index must be len - 1
- Caution with the e and o indexes, one move to right +1 and the other to the
    left -1
"""


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
