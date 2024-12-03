import re


##
# Entry point for Day 3
#
def main():
    # Read input file into string
    with open('input.txt') as file:
        input_text = file.read()

    # Parse input file for mul(), do(), and don't() tokens
    valid_tokens = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", input_text)

    total = 0
    enabled = True

    # Loop through valid
    for i in range(len(valid_tokens)):

        if valid_tokens[i] == "do()":
            enabled = True
            continue

        if valid_tokens[i] == "don't()":
            enabled = False
            continue

        # Only add if instructions are enabled
        if enabled:
            operands = re.findall("[0-9]{1,3}", valid_tokens[i])
            total = total + int(operands[0]) * int(operands[1])

    print(total)


if __name__ == "__main__":
    main()
