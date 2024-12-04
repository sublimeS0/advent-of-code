def main():
    """
    Entry point for Day 4, Part 1

    :return: Exit code
    """
    # Read input file into string
    with open('input.txt') as file:
        word_search_list = [list(line.strip()) for line in file]

    xmas_count = 0

    # Loop through each character to use as start location
    for i in range(len(word_search_list)):

        for j in range(len(word_search_list[i])):

            # For each letter, check all 8 directions for XMAS
            if check_horizontal_right(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_horizontal_left(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_vertical_down(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_vertical_up(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_diag_down_right(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_diag_down_left(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_diag_up_right(i, j, word_search_list):
                xmas_count = xmas_count + 1

            if check_diag_up_left(i, j, word_search_list):
                xmas_count = xmas_count + 1

    print('XMAS count: ' + str(xmas_count))


def check_horizontal_right(r, c, board):
    """
    Check for words written horizontally and to the right

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """

    if c + 4 > len(board[r]):
        return False

    if board[r][c] == 'X' and board[r][c + 1] == 'M' and board[r][c + 2] == 'A' and board[r][c + 3] == 'S':
        return True

    return False


def check_horizontal_left(r, c, board):
    """
    Check for words written horizontally and to the left

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if c - 3 < 0:
        return False

    if board[r][c] == 'X' and board[r][c - 1] == 'M' and board[r][c - 2] == 'A' and board[r][c - 3] == 'S':
        return True

    return False


def check_vertical_down(r, c, board):
    """
    Check for words written vertically and downward

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if r + 4 > len(board):
        return False

    if board[r][c] == 'X' and board[r + 1][c] == 'M' and board[r + 2][c] == 'A' and board[r + 3][c] == 'S':
        return True

    return False


def check_vertical_up(r, c, board):
    """
    Check for words written vertically and upward

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if r - 3 < 0:
        return False

    if board[r][c] == 'X' and board[r - 1][c] == 'M' and board[r - 2][c] == 'A' and board[r - 3][c] == 'S':
        return True

    return False


def check_diag_down_right(r, c, board):
    """
    Check for words written diagonally and down/right

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if c + 4 > len(board[r]) or r + 4 > len(board):
        return False

    if board[r][c] == 'X' and board[r + 1][c + 1] == 'M' and board[r + 2][c + 2] == 'A' and board[r + 3][c + 3] == 'S':
        return True

    return False


def check_diag_down_left(r, c, board):
    """
    Check for words written diagonally and down/left

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if c - 3 < 0 or r + 4 > len(board):
        return False

    if board[r][c] == 'X' and board[r + 1][c - 1] == 'M' and board[r + 2][c - 2] == 'A' and board[r + 3][c - 3] == 'S':
        return True

    return False


def check_diag_up_right(r, c, board):
    """
    Check for words written diagonally and up/right

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if c + 4 > len(board[r]) or r - 3 < 0:
        return False

    if board[r][c] == 'X' and board[r - 1][c + 1] == 'M' and board[r - 2][c + 2] == 'A' and board[r - 3][c + 3] == 'S':
        return True

    return False


def check_diag_up_left(r, c, board):
    """
    Check for words written diagonally and up/left

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if c - 3 < 0 or r - 3 < 0:
        return False

    if board[r][c] == 'X' and board[r - 1][c - 1] == 'M' and board[r - 2][c - 2] == 'A' and board[r - 3][c - 3] == 'S':
        return True

    return False


if __name__ == "__main__":
    main()
