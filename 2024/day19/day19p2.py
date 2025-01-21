from functools import cache


def main():
    """
    Entry point for day 19, part 1

    1041529704688380 - correct

    :return: Exit code
    """
    towels, patterns = read_input('input.txt')

    pattern_sum = 0
    for pattern in patterns:

        # Get only the usable subset of towels
        available_towels = []
        for towel in towels:
            if towel in pattern:
                available_towels.append(towel)

        available_towels = tuple(available_towels)

        pattern_sum += is_composable(pattern, available_towels)

    print('Number of possible designs: ' + str(pattern_sum))


@cache
def is_composable(pattern, towels):
    """
    Return the number of combinations of towels that can make up a pattern

    Cache results for improved runtime

    :param pattern: Pattern to be made with towels
    :param towels: Tuple of available towels
    :return: Number of combinations of towels that can make up a pattern
    """
    if pattern == '':
        return 1

    count = 0
    for towel in towels:
        if pattern.startswith(towel):
            count += is_composable(pattern[len(towel):], towels)

    return count


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
