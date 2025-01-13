def main():
    """
    Entry point for day 18, part 2
    :return: Exit code
    """
    space_size, byte_sim = 71, 1024

    byte_positions = read_input('input.txt')
    space = init_space(space_size)

    # Simulate memory drops
    for i in range(byte_sim):
        coord = (byte_positions[i][1], byte_positions[i][0])

        # coord = byte_positions[i]
        space[coord] = '#'

    for i in range(byte_sim, len(byte_positions)):
        print('Step: ' + str(i))

        coord = (byte_positions[i][1], byte_positions[i][0])

        # coord = byte_positions[i]
        space[coord] = '#'

        path = a_star_search(space, (0, 0), (space_size - 1, space_size - 1))
        if not path:
            break


    print_map(space)

    print('First blocking byte: ' + str(byte_positions[i]))


def a_star_search(space, start_tile, end_tile):
    """
    Use A* to find the shortest path through maze

    :param space: Maze layout in a dictionary
    :param start_tile: Starting location
    :param end_tile: Ending location
    :return: List of the shortest path nodes
    """
    open_list = {start_tile: {'f': 0, 'g': 0, 'h': 0}}
    closed_list = {}

    while open_list:

        min_f = 999999999
        lowest_key = (-1, -1)
        for key, value in open_list.items():
            if value['f'] < min_f:
                min_f = value['f']
                lowest_key = key

        q = open_list.pop(lowest_key)
        up_node = {'pos': (lowest_key[0] - 1, lowest_key[1]), 'parent': q}
        down_node = {'pos': (lowest_key[0] + 1, lowest_key[1]), 'parent': q}
        left_node = {'pos': (lowest_key[0], lowest_key[1] - 1), 'parent': q}
        right_node = {'pos': (lowest_key[0], lowest_key[1] + 1), 'parent': q}

        successors = [up_node, down_node, left_node, right_node]

        for successor in successors:

            if successor['pos'] not in space:
                continue

            if space[successor['pos']] == '#':
                continue

            if successor['pos'] == end_tile:
                # print('goal found')
                path = []
                t = successor

                while 'parent' in t:
                    path.append(t['pos'])
                    t = t['parent']

                return path

            successor['g'] = q['g'] + 1
            successor['h'] = calculate_heuristic(lowest_key, end_tile)
            successor['f'] = successor['g'] + successor['h']

            better_open = False
            if lowest_key in open_list and open_list[lowest_key]['f'] < successor['f']:
                better_open = True

            better_closed = False
            if lowest_key in closed_list and closed_list[lowest_key]['f'] < successor['f']:
                better_closed = True

            if better_open or better_closed:
                continue

            open_list[successor['pos']] = successor

        closed_list[lowest_key] = q

    return []


def calculate_heuristic(node, end_tile):
    """
    Calculate A* heuristic as Manhattan distance

    :param node: Current node location
    :param end_tile: End tile location
    :return: Manhattan distance between the two nodes
    """

    return abs(node[0] - end_tile[0]) + abs(node[1] - end_tile[1])


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
    Reads input file into list of tuples
    :param filename: Name of input file to read
    :return: List of coordinate tuples
    """
    byte_positions = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            byte_positions.append((int(line[0:line.index(',')]), int(line[line.index(',') + 1:])))

    return byte_positions


def init_space(size):
    """
    Initializes memory space as square dictionary
    :param size: Height and width of dictionary
    :return: [size x size] dictionary initialized with '.'s
    """
    space = {}

    for r in range(size):
        for c in range(size):
            space[(r, c)] = '.'

    return space


if __name__ == "__main__":
    main()
