import math


def main():
    """
    Entry point for Day 8, Part 2

    356799792 - too low
    2573952864 - correct
    9859012086
    3788348240 - peter correct

    13443849


    :return: Exit code
    """
    # Setup
    boxes = read_input('peter_input.txt')

    # Collect node distance information - gives us a list of "unconnected" nodes
    unconnected = find_distances(boxes)
    num_nodes = len(unconnected)
    circuit = {}

    # Algorithm allows for two nodes to point to each other, resolve at the end
    cycled_nodes = []
    distances = unconnected.copy()

    while len(circuit) < num_nodes - 1:
        unconnected_node = unconnected.popitem()
        shortest_connection = next(iter(unconnected_node[1]))
        circuit[(unconnected_node[0], shortest_connection)] = unconnected_node[1][shortest_connection]

        if (shortest_connection, unconnected_node[0]) in circuit:
            cycled_nodes.append((unconnected_node[0], shortest_connection))

    # Resolve unconnected cycles
    resolve_cycles(cycled_nodes, distances, circuit)

    last_connection = max(circuit, key=circuit.get)
    print('Coord product: ' + str(boxes[last_connection[0]]['x'] * boxes[last_connection[1]]['x']))


def resolve_cycles(cycles, distances, circuit):
    for cycle in cycles:
        distances[cycle[0]].pop(cycle[1])
        distances[cycle[1]].pop(cycle[0])

        cycle_node_0_next = next(iter(distances[cycle[0]]))
        cycle_node_1_next = next(iter(distances[cycle[1]]))

        bad_cycle, new_cycle = (cycle, (cycle[0], cycle_node_0_next)) if (cycle_node_0_next < cycle_node_1_next) else (tuple(reversed(cycle)), (cycle[1], cycle_node_1_next))
        circuit.pop(bad_cycle)

        circuit[new_cycle] = distances[bad_cycle[0]][new_cycle[1]]
        pass


def find_distances(boxes):
    """
    Find all the distances between boxes. Create a dictionary of dictionaries where they key of the outer dict is a
    node, and it's value is a dict where they key is a different node and the value is the distance between nodes.

    Brute force :( very sad

    :param boxes: Set of boxes
    :return: Dictionary of key-nodes whose values are dictionaries of distances between the key and a second node
    """
    distances = {}

    for box_a in boxes:
        inner_dict = {}
        for box_b in boxes:
            if box_a['id'] == box_b['id']:
                continue

            inner_dict[box_b['id']] = calculate_distance(box_a, box_b)

        distances[box_a['id']] = dict(sorted(inner_dict.items(), key=lambda item: item[1]))

    return distances


def calculate_distance(box_a, box_b):
    """
    Returns the Euclidean distance between two boxes
    :param box_a: First box
    :param box_b: Second box
    :return: Absolute value of the Euclidean distance between two boxes
    """

    return abs(math.sqrt(
        (box_a['x'] - box_b['x']) ** 2 +
        (box_a['y'] - box_b['y']) ** 2 +
        (box_a['z'] - box_b['z']) ** 2
    ))


def read_input(filename):
    """
    Read input file into relevant data structures
    :param filename: Name of input file
    :return: Return relevant data structures
    """
    boxes = []
    coord_names = ['x', 'y', 'z']
    with open(filename, 'r') as file:
        for l, line in enumerate(file):
            d = {key: value for key, value in zip(coord_names, map(int, line.strip().split(',')))}
            d['id'] = l
            boxes.append(d)

    return boxes


if __name__ == "__main__":
    main()
