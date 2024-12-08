from itertools import combinations


def main():
    """
    Entry point for day 8, part 2

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
            calculated_antinodes = calculate_antinodes(antenna_com[0], antenna_com[1], antenna_map)

            # Add unique antinode locations
            for c_node in calculated_antinodes:
                if is_coord_in_map(c_node, antenna_map) and c_node not in antinodes:
                    antinodes.append(c_node)

    for antinode in antinodes:
        if not str(antenna_map[antinode[0]][antinode[1]]).isalnum():
            antenna_map[antinode[0]][antinode[1]] = '#'

    print(antinodes)
    print(antennas)

    pretty_print(antenna_map)

    print('Unique antinodes: ' + str(len(antinodes)))


def calculate_antinodes(antenna_a, antenna_b, antenna_map):
    """
    Locate the two antinodes based on the locations of the antennas provided.

    :param antenna_a: Coordinates of first antenna
    :param antenna_b: Coordinates of second antenna
    :return: Antinode coordinate tuples
    """

    diff = (antenna_a[0] - antenna_b[0], antenna_a[1] - antenna_b[1])

    calculated_antinodes = []

    multiplier = 0

    while True:

        current_coord = ([antenna_b[0] - diff[0] * multiplier, antenna_b[1] - diff[1] * multiplier])

        # If the current coord is in the map, add it to the list. If not, start calculating other direction
        if is_coord_in_map(current_coord, antenna_map):
            calculated_antinodes.append(current_coord)

            if multiplier >= 0:
                multiplier = multiplier + 1
            else:
                multiplier = multiplier - 1
        else:
            if multiplier > 0:
                multiplier = -1
            else:
                break

    return calculated_antinodes

    # return ([antenna_b[0] - diff[0], antenna_b[1] - diff[1]]), ([antenna_a[0] + diff[0], antenna_a[1] + diff[1]])


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
