def main():
    """
    Entry point for day 15, part 2

    1448573 - too high
    1448458 - correct

    :return: Exit code
    """

    floor_map, instructions, pos = read_input('input.txt')

    print_map(floor_map)

    # Parse instructions to move robot
    i = 0
    for inst in instructions:
        convert_map_to_array(floor_map)
        pos, floor_map = move_robot(pos, inst, floor_map)
        # print(inst + ' ' + str(i))
        i += 1
        # print_map(floor_map)
        # print()

    # Calculate box GPS sum
    # TODO: Rework scoring mechanism
    gps_score = 0
    for key, value in floor_map.items():
        if value in ['[']:
            gps_score = gps_score + (key[0] * 100 + key[1])

    print_map(floor_map)
    print('GPS Score: ' + str(gps_score))


def move_robot(pos, inst, floor_map):
    """
    Move the robot according to the provided instruction
    :param pos: Current robot position
    :param inst: Instruction to execute
    :param floor_map: Floor map of obstacles
    :return: Updated position and floor map
    """
    # Get the destination position
    if inst == '^':
        new_pos = (pos[0] - 1, pos[1])
    elif inst == '>':
        new_pos = (pos[0], pos[1] + 1)
    elif inst == 'v':
        new_pos = (pos[0] + 1, pos[1])
    else:  # inst == '<'
        new_pos = (pos[0], pos[1] - 1)

    # Check if new position is valid
    if new_pos not in floor_map:
        return pos, floor_map

    char = floor_map[new_pos]

    if char in ['[', ']']:
        # Box, try to push the boxes

        if can_shift(new_pos, inst, floor_map):
            floor_map = shift_boxes(new_pos, inst, floor_map, True)
            char = floor_map[new_pos]

    if char == '.':
        # Open space, just move the robot
        floor_map[pos] = '.'
        floor_map[new_pos] = '@'

        return new_pos, floor_map

    # Wall (or out of the map), ignore instruction and do nothing
    return pos, floor_map


def can_shift(pos, inst, floor_map):
    """
    Recursively check if boxes can move, without actualy updating data
    :param pos: Position of box to move
    :param inst: Instruction (direction to move the box)
    :param floor_map: Current floor map layout
    :return: True if this box can be moved, false otherwise
    """
    # Get target position
    if inst == '^':
        new_pos = (pos[0] - 1, pos[1])
    elif inst == '>':
        new_pos = (pos[0], pos[1] + 1)
    elif inst == 'v':
        new_pos = (pos[0] + 1, pos[1])
    else:  # inst == '<'
        new_pos = (pos[0], pos[1] - 1)

    if floor_map[pos] == '.':
        return True

    if floor_map[pos] == '#':
        return False

    # Check if position is valid
    if new_pos not in floor_map:
        return False

    if floor_map[new_pos] == '#':
        return False

    # Left to right moves are trivial
    if inst in ['<', '>']:

        if floor_map[new_pos] == '.':
            return True

        return can_shift(new_pos, inst, floor_map)

    if inst in ['^', 'v']:

        if floor_map[pos] == '[':
            return can_shift(new_pos, inst, floor_map) and can_shift((new_pos[0], new_pos[1] + 1), inst, floor_map)

        if floor_map[pos] == ']':
            return can_shift(new_pos, inst, floor_map) and can_shift((new_pos[0], new_pos[1] - 1), inst, floor_map)

    return True


def shift_boxes(pos, inst, floor_map, move_neighbor=False):
    """
    Recursively move boxes if robot is pushing them
    :param move_neighbor:
    :param pos: Position of box to move
    :param inst: Instruction (direction to move the box)
    :param floor_map: Current floor map layout
    :return: Updated floor map (dictionary)
    """
    # Get target position
    if inst == '^':
        new_pos = (pos[0] - 1, pos[1])
    elif inst == '>':
        new_pos = (pos[0], pos[1] + 1)
    elif inst == 'v':
        new_pos = (pos[0] + 1, pos[1])
    else:  # inst == '<'
        new_pos = (pos[0], pos[1] - 1)

    # Left to right moves are trivial
    if inst in ['<', '>']:

        if floor_map[new_pos] in ['[', ']']:
            floor_map = shift_boxes(new_pos, inst, floor_map)

        if floor_map[pos] == '[' and floor_map[new_pos] == '.':
            floor_map[new_pos] = '['
            floor_map[pos] = '.'

        if floor_map[pos] == ']' and floor_map[new_pos] == '.':
            floor_map[new_pos] = ']'
            floor_map[pos] = '.'

    if inst in ['^', 'v']:

        if floor_map[pos] == '[':
            floor_map = shift_boxes(new_pos, inst, floor_map, True)
            floor_map[new_pos] = '['
            floor_map[pos] = '.'

            if move_neighbor:
                floor_map = shift_boxes((pos[0], pos[1] + 1), inst, floor_map, False)

        if floor_map[pos] == ']':
            floor_map = shift_boxes(new_pos, inst, floor_map, True)
            floor_map[new_pos] = ']'
            floor_map[pos] = '.'

            if move_neighbor:
                floor_map = shift_boxes((pos[0], pos[1] - 1), inst, floor_map, False)

    return floor_map


def convert_map_to_array(floor_map):
    """
    Converts floor map dictionary into an 2D array for visualization purposes
    :param floor_map: Floor dictionary
    :return: 2D array dictionary conversion
    """

    conv_list = []
    row = []
    current_row = 0
    for key, value in floor_map.items():

        if key[0] == current_row:
            if value == '.':
                row.append('_')
            else:
                row.append(value)
        else:
            current_row = current_row + 1

            conv_list.append(row[:])
            row = []

            if value == '.':
                row.append('_')
            else:
                row.append(value)

    conv_list.append(row[:])
    return conv_list


def print_map(floor_map):
    """
    Prints the floor map dictionary in an easy to read and debug format
    :param floor_map: Floor map to print
    :return: None
    """
    current_line = 0
    for key, value in floor_map.items():
        if key[0] == current_line:
            print(value, end='')
        else:
            current_line = key[0]
            print()
            print(value, end='')

    print()
    print()


def read_input(filename):
    """
    Read input file into starting data structures
    :param filename: Input file to read
    :return: Dictionary of floor map, list of instructions, starting robot position
    """

    pos = (-1, -1)
    reading_map = True

    floor_map = {}

    with open(filename, 'r') as file:
        for r, line in enumerate(file):
            if line == '\n':
                break

            line = line.strip()

            # Read the map portion of the input into a dictionary
            if reading_map:
                for c, char in enumerate(line):
                    # floor_map[(r, c)] = char

                    # Convert to ##
                    if char == '#':
                        floor_map[(r, c * 2)] = '#'
                        floor_map[(r, c * 2 + 1)] = '#'

                    # Convert to []
                    if char == 'O':
                        floor_map[(r, c * 2)] = '['
                        floor_map[(r, c * 2 + 1)] = ']'

                    # Convert to . .
                    if char == '.':
                        floor_map[(r, c * 2)] = '.'
                        floor_map[(r, c * 2 + 1)] = '.'

                    # Convert to @.
                    if char == '@':
                        pos = (r, c * 2)

                        floor_map[(r, c * 2)] = '@'
                        floor_map[(r, c * 2 + 1)] = '.'

    with open(filename, 'r') as file:
        instructions = [list(line.strip()) for line in file if "#" not in line and line != '\n']

    return floor_map, sum(instructions, []), pos


if __name__ == "__main__":
    main()
