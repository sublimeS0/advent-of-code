def main():
    """
    Entry point for day 14, part 1
    :return:
    """
    guards = read_input('input.txt')

    seconds = 9300
    map_size = (103, 101)

    guard_map = [['.'] * map_size[1] for _ in range(map_size[0])]

    # Draw starting guard locations
    # for guard in guards:
    #     pos = guard['position']
    #     if guard_map[pos[1]][pos[0]] == '.':
    #         guard_map[pos[1]][pos[0]] = '1'
    #     else:
    #         count = int(guard_map[pos[1]][pos[0]])
    #         count = count + 1
    #         guard_map[pos[1]][pos[0]] = str(count)

    for sec in range(seconds):
        for guard in guards:
            new_pos, guard_map = move_guard(guard, guard_map)
            guard['position'] = new_pos

        print('Second: ' + str(sec + 1))
        draw_map(guards, guard_map)

    draw_map(guards, guard_map)

    # Calculate safety score
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for guard in guards:
        pos = guard['position']

        if pos[1] < map_size[0] // 2 and pos[0] < map_size[1] // 2:
            q1 = q1 + 1
        elif pos[1] < map_size[0] // 2 and pos[0] > map_size[1] // 2:
            q2 = q2 + 1
        elif pos[1] > map_size[0] // 2 and pos[0] < map_size[1] // 2:
            q3 = q3 + 1
        elif pos[1] > map_size[0] // 2 and pos[0] > map_size[1] // 2:
            q4 = q4 + 1

    safety_score = q1 * q2 * q3 * q4

    print('Safety Score: ' + str(safety_score))


def move_guard(guard, guard_map):
    pos = guard['position']
    vel = guard['velocity']

    new_pos = (pos[0] + vel[0], pos[1] + vel[1])

    # Update new position
    wrap_pos = new_pos
    if new_pos[0] < 0:
        wrap_pos = (wrap_pos[0] + len(guard_map[0]), wrap_pos[1])

    elif new_pos[0] >= len(guard_map[0]):
        wrap_pos = (wrap_pos[0] - len(guard_map[0]), wrap_pos[1])

    if new_pos[1] < 0:
        wrap_pos = (wrap_pos[0], wrap_pos[1] + len(guard_map))

    elif new_pos[1] >= len(guard_map):
        wrap_pos = (wrap_pos[0], wrap_pos[1] - len(guard_map))

    new_pos = wrap_pos

    if guard_map[new_pos[1]][new_pos[0]] == '.':
        guard_map[new_pos[1]][new_pos[0]] = '1'
    else:
        count = int(guard_map[new_pos[1]][new_pos[0]])
        count = count + 1
        guard_map[new_pos[1]][new_pos[0]] = count

    # Update old position
    if guard_map[pos[1]][pos[0]] == '1':
        guard_map[pos[1]][pos[0]] = '.'
    elif guard_map[pos[1]][pos[0]] == '.':
        test = 0
    else:
        count = int(guard_map[pos[1]][pos[0]])
        count = count - 1
        guard_map[pos[1]][pos[0]] = str(count)

    return new_pos, guard_map


def draw_map(guards, guard_map):
    """
    Prints the current state of the map to the console
    :param guards: Current guard locations
    :param guard_map: Tuple of map dimensions
    :return: None
    """

    for r in guard_map:
        for c in r:
            print(c, end='', flush=True)
        print(flush=True)
    print(flush=True)


def read_input(filename):
    """
    Reads input file into list of guard locations and velocities
    :param filename: Name of input file to read
    :return: List of dictionaries of guards locations and velocities
    """
    guards = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            pos = line[line.index('p') + 2:line.index(' ')]
            vel = line[line.index('v') + 2:]

            guard = {
                'position': (int(pos.split(',')[0]), int(pos.split(',')[1])),
                'velocity': (int(vel.split(',')[0]), int(vel.split(',')[1]))
            }
            guards.append(guard)

    return guards


if __name__ == "__main__":
    main()
