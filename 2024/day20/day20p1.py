def main():
    """
    Entry point for day 20, part 1

    1028 - too low
    1362 - too high

    1343 - correct
    :return: Exit status
    """
    track, start_tile, end_tile = read_input('input.txt')

    path, shortest_pico_seconds = a_star_search(track, start_tile, end_tile)
    shortcuts = find_shortcuts(track, path)
    test = 0

    for node in shortcuts:
        track[node[0]] = '1'
        track[node[1]] = '2'

    print_map(track)
    print('Number of shortcuts: ' + str(len(shortcuts)))
    print(shortcuts)

def find_shortcuts(track, path):
    """
    Finds the shortcuts based on the given track and list of (path nodes, score) in the shortest path
    :param track: Track to navigate
    :param path: List of tuples of (path node coordinates, distance to goal)
    :return: List of cheat coordinate start/end points
    """

    time_save = 100

    path.reverse()

    shortcuts = []
    for node in path:
        node_pos = node[0]
        node_dis = node[1]
        # Find possible cheat successors

        up_cheat_node = (node_pos[0] - 2, node_pos[1])
        right_cheat_node = (node_pos[0], node_pos[1] + 2)
        down_cheat_node = (node_pos[0] + 2, node_pos[1])
        left_cheat_node = (node_pos[0], node_pos[1] - 2)

        cheat_successors = [up_cheat_node, right_cheat_node, down_cheat_node, left_cheat_node]

        for successor in cheat_successors:
            # Ensure cheat is in track
            if successor not in track:
                continue

            # Ensure cheat is not wall
            if track[successor] not in ['S', 'E', '.']:
                continue

            for path_node in path:

                if successor == path_node[0] and ((path_node[1] - node_dis) - 2 >= time_save):
                    shortcuts.append((node_pos, successor))
                    break

    return shortcuts


def a_star_search(track, start_tile, end_tile):
    """
    Use A* to find the shortest path through track

    :param track: Track layout in a dictionary
    :param start_tile: Starting location
    :param end_tile: Ending location
    :return: List of the shortest path nodes
    """
    open_list = [{'pos': start_tile, 'char': track[start_tile], 'f': 0, 'g': 0, 'parent': None, }]
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
            if successor['pos'] not in track:
                continue

            # Check for valid move
            if track[successor['pos']] == '#':
                continue

            # Check for goal node
            if track[successor['pos']] == 'E':
                path = []

                successor['g'] = q['g'] + 1

                node = successor

                while node['parent'] is not None:
                    if 'g' not in node:
                        val = 0
                    else:
                        val = node['g']

                    path.append((node['pos'], val))
                    node = node['parent']

                path.append((node['pos'], node['g']))

                return path, len(path)

            # Calculate successor g, h, and f values
            successor['g'] = q['g'] + 1
            successor['h'] = calculate_heuristic(successor['pos'], end_tile)
            successor['f'] = successor['g'] + successor['h']

            better = False
            for node in open_list:
                if node['pos'] == successor['pos'] and node['f'] < successor['f']:
                    better = True

            for node in closed_list:
                if node['pos'] == successor['pos'] and node['f'] < successor['f']:
                    better = True

            if better:
                continue

            open_list.append(successor)

        closed_list.append(q)

    return []


def calculate_heuristic(node, end_tile):
    """
    Calculate A* heuristic as Manhattan distance

    :param node: Current node location
    :param end_tile: End tile location
    :return: Manhattan distance between the two nodes
    """

    return abs(node[0] - end_tile[0]) + abs(node[1] - end_tile[1])


def convert_map_to_array(track):
    """
    Converts floor map dictionary into an 2D array for visualization purposes
    :param track: Floor dictionary
    :return: 2D array dictionary conversion
    """

    conv_list = []
    row = []
    current_row = 0
    for key, value in track.items():

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


def print_map(track):
    """
    Prints the floor map dictionary in an easy to read and debug format
    :param track: Floor map to print
    :return: None
    """
    current_line = 0
    for key, value in track.items():
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

    track = {}

    with open(filename, 'r') as file:
        for r, line in enumerate(file):
            line = line.strip()

            for c, char in enumerate(line):
                track[(r, c)] = char

                if char == 'S':
                    start_tile = (r, c)

                if char == 'E':
                    end_tile = (r, c)

    return track, start_tile, end_tile


if __name__ == "__main__":
    main()
