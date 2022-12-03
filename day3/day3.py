

def calculate_priority_sum(f):
    total_sum = 0

    for line in f:
        compartment = line.strip()
        compartment_size = int(len(compartment) / 2)

        first_compartment = compartment[0:compartment_size]
        second_compartment = compartment[compartment_size:len(compartment)]

        for c in first_compartment:
            found_index = second_compartment.find(c)

            if found_index != -1:
                if c.islower():
                    total_sum += ord(c) - 96
                else:
                    total_sum += ord(c) - 38
                break

    print("Total sum: " + str(total_sum))


calculate_priority_sum(open("input.txt", "r"))
