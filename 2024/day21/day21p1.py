import math


def main():
    """
    Entry point for day 21, part 1

    166228 - ???
    166056 - too high
    170248 - too high

    :return: Exit status
    """

    # Get codes
    codes = read_input('input.txt')

    # Get keypads
    numeric_keypad, numeric_keypad_start = get_numeric_keypad_info()
    directional_keypad, directional_keypad_start = get_directional_keypad_info()

    complexity_sum = 0
    for code in codes:
        print(code + ': ', end='')
        numeric_keypad_inputs = [key[1] for key in get_numeric_keypad_code(numeric_keypad, numeric_keypad_start, code)]
        print(''.join(numeric_keypad_inputs))

        directional_keypad_inputs = [key[1] for key in
                                     get_directional_keypad_code(directional_keypad, directional_keypad_start,
                                                                 numeric_keypad_inputs)]
        print(''.join(directional_keypad_inputs))

        directional_keypad_inputs_2 = [key[1] for key in
                                       get_directional_keypad_code(directional_keypad, directional_keypad_start,
                                                                   directional_keypad_inputs)]
        print(''.join(directional_keypad_inputs_2))

        print(code + ': ' + str(len(directional_keypad_inputs_2)) + ' - ' + str(int(code[:-1])))

        complexity_sum += calculate_complexity(code, directional_keypad_inputs_2)

    print('Complexity Sum: ' + str(complexity_sum))


def calculate_complexity(code, inputs):
    return len(inputs) * int(code[:-1])


def get_directional_keypad_code(directional_keypad, directional_keypad_start, code):
    current_location = directional_keypad_start

    path = []
    for key in code:
        p = a_star_search(directional_keypad, directional_keypad[current_location], directional_keypad[key])
        path.extend(p)
        current_location = key

    return path


def get_numeric_keypad_code(numeric_keypad, numeric_keypad_start, code):
    """
    Produces the string code based off the keypad layout, starting location, and code
    :param numeric_keypad:
    :param numeric_keypad_start:
    :param code:
    :return:
    """

    current_location = numeric_keypad_start

    path = []
    for key in list(code):
        path.extend(a_star_search(numeric_keypad, numeric_keypad[current_location], numeric_keypad[key]))
        current_location = key

    return path


def get_directional_keypad_info():
    directional_keypad = {
        '^': (0, 1),
        'A': (0, 2),
        '<': (1, 0),
        'v': (1, 1),
        '>': (1, 2),
    }
    directional_keypad_start = 'A'

    return directional_keypad, directional_keypad_start


def get_numeric_keypad_info():
    """
    Provides data for the number keypad

    :return: Dictionary of coordinates/values of the numeric keypad
    """
    numeric_keypad = {
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '0': (3, 1),
        'A': (3, 2),
    }
    numeric_keypad_start = 'A'  # Robot starts looking at 'A' square

    return numeric_keypad, numeric_keypad_start


def a_star_search(keypad, start_tile, end_tile):
    """
    Use A* to find the shortest path through track

    :param keypad: Track layout in a dictionary
    :param start_tile: Starting location
    :param end_tile: Ending location
    :return: List of the shortest path nodes
    """

    if start_tile == end_tile:
        return [(start_tile, 'A')]

    open_list = [{'pos': start_tile, 'f': 0, 'g': 0, 'parent': None, }]
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
        up_node = {'pos': (pos[0] - 1, pos[1]), 'parent': q, 'move': '^'}
        down_node = {'pos': (pos[0] + 1, pos[1]), 'parent': q, 'move': 'v'}
        left_node = {'pos': (pos[0], pos[1] - 1), 'parent': q, 'move': '<'}
        right_node = {'pos': (pos[0], pos[1] + 1), 'parent': q, 'move': '>'}

        # successors = [left_node, right_node, down_node, up_node]
        # successors = [down_node, right_node, left_node, up_node]
        successors = [right_node, up_node, down_node, left_node]

        # Loop through successors
        for successor in successors:
            # Check move in bounds
            if successor['pos'] not in keypad.values():
                continue

            # Check for goal node
            if successor['pos'] == end_tile:
                path = []

                successor['g'] = q['g'] + 1

                node = successor

                while node['parent'] is not None:
                    # path.append((node['pos'], node['move']))
                    path.insert(0, (node['pos'], node['move']))
                    node = node['parent']

                # path.insert(0, (node['pos'], 'A'))
                path.append((node['pos'], 'A'))
                # path.reverse()

                return path

            # Calculate successor g, h, and f values
            diff = 0
            if 'move' in q and q['move'] == successor['move']:
                diff = -1

            successor['g'] = q['g'] + 1 + diff
            successor['h'] = calculate_heuristic(successor['pos'], end_tile)
            successor['f'] = successor['g'] + successor['h']

            if successor['move'] in ['<']:
                successor['f'] -= 1

            if 'move' in q and q['move'] == successor['move']:
                successor['f'] -= 1
                successor['double'] = True

            t_node = successor['parent']
            while t_node is not None:
                if 'double' in t_node:
                    successor['f'] -= 1
                t_node = t_node['parent']

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
    # return math.sqrt((abs(node[0] - end_tile[0])) ** 2 + (abs(node[1] - end_tile[1])) ** 2)
    # return -1 * max(abs(node[0] - end_tile[0]), abs(node[1] - end_tile[1]))


def read_input(filename):
    """
    Reads input file into a list of door codes
    :param filename: Name of input file
    :return: List of codes
    """
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    main()
