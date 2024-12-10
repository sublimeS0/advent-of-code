from collections import defaultdict


class Graph:
    """
    Class to represent trail map graph

    :cite: https://www.geeksforgeeks.org/python-program-for-depth-first-search-or-dfs-for-a-graph/ - DFS algorithm. This
    algorithm was slightly modified for use in this puzzle.
    """

    def __init__(self):
        self.graph = defaultdict(list)
        self.path_list = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, trail_map):
        visited.append(v)
        # print(v, end='')

        for neighbor in self.graph[v]:
            branch = visited[:]

            if neighbor not in visited:
                self.DFSUtil(neighbor, branch, trail_map)

            if trail_map[neighbor[0]][neighbor[1]] == 9:
                self.path_list.append(branch)
                # print(branch)
                # print('')

    def DFS(self, v, trail_map):

        visited = []
        self.DFSUtil(v, visited, trail_map)


def main():
    """
    Entry point for day 10, part 2
    :return: Exit status
    """

    # Read input file
    trail_map_input = read_input('input.txt')

    # Build graph w/ edges
    trail_map = Graph()
    add_edges(trail_map_input, trail_map)

    # Find all trailheads in the map
    total_score = 0
    for trailhead in find_trailheads(trail_map_input):
        trail_map.DFS(trailhead, trail_map_input)

        # unique_endpoints = []
        # for path in trail_map.path_list:
        #     endpoint = path[-1]
        #
        #     if endpoint not in unique_endpoints:
        #         unique_endpoints.append(endpoint)
        #
        # total_score = total_score + len(unique_endpoints)

        total_score = total_score + len(trail_map.path_list)

        trail_map.path_list = []

    print('Total Map Score: ' + str(total_score))


def add_edges(trail_map, graph):
    """
    Adds edges to trail map graph for search

    :param trail_map:
    :param graph:
    :return:
    """

    for r in range(len(trail_map)):
        for c in range(len(trail_map[r])):
            current_val = trail_map[r][c]

            if current_val == '.':
                continue

            if r + 1 < len(trail_map) and trail_map[r + 1][c] == current_val + 1:
                graph.add_edge((r, c), (r + 1, c))

            if r - 1 >= 0 and trail_map[r - 1][c] == current_val + 1:
                graph.add_edge((r, c), (r - 1, c))

            if c + 1 < len(trail_map[r]) and trail_map[r][c + 1] == current_val + 1:
                graph.add_edge((r, c), (r, c + 1))

            if c - 1 >= 0 and trail_map[r][c - 1] == current_val + 1:
                graph.add_edge((r, c), (r, c - 1))


def find_trailheads(trail_map):
    trailheads = []
    for r in range(len(trail_map)):
        for c in range(len(trail_map[r])):
            if trail_map[r][c] == 0:
                trailheads.append((r, c))

    return trailheads


def read_input(filename):
    """
    Read input file into trail map
    :param filename: Name of file to read
    :return: 2D list of trail input
    """

    with open(filename) as file:
        map_input = [list(line.strip()) for line in file]

    for r in range(len(map_input)):
        for c in range(len(map_input[r])):
            if map_input[r][c] == '.':
                continue

            map_input[r][c] = int(map_input[r][c])
    return map_input


if __name__ == "__main__":
    main()
