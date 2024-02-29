#!/usr/bin/python3
"""
Module for making change using fewest number of coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    Args:
        coins: list of the values of the coins in your possession
        total: the amount to make change for
    Returns:
        The fewest number of coins needed to meet the total
    """
    if total < 1:
        return 0

    # Initialize a list to store the fewest
    # number of coins needed for each amount
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Calculate the fewest number of coins for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float("inf") else -1
