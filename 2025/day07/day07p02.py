def main():
    """
    Entry point for Day 7, Part 2

    1537373473728 - correct

    :return: Exit code
    """
    diagram, start_tile = read_input('input.txt')
    laser_cols = {num: 0 for num in range(len(diagram[0]))}
    laser_cols[start_tile[1]] = 1

    for r, row in enumerate(diagram):
        if r == 0 or ('^' not in row.values()):
            continue

        # Check each column. If the column is a splitter, "pass" its laser count to its neighbors
        for col in laser_cols.copy():
            if row[col] == '^':
                laser_cols[col - 1] += laser_cols[col]
                laser_cols[col + 1] += laser_cols[col]

                laser_cols[col] = 0  # Reset current col count since lasers cannot pass through

    print('Timelines: ' + str(sum(laser_cols.values())))


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
