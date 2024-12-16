def main():
    """
    Entry point for day 13, part 2
    :return: Exit status

    35997 - p1 answer
    82510994362072 - p2 answer
    """
    machines = read_input('input.txt')

    tolerance = 0.01

    total_tokens = 0

    for machine in machines:
        a_moves = machine['a_moves']
        b_moves = machine['b_moves']
        prize = machine['prize']

        # Solve for a_val, given two equations. Then use a_val to solve for b.
        a_val = ((prize[0] / b_moves[0]) - (prize[1] / b_moves[1])) / ((a_moves[0] / b_moves[0]) - (a_moves[1] / b_moves[1]))
        b_val = (prize[1] - a_val * a_moves[1]) / b_moves[1]

        if (abs(round(a_val) - a_val) < tolerance) and (abs(round(b_val) - b_val < tolerance)):
            total_tokens = total_tokens + (3 * round(a_val)) + round(b_val)

    print('Tokens: ' + str(total_tokens))


def read_input(filename):
    """
    Read input file into list of dictionaries containing prize, a button moves, and b button moves
    :param filename:  Name of input file to read
    :return: List of dictionaries
    """
    machines = []

    with open(filename, 'r') as file:

        lines = []

        part2_modifier = 10000000000000
        # part2_modifier = 0

        for line in file:
            lines.append(line.strip())

            if len(lines) == 4:  # 4th line is blank, but we want to iterate past that
                a_string = lines[0]
                b_string = lines[1]
                prize = lines[2]

                machine = {
                    'prize':
                        (int(prize[prize.find('X') + 2:prize.find(',')]) + part2_modifier,
                         int(prize[prize.find('Y') + 2:]) + part2_modifier),
                    'a_moves':
                        (int(a_string[a_string.find('X') + 2:a_string.find(',')]),
                         int(a_string[a_string.find('Y') + 2:])),
                    'b_moves':
                        (int(b_string[b_string.find('X') + 2:b_string.find(',')]),
                         int(b_string[b_string.find('Y') + 2:])),
                }

                machines.append(machine)
                lines = []

        if len(lines) > 0:
            a_string = lines[0]
            b_string = lines[1]
            prize = lines[2]

            machine = {
                'prize':
                    (int(prize[prize.find('X') + 2:prize.find(',')]) + part2_modifier,
                     int(prize[prize.find('Y') + 2:]) + part2_modifier),
                'a_moves':
                    (int(a_string[a_string.find('X') + 2:a_string.find(',')]),
                     int(a_string[a_string.find('Y') + 2:])),
                'b_moves':
                    (int(b_string[b_string.find('X') + 2:b_string.find(',')]),
                     int(b_string[b_string.find('Y') + 2:])),
            }

            machines.append(machine)
            lines = []

    return machines


if __name__ == "__main__":
    main()
