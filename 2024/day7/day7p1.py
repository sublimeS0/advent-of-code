from itertools import product


def main():
    """
    Entry point for day 7 part 1
    :return: Exit status
    """
    equations = read_input('input.txt')

    operators = ['+', '*']

    valid_test_values = []
    for i in range(len(equations)):
        test_value = equations[i][0]
        operands = equations[i][1]

        operator_permutations = list(product(operators, repeat=len(operands) - 1))

        is_valid_test_value = False
        for order in list(operator_permutations):
            if operands_eval(operands[:], order) == test_value:
                is_valid_test_value = True
                break

        if is_valid_test_value:
            valid_test_values.append(test_value)

    test_value_sum = 0
    for x in valid_test_values:
        test_value_sum = test_value_sum + x

    print("Sum: " + str(test_value_sum))


def operands_eval(operands, order):
    """
    Evaluate total given list of operands and order of operators
    :param operands: List of operands to total
    :param order: List of order of operands
    :return: Evaluated total given operands and order of operators
    """

    running_total = operands.pop(0)

    for i in range(len(operands)):
        test = 0

        if order[i] == '+':
            # Add
            running_total = running_total + operands[i]
        elif order[i] == '*':
            # Multiply
            running_total = running_total * operands[i]
        else:
            print('problem')

    return running_total


def read_input(filename):
    """
    Read input file into list with format:
        [test_value, [operand, operand, ...]]
    :param filename: Name of input file
    :return: List with corresponding test values and operands
    """
    with open(filename) as file:
        test_values = [int(line.strip().split(':')[0]) for line in file]

    with open(filename) as file:
        operands = [line.strip().split(':')[1].strip().split(' ') for line in file]

    for i in range(len(operands)):
        for j in range(len(operands[i])):
            operands[i][j] = int(operands[i][j])

    ret = []
    for i in range(len(test_values)):
        ret.append([test_values[i], operands[i]])

    return ret


if __name__ == "__main__":
    main()
