def main():
    """
    Entry point for Day 4, Part 2

    :return: Exit code
    """
    # Read input file into string
    with open('input.txt') as file:
        word_search_list = [list(line.strip()) for line in file]

    xmas_count = 0

    # Loop through each character to use as start location
    for r in range(len(word_search_list)):

        for c in range(len(word_search_list[r])):

            # For each letter, search for diagonal "MAS"s
            # If one is found, search for the other relevant diagonals
            if check_diag_down_right(r, c, word_search_list):

                if check_diag_down_left(r, c + 2, word_search_list) or check_diag_up_right(r + 2, c, word_search_list):
                    xmas_count = xmas_count + 1

            if check_diag_down_left(r, c, word_search_list):

                if check_diag_up_left(r + 2, c, word_search_list):
                    xmas_count = xmas_count + 1

            if check_diag_up_right(r, c, word_search_list):

                if check_diag_up_left(r, c + 2, word_search_list):
                    xmas_count = xmas_count + 1

            # if check_diag_up_left(i, j, word_search_list):
            #
            #     if check_diag_down_left(i, j, word_search_list) or check_diag_up_right(i, j, word_search_list):
            #         xmas_count = xmas_count + 1

    print('XMAS count: ' + str(xmas_count))


def check_diag_down_right(r, c, board):
    """
    Check for words written diagonally and down/right

    :param r:       Row ID of start square
    :param c:       Column ID of start square
    :param board:   Word search board to check
    :return:        True if word found in orientation from starting point, false otherwise
    """
    if c + 3 > len(board[r]) or r + 3 > len(board):
        return False

    if board[r][c] == 'M' and board[r + 1][c + 1] == 'A' and board[r + 2][c + 2] == 'S':
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
    if c - 2 < 0 or r + 3 > len(board):
        return False

    if board[r][c] == 'M' and board[r + 1][c - 1] == 'A' and board[r + 2][c - 2] == 'S':
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
    if c + 3 > len(board[r]) or r - 2 < 0:
        return False

    if board[r][c] == 'M' and board[r - 1][c + 1] == 'A' and board[r - 2][c + 2] == 'S':
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
    if c - 2 < 0 or r - 2 < 0:
        return False

    if board[r][c] == 'M' and board[r - 1][c - 1] == 'A' and board[r - 2][c - 2] == 'S':
        return True

    return False


if __name__ == "__main__":
    main()
