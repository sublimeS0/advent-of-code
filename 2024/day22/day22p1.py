import math


def main():
    """
    Entry point for day 22, part 1
    :return: Exit code
    """
    initial_numbers = read_input('input.txt')

    count = 2000
    total = 0
    for value in initial_numbers:
        initial_value = value
        for i in range(count):
            value = calculate_next_secret(value)
            # print(value)
        total += value
        # print(str(initial_value) + ': ' + str(value))

    print()
    print('Sum: ' + str(total))


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
