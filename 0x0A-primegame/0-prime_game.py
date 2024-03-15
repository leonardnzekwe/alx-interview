#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """ # noqa
    Determines the winner of the game of primes between Maria and Ben
    based on the number of primes in the list of numbers provided as input.

    Args:
        x (int): The number of rounds.
        nums (list of int): List of integers representing the numbers in each round.

    Returns:
        str or None: The name of the winner, or None if there's no clear winner.
                     If Maria wins, returns 'Maria'. If Ben wins, returns 'Ben'.

    Notes:
        - If the input list is empty or the number of rounds is less than 1, returns None.
        - The winner is determined by the player who wins the most rounds. If both players win an equal number of rounds, the function returns None.
        - The function assumes that the input list contains only positive integers.

    Example:
        >>> isWinner(3, [1, 5, 10])
        'Ben'
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
