def main():
    """
    Entry point for Day 2, Part 2

    18952700150 - correct

    :return: Exit code
    """

    ranges = read_input('input.txt')

    invalid_sum = 0
    for range_item in ranges:
        for value in range(range_item['lower'], range_item['upper'] + 1):
            value_str = str(value)

            if value_str in (value_str + value_str)[1:-1]:
                invalid_sum += value

    print('Invalid Sum: ' + str(invalid_sum))


def read_input(filename):
    """
    Read input and covert to relevant data structure
    :param filename: Name of input file
    :return: List of dictionaries containing range info
    """
    with open(filename) as file:
        for line in file:
            ranges = line.split(',')

    split_ranges = []
    for item in ranges:
        values = item.split('-')

        split_ranges.append({
            'lower': int(values[0]),
            'upper': int(values[1]),
        })

    return split_ranges


if __name__ == "__main__":
    main()
