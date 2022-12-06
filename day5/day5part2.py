import re


def load_stacks(f):
    stacks = [[] for _ in range(9)]

    for line in reversed(f.readlines()):
        boxes = re.findall(r"\[[A-Z]]|\s{4}", line)

        if len(boxes) < 9:
            for x in range(len(boxes), 9):
                boxes.append("   ")

        for x in range(0, 9):
            if not boxes[x].isspace():
                stacks[x].append(boxes[x])

    return stacks


def make_moves_in_order(f, stacks):
    for line in f:
        move_numbers = re.findall(r"\d+", line)
        num_to_move = int(move_numbers[0])
        donor_stack = stacks[int(move_numbers[1])-1]
        target_stack = stacks[int(move_numbers[2])-1]

        stack_to_move = donor_stack[len(donor_stack) - num_to_move:]
        for item in stack_to_move:
            target_stack.append(item)

        del donor_stack[len(donor_stack) - num_to_move:]

    for stack in stacks:
        print(stack[len(stack) - 1] + " ", end='')


loaded_stacks = load_stacks(open("stack_input.txt", "r"))
make_moves_in_order(open("movement_input.txt", "r"), loaded_stacks)
