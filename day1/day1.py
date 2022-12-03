def find_max_calories(f):
    max_calories = [0, 0, 0]

    current_calories = 0
    for line in f:
        if line.isspace():
            if current_calories > max_calories[2]:
                insert_new_max(max_calories, current_calories, 2)

            current_calories = 0
        else:
            current_calories += int(line)

    print("Single elf: " + str(max_calories[0]))
    print("Top three elves: " + str(sum(max_calories)))


def insert_new_max(max_calories, new_value, index_to_check):
    if index_to_check < 0 or index_to_check > 2:
        return

    if max_calories[index_to_check] > new_value:
        return

    # Swap the values down
    temp = max_calories[index_to_check]
    max_calories[index_to_check] = new_value

    if index_to_check + 1 <= 2:
        max_calories[index_to_check + 1] = temp

    if index_to_check - 1 < 0:
        return

    insert_new_max(max_calories, new_value, index_to_check - 1)


find_max_calories(open("input.txt", "r"))
