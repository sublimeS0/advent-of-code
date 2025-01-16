def main():
    """
    Entry point for day 15, part 1

    :return: Exit code
    """
    towels, patterns = read_input('input_ex.txt')

    for pattern in patterns:
        pass


def remove_towel(towel, pattern):

    pass


def read_input(filename):
    with open(filename, 'r') as file:
        towels = [line.strip().split(',') for line in file if "," in line and line != '\n']

    with open(filename, 'r') as file:
        patterns = [line.strip() for line in file if "," not in line and line != '\n']

    return towels[0], patterns


if __name__ == "__main__":
    main()
