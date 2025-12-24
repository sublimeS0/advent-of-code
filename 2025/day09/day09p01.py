def main() -> int:
    """
    Entry point for Day 9, Part 1

    :return: Exit code
    """
    red_tiles: list = read_input('input_ex.txt')

    # Get max and min values for both axes
    x_coords, y_coords = zip(*red_tiles)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    center = ((max_x + min_x) / 2, ((max_y + min_y) / 2))

    check_tiles = list(filter(lambda tile: (tile[0] in [min_x, max_x]) or (tile[1] in [min_y, max_y]), red_tiles))

    return 0


def read_input(filename: str) -> list[tuple]:
    """
    Read input file into relevant data structures
    :param filename: Name of input file
    :return: Return relevant data structures
    """
    with open(filename, 'r') as file:
        line: str
        return [tuple(map(int, line.strip().split(','))) for line in file]


if __name__ == "__main__":
    main()
