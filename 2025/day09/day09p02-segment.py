from numpy.ma.extras import average


def main() -> int:
    """
    Entry point for Day 9, Part 2

    Answers:
     - 4756442270 (too high)
     - 4570245558 (too high)
     - 6191504 (too low)
     - 116146088 (incorrect)
     - 3076696026 (incorrect)
     - 571015060 (incorrect)
     - 1684971312 (incorrect)
     -

    :return: Exit code
    """
    red_tiles: list = read_input('input_ex.txt')

    max_area = 0
    for tile in red_tiles:
        for tile_check in red_tiles:
            # print(f'Tiles: {tile} - {tile_check}')
            # print(f'Area: {calculate_area(tile, tile_check)}\n')

            # if calculate_area(tile, tile_check) > max_area:
            #     print(f'Tiles: {tile} - {tile_check}')
            #     print(f'Area: {calculate_area(tile, tile_check)}')
            #     print(f'Valid: {is_rectangle_contained((tile, tile_check), red_tiles)}\n')

            if is_rectangle_contained((tile, tile_check), red_tiles) != debug_get_expected()[(tile, tile_check)]:
                print(f'Error: {(tile, tile_check)}. Expected {debug_get_expected()[(tile, tile_check)]}, got {not debug_get_expected()[(tile, tile_check)]}.')

            # is_rectangle_contained((tile, tile_check), red_tiles)

            # print(f'Tiles: {tile} - {tile_check}')
            # print(f'Area: {calculate_area(tile, tile_check)}')
            # print(f'Valid: {is_rectangle_contained((tile, tile_check), red_tiles)}\n')

            # real
            if calculate_area(tile, tile_check) > max_area and is_rectangle_contained((tile, tile_check), red_tiles):
                max_area = calculate_area(tile, tile_check)

                # print(f'Tiles: {tile} - {tile_check}')
                # print(f'Area: {max_area}\n')

    print(f'Max area: {max_area}')

    return 0  # Return success


def is_rectangle_contained(rect: tuple, shape: list) -> bool:
    """
    Detect whether `rec` is completely contained within `shape`.
    
    :param rect: A rectangle, defined by a tuple of diagonal coordinates
    :param shape: A shape, defined by a list of tuple coordinates
    :return: True if the rectangle is completely contained, false otherwise
    """
    # A rectangle that is just a single point in shape is always contained
    if rect[0] == rect[1]:
        return True

    # Get the edges of the rectangle
    (x1, y1), (x2, y2) = rect
    rect_edges = [
        ((x1, y1), (x1, y2)),
        ((x1, y2), (x2, y2)),
        ((x2, y2), (x2, y1)),
        ((x2, y1), (x1, y1)),
    ]

    # Check if the line segment that defines the rectangle intersects any edge of the shape
    for rect_edge in rect_edges:
        for i in range(len(shape)):
            j = (i + 1) if (i < len(shape) - 1) else 0
            edge = (shape[i], shape[j])

            # If the rectangle IS the edge, it's contained
            if set(rect) == set(edge):
                return True

            if intersect(rect_edge, edge, False):
                return False

    # Now `rect` is either entirely inside or entirely outside `shape`. If one point of `rect` is inside, they all are!
    center_point = ((rect[0][0] + rect[1][0]) / 2, (rect[0][1] + rect[1][1]) / 2)
    return is_point_contained(center_point, shape)


def is_point_contained(point: tuple, shape: list) -> bool:
    """
    Determine whether `point` lies within `shape`.

    :param point: Point to check
    :param shape: Shape to check
    :return: True if the point lies within the shape, false otherwise
    """
    if point in shape:
        return True

    ray: tuple = (point, (0, 0))

    intersections = 0
    for i in range(len(shape)):
        j = (i + 1) if (i < len(shape) - 1) else 0
        edge = (shape[i], shape[j])

        # If `point` lies on `edge`, for our purposes, it is contained
        min_x, max_x = sorted((edge[0][0], edge[1][0]))
        min_y, max_y = sorted((edge[0][1], edge[1][1]))

        if point[0] == min_x == max_x and min_y <= point[1] <= max_y:
            return True
        if point[1] == min_y == max_y and min_x <= point[0] <= max_x:
            return True

        if intersect(ray, edge):
            intersections += 1

    return intersections % 2 != 0


def intersect(line_a: tuple, line_b: tuple, inclusive: bool = True) -> bool:
    """
    Detect whether two line segments, defined by their endpoints, intersect

    :param line_a: Line A
    :param line_b: Line B
    :param inclusive: TODO: figure
    :return: True if the lines intersect, false otherwise
    """

    if not inclusive:
        def remove_endpoints(line: tuple) -> tuple:
            if line[0][0] == line_a[1][0]:
                min_y = min(line[0][1], line[1][1]) + 1
                max_y = max(line[0][1], line[1][1]) - 1

                return (line[0][0], min_y), (line[0][0], max_y)

            else:
                min_x = min(line[0][0], line[1][0]) + 1
                max_x = max(line[0][0], line[1][0]) - 1

                return (min_x, line[0][1]), (max_x, line[0][1])

        line_a = remove_endpoints(line_a)
        # line_b = remove_endpoints(line_b)

    a_dx, a_dy = line_a[0][0] - line_a[1][0], line_a[0][1] - line_a[1][1]
    b_dx, b_dy = line_b[0][0] - line_b[1][0], line_b[0][1] - line_b[1][1]

    # Check and handle if lines are co-linear
    try:
        if (a_dy / a_dx) == (b_dy / b_dx):
            return False
    except ZeroDivisionError:
        # jfc man they aren't co linear fuck off
        if a_dx == 0 and b_dx == 0:
            return False

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


def debug_get_expected() -> dict:
    return {
        ((7, 1), (7, 1)): True,
        ((7, 1), (11, 1)): True,
        ((7, 1), (11, 7)): False,
        ((7, 1), (9, 7)): False,
        ((7, 1), (9, 5)): True,
        ((7, 1), (2, 5)): False,
        ((7, 1), (2, 3)): False,
        ((7, 1), (7, 3)): True,

        ((11, 1), (7, 1)): True,
        ((11, 1), (11, 1)): True,
        ((11, 1), (11, 7)): True,
        ((11, 1), (9, 7)): True,
        ((11, 1), (9, 5)): True,
        ((11, 1), (2, 5)): False,
        ((11, 1), (2, 3)): False,
        ((11, 1), (7, 3)): True,

        ((11, 7), (7, 1)): False,
        ((11, 7), (11, 1)): True,
        ((11, 7), (11, 7)): True,
        ((11, 7), (9, 7)): True,
        ((11, 7), (9, 5)): True,
        ((11, 7), (2, 5)): False,
        ((11, 7), (2, 3)): False,
        ((11, 7), (7, 3)): False,

        ((9, 7), (7, 1)): False,
        ((9, 7), (11, 1)): True,
        ((9, 7), (11, 7)): True,
        ((9, 7), (9, 7)): True,
        ((9, 7), (9, 5)): True,
        ((9, 7), (2, 5)): False,
        ((9, 7), (2, 3)): False,
        ((9, 7), (7, 3)): False,

        ((9, 5), (7, 1)): True,
        ((9, 5), (11, 1)): True,
        ((9, 5), (11, 7)): True,
        ((9, 5), (9, 7)): True,
        ((9, 5), (9, 5)): True,
        ((9, 5), (2, 5)): True,
        ((9, 5), (2, 3)): True,
        ((9, 5), (7, 3)): True,

        ((2, 5), (7, 1)): False,
        ((2, 5), (11, 1)): False,
        ((2, 5), (11, 7)): False,
        ((2, 5), (9, 7)): False,
        ((2, 5), (9, 5)): True,
        ((2, 5), (2, 5)): True,
        ((2, 5), (2, 3)): True,
        ((2, 5), (7, 3)): True,

        ((2, 3), (7, 1)): False,
        ((2, 3), (11, 1)): False,
        ((2, 3), (11, 7)): False,
        ((2, 3), (9, 7)): False,
        ((2, 3), (9, 5)): True,
        ((2, 3), (2, 5)): True,
        ((2, 3), (2, 3)): True,
        ((2, 3), (7, 3)): True,

        ((7, 3), (7, 1)): True,
        ((7, 3), (11, 1)): True,
        ((7, 3), (11, 7)): False,
        ((7, 3), (9, 7)): False,
        ((7, 3), (9, 5)): True,
        ((7, 3), (2, 5)): True,
        ((7, 3), (2, 3)): True,
        ((7, 3), (7, 3)): True,
    }


if __name__ == "__main__":
    main()
