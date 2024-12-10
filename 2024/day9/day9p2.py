def main():
    """
    Entry point for day 9, part 2
    :return: Exit status
    """

    disk_map = read_input('input.txt')
    ex_disk_map = expand_disk_map(disk_map)

    formatted_map = format_map(ex_disk_map[:])

    # print(disk_map)
    # print(ex_disk_map, flush=True)
    print(formatted_map)

    print('Checksum: ' + str(calculate_checksum(formatted_map)))


def calculate_checksum(formatted_map):
    """
    Calculate check some for given formatted map
    :param formatted_map: Map to get checksum from
    :return: Checksum of map
    """
    checksum = 0
    for i in range(len(formatted_map)):
        if formatted_map[i] == '.':
            continue
        checksum = checksum + i * int(formatted_map[i])

    return checksum


def format_map(disk_map):
    """
    Formats a disk map
    :param disk_map:  Disk map to be formatted
    :return: Formatted version of disk map
    """

    i = len(disk_map) - 1
    while i >= 0:

        current_char = disk_map[i]

        if current_char == '.':
            i = i - 1
            continue

        first_char_idx = disk_map.index(current_char)

        block_size = i - first_char_idx + 1

        # Search for group of '.'s of size `block_size
        move_to_idx = find_open_space(disk_map, block_size)

        if 0 <= move_to_idx < i:
            for j in range(block_size):
                disk_map[move_to_idx + j], disk_map[first_char_idx + j] = disk_map[first_char_idx + j], disk_map[
                    move_to_idx + j]

        i = i - block_size

    return disk_map


def find_open_space(disk_map, size):
    """
    Finds a subarray of periods of length `size`, if it exists
    :param disk_map: Map to search for open space
    :param size: Size of required open space
    :return: Index of start of open space, -1 otherwise

    :cite: https://stackoverflow.com/a/17870684/22181934 - Algorithm to find first index of sublist given list and
    sublist
    """
    l = disk_map
    sl = list(size * '.')

    sll = len(sl)
    for ind in (i for i, e in enumerate(l) if e == sl[0]):
        if l[ind:ind + sll] == sl:
            return ind

    return -1

    # i = 0
    # while i < len(disk_map) - 1:
    #     current_char = disk_map[i]
    #
    #     if current_char == '.':
    #         space = True
    #         for j in range(size):
    #             if i + j < len(disk_map) - 1 and disk_map[i + j] != '.':
    #                 space = False
    #                 i = i + 1
    #                 continue
    #
    #     else:
    #         i = i + 1
    #         continue
    #
    #     if space:
    #         return i
    #
    #     i = i + 1
    #
    # return -1


def find_sub_list(sl, l):
    sll = len(sl)
    for ind in (i for i, e in enumerate(l) if e == sl[0]):
        if l[ind:ind + sll] == sl:
            return ind, ind + sll - 1


def expand_disk_map(disk_map):
    """
    Converts dense disk map format into expanded format

    :param disk_map: Disk map in dense format
    :return: Expanded disk map format
    """

    expanded_format = []
    on_file_length = True
    file_id = 0

    # Loop through each character of dense disk map and convert to expanded form
    for c in disk_map:

        if on_file_length:
            for i in range(c):
                expanded_format.append(str(file_id))

            file_id = file_id + 1
            on_file_length = False
        else:
            if c != 0:
                for i in range(c):
                    expanded_format.append('.')
            on_file_length = True

    return expanded_format


def read_input(filename):
    """
    Read input file into list.

    :param filename: Name of file to read
    :return: List of input data string
    """
    disk_map = []
    with open(filename) as file:
        while True:
            c = file.read(1)
            if not c:
                break
            # disk_map.append(c)
            disk_map.append(int(c))

    return disk_map


if __name__ == "__main__":
    main()
