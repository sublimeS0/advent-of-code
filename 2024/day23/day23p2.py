from collections import defaultdict


def main():
    """
    Entry point for day 23, part 2

    da,do,gx,ly,mb,ns,nt,pz,sc,si,tp,ul,vl - correct

    :return: Exit code
    """
    connections = read_input('input.txt')
    connection_graph = construct_graph(connections)

    # Find all maximal cycles
    g = connection_graph.graph
    maximal_cliques = bron_kerbosch(set(), set(g), set(), g)

    # Fine largest maximal clique in list of all maximal cliques
    largest_clique_size = 0
    largest_clique = []
    for clique in maximal_cliques:
        if len(clique) > largest_clique_size:
            largest_clique_size = len(clique)
            largest_clique = clique

    print('Largest clique size: ' + str(largest_clique_size))
    print('Largest clique: ' + str(largest_clique))
    print('Largest clique sorted: ' + str(sorted(list(largest_clique))))
    print()
    print('Password: ' + ','.join(sorted(list(largest_clique))))


def bron_kerbosch(r, p, x, g):
    """
    Executes Bron-Kerbosh algorithm on graph to find list of all maximal cliques

    :cite: This algorithm was implemented using pseudocode code found at
    https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

    :param r: R set for Bron-Kerbosch
    :param p: P set for Bron-Kerbosch
    :param x: X set for Bron-Kerbosch
    :param g: Graph being searched
    :return: List of all maximal cliques in the graph
    """

    maximal_cliques = []

    if p == set() and x == set():
        # print(r)
        maximal_cliques.append(r)

    for v in p:
        n = set(g[v])

        maximal_cliques.extend(bron_kerbosch(r | {v}, p & n, x & n, g))
        p = p - {v}
        x = x | {v}

    return maximal_cliques


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
