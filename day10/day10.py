def main():
    lines = open("input.txt", "r")
    print("Total strength: " + str(calculate_signal_strength(lines)))


def calculate_signal_strength(lines):
    cycles = 0
    register = 1
    total_signal_strength = 0

    for operation in lines:
        if operation.startswith("noop"):
            cycles += 1
            if check_cycles(cycles):
                total_signal_strength += register * cycles

        elif operation.startswith("addx"):
            cycles += 1
            if check_cycles(cycles):
                total_signal_strength += register * cycles

            cycles += 1
            if check_cycles(cycles):
                total_signal_strength += register * cycles

            value_to_add = int(operation[5:].strip())
            register += value_to_add

    return total_signal_strength


def check_cycles(cycles):
    if cycles > 220:
        return False

    return cycles - 20 == 0 or (cycles - 20) % 40 == 0


if __name__ == "__main__":
    main()
