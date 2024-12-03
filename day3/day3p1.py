import re


##
# Entry point for Day 3
#
def main():
    # Read input file into string
    with open('input.txt') as file:
        input_text = file.read()

    # Parse input file for mul() tokens
    valid_tokens = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", input_text)

    total = 0

    for i in range(len(valid_tokens)):
        operands = re.findall("[0-9]{1,3}", valid_tokens[i])
        total = total + int(operands[0]) * int(operands[1])

    print(total)


if __name__ == "__main__":
    main()
