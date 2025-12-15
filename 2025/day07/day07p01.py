def main():
    """
    Entry point for Day 7, Part 1

    1507 - correct

    :return: Exit code
    """
    diagram, start_tile = read_input('input_ex.txt')
    laser_cols = {start_tile[1]}

    splits = 0
    for r, row in enumerate(diagram):
        if r == 0:
            continue

        for col in laser_cols.copy():
            if row[col] == '^':
                splits += 1

                laser_cols.remove(col)
                laser_cols.add(col - 1)
                laser_cols.add(col + 1)

    print('Splits: ' + str(splits))


def read_input(filename):
    """
    Read input file into relevant data structures
    :param filename: Name of input file
    :return: Return relevant data structures
    """

    diagram = []
    with open(filename, 'r') as file:
        for r, line in enumerate(file):
            line = line.strip()
            line_dict = {}

            for c, char in enumerate(line):
                line_dict[c] = char

                if char == 'S':
                    start_tile = (r, c)

            diagram.append(line_dict)

    return diagram, start_tile


if __name__ == "__main__":
    main()
