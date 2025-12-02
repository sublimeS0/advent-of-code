def main():
    """
    Entry point for Day 1, Part 2

    6536 - too high
    6420 - too low
    6530 - correct

    :return: Exit code
    """
    rotations, current_position = read_input('input.txt')

    zero_count = 0
    for rotation in rotations:
        current_position, zero_inc = turn_dial(rotation, current_position)
        zero_count += zero_inc

    print('Password: ' + str(zero_count))


def turn_dial(rotation, current_position):
    """
    Execute a dial rotation

    :param rotation: Rotation instruction
    :param current_position: Current dial position
    :return: New dial position
    """
    direction, distance = rotation[:1], int(rotation[1:])
    starting_position = current_position

    if direction == 'R':
        current_position += distance

    if direction == 'L':
        current_position -= distance

    zero_count = 0

    while current_position > 99:
        current_position -= 100
        zero_count += 1

    while current_position < 0:
        current_position += 100
        zero_count += 1

    """
    Account for special cases
    """

    # The dial was turned left onto 0, without completing a full spin
    if direction == 'L' and current_position == 0 and distance % 100 != 0:
        zero_count += 1

    # The dial was turned left from zero - the last rotation would have accounted for it
    if direction == 'L' and starting_position == 0 and current_position != 0:
        zero_count -= 1

    # Can't ever be negative
    if zero_count < 0:
        zero_count = 0

    return current_position, zero_count


def read_input(filename):
    with open(filename) as file:
        rotations = [line.strip() for line in file]

    return rotations, 50


if __name__ == "__main__":
    main()
