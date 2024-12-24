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
    Entry point for day 12, part 2
    :return: Exit code
    """
    garden_plot = read_input('input.txt')

    graph = construct_graph(garden_plot)

    print(garden_plot)
    print('Graph score: ' + str(calculate_score(graph)))


def calculate_score(graph):
    area_score = 0.0

    checked_nodes = []
    for node in graph.graph.items():

        if node[0] in checked_nodes:
            continue

        if node[1] == [(-1, -1)]:
            area_score = area_score + 4
            continue

        area_nodes = graph.DFS(node[0])

        convex_corners = 0
        concave_corners = 0

        for area_node in area_nodes:

            edges = graph.graph[area_node]

            # Calculate corners

            has_top = (area_node[0] - 1, area_node[1]) in edges
            has_right = (area_node[0], area_node[1] + 1) in edges
            has_bottom = (area_node[0] + 1, area_node[1]) in edges
            has_left = (area_node[0], area_node[1] - 1) in edges

            has_top_right = (area_node[0] - 1, area_node[1] + 1) in edges
            has_bottom_right = (area_node[0] + 1, area_node[1] + 1) in edges
            has_bottom_left = (area_node[0] + 1, area_node[1] - 1) in edges
            has_top_left = (area_node[0] - 1, area_node[1] - 1) in edges


            if has_top_left:
                if has_top and has_left:
                    pass
                elif has_top != has_left:
                    concave_corners = concave_corners + 1
                else:
                    convex_corners = convex_corners + 1
            else:
                if has_top and has_left:
                    concave_corners = concave_corners + 1
                elif has_top != has_left:
                    # concave_corners = concave_corners + 1
                    pass
                else:
                    convex_corners = convex_corners + 1

            if has_top_right:
                if has_top and has_right:
                    pass
                elif has_top != has_right:
                    concave_corners = concave_corners + 1
                else:
                    convex_corners = convex_corners + 1
            else:
                if has_top and has_right:
                    concave_corners = concave_corners + 1
                elif has_top != has_right:
                    # concave_corners = concave_corners + 1
                    pass
                else:
                    convex_corners = convex_corners + 1

            if has_bottom_right:
                if has_bottom and has_right:
                    pass
                elif has_bottom != has_right:
                    concave_corners = concave_corners + 1
                else:
                    convex_corners = convex_corners + 1
            else:
                if has_bottom and has_right:
                    concave_corners = concave_corners + 1
                elif has_bottom != has_right:
                    # concave_corners = concave_corners + 1
                    pass
                else:
                    convex_corners = convex_corners + 1

            if has_bottom_left:
                if has_bottom and has_left:
                    pass
                elif has_bottom != has_left:
                    concave_corners = concave_corners + 1
                else:
                    convex_corners = convex_corners + 1
            else:
                if has_bottom and has_left:
                    concave_corners = concave_corners + 1
                elif has_bottom != has_left:
                    # concave_corners = concave_corners + 1
                    pass
                else:
                    convex_corners = convex_corners + 1

        area = len(area_nodes)
        perimeter = convex_corners + (concave_corners / 3)
        area_score = area_score + area * perimeter

        checked_nodes.extend(area_nodes)

    return area_score


def construct_graph(garden_plot):
    """
    Construct the graph from the input

    :param garden_plot: Input to construct graph from
    :return: Graph representing the garden plot
    """
    graph = Graph()

    for r in range(len(garden_plot)):
        for c in range(len(garden_plot[r])):

            current_char = garden_plot[r][c]

            edge_found = False
            # Cardinal directions
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

            # Ordinal directions
            if (r - 1 >= 0 and c - 1 >= 0 and garden_plot[r - 1][c - 1] == current_char and
                    (garden_plot[r - 1][c] == current_char or garden_plot[r][c - 1] == current_char)):
                graph.add_edge((r,c), (r - 1, c - 1))

            if (r - 1 >= 0 and c + 1 < len(garden_plot[r]) and garden_plot[r - 1][c + 1] == current_char and
                    (garden_plot[r - 1][c] == current_char or garden_plot[r][c + 1] == current_char)):
                graph.add_edge((r, c), (r - 1, c + 1))

            if  (r + 1 < len(garden_plot) and c - 1 >= 0 and garden_plot[r + 1][c - 1] == current_char and
                    (garden_plot[r + 1][c] == current_char or garden_plot[r][c - 1] == current_char)):
                graph.add_edge((r, c), (r + 1, c - 1))

            if (r + 1 < len(garden_plot) and c + 1 < len(garden_plot[r]) and garden_plot[r + 1][c + 1] == current_char and
                    (garden_plot[r + 1][c] == current_char or garden_plot[r][c + 1] == current_char)):
                graph.add_edge((r, c), (r + 1, c + 1))

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
