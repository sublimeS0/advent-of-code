def main():
    """
    Entry point for Day 5, Part 2

    :return: Exit code
    """

    floor_map = read_input("input.txt")

    print(floor_map)
    guard_location, direction = find_guard(floor_map)

    moves = []
    while 0 <= guard_location[0] < len(floor_map) - 1 and 0 <= guard_location[1] < len(floor_map[0]):
        if direction == 0:  # Moving up
            if is_valid_move(guard_location, direction, floor_map):

                if guard_location not in moves:
                    moves.append(guard_location)

                guard_location, floor_map = move_up(floor_map, guard_location)
            else:
                direction = 1

        elif direction == 1:  # Moving right
            if is_valid_move(guard_location, direction, floor_map):

                if guard_location not in moves:
                    moves.append(guard_location)

                guard_location, floor_map = move_right(floor_map, guard_location)
            else:
                direction = 2

        elif direction == 2:  # Moving down
            if is_valid_move(guard_location, direction, floor_map):

                if guard_location not in moves:
                    moves.append(guard_location)

                guard_location, floor_map = move_down(floor_map, guard_location)
            else:
                direction = 3

        elif direction == 3:  # Moving left
            if is_valid_move(guard_location, direction, floor_map):

                if guard_location not in moves:
                    moves.append(guard_location)

                guard_location, floor_map = move_left(floor_map, guard_location)
            else:
                direction = 0

        # pretty_print(floor_map)

    print(len(moves) + 1)


def is_valid_move(guard_location, direction, floor_map):
    if direction == 0:  # Moving up
        return guard_location[0] >= 0 and floor_map[guard_location[0] - 1][guard_location[1]] != '#'

    elif direction == 1:  # Moving right
        return guard_location[1] < len(floor_map) and floor_map[guard_location[0]][guard_location[1] + 1] != '#'

    elif direction == 2:  # Moving down
        return guard_location[0] < len(floor_map) and floor_map[guard_location[0] + 1][guard_location[1]] != '#'

    elif direction == 3:  # Moving left
        return guard_location[1] >= 0 and floor_map[guard_location[0]][guard_location[1] - 1] != '#'


def move_up(floor_map, guard_location):
    if guard_location[0] > 0:
        floor_map[guard_location[0]][guard_location[1]] = '.'
        floor_map[guard_location[0] - 1][guard_location[1]] = '^'

    return [guard_location[0] - 1, guard_location[1]], floor_map


def move_right(floor_map, guard_location):
    if guard_location[1] < len(floor_map[guard_location[1]]) - 1:
        floor_map[guard_location[0]][guard_location[1]] = '.'
        floor_map[guard_location[0]][guard_location[1] + 1] = '>'

    return [guard_location[0], guard_location[1] + 1], floor_map


def move_down(floor_map, guard_location):
    if guard_location[0] < len(floor_map) - 1:
        floor_map[guard_location[0]][guard_location[1]] = '.'
        floor_map[guard_location[0] + 1][guard_location[1]] = 'v'

    return [guard_location[0] + 1, guard_location[1]], floor_map


def move_left(floor_map, guard_location):
    if guard_location[1] > 0:
        floor_map[guard_location[0]][guard_location[1]] = '.'
        floor_map[guard_location[0]][guard_location[1] - 1] = '<'

    return [guard_location[0], guard_location[1] - 1], floor_map


def find_guard(floor_map):
    """
    Find guard given a floor map.

    Direction:
    ^ - 0
    > - 1
    v - 2
    < - 3

    :param floor_map: Map of current floor with a guard
    :return:
    """
    # Find the guard's current location
    guard_location = [-1, -1]
    direction = -1
    for r in range(len(floor_map)):
        for c in range(len(floor_map[r])):
            current = floor_map[r][c]

            if current == "^":
                guard_location = [r, c]
                direction = 0

            if current == ">":
                guard_location = [r, c]
                direction = 1

            if current == "v":
                guard_location = [r, c]
                direction = 2

            if current == "<":
                guard_location = [r, c]
                direction = 3

    return guard_location, direction


def pretty_print(floor_map):
    """
    Prints a formatted version of the map (for visualization purposes)
    :param floor_map: Map to be printed
    :return: None
    """
    for r in range(len(floor_map)):
        for c in range(len(floor_map[r])):
            print(floor_map[r][c], end='')
        print('')
    print('')


def read_input(filename):
    """
    Read input file into lists.

    :param filename: Name of file to read
    :return:
    """
    with open(filename) as file:
        lab_map = [list(line.strip()) for line in file]

    return lab_map


if __name__ == "__main__":
    main()
