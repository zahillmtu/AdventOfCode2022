import re


def find_overlaps(f):
    overlap_count = 0

    for line in f:
        overlap = is_overlap(re.findall(r"\d+", line))

        if overlap:
            overlap_count += 1

    print("Total overlaps: " + str(overlap_count))


def is_overlap(elf_records):
    elf1_start = int(elf_records[0])
    elf1_end = int(elf_records[1])
    elf2_start = int(elf_records[2])
    elf2_end = int(elf_records[3])

    if elf2_start <= elf1_start <= elf2_end or elf2_start <= elf1_end <= elf2_end:
        return True

    if elf1_start <= elf2_start <= elf1_end or elf1_start <= elf2_end <= elf1_end:
        return True

    return False


find_overlaps(open("input.txt", "r"))
