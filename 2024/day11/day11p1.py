import numpy as np

def main():
    """
    Entry point for day 11, part 1.

    :return: Exit status
    """

    stones = read_input('input.txt')
    # print(stones)

    blink_count = 25

    for count in range(blink_count):
        new_stones = []
        for stone in stones:

            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                string_stone = str(stone)
                stone_len = len(string_stone)

                new_stones.append(int(string_stone[0:stone_len//2]))
                new_stones.append(int(string_stone[stone_len//2:]))

            else:
                new_stones.append(stone * 2024)

        stones = new_stones[:]
        # print(stones)

    print('Number of stones: ' + str(len(stones)))


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
