def main():
    """
    Entry point for day 9, part 1
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
            break
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
        try:
            first_space = disk_map.index('.')
        except ValueError:
            break

        if first_space >= i:
            break

        if current_char != '.':
            disk_map[i], disk_map[first_space] = disk_map[first_space], disk_map[i]

        i = i - 1

    return disk_map


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
