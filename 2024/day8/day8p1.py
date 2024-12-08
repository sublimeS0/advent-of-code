from itertools import combinations


def main():
    """
    Entry point for day 8, part 1

    :return: Exit code
    """
    antenna_map = read_input('input.txt')

    antennas = locate_antennas(antenna_map)
    antinodes = []

    # Loop through sets of antennas to calculate antinodes
    for key in antennas:
        antenna_set = antennas[key]

        antenna_combinations = list(combinations(antenna_set, 2))

        # Loop through each combination and calculate antinode
        for antenna_com in antenna_combinations:
            antinode1, antinode2 = calculate_antinodes(antenna_com[0], antenna_com[1])

            # Add unique antinode locations
            if is_coord_in_map(antinode1, antenna_map) and antinode1 not in antinodes:
                antinodes.append(antinode1)
            if is_coord_in_map(antinode2, antenna_map) and antinode2 not in antinodes:
                antinodes.append(antinode2)

    for antinode in antinodes:
        antenna_map[antinode[0]][antinode[1]] = '#'

    print(antinodes)
    print(antennas)

    pretty_print(antenna_map)

    print('Unique antinodes: ' + str(len(antinodes)))


def calculate_antinodes(antenna_a, antenna_b):
    """
    Locate the two antinodes based on the locations of the antennas provided.

    :param antenna_a: Coordinates of first antenna
    :param antenna_b: Coordinates of second antenna
    :return: Antinode coordinate tuples
    """

    slope = (antenna_a[0] - antenna_b[0]) / (antenna_a[1] - antenna_b[1]) * -1

    # if False:
    #     test = 0
    # else:
    diff = (antenna_a[0] - antenna_b[0], antenna_a[1] - antenna_b[1])
    return ([antenna_b[0] - diff[0], antenna_b[1] - diff[1]]), ([antenna_a[0] + diff[0], antenna_a[1] + diff[1]])


def is_coord_in_map(coord, antenna_map):
    return 0 <= coord[0] < len(antenna_map) and 0 <= coord[1] < len(antenna_map[0])


def locate_antennas(antenna_map):
    """
    Finds all antennas and loads them into dictionary of sets of coordinate tuples.

    Ex:
    {
        '0': {(4, 4), (3, 7), (1, 8), (2, 5)},
        'A': {(8, 8), (5, 6), (9, 9)}
    }

    :param antenna_map: Map to search for antennas
    :return: Dictionary containing antenna locations
    """
    antennas = {}

    # Collect coordinates of matching antennas
    for r in range(len(antenna_map)):
        for c in range(len(antenna_map[r])):

            current_char = antenna_map[r][c]

            # Check for character or digit
            if current_char.isalnum():
                # Load antennas into dictionary of sets of coordinate tuples
                if current_char in antennas:
                    antennas[current_char].update([(r, c)])
                else:
                    antennas[current_char] = {(r, c)}

    return antennas


def pretty_print(antenna_map):
    """
    Print the antenna map list formatted.
    :param antenna_map: Map to be printed
    :return: None
    """
    print('')
    for r in antenna_map:
        for c in r:
            print(c, end='')
        print('')
    print('')


def read_input(filename):
    """
    Read input file into 2D list.
    :param filename: Name of file to read
    :return: Data in input file as a list
    """
    with open(filename) as file:
        map_input = [list(line.strip()) for line in file]
    return map_input


if __name__ == "__main__":
    main()
