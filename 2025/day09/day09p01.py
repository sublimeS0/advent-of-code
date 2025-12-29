def main() -> int:
    """
    Entry point for Day 9, Part 1

    Answers:
     - 2636870220 (too low)
     - 4756718172 (correct)

    :return: Exit code
    """
    red_tiles: list = read_input('input.txt')

    # Just brute force the area??? I'm surprised this actually runs instantly
    max_area = 0
    for tile in red_tiles:
        for tile_check in red_tiles:
            if calculate_area(tile, tile_check) > max_area:
                max_area = calculate_area(tile, tile_check)

    print('Max area: ' + str(max_area))

    return 0


def calculate_area(coord_a: tuple, coord_b: tuple):
    """
    Calculates area of rectangle give two points

    :param coord_a: Point A
    :param coord_b: Point B
    :return: Area of rectangle formed by the two points
    """
    return abs(coord_a[0] + 1 - coord_b[0]) * abs(coord_a[1] + 1 - coord_b[1])


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
