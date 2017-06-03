#!/bin/python3

import sys
# import numpy as np


def _get_change_making_matrix(set_of_coins, r):
    matrix = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    # matrix = np.array(matrix)
    for i in range(1,len(set_of_coins) + 1):
        matrix[i][0] = i

    return matrix


def change_making(coins, target):
    """This function assumes that all coins are available infinitely.
    n is the number that we need to obtain with the fewest number of coins.
    coins is a list or tuple with the available denominations."""
    matrix = _get_change_making_matrix(coins, target)

    for coin in range(1, len(coins) + 1):

        for sub_target in range(1, target + 1):

            # Just use the coin coins[c - 1].
            if coins[coin - 1] == sub_target:
                matrix[coin][sub_target] = 1+matrix[coin-1][sub_target]

            # coins[c - 1] cannot be included.
            # We use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[coin - 1] > sub_target:
                matrix[coin][sub_target] = matrix[coin - 1][sub_target]

            # We can use coins[c - 1].
            # We need to decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without using coins[c - 1]) plus this 1 extra coin.
            else:
                matrix[coin][sub_target] = (matrix[coin - 1][sub_target]) + (
                     matrix[coin][sub_target - coins[coin - 1]])

    return matrix[-1][-1]


input1 = input()
input2 = input()

# input1 = "10 4"
# input2 = "2 5 3 6"

n, m = input1.strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input2.strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = change_making(c, n)
print(ways)
