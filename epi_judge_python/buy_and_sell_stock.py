from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once_naive(prices: List[float]) -> float:
    """
    Time O(n^2)
    Space O(1)
    The test 400 it takes to much time, I had to stop it.
    :param prices:
    :return:
    """
    max_ = float('-inf')
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_ = max(prices[j] - prices[i], max_)

    return 0.0 if max_ <= 0 else max_


def buy_and_sell_stock_once_div_conq(prices: List[float]) -> float:
    """
    The test 400/402 again was taking too much time
    Time T(n) = 2T(n/2) + O(n) => O(n log n)
    O(n)???
    Space O(n)
    :param prices:
    :return:
    """
    mid = len(prices) // 2
    max1 = float('-inf')
    min_loc = float('inf')
    for i in range(mid):
        min_loc = min(min_loc, prices[i])
        for j in range(i + 1, mid):
            max1 = max(max1, prices[j] - prices[i])

    max2 = float('-inf')
    max_local = float('-inf')
    idx = None
    for i in range(mid, len(prices)):
        max_local = max(max_local, prices[i])
        # second mistake
        # with mid instead of i, i was violating the constraint of buy in a
        #   day before sell. When i was > mid, then I was taking into account
        #   sell in a day before buying XD.
        # for j in range(mid + 1, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max2:
                idx = (prices[i], prices[j], i, j, mid)

            max2 = max(max2, prices[j] - prices[i])

    # this was my mistake
    # max_mid = max2 - max1
    max_mid = max_local - min_loc
    # print(max1, max2, idx, max_mid, min_loc, max_local)
    if max1 > 0 and max1 >= max2:
        res_max = max1
    else:
        res_max = max2

    if max_mid > 0 and max_mid > res_max:
        return max_mid
    elif res_max > 0:
        return res_max

    return 0.0


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_ = float('inf')
    max_prof = float('-inf')
    for i in range(len(prices)):
        min_ = min(min_, prices[i])
        max_prof = max(max_prof, prices[i] - min_)

    return 0.0 if max_prof <= 0 else max_prof


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
