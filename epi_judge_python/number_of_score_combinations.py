from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    memo = dict()
    def go(cur_sum, idx):
        k = (cur_sum, idx)
        if k in memo:
            return memo[k]

        if cur_sum == final_score:
            return  1
        elif cur_sum > final_score:
            return 0

        sum_ = 0
        for i in range(len(individual_play_scores)):
            sum_ += go(individual_play_scores[i] + cur_sum, i)

        memo[k] = sum_
        return sum_


    def go2(cur_sum, idx):
        k = cur_sum
        if k in memo:
            print('memo', k, memo[k])
            return memo[k]

        if cur_sum == final_score:
            return  1
        elif cur_sum > final_score:
            return 0

        sum_ = 0
        for i in range(len(individual_play_scores)):
            sum_ += go2(individual_play_scores[i] + cur_sum, i)

        memo[k] = sum_
        print('calculated', k, memo[k])
        return sum_


    def go_no_idx(cur_sum):
        k = cur_sum
        if k in memo:
            return memo[k]

        if cur_sum == final_score:
            return  1
        elif cur_sum > final_score:
            return 0

        sum_ = 0
        for play in individual_play_scores:
            sum_ += go_no_idx(play + cur_sum)

        memo[k] = sum_
        return sum_

    def go_bottom(left_sum):
        if left_sum == 0:
            return 1
        if left_sum < 0:
            return 0
        s = 0
        for play in individual_play_scores:
            s += go_bottom(left_sum - play)
        return s

    # return go(0, 0)
    # return go_no_idx(0)
    r = go2(0, 0)
    print(memo)
    return r


if __name__ == '__main__':
   print(num_combinations_for_final_score(12, [2,3,7]))
"""

[
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
[1, 0, 0, 1, 1, 0, 2, 1, 1, 2, 2, 1, 3],
[1, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 3]]

"""
