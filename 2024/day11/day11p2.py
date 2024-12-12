from functools import cache


def main():
    """
    Entry point for day 11, part 2.

    :return: Exit status
    """

    stones = read_input('input.txt')
    # print(stones)

    total_stones = 0
    blink_count = 75

    for stone in stones:
        total_stones = total_stones + blink_score(stone, blink_count)

    print('Number of stones: ' + str(total_stones))


@cache
def blink_score(stone_number, iterations):
    """
    Calculates the "score" of a stone given a number and iterations
    :param stone_number: Stone number to score
    :param iterations: Number of remaining iterations
    :return: Score of a stone
    """
    if iterations == 0:
        # Base case
        return 1
    else:
        new_stones = []
        if stone_number == 0:
            new_stones.append(1)
        elif len(str(stone_number)) % 2 == 0:
            string_stone = str(stone_number)
            stone_len = len(string_stone)

            new_stones.append(int(string_stone[0:stone_len // 2]))
            new_stones.append(int(string_stone[stone_len // 2:]))

        else:
            new_stones.append(stone_number * 2024)

        stone_score = 0

        for stone in new_stones:
            stone_score = stone_score + blink_score(stone, iterations - 1)

        return stone_score


def process_stone_old(stone_number):
    """
    Processes a blink for a stone number
    :param stone_number:  Number on stone
    :return: List of resulting stones
    """
    new_stones = []
    if stone_number == 0:
        new_stones.append(1)
    elif len(str(stone_number)) % 2 == 0:
        string_stone = str(stone_number)
        stone_len = len(string_stone)

        new_stones.append(int(string_stone[0:stone_len // 2]))
        new_stones.append(int(string_stone[stone_len // 2:]))

    else:
        new_stones.append(stone_number * 2024)

    return new_stones


def read_input(filename):
    """
    Read the input file
    :param filename: Name of input file
    :return: List of starting stone numbers
    """
    with open(filename) as file:
        stones = [line.split(' ') for line in file]

    return [int(x) for x in stones[0]]


if __name__ == "__main__":
    main()
