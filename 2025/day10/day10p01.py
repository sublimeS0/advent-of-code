import re
import itertools
import sys


def main() -> int:
    """
    Entry point for Day 10, Part 1

    TODO: refactor light diagrams into binaries and XOR?

    Answers:
     - 532 (correct)

    :return: Exit code
    """
    machines: list = read_input('input.txt')
    press_sum: int = 0

    # Configure machines
    machine: dict
    for machine in machines:
        press_sum += configure_machine(machine)

    print(f'Total Presses: {press_sum}')
    return 0


def configure_machine(machine: dict) -> int:
    """
    "Configures" a machine by calculating the min presses required to meet the intended diagram

    :param machine: Machine dict to configure
    :return: Minimum number of presses to configure machine
    """
    # Generate all combinations of buttons (2^n... v sad)
    len_combos: list = []
    for i in range(1, len(machine['buttons'])):
        len_combos.append(itertools.combinations(machine['buttons'], i))

    # Try all button combinations
    fewest_presses: int = sys.maxsize
    for len_combo in len_combos:  # Loop through all sets of combinations
        for combo in len_combo:  # Loop through combinations of n length
            diagram: list = ['.'] * len(machine['diagram'])

            # Press each button
            for b, button in enumerate(combo):
                diagram = press_button(button, diagram)

            # If we reached our designated diagram, count it
            if diagram == machine['diagram'] and len(combo) < fewest_presses:
                fewest_presses = len(combo)  # TODO: double break here. the first will be the fewest presses.
                break

    return fewest_presses


def press_button(button: set, diagram: list) -> list:
    """
    Executes a button press for a given button and light diagram

    :param button: Button definition
    :param diagram: Light diagram
    :return: An updated button diagram
    """
    for i in button:
        diagram[i] = '#' if diagram[i] == '.' else '.'
    return diagram


def read_input(filename: str) -> list:
    """
    Read input file into relevant data structures

    :param filename: Name of input file
    :return: Return relevant data structures
    """
    machines: list = []
    with open(filename, 'r') as file:
        line: str
        for line in file:
            machines.append({
                'diagram': list(line[line.index('[') + 1:line.index(']')]),
                'buttons': [set(map(int, button.split(','))) for button in re.findall(r"\((.*?)\)", line)],
                'joltage': set(map(int, line[line.index('{') + 1:line.index('}')].split(',')))
            })

    return machines


if __name__ == "__main__":
    main()
