import math


def main():
    """
    Entry point for Day 8, Part 1

    2940 - too low
    3744 - too low
    112230 - correct

    :return: Exit code
    """

    # Setup
    boxes = read_input('input_ex.txt')
    num_connections = 10
    n = 3  # Number of the largest circuits to multiply

    # Collect distances between boxes
    distances = find_distances(boxes)

    # Collect the n-closest boxes
    connections = []
    for i in range(num_connections):
        min_dis = min(distances, key=distances.get)
        connections.append(set(min_dis))
        distances.pop(min_dis)

    # Combine connections into circuits
    circuits = combine_connections(connections)

    # Sort the list by size, grab the n largest, and multiply their lengths
    top_n = sorted(circuits, key=len, reverse=True)[:n]
    print('Circuit Product: ' + str(math.prod([len(c) for c in top_n])))


def combine_connections(connections):
    """
    Combines a list of connections (sets) into a list of circuits (sets)
    :param connections: Input list of connection sets
    :return: Output list of circuit sets
    """

    # Maintain two lists: a "master" list and an unchecked list
    circuits = [connections.pop()]
    while connections:
        connection = connections.pop()
        overlap = False

        for i in range(len(circuits)):
            circuit = circuits[i]

            # Check for overlap (the connections should be in the same circuit)
            if connection & circuit:
                # Add the existing circuit to the connection and add the connection to the unchecked list
                connection.update(circuit)
                connections.append(connection)

                # Remove the "old" circuit
                overlap = True
                circuits.pop(i)
                break

        # Add new circuit to the master list
        if not overlap:
            circuits.append(connection)

    return circuits


def find_distances(boxes):
    """
    Find all the distances between boxes

    Brute force :( very sad

    :param boxes: Set of boxes
    :return: Dictionary with id-tuple keys and distance values
    """

    distances = {}

    for box_a in boxes:
        for box_b in boxes:
            if box_a['id'] == box_b['id']:
                continue

            key_tuple = (min(box_a['id'], box_b['id']), max(box_a['id'], box_b['id']))
            if key_tuple in distances:
                continue

            distances[key_tuple] = calculate_distance(box_a, box_b)

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
