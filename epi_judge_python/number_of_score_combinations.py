from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    if final_score == 0:
        return 1

    scores = individual_play_scores
    total = final_score
    rows = range(len(scores))
    cols = range(total + 1)
    t = [[0 for _ in cols] for _ in rows]
    for row in rows:
        curr_scores_range = range(row + 1)
        for col in cols:
            curr_total = col
            sum_ways = 0
            for curr_score_idx in curr_scores_range:
                delta = curr_total - scores[curr_score_idx]
                if delta >= 0:
                    if delta == 0:
                        sum_ways += 1
                    else:
                        sum_ways += t[curr_score_idx][delta]
            t[row][col] = sum_ways
    return t[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
