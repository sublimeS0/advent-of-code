import numpy as np


def main():
    """
    Entry point for Day 6, Part 1

    6100348226985 - correct

    :return: Exit code
    """
    lines, operations = read_input('input.txt')

    problems = list(np.transpose(np.array(lines)))

    total = 0
    for problem in problems:
        operation = operations.pop(0)
        problem = list(problem)
        start = int(problem.pop(0))

        if operation == '+':
            for num in problem:
                start += int(num)

        if operation == '*':
            for num in problem:
                start *= int(num)

        total += start

    print('Total: ' + str(total))


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip().split() for line in file]

    operations = lines.pop()

    return lines, operations


if __name__ == "__main__":
    main()
