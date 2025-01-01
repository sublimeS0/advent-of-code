from collections import defaultdict


class Graph:
    def __init__(self, start_tile, end_tile):
        self.graph = defaultdict(list)
        self.start_tile = start_tile
        self.end_tile = end_tile

    def add_edge(self, u, v):
        self.graph[u].append(v)

def main():
    maze, start_tile, end_tile = read_input('input_ex.txt')
    maze_graph = construct_graph(maze, start_tile, end_tile)


def construct_graph(maze, start_tile, end_tile):

    valid_chars = ['.', 'S', 'E']
    maze_graph = Graph(start_tile, end_tile)

    for key, value in maze.items():
        r = key[0]
        c = key[1]

        if value == '#':
            continue

        if (r + 1, c) in maze and maze[(r + 1, c)] in valid_chars:
            maze_graph.add_edge((r, c), (r + 1, c))

        if (r - 1, c) in maze and maze[(r - 1, c)] in valid_chars:
            maze_graph.add_edge((r, c), (r - 1, c))

        if (r, c + 1) in maze and maze[(r, c + 1)] in valid_chars:
            maze_graph.add_edge((r, c), (r, c + 1))

        if (r, c - 1) in maze and maze[(r, c - 1)] in valid_chars:
            maze_graph.add_edge((r, c), (r, c - 1))

    return maze_graph

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