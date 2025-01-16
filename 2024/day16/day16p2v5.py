def main():
    """
    Entry point for day 16, part 2


    632 - too low
    665 - too low
    689 - too high

    669 - wrong
    680 - wrong

    :return: Exit status
    """
    maze, start_tile, end_tile = read_input('input_ex.txt')
    starting_direction = 1

    shortest_path, path_score = a_star_search(maze, start_tile, end_tile, starting_direction)

    m_copy = dict(maze)

    for node in shortest_path:
        m_copy[node[0]] = '$'

    print_map(m_copy)
    print('Path Score: ' + str(path_score))

    for i, node in enumerate(shortest_path):
        shortest_path[i] = (node[0], node[1], path_score - node[1])

    shortest_path.reverse()

    # Find other paths from intersections that have same path score
    alt_paths = check_intersections(maze, shortest_path, end_tile, path_score)

    # Get unique nodes from all path lists
    path_nodes = []
    for node in shortest_path:
        path_nodes.append(node[0])
    for alt_path in alt_paths:
        for node in alt_path:
            path_nodes.append(node[0])
    path_nodes = list(set(path_nodes))

    for node in path_nodes:
        maze[node] = '$'

    print_map(maze)

    print('Total shortest path nodes: ' + str(len(path_nodes)))


def check_intersections(maze, path, end_tile, shortest_path_length):
    alt_paths = []

    # Create dictionary of [coordinate -> distance] to goal
    path_nodes = dict()
    for node in path:
        path_nodes[node[0]] = node[2]

    # Check each intersection for valid moves that aren't in the path. A* from them.
    for key, node in enumerate(path):

        current_direction = 1

        if key != 0:
            parent = path[key - 1]
            if parent[0] == (node[0][0] - 1, node[0][1]):
                current_direction = 2
            elif parent[0] == (node[0][0], node[0][1] + 1):
                current_direction = 3
            elif parent[0] == (node[0][0] + 1, node[0][1]):
                current_direction = 0
            elif parent[0] == (node[0][0], node[0][1] - 1):
                current_direction = 1
            else:
                current_direction = -1

        node_pos = node[0]
        up_node = (node_pos[0] - 1, node_pos[1])
        down_node = (node_pos[0] + 1, node_pos[1])
        left_node = (node_pos[0], node_pos[1] - 1)
        right_node = (node_pos[0], node_pos[1] + 1)

        successors = [up_node, right_node, down_node, left_node]

        # Find the length of neighbor in path
        n_length = float('inf')
        for successor in successors:
            if successor in path_nodes and path_nodes[successor] < n_length:
                n_length = path_nodes[successor]

        for node_direction, successor in enumerate(successors):
            # Check move in bounds
            if successor not in maze:
                continue

            # Check for valid move
            if maze[successor] == '#':
                continue

            # Skip intersections nodes that are already in the path. We want to find new paths.
            if successor in path_nodes:
                continue

            alt_path, alt_path_length = a_star_search(maze, successor, end_tile, node_direction,
                                                      node[1] + 1 + calculate_turns(current_direction, node_direction))
            # alt_path, alt_path_length = a_star_search(maze, successor, end_tile, node_direction, node[1])
            test = 0

            if alt_path[0][1] == shortest_path_length:
                alt_paths.append(alt_path)

    return alt_paths


def a_star_search(maze, start_tile, end_tile, starting_direction, partial_path_starting_score=0):
    open_list = [{'pos': start_tile, 'char': maze[start_tile], 'f': 0, 'g': 0, 'parent': None}]
    closed_list = []

    current_direction = starting_direction

    while open_list:
        # Find lowest 'f' value
        lowest_idx = 0
        min_f = open_list[0]['f']
        for i, node in enumerate(open_list):
            if node['f'] < min_f:
                min_f = node['f']
                lowest_idx = i

        q = open_list.pop(lowest_idx)
        pos = q['pos']
        up_node = {'pos': (pos[0] - 1, pos[1]), 'parent': q}
        down_node = {'pos': (pos[0] + 1, pos[1]), 'parent': q}
        left_node = {'pos': (pos[0], pos[1] - 1), 'parent': q}
        right_node = {'pos': (pos[0], pos[1] + 1), 'parent': q}

        successors = [up_node, right_node, down_node, left_node]

        if 'direction' in q:
            current_direction = q['direction']

        # Loop through successors
        for node_direction, successor in enumerate(successors):
            # Check move in bounds
            if successor['pos'] not in maze:
                continue

            # Check for valid move
            if maze[successor['pos']] == '#':
                continue

            # Check for goal node
            if maze[successor['pos']] == 'E':
                # print('goal found')
                path = []

                successor['g'] = q['g'] + 1 + calculate_turns(current_direction, node_direction)

                node = successor
                path_score = node['g']

                while node['parent'] is not None:
                    if 'g' not in node:
                        val = 0
                    else:
                        val = node['g']

                    path.append((node['pos'], val + partial_path_starting_score))
                    node = node['parent']

                    if 'parent' not in node:
                        break

                path.append((node['pos'], 1))

                return path, path_score

            # Calculate successor g, h, and f values
            pre_turn_correction = 0

            pre_node = (-1, -1)

            if node_direction == 0:
                pre_node = (successor['pos'][0] - 1, successor['pos'][1])
            if node_direction == 1:
                pre_node = (successor['pos'][0], successor['pos'][1] + 1)
            if node_direction == 2:
                pre_node = (successor['pos'][0] + 1, successor['pos'][1])
            if node_direction == 3:
                pre_node = (successor['pos'][0], successor['pos'][1] - 1)

            if maze[pre_node] == '#':
                pre_turn_correction = 1000


            # successor['g'] = q['g'] + 1 + calculate_turns(current_direction, node_direction)
            successor['g'] = q['g'] + 1 + pre_turn_correction
            successor['h'] = calculate_heuristic(successor['pos'], end_tile)
            successor['f'] = successor['g'] + successor['h']

            successor['direction'] = node_direction

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

    return [], -1


def calculate_turns(current_direction, node_direction):
    if current_direction == node_direction:
        return 0

    if abs(current_direction - node_direction) == 1:
        return 1000

    if (current_direction == 3 and node_direction == 0) or (current_direction == 0 and node_direction == 3):
        return 1000

    return 2000


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
