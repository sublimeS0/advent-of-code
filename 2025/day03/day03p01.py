def main():
    """
    Entry point for Day 3, Part 1

    :return: Exit code
    """
    banks = read_input('input.txt')

    max_joltage = 0

    for bank in banks:
        tens = 0
        ones = 0
        ones_set = False
        best_joltage = 0
        old_tens = 0

        for num in bank:
            if int(num) > tens:
                old_tens = tens
                tens = int(num)
                ones = 0

                ones_set = False
            elif int(num) > ones:
                ones = int(num)
                ones_set = True

            if ones_set and tens * 10 + ones > best_joltage:
                best_joltage = tens * 10 + ones
            elif old_tens * 10 + tens > best_joltage:
                best_joltage = old_tens * 10 + tens

        max_joltage += best_joltage

        # print(bank + ': ' + str(best_joltage))

    print('Max Joltage: ' + str(max_joltage))


def read_input(filename):
    """
    Reads the input file and moves data to relevant data structure

    :param filename:
    :return:
    """

    with open(filename) as file:
        banks = [line.strip() for line in file]

    return banks


if __name__ == "__main__":
    main()
