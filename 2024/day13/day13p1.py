def main():
    """
    Entry point for day 13, part 1
    :return: Exit status

    35887 - too low
    95863 - too high

    35997 - p1 answer
    """
    machines = read_input('input.txt')

    total_tokens = 0

    for machine in machines:
        min_a_presses = 101
        min_b_presses = 101

        for a_presses in range(101):
            for b_presses in range(101):

                coords = ((a_presses * machine['a_moves'][0]) + (b_presses * machine['b_moves'][0]),
                          (a_presses * machine['a_moves'][1]) + (b_presses * machine['b_moves'][1]))

                if coords == machine['prize']:
                    if a_presses + b_presses < min_a_presses + min_b_presses:
                        min_a_presses = a_presses
                        min_b_presses = b_presses

        if min_a_presses < 101:
            total_tokens = total_tokens + (min_a_presses * 3) + min_b_presses

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

        for line in file:
            lines.append(line.strip())

            if len(lines) == 4:  # 4th line is blank, but we want to iterate past that
                a_string = lines[0]
                b_string = lines[1]
                prize = lines[2]

                machine = {
                    'prize':
                        (int(prize[prize.find('X') + 2:prize.find(',')]), int(prize[prize.find('Y') + 2:])),
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
                    (int(prize[prize.find('X') + 2:prize.find(',')]), int(prize[prize.find('Y') + 2:])),
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
