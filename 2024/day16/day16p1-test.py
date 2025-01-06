def main():
    """
    Entry point for day 16, part 1

    :return: Exit status
    """
    maze, start_tile, end_tile = read_input('input_ex.txt')
    path = a_star_search(maze, start_tile, end_tile)

    for node in path:
        maze[node[0]] = '$'

    print_map(maze)

    print('Path Score: ' + str(path[0][1]))


def a_star_search(maze, start_tile, end_tile, branch_parent=None):
    """
    Use A* to find the shortest path through maze

    :param maze: Maze layout in a dictionary
    :param start_tile: Starting location
    :param end_tile: Ending location
    :return: List of the shortest path nodes
    """
    open_list = [{'pos': (10, 1), 'char': maze[start_tile], 'f': 0, 'g': 0, 'parent': None, }]
    closed_list = []

    # Loop through open list
    while open_list:

        # Find lowest 'f' value
        lowest_idx = 0
        min_f = open_list[0]['f']
        for i, node in enumerate(open_list):
            if node['f'] < min_f:
                min_f = node['f']
                lowest_idx = i

        # Generate current node successors
        q = open_list.pop(lowest_idx)
        pos = q['pos']
        up_node = {'pos': (pos[0] - 1, pos[1]), 'parent': q}
        down_node = {'pos': (pos[0] + 1, pos[1]), 'parent': q}
        left_node = {'pos': (pos[0], pos[1] - 1), 'parent': q}
        right_node = {'pos': (pos[0], pos[1] + 1), 'parent': q}

        successors = [up_node, down_node, left_node, right_node]

        # Loop through successors
        for successor in successors:
            # Check move in bounds
            if successor['pos'] not in maze:
                continue

            # Check for valid move
            if maze[successor['pos']] == '#':
                continue

            # Check for goal node
            if maze[successor['pos']] == 'E':
                path = []

                successor['g'] = q['g'] + calculate_distance(successor, q, branch_parent)

                node = successor

                while node['parent'] is not None:
                    if 'g' not in node:
                        val = 0
                    else:
                        val = node['g']

                    path.append((node['pos'], val))
                    node = node['parent']

                path.append((node['pos'], node['g']))

                return path

            # Calculate successor g, h, and f values
            successor['g'] = q['g'] + calculate_distance(successor, q, branch_parent)
            successor['h'] = calculate_heuristic(successor['pos'], end_tile)
            successor['f'] = successor['g'] + successor['h']

            better_open = False
            for node in open_list:
                if node['pos'] == successor['pos'] and node['f'] < successor['f']:
                    better_open = True

            better_closed = False
            for node in closed_list:
                if node['pos'] == successor['pos'] and node['f'] < successor['f']:
                    better_open = True

            if better_open or better_closed:
                continue

            open_list.append(successor)

        closed_list.append(q)


def calculate_distance(node, parent, branch_parent=None):
    """
    Calculate the existing distance between current node and the parent node

    :param node: Current location
    :param parent: Previous node
    :return: Distance between current location and
    """

    if branch_parent is not None:
        grand = dict()
        grand['pos'] = branch_parent
    else:
        grand = parent['parent']
    parent_pos = parent['pos']

    if grand is None:
        original_direction = 1
    elif parent_pos == (grand['pos'][0] - 1, grand['pos'][1]):
        original_direction = 0
    elif parent_pos == (grand['pos'][0], grand['pos'][1] + 1):
        original_direction = 1
    elif parent_pos == (grand['pos'][0] + 1, grand['pos'][1]):
        original_direction = 2
    elif parent_pos == (grand['pos'][0], grand['pos'][1] - 1):
        original_direction = 3
    else:
        original_direction = -1

    current_pos = node['pos']
    if parent is None:
        current_direction = 1
    elif current_pos == (parent['pos'][0] - 1, parent['pos'][1]):
        current_direction = 0
    elif current_pos == (parent['pos'][0], parent['pos'][1] + 1):
        current_direction = 1
    elif current_pos == (parent['pos'][0] + 1, parent['pos'][1]):
        current_direction = 2
    elif current_pos == (parent['pos'][0], parent['pos'][1] - 1):
        current_direction = 3
    else:
        current_direction = -1

    if current_direction != original_direction:
        return 1001
    else:
        return 1


def calculate_heuristic(node, end_tile):
    """
    Calculate A* heuristic as Manhattan distance

    :param node: Current node location
    :param end_tile: End tile location
    :return: Manhattan distance between the two nodes
    """

    return abs(node[0] - end_tile[0]) + abs(node[1] - end_tile[1])


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
    Read input file into dictionary
    :param filename: Input file to read
    :return: Dictionary with tuple coordinate keys and character values
    """
    start_tile = (-1, -1)
    end_tile = (-1, -1)

    maze = {}

    with open(filename, 'r') as file:
        for r, line in enumerate(file):
            line = line.strip()

            for c, char in enumerate(line):
                maze[(r, c)] = char

                if char == 'S':
                    start_tile = (r, c)

                if char == 'E':
                    end_tile = (r, c)

    return maze, start_tile, end_tile


if __name__ == "__main__":
    main()
