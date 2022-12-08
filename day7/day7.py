from DirectoryTree import DirectoryTree
from DirectoryNode import DirectoryNode
import re


def main():
    lines = open("input.txt", "r")
    tree = build_tree(lines)

    print("Total size: " + str(tree.sum_total_file_size_from_root()))

    print("Min to delete: " + str(tree.current_min))


def build_tree(f):
    tree = DirectoryTree(DirectoryNode("/", None))

    for line in f:
        if line.startswith('$'):
            # Command
            command = line[2:4]

            # Can totally ignore the ls command
            if command == "cd":
                tree.change_directory(line[4:].strip())

        elif line.startswith('dir'):
            tree.add_directory(line[4:].strip())

        else:
            # This means it's a number
            file_size = re.search(r'\d+', line)
            file_name = re.search(r'[a-z.]+', line)

            tree.add_file(file_name.group(), int(file_size.group()))

    return tree


if __name__ == "__main__":
    main()
