#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Determines the winner of each game in a
    list of games with a list of numbers.

    Args:
    - x (int): The number of rounds.
    - nums (List[int]): A list of integers representing
    the upper bounds for each game.

    Returns:
    - str or None: The name of the player who won the most rounds.
                   If the winner cannot be determined, returns None.

    The winner is the first player to remove all prime numbers from the list.
    If the number of prime numbers is even, Ben wins.
    If the number of prime numbers is odd, Maria wins.
    If there are no prime numbers, the game is a draw.
    """

    def calculate_primes(n):
        """
        Calculates prime numbers up to a given number n
        using the Sieve of Eratosthenes algorithm.

        Args:
        - n (int): The upper limit to generate prime numbers up to.

        Returns:
        - List[int]: A list of prime numbers up to n.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    def play_game(n):
        """
        Simulates a single round of the game for a given upper bound.

        Args:
        - n (int): The upper bound for the current game.

        Returns:
        - str: The name of the winner ('Maria' or 'Ben').
        """
        primes = calculate_primes(n)
        num_primes = len(primes)
        if num_primes % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    results = {"Maria": 0, "Ben": 0}

    for i in range(x):
        winner = play_game(nums[i])
        results[winner] += 1

    max_wins = max(results.values())
    if max_wins == 0 or results["Maria"] == results["Ben"]:
        return None
    else:
        return max(results, key=results.get)
