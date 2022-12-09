

def main():
    lines = open("input.txt", "r")
    grid = load_grid(lines)
    print("Most scenic: " + str(find_most_scenic(grid)))


def load_grid(f):
    grid = []

    for line in f:
        row = [*line.strip()]
        grid.append(row)

    return grid


def find_most_scenic(grid):
    highest_value = 0

    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            tree_value = find_tree_value(grid, row, col)

            if tree_value > highest_value:
                highest_value = tree_value

    return highest_value


def find_tree_value(grid, row, col):
    return left_value(grid, row, col) * right_value(grid, row, col) \
        * up_value(grid, row, col) * down_value(grid, row, col)


def left_value(grid, row, col):
    if col == 0:
        return 0

    seeable_trees = 0

    for left_index in reversed(range(0, col)):
        current_value = int()
        if grid[row][left_index] >= grid[row][col]:
            seeable_trees += 1
            return seeable_trees

        seeable_trees += 1

    return seeable_trees


def right_value(grid, row, col):
    if col + 1 == len(grid[row]):
        # On the edge
        return 0

    seeable_trees = 0

    for right_index in range(col + 1, len(grid[row])):
        if grid[row][right_index] >= grid[row][col]:
            seeable_trees += 1
            return seeable_trees

        seeable_trees += 1

    return seeable_trees


def up_value(grid, row, col):
    if row == 0:
        return 0

    seeable_trees = 0

    for top_index in reversed(range(0, row)):
        if grid[top_index][col] >= grid[row][col]:
            seeable_trees += 1
            return seeable_trees

        seeable_trees += 1

    return seeable_trees


def down_value(grid, row, col):
    if row + 1 == len(grid):
        # at bottom
        return 0

    seeable_trees = 0

    for bottom_index in range(row + 1, len(grid)):
        if grid[bottom_index][col] >= grid[row][col]:
            seeable_trees += 1
            return seeable_trees

        seeable_trees += 1

    return seeable_trees


if __name__ == "__main__":
    main()
