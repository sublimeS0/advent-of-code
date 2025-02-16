from functools import cache


def main():
    """
    Entry point for day 19, part 1

    132 - too low
    272 - correct

    :return: Exit code
    """
    towels, patterns = read_input('input.txt')

    possible_designs = []
    for pattern in patterns:

        # Get only the usable subset of towels
        available_towels = []
        for towel in towels:
            if towel in pattern:
                available_towels.append(towel)

        available_towels = tuple(available_towels)

        if is_composable(pattern, available_towels):
            possible_designs.append(pattern)

    print('Number of possible designs: ' + str(len(possible_designs)))
    print(possible_designs)


@cache
def is_composable(pattern, towels):
    """
    Return whether a pattern is composable using a given set of towels

    Cache results for improved runtime

    :param pattern: Pattern to be made with towels
    :param towels: Tuple of available towels
    :return: True if pattern can be mase up of towels, false otherwise
    """
    if pattern == '':
        return True

    for towel in towels:
        if pattern.startswith(towel) and is_composable(pattern[len(towel):], towels):
            return True

    return False


def read_input(filename):
    """
    Reads input file into data structures
    :param filename: Name of input file to read
    :return: List of available towels and list of desired patterns
    """
    with open(filename, 'r') as file:
        towels = [line.strip().split(', ') for line in file if "," in line and line != '\n'][0]

    with open(filename, 'r') as file:
        patterns = [line.strip() for line in file if "," not in line and line != '\n']

    return towels, patterns


if __name__ == "__main__":
    main()
