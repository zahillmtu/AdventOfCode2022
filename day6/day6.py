import queue


def main():
    f = open("input.txt", "r")
    line = [*f.readline()]

    print("Unique sequence at: " + str(find_unique_sequence(line)))


def find_unique_sequence(line):
    last_four = queue.Queue(14)

    for i in range(0, len(line)):
        c = line[i]
        # add char to seq
        if last_four.qsize() < 14:
            last_four.put(c)
        else:
            last_four.get()
            last_four.put(c)

        if last_four.qsize() == 14:
            if check_unique(last_four):
                return i + 1


def check_unique(last_four):

    for i in range(0, 13):
        for j in range(i + 1, 14):
            if last_four.queue[i] == last_four.queue[j]:
                return False

    return True


if __name__ == "__main__":
    main()
