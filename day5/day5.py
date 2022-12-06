import queue
import re


def load_stacks(f):
    stacks = [queue.LifoQueue()] * 9

    for line in reversed(f.readlines()):
        boxes = re.findall(r"\[[A-Z]]|\s{4}", line)

        if len(boxes) < 9:
            for x in range(len(boxes), 9):
                boxes.append("   ")

        for x in range(0, 9):
            if not boxes[x].isspace():
                stacks[x].put(boxes[x])

    return stacks


def make_moves(f, stacks):
    for line in f:
        move_numbers = re.findall(r"\d+", line)
        num_to_move = int(move_numbers[0])
        donor_stack = stacks[int(move_numbers[1])-1]
        target_stack = stacks[int(move_numbers[2])-1]

        for x in range(0, num_to_move):
            target_stack.put(donor_stack.get())

    for stack in stacks:
        print(stack.get() + " ", end='')


loaded_stacks = load_stacks(open("stack_input.txt", "r"))
make_moves(open("movement_input.txt", "r"), loaded_stacks)
