# Every line is a single elf
# Elves are in groups of 3
# Find the item that is the same between all elves

def calculate_priority_sum(f):
    lines = f.readlines()
    total_sum = 0

    for x in range(0, len(lines), 3):
        first_elf = lines[x].strip()
        second_elf = lines[x+1].strip()
        third_elf = lines[x+2].strip()

        for c in first_elf:
            found_in_second_index = second_elf.find(c)

            if found_in_second_index != -1:
                found_in_third_index = third_elf.find(c)

                if found_in_third_index != -1:
                    if c.islower():
                        total_sum += ord(c) - 96
                    else:
                        total_sum += ord(c) - 38
                    break

    print("Total sum: " + str(total_sum))


calculate_priority_sum(open("input.txt", "r"))
