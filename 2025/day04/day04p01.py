def main():
    """
    Entry point for Day 4, Part 1

    1489 - correct

    :return: Exit code
    """
    diagram = read_input('input.txt')

    # print_diagram(diagram)

    accessible = 0

    for key, value in diagram.items():
        if value != '@':
            continue

        adjacent = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                coord = (key[0] + i, key[1] + j)
                if coord == key:
                    continue

                if coord in diagram and diagram[coord] == '@':
                    adjacent += 1

        if adjacent < 4:
            accessible += 1

    print('Accessible boxes: ' + str(accessible))


def read_input(filename):
    """
    Reads the input file and moves data to relevant data structure

    :param filename: Name of input file
    :return: Dictionary of coordinate - character pairs
    """

    diagram = {}

    with open(filename, 'r') as file:
        for r, line in enumerate(file):
            line = line.strip()

            for c, char in enumerate(line):
                diagram[(r, c)] = char

    return diagram


def print_diagram(diagram):
    """
    Prints the diagram dictionary in an easy to read and debug format
    :param diagram: Diagram to print
    :return: None
    """
    current_line = 0
    for key, value in diagram.items():
        if key[0] == current_line:
            print(value, end='')
        else:
            current_line = key[0]
            print()
            print(value, end='')

    print()
    print()


if __name__ == "__main__":
    main()
