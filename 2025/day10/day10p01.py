import re


def main() -> int:
    """
    Entry point for Day 10, Part 1

    :return: Exit code
    """
    machines: list = read_input('input_ex.txt')

    presses: int = 0
    machine: dict
    for machine in machines:
        pass

    return 0


def press_button(button: set, diagram: str) -> str:
    """

    :param button:
    :param diagram:
    :return:
    """
    pass


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
                'diagram': line[line.index('[') + 1:line.index(']')],
                'buttons': [set(map(int, button.split(','))) for button in re.findall(r"\((.*?)\)", line)],
                'joltage': set(map(int, line[line.index('{') + 1:line.index('}')].split(',')))
            })

    return machines


if __name__ == "__main__":
    main()
