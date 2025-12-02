def main():
    """
    Entry point for Day 1, Part 1

    445 - too low
    1089 - correct

    :return: Exit code
    """
    rotations, current_position = read_input('input.txt')

    zero_count = 0
    for rotation in rotations:
        current_position = turn_dial(rotation, current_position)

        if current_position == 0:
            zero_count += 1

    print('Password: ' + str(zero_count))


def turn_dial(rotation, current_position):
    """
    Execute a dial rotation

    :param rotation: Rotation instruction
    :param current_position: Current dial position
    :return: New dial position
    """
    direction, distance = rotation[:1], int(rotation[1:])

    # Distances over 100 can be reduced to just the remainder of dividing by 100
    if distance > 100:
        distance %= 100

    if direction == 'R':
        current_position += distance

    if direction == 'L':
        current_position -= distance

    if current_position > 99:
        current_position -= 100

    if current_position < 0:
        current_position += 100

    return current_position


def read_input(filename):
    with open(filename) as file:
        rotations = [line.strip() for line in file]

    return rotations, 50


if __name__ == "__main__":
    main()
