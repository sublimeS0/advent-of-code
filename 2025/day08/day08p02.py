import math


def main():
    """
    Entry point for Day 8, Part 2

    :return: Exit code
    """

    # Setup
    boxes = read_input('input_ex.txt')

    # Collect node distance information - gives us a list of "unconnected" nodes
    unconnected = find_distances(boxes)
    connected = {0: unconnected.pop(0)}
    circuit = []

    while unconnected:
        for connected_node in connected.items():

            best_connection =

            node_added = False
            for connection in connected_node[1]:
                if connection not in connected:
                    node_added = True
                    connected[connection] = unconnected.pop(connection)
                    circuit.append({connected_node[0], connection})
                    break

            if node_added:
                break

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
