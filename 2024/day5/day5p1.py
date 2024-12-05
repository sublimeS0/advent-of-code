def main():
    """
    Entry point for Day 5, Part 1

    :return: Exit code
    """

    rules, pages = read_input('input.txt')

    correctly_ordered = []

    # Check each page ordering
    for page in pages:
        page.reverse()
        page = [int(val) for val in page]

        valid_page = True

        # Validate each page against each rule
        for rule in rules:
            rule = [int(val) for val in rule.split('|')]

            if rule[0] in page and rule[1] in page and page.index(rule[0]) < page.index(rule[1]):
                valid_page = False

        if valid_page:
            page.reverse()  # Get page back in correct order for readability
            correctly_ordered.append(page)

    # Sum middle items
    middle_sum = 0
    for page in correctly_ordered:
        middle_sum = middle_sum + page[int((len(page) - 1) / 2)]

    print('Middle number sum: ' + str(middle_sum))


def read_input(filename):
    """
    Read input file into relevant variables

    :param filename: Name of input file
    :return: rules, pages: Variables containing the ordering rules and page updates
    """
    with open(filename) as file:
        rules = [line.strip() for line in file if "|" in line]

    with open(filename) as file:
        pages = [line.strip().split(',') for line in file if "," in line]

    return rules, pages


if __name__ == "__main__":
    main()
