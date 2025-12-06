def main():
    """
    Entry point for Day 3, Part 2

    167384358365132 - correct

    :return: Exit code
    """
    banks = read_input('input.txt')

    battery_length = 12

    max_joltage = 0

    for bank in banks:

        current_joltage = ''
        max_index = 0

        for i in range(battery_length - 1):
            search_list = bank[max_index:-battery_length + i + 1]

            current_joltage += max(search_list)
            max_index += search_list.index(max(search_list)) + 1

        current_joltage += max(bank[max_index:])

        max_joltage += int(current_joltage)

    print('Max Joltage: ' + str(max_joltage))


def read_input(filename):
    """
    Reads the input file and moves data to relevant data structure

    :param filename:
    :return:
    """

    with open(filename) as file:
        banks = [list(line.strip()) for line in file]

    return banks


if __name__ == "__main__":
    main()
