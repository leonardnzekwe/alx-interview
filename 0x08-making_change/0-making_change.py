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
    if total <= 0:  # If the total amount is 0 or less,
        return 0

    coins.sort(reverse=True)  # Sort the coins in descending order

    change = 0  # Variable to keep track of the number of coins used for change

    for coin in coins:  # Iterate through each coin value
        if total <= 0:  # If the total amount is already met, exit the loop
            break

        temp = (
            total // coin
        )  # Calculate the max number of coins of this value that can be used
        change += temp  # Add the number of coins used to the change count
        total -= (
            temp * coin
        )  # Subtract the value of the coins used from the total amount

    if total != 0:  # If the total amount is not completely met, return -1
        return -1

    return change  # Return the total number of coins used for change
