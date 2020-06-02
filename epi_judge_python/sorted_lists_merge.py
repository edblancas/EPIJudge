from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists_book_me(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode()
    tail = dummy_head

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
            tail = tail.next
        else:
            tail.next = L2
            L2 = L2.next
            tail = tail.next

    tail.next = L1 or L2

    return dummy_head.next


def merge_two_sorted_lists(L1: Optional[ListNode],
                                    L2: Optional[ListNode]) -> Optional[ListNode]:
    tail = dummy_head = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2

    return dummy_head.next


def merge_two_sorted_lists_me(L1: Optional[ListNode],
                              L2: Optional[ListNode]) -> Optional[ListNode]:
    """
    1->2
    2->3
    1->2->2->3
    """

    dummy_head = ListNode()
    merged_curr = ListNode()
    dummy_head.next = merged_curr
    prev = dummy_head
    while L1 and L2:
        if L1.data <= L2.data:
            merged_curr.data = L1.data
            L1 = L1.next
        else:
            merged_curr.data = L2.data
            L2 = L2.next

        if L1 and L2:
            merged_curr.next = ListNode()

        prev = merged_curr
        merged_curr = merged_curr.next

    if prev is not dummy_head:
        prev.next = ListNode()
        merged_curr = prev.next

    while L1:
        merged_curr.data = L1.data
        L1 = L1.next
        if L1:
            merged_curr.next = ListNode()

        merged_curr = merged_curr.next

    while L2:
        merged_curr.data = L2.data
        L2 = L2.next
        if L2:
            merged_curr.next = ListNode()

        merged_curr = merged_curr.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
