def main():
    floor_map = read_input('input.txt')
    starting_guard_location, starting_direction = find_guard(floor_map)

    loops_found = 0
    for r in range(len(floor_map)):
        for c in range(len(floor_map[r])):

            # Skip the starting location and existing obstacles
            if floor_map[r][c] in ['^', '#']:
                continue

            floor_map[r][c] = '0'

            visited_locations = []
            guard_location = starting_guard_location
            direction = starting_direction

            # Simulate guard's movements with new obstacle
            while 0 < guard_location[0] < len(floor_map) - 1 and 0 < guard_location[1] < len(floor_map[r]) - 1:

                # If we have already been on this square/direction, loop detected. Break.
                if [guard_location, direction] in visited_locations:
                    # Loop detected
                    loops_found = loops_found + 1
                    break

                # Record current location/direction
                visited_locations.append([guard_location, direction])

                # Make next move
                try:
                    guard_location, direction, floor_map = move_guard(guard_location, direction, floor_map)
                except IndexError:
                    break

            # Reset simulation
            floor_map[guard_location[0]][guard_location[1]] = '.'
            floor_map[r][c] = '.'
            floor_map[starting_guard_location[0]][starting_guard_location[1]] = '^'

    pretty_print(floor_map)
    print('Loops found: ' + str(loops_found))


def move_guard(guard_location, direction, floor_map):
    if direction == 0:
        if floor_map[guard_location[0] - 1][guard_location[1]] not in ['#', '0']:
            # Move guard
            floor_map[guard_location[0]][guard_location[1]] = "."
            floor_map[guard_location[0] - 1][guard_location[1]] = "^"

            return [guard_location[0] - 1, guard_location[1]], direction, floor_map
        else:
            # Rotate guard
            direction = 1
            floor_map[guard_location[0]][guard_location[1]] = ">"

            return [guard_location[0], guard_location[1]], direction, floor_map

    elif direction == 1:
        if floor_map[guard_location[0]][guard_location[1] + 1] not in ['#', '0']:
            # Move guard
            floor_map[guard_location[0]][guard_location[1]] = "."
            floor_map[guard_location[0]][guard_location[1] + 1] = ">"

            return [guard_location[0], guard_location[1] + 1], direction, floor_map
        else:
            # Rotate guard
            direction = 2
            floor_map[guard_location[0]][guard_location[1]] = "v"

            return [guard_location[0], guard_location[1]], direction, floor_map

    elif direction == 2:
        if floor_map[guard_location[0] + 1][guard_location[1]] not in ['#', '0']:
            # Move guard
            floor_map[guard_location[0]][guard_location[1]] = "."
            floor_map[guard_location[0] + 1][guard_location[1]] = "v"

            return [guard_location[0] + 1, guard_location[1]], direction, floor_map
        else:
            # Rotate guard
            direction = 3
            floor_map[guard_location[0]][guard_location[1]] = "<"

            return [guard_location[0], guard_location[1]], direction, floor_map

    elif direction == 3:
        if floor_map[guard_location[0]][guard_location[1] - 1] not in ['#', '0']:
            # Move guard
            floor_map[guard_location[0]][guard_location[1]] = "."
            floor_map[guard_location[0]][guard_location[1] - 1] = "<"

            return [guard_location[0], guard_location[1] - 1], direction, floor_map
        else:
            # Rotate guard
            direction = 0
            floor_map[guard_location[0]][guard_location[1]] = "^"

            return [guard_location[0], guard_location[1]], direction, floor_map

    return guard_location, direction, floor_map


def find_guard(floor_map):
    for r in range(len(floor_map)):
        for c in range(len(floor_map[r])):

            current = floor_map[r][c]

            if current == "^":
                return [[r, c], 0]

            if current == ">":
                return [[r, c], 1]

            if current == "v":
                return [[r, c], 2]

            if current == "<":
                return [[r, c], 3]

    return -1


def read_input(filename):
    """
    Read input file into lists.

    :param filename: Name of file to read
    :return:
    """
    with open(filename) as file:
        lab_map = [list(line.strip()) for line in file]

    return lab_map


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


if __name__ == "__main__":
    main()
