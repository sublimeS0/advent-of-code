def main():
    """
    Entry point for day 17, part 1

    6,4,6,0,7,6,2,0,0 - wrong
    5,0,3,5,7,6,1,5,4 - correct

    :return: Exit code
    """
    register_a, register_b, register_c, command_list = read_input('input_ex_pt2.txt')
    output = process_instructions(register_a, register_b, register_c, command_list)

    print(','.join(map(str, output)))


def process_instructions(register_a, register_b, register_c, command_list):
    INST_ADV = 0
    INST_BXL = 1
    INST_BST = 2
    INST_JNZ = 3
    INST_BXC = 4
    INST_OUT = 5
    INST_BDV = 6
    INST_CDV = 7

    inst_pointer = 0

    output = []

    while inst_pointer < len(command_list):
        inst = command_list[inst_pointer]
        operand = command_list[inst_pointer + 1]

        inst_inc = True

        # INST_ADV
        if inst == INST_ADV:
            register_a = dv(register_a, register_b, register_c, operand)

        # INST_BXL
        elif inst == INST_BXL:
            register_b = bxl(register_b, operand)

        # INST_BST
        elif inst == INST_BST:
            register_b = bst(register_a, register_b, register_c, operand)

        # INST_JNZ
        elif inst == INST_JNZ:
            inst_pointer, inst_inc = jnz(register_a, operand, inst_pointer)

        # INST_BXC
        elif inst == INST_BXC:
            register_b = bxc(register_b, register_c)

        # INST_OUT
        elif inst == INST_OUT:
            output.append(out(register_a, register_b, register_c, operand))

        # INST_BDV
        elif inst == INST_BDV:
            register_b = dv(register_a, register_b, register_c, operand)  # Re-use adv code, just store in register b

        # INST_CDV
        elif inst == INST_CDV:
            register_c = dv(register_a, register_b, register_c, operand)  # Re-use adv code, just store in register b

        if inst_inc:
            inst_pointer += 2

    return output


def out(register_a, register_b, register_c, operand):
    """
    Executes `out` instruction

    :param register_a: Value in register a
    :param register_b: Value in register b
    :param register_c: Value in register c
    :param operand: Current operand
    :return: None
    """

    # Handle combo operators
    if operand == 4:
        operand = register_a
    elif operand == 5:
        operand = register_b
    elif operand == 6:
        operand = register_c

    return operand % 8


def bxc(register_b, register_c):
    """
    Executes `bxc` instruction

    :param register_b: Value in register b
    :param register_c: Value in register c
    :return: Result of bitwise xor, to be stored in register b
    """
    return register_b ^ register_c


def jnz(register_a, operand, inst_pointer):
    """
    Executes `jnz` instruction

    :param register_a: Value in register a
    :param operand: Current operand
    :param inst_pointer: Value of instruction pointer
    :return: New value of instruction pointer, True if instruction pointer should still be incremented, false otherwise
    """
    if register_a == 0:
        return inst_pointer, True

    return operand, False


def bst(register_a, register_b, register_c, operand):
    """
    Executes `bst` instruction

    :param operand: Current operand
    :return: Result of modulus division, to be stored in register b
    """

    # Handle combo operators
    if operand == 4:
        operand = register_a
    elif operand == 5:
        operand = register_b
    elif operand == 6:
        operand = register_c

    return operand % 8


def bxl(register_b, operand):
    """
    Executes `bxl` instruction

    :param register_b: Value in register b
    :param operand: Current operand
    :return: Result of bitwise xor, to be placed in register b
    """

    return register_b ^ operand


def dv(register_a, register_b, register_c, operand):
    """
    Executes `adv` instruction

    :param register_a: Value in register a
    :param register_b: Value in register b
    :param register_c: Value in register c
    :param operand: Current operand
    :return: Result of division, to be placed in register a
    """

    # Handle combo operators
    if operand == 4:
        operand = register_a
    elif operand == 5:
        operand = register_b
    elif operand == 6:
        operand = register_c

    return register_a // (2 ** operand)


def read_input(filename):
    with open(filename, 'r') as file:
        register_a = file.readline().strip()
        register_b = file.readline().strip()
        register_c = file.readline().strip()

        file.readline()  # Skip newline

        command_list = file.readline()

    register_a = int(register_a[register_a.index(': ') + 2:])
    register_b = int(register_b[register_b.index(': ') + 2:])
    register_c = int(register_c[register_c.index(': ') + 2:])

    command_list = [int(item) for item in command_list[command_list.index(' ') + 1:].split(',')]

    return register_a, register_b, register_c, command_list


if __name__ == "__main__":
    main()
