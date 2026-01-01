def main() -> int:
    """
    Entry point for Day 9, Part 2

    Answers:
     - 4756442270 (too high)
     - 4570245558 (too high)
     _ 6191504 (too low)
     _

     - 116146088
     - 116146088
     - 3076696026

    :return: Exit code
    """
    red_tiles: list = read_input('input_ex.txt')

    max_area = 0
    for tile in red_tiles:
        for tile_check in red_tiles:
            # print(f'Tiles: {tile} - {tile_check}')
            # print(f'Area: {calculate_area(tile, tile_check)}\n')

            if calculate_area(tile, tile_check) > max_area and is_fully_contained((tile, tile_check), red_tiles):
                max_area = calculate_area(tile, tile_check)

                # print('valid\n')
                print(f'Tiles: {tile} - {tile_check}')
                print(f'Area: {max_area}\n')

    print(f'Max area: {max_area}')

    return 0  # Return success


def is_fully_contained(rect: tuple, shape: list) -> bool:
    """
    Detect whether `rec` is completely contained within `shape`.
    
    :param rect: A rectangle, defined by a tuple of diagonal coordinates
    :param shape: A shape, defined by a list of tuple coordinates
    :return: True if the rectangle is completely contained, false otherwise
    """
    rect_corner_a: tuple = rect[0]
    rect_corner_b: tuple = rect[1]

    max_x: tuple = max(rect_corner_a[0], rect_corner_b[0])
    max_y: tuple = max(rect_corner_a[1], rect_corner_b[1])
    min_x: tuple = min(rect_corner_a[0], rect_corner_b[0])
    min_y: tuple = min(rect_corner_a[1], rect_corner_b[1])

    # Check for points contained in the rectangle
    shape_coord: tuple
    for shape_coord in shape:
        if shape_coord in [rect_corner_a, rect_corner_b]:
            continue

        if min_x < shape_coord[0] < max_x and min_y < shape_coord[1] < max_y:
            return False

    corners = [
        (min_x, min_y),
        (min_x, max_y),
        (max_x, min_y),
        (max_x, max_y),
    ]

    return True


def calculate_area(coord_a: tuple, coord_b: tuple):
    """
    Calculates area of rectangle give two points

    :param coord_a: Point A
    :param coord_b: Point B
    :return: Area of rectangle formed by the two points
    """
    return (abs(coord_a[0] - coord_b[0]) + 1) * (abs(coord_a[1] - coord_b[1]) + 1)


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
