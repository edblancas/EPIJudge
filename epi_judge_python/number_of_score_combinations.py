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
        for i in range(idx, len(individual_play_scores)):
            sum_ += go(individual_play_scores[i] + cur_sum, i)

        memo[k] = sum_
        print(k, sum_)
        return sum_


    def go_it():
        dp = [[1] + [0] * final_score 
              for _ in individual_play_scores]

        for score in range(1, final_score + 1):
            if individual_play_scores[0] > score: continue
            dp[0][score] = dp[0][score - individual_play_scores[0]]

        for play in range(1, len(individual_play_scores)):
            for score in range(1, final_score + 1):
                # Watch for negative array indexes, in this case we only add the above result
                # I was not putting the next if
                if individual_play_scores[play] > score: 
                    dp[play][score] = dp[play - 1][score]

                else:
                    dp[play][score] = dp[play - 1][score] + dp[play][score - individual_play_scores[play]]

        # print(dp)
        return dp[len(individual_play_scores) - 1][final_score]

    def go_it_constant_space():
        dp = [1] + [0] * final_score
        for play in range(len(individual_play_scores)):
            for score in range(1, final_score + 1):
                if individual_play_scores[play] > score: continue
                dp[score] = dp[score] + dp[score - individual_play_scores[play]]
        return dp[-1]

    # return go(0,0)
    # return go_it()
    return go_it_constant_space()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
"""

[
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
[1, 0, 0, 1, 1, 0, 2, 1, 1, 2, 2, 1, 3],
[1, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 3]]

"""
