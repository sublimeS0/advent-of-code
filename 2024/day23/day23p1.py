from collections import defaultdict


def main():
    """
    Entry point for day 23, part 1

    1437 - correct

    :return: Exit code
    """
    connections = read_input('input.txt')
    connection_graph = construct_graph(connections)

    # Find triangle cycles in graph
    g = connection_graph.graph
    connection_set = []
    for node in g:
        for neighbor in g[node]:
            for successor in g[neighbor]:
                if successor == node:
                    continue

                if node in g[successor]:
                    connection_set.append({node, neighbor, successor})

    # Remove duplicate cycles
    unique_connection_set = []
    for connection in connection_set:
        if connection not in unique_connection_set:
            unique_connection_set.append(connection)

    # Count cycles that contain a computer that starts with 't'
    t_count = 0
    for connection in unique_connection_set:
        for element in connection:
            if element.startswith('t'):
                t_count += 1
                break

    print('T computer count: ' + str(t_count))


def construct_graph(connections):
    """
    Constructs graph object from list of connections
    Graph edges are bidirectional

    :param connections: List of tuple of connections
    :return: Constructed graph object
    """
    g = Graph()

    for connection in connections:
        g.add_edge(connection[0], connection[1])

    return g


def read_input(filename):
    """
    Reads input file into data structures

    :param filename: Name of input file
    :return: List of tuples of connections
    """

    with open(filename, 'r') as file:
        return [tuple(line.strip().split('-')) for line in file]


class Graph:
    """
    Class to represent graph of connected computers
    """

    def __init__(self):
        """
        Construct graph object
        :return: None
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Adds a bidirectional edge to the graph
        :param u: First node in the connection
        :param v: Second node in the connection
        :return: None
        """
        self.graph[u].append(v)
        self.graph[v].append(u)


if __name__ == "__main__":
    main()
