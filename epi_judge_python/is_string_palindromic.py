from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    mid_len = len(s) // 2
    if mid_len == 0:
        return True

    left = range(mid_len)
    right = range(-1, -(mid_len+1), -1)

    return all(s[i] == s[j] for i, j in zip(left, right))


def is_palindromic_book(s: str) -> bool:
    # the xor bitwise ~ has the effect of -(x+1)
    return all(s[x] == s[~x] for x in range(len(s)))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
