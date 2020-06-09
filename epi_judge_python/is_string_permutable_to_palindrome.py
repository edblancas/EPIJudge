from test_framework import generic_test
from collections import defaultdict


def can_form_palindrome(s: str) -> bool:
    chrs = defaultdict(lambda: 0)
    for c in s:
        chrs[c] += 1
    odds = 0
    for v in chrs.values():
        odds += int(v % 2 == 1)
        if odds > 1:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
