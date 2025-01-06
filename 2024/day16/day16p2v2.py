def main():
    """
    Entry point for day 16, part 2

    :return: Exit status
    """
    maze, start_tile, end_tile = read_input('input_ex.txt')
    path = dijkstra_search(maze, start_tile, end_tile)

    for node in path:
        maze[node[0]] = '$'

    print_map(maze)

    print('Path Score: ' + str(path[0][1]))


def dijkstra_search(maze, start_tile, end_tile):
    start_node = {'pos': start_tile, 'distance': 0}
    visited = []
    queue = [start_node]

    while queue:
        node = queue.pop(0)

        if node['pos'] in visited:
            continue

        visited.append(node['pos'])

        pos = node['pos']
        up_node = {'pos': (pos[0] - 1, pos[1]),
                   'distance': node['distance'] + calculate_distance(pos, (pos[0] - 1, pos[1]))}
        down_node = {'pos': (pos[0] + 1, pos[1]),
                     'distance': node['distance'] + calculate_distance(pos, (pos[0] + 1, pos[1]))}
        left_node = {'pos': (pos[0], pos[1] - 1),
                     'distance': node['distance'] + calculate_distance(pos, (pos[0], pos[1] - 1))}
        right_node = {'pos': (pos[0], pos[1] + 1),
                      'distance': node['distance'] + calculate_distance(pos, (pos[0], pos[1] + 1))}

        successors = [up_node, down_node, left_node, right_node]

        for successor in successors:
            if successor['distance'] <

                queue.append(successor)

    return []


def calculate_distance(node, parent):
    """
    Calculate the existing distance between current node and the parent node

    :param calc_type:
    :param node: Current location
    :param parent: Previous node
    :return: Distance between current location and
    """
    if parent['parents']:
        grand = parent['parents'][-1]
    else:
        grand = None
    parent_pos = parent['pos']

    if grand is None:
        original_direction = 1
    elif parent_pos == (grand[0] - 1, grand[1]):
        original_direction = 0
    elif parent_pos == (grand[0], grand[1] + 1):
        original_direction = 1
    elif parent_pos == (grand[0] + 1, grand[1]):
        original_direction = 2
    elif parent_pos == (grand[0], grand[1] - 1):
        original_direction = 3
    else:
        original_direction = -1

    current_pos = node['pos']
    if parent is None:
        current_direction = 1
    elif current_pos == (parent_pos[0] - 1, parent_pos[1]):
        current_direction = 0
    elif current_pos == (parent_pos[0], parent_pos[1] + 1):
        current_direction = 1
    elif current_pos == (parent_pos[0] + 1, parent_pos[1]):
        current_direction = 2
    elif current_pos == (parent_pos[0], parent_pos[1] - 1):
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
