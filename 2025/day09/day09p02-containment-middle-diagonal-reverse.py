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
     - 1665679194 (correct)

    :return: Exit code
    """
    red_tiles: list = read_input('input_tiny_u.txt')

    max_area = 0
    for tile in red_tiles:
        for tile_check in red_tiles:

            # Check every set of tiles. This could probably be optimized.
            if calculate_area(tile, tile_check) > max_area and is_rectangle_contained((tile, tile_check), red_tiles):
                max_area = calculate_area(tile, tile_check)

    print(f'Max area: {max_area}')

    return 0  # Return success


def is_rectangle_contained(rect: tuple, shape: list) -> bool:
    """
    Detect whether `rec` is completely contained within `shape`.
    
    :param rect: A rectangle, defined by a tuple of diagonal coordinates
    :param shape: A shape, defined by a list of tuple coordinates
    :return: True if the rectangle is completely contained, false otherwise
    """
    # Get the corners of the rectangle
    (x1, y1), (x2, y2) = rect
    rect_corners = [
        (x1, y1),
        (x1, y2),
        (x2, y2),
        (x2, y1),
    ]

    "Step 1: Ensure no rectangle corner lies outside of shape"
    for corner in rect_corners:
        if not is_point_contained(corner, shape):
            return False

    "Step 2: Ensure no vertex of shape lies *entirely* within rect"
    for vertex in shape:
        if is_point_contained(vertex, rect_corners, False):
            return False

    "Step 3: Ensure the diagonals of rect never intersect an edge of shape"
    # Rect is defined by a diagonal. We need to collect the other diagonal as well.
    opposite_rect = ((x1, y2), (x2, y1))
    for i in range(len(shape)):
        j = (i + 1) if (i < len(shape) - 1) else 0
        edge = (shape[i], shape[j])

        # Skip if the points of `rect` lie *on* `edge`. For our purposes, that's not an "intersection" (even though in
        # reality it is).
        if set(rect) & set(edge):
            continue

        # Check for intersections for both diagonals
        if intersect(rect, edge) or intersect(opposite_rect, edge):
            return False

    "Step 4: Ensure the midpoint (or any point) of rect is within shape"
    return is_point_contained(((x1 + x2) / 2, (y1 + y2) / 2), shape)


def is_point_contained(point: tuple, shape: list, count_inclusive: bool = True) -> bool:
    """
    Determine whether `point` lies within `shape`.

    :param point: Point to check
    :param shape: Shape to check
    :param count_inclusive:
    :return: True if the point lies within the shape, false otherwise
    """
    if point in shape:
        return count_inclusive

    ray: tuple = (point, (0, 0))

    intersections = 0
    for i in range(len(shape)):
        j = (i + 1) if (i < len(shape) - 1) else 0
        edge = (shape[i], shape[j])

        # If `point` lies on `edge`, for our purposes, it is contained
        min_x, max_x = sorted((edge[0][0], edge[1][0]))
        min_y, max_y = sorted((edge[0][1], edge[1][1]))

        if point[0] == min_x == max_x and min_y <= point[1] <= max_y:
            return count_inclusive
        if point[1] == min_y == max_y and min_x <= point[0] <= max_x:
            return count_inclusive

        if intersect(ray, edge):
            intersections += 1

    return intersections % 2 != 0


def intersect(line_a: tuple, line_b: tuple) -> bool:
    """
    Detect whether two line segments, defined by their endpoints, intersect

    :param line_a: Line A
    :param line_b: Line B
    :return: True if the lines intersect, false otherwise
    """
    line_a = tuple(sorted(line_a))
    line_b = tuple(sorted(line_b))

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


if __name__ == "__main__":
    main()
