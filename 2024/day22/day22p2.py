import math
from collections import Counter
from functools import cache


def main():
    """
    Entry point for day 22, part 1

    1434 - too low
    1483 - too high


    :return: Exit code
    """
    initial_numbers = read_input('input.txt')

    count = 2000
    total = 0

    scores = {}

    for value in initial_numbers:

        digits = []
        diffs = []

        initial_value = value

        # print(str(initial_value) + ': ' + str(value % 10))
        digits.append(value % 10)

        # Calculate diffs between final digits
        for i in range(count):
            value = calculate_next_secret(value)

            digit = value % 10
            digits.append(digit)
            diffs.append(digits[-1] - digits[-2])

            # print(str(value) + ': ' + str(digit), end='')
            # print(' (' + str(diffs[i]) + ')')

        # print()
        # print(str(initial_value) + ': ' + str(value))

        # Collect sequence/score pairs for each starting secret num
        num_scores = {}
        for j in range(4, len(diffs)):
            key = tuple(diffs[j - 4:j])
            value = digits[j]

            if key in num_scores:
                continue
            else:
                num_scores[key] = value

        scores[initial_value] = num_scores

    # Find best sequence
    c = Counter()

    for value in scores.values():
        c.update(value)

    sequence_scores = dict(c)
    best_sequence = max(sequence_scores, key=sequence_scores.get)

    print()
    print('Max bananas: ' + str(sequence_scores[best_sequence]))


@cache
def calculate_next_secret(secret):
    """
    Calculates next secret number
    :param secret: Current secret number
    :return: Next secret number
    """
    new_secret = prune(mix(secret * 64, secret))
    new_secret = prune(mix(math.floor(new_secret / 32), new_secret))
    new_secret = prune(mix(new_secret * 2048, new_secret))

    return new_secret


def mix(number, secret):
    """
    Perform 'mix' operation
    :param number: Number to be mixed
    :param secret: Current secret number
    :return: New secret number
    """
    return number ^ secret


def prune(secret):
    """
    Perform 'prune' operation
    :param secret: Current secret number
    :return: New secret number
    """
    MODULO_VALUE = 16777216
    return secret % MODULO_VALUE


def read_input(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]


if __name__ == "__main__":
    main()
