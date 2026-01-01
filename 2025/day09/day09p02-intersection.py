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
    # Rect is defined by a diagonal. We need to collect the other diagonal as well.
    opposite_rect = ((rect[0][0], rect[1][1]), (rect[1][0], rect[0][1]))
    pass

    # Check if the line segment that defines the rectangle intersects any edge of the shape
    for i in range(len(shape)):
        j = (i + 1) if (i < len(shape) - 1) else 0
        if intersect(rect, (shape[i], shape[j])) or intersect(opposite_rect, (shape[i], shape[j])):
            return False

    return True


def intersect(line_a: tuple, line_b: tuple) -> bool:
    """
    Detect whether two line segments, defined by their endpoints, intersect

    :param line_a: Line A
    :param line_b: Line B
    :return: True if the lines intersect, false otherwise
    """
    a_dx, a_dy = line_a[0][0] - line_a[1][0], line_a[0][1] - line_a[1][1]
    b_dx, b_dy = line_b[0][0] - line_b[1][0], line_b[0][1] - line_b[1][1]

    # Check and handle if lines are co-linear
    try:
        if (a_dy == 0 and b_dy == 0) or (a_dx / a_dy == b_dx / b_dy):
            return True
    except ZeroDivisionError:
        # jfc man they aren't co linear fuck off
        pass

    # Handle all non-co-linear cases
    def ccw(p_q: tuple, p_r: tuple, p_s: tuple):
        return (p_s[1] - p_q[1]) * (p_r[0] - p_q[0]) > (p_r[1] - p_q[1]) * (p_s[0] - p_q[0])

    return ccw(line_a[0], line_b[0], line_b[1]) != ccw(line_a[1], line_b[0], line_b[1]) and \
        ccw(line_a[0], line_a[1], line_b[0]) != ccw(line_a[0], line_a[1], line_b[1])


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
