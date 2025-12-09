def main():
    """
    Entry point for Day 6, Part 2

    12377473011151 - correct

    TODO: redo this with a transposed array. dipshit.

    :return: Exit code
    """
    lines, operations = read_input('input.txt')
    total = 0

    # Loop through the characters in all four lines "at the same time" to compile the vertical numbers
    problems = dict()
    problem_num = 0
    for i in range(len(lines[0])):

        num = ''
        num_found = False
        for l, line in enumerate(lines):
            if line[i] not in [' ', '\n']:
                num += line[i]
                num_found = True

        if problem_num not in problems:
            problems[problem_num] = []

        if num_found:
            problems[problem_num].append(int(num))
        else:
            problem_num += 1

    # Calculate the sum
    for op, problem in enumerate(problems.values()):
        p_sum = 1 if operations[op] == '*' else 0
        for num in problem:
            if operations[op] == '*':
                p_sum *= num
            if operations[op] == '+':
                p_sum += num

        total += p_sum

    print('Total: ' + str(total))


def read_input(filename):
    """
    Read the input file
    :param filename: File to read
    :return: List of line values and list of operations (with whitespace removed)
    """
    with open(filename) as file:
        lines = [list(line) for line in file if '*' not in line]

    with open(filename) as file:
        operations = [list(line.strip().replace(' ', '')) for line in file if '*' in line]

    return lines, operations.pop()


if __name__ == "__main__":
    main()
