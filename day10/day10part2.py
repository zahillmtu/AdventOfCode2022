def main():
    lines = open("input.txt", "r")
    draw_pixels(lines)


def draw_pixels(lines):
    cycles = 0
    register = 0  # draw pixel if register in range
    pixel_position = 0

    for operation in lines:
        if operation.startswith("noop"):

            pixel_position = print_pixel(pixel_position, register)

            cycles += 1

        elif operation.startswith("addx"):

            pixel_position = print_pixel(pixel_position, register)

            cycles += 1

            pixel_position = print_pixel(pixel_position, register)

            cycles += 1

            value_to_add = int(operation[5:].strip())
            register += value_to_add


def print_pixel(pixel_position, register):
    if register <= pixel_position <= register + 2:
        print('#', end='')
    else:
        print('.', end='')

    pixel_position += 1
    if pixel_position >= 40:
        pixel_position = 0
        print()

    return pixel_position


def check_cycles(cycles):
    if cycles > 220:
        return False

    return cycles - 20 == 0 or (cycles - 20) % 40 == 0


if __name__ == "__main__":
    main()
