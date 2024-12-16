from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        # print(v, end='')
        visited.append(v)

        for neighbor in self.graph[v]:

            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):

        visited = []
        self.DFSUtil(v, visited)

        return visited


def main():
    """
    Entry point for day 12, part 1
    :return: Exit code
    """
    garden_plot = read_input('input.txt')

    graph = construct_graph(garden_plot)

    print(garden_plot)
    print('Graph score: ' + str(calculate_score(graph)))


def calculate_score(graph):
    area_score = 0

    checked_nodes = []
    for node in graph.graph.items():

        if node[0] in checked_nodes:
            continue

        if node[1] == [(-1, -1)]:
            area_score = area_score + 4
            continue

        area_nodes = graph.DFS(node[0])

        perimeter = 0
        for spec_node in area_nodes:
            perimeter = perimeter + (4 - len(graph.graph.get(spec_node)))
        area = len(area_nodes)

        checked_nodes.extend(area_nodes)

        area_score = area_score + area * perimeter

    return area_score


def construct_graph(garden_plot):
    graph = Graph()

    for r in range(len(garden_plot)):
        for c in range(len(garden_plot[r])):

            current_char = garden_plot[r][c]

            edge_found = False
            if r - 1 >= 0 and garden_plot[r - 1][c] == current_char:
                graph.add_edge((r, c), (r - 1, c))
                edge_found = True

            if c - 1 >= 0 and garden_plot[r][c - 1] == current_char:
                graph.add_edge((r, c), (r, c - 1))
                edge_found = True

            if r + 1 < len(garden_plot) and garden_plot[r + 1][c] == current_char:
                graph.add_edge((r, c), (r + 1, c))
                edge_found = True

            if c + 1 < len(garden_plot[r]) and garden_plot[r][c + 1] == current_char:
                graph.add_edge((r, c), (r, c + 1))
                edge_found = True

            if not edge_found:
                # Item has no edges
                graph.add_edge((r, c), (-1, -1))

    return graph


def read_input(filename):
    """
    Read the input file
    :param filename: Name of input file
    :return: 2D list of crop plot
    """
    with open(filename) as file:
        plot = [list(line.strip()) for line in file]

    return plot


if __name__ == "__main__":
    main()
