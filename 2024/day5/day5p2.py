def main():
    """
    Entry point for Day 5, Part 2

    :return: Exit code
    """

    rules, pages = read_input('input.txt')

    correctly_ordered = []

    # Check each page ordering, find the incorrectly ordered pages
    for page in pages:
        page = [int(val) for val in page]

        valid = True

        # Validate each page against each rule
        while not is_correctly_ordered(page, rules):
            valid = False

            for rule in rules:
                rule = [int(val) for val in rule.split('|')]

                if rule[0] in page and rule[1] in page and page.index(rule[0]) > page.index(rule[1]):

                    page = fix_order(page, rule)

        if not valid:
            # After validating each rule, the page will be properly ordered (hopefully)
            correctly_ordered.append(page)

    # Sum the now correctly ordered middle items
    middle_sum = 0
    for page in correctly_ordered:
        middle_sum = middle_sum + page[int((len(page) - 1) / 2)]

    print('Middle number sum: ' + str(middle_sum))


def is_correctly_ordered(page, rules):
    """
    Check if a page update is correctly ordered, given a set of rules
    :param page: Page to check
    :param rules: Rules to validate page against
    :return: True if the page is correctly ordered, false otherwise
    """
    for rule in rules:
        rule = [int(val) for val in rule.split('|')]
        if rule[0] in page and rule[1] in page and page.index(rule[0]) > page.index(rule[1]):
            return False

    return True


def fix_order(page, rule):
    """
    Fix the order of a page update to comply with given rule

    :param page: Page to be correctly ordered
    :param rule: Specific rule causing page to be improperly ordered
    :return: Original page, but in correct order
    """
    page.insert(page.index(rule[1]), page.pop(page.index(rule[0])))
    return page


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
