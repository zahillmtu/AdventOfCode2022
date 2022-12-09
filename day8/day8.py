

def main():
    lines = open("input.txt", "r")
    grid = load_grid(lines)
    print("Total visible: " + str(count_visible(grid)))


def load_grid(f):
    grid = []

    for line in f:
        row = [*line.strip()]
        grid.append(row)

    return grid


def count_visible(grid):
    total_visible = 0

    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if is_visible(grid, row, col):
                total_visible += 1

    return total_visible


def is_visible(grid, row, col):
    if is_visible_from_left(grid, row, col) or is_visible_from_right(grid, row, col)\
            or is_visible_from_top(grid, row, col) or is_visible_from_bottom(grid, row, col):
        return True

    return False


def is_visible_from_left(grid, row, col):
    if col == 0:
        return True

    for left_index in range(0, col):
        if grid[row][left_index] >= grid[row][col]:
            return False

    return True


def is_visible_from_right(grid, row, col):
    if col + 1 == len(grid[row]):
        # On the edge
        return True

    for right_index in range(col + 1, len(grid[row])):
        if grid[row][right_index] >= grid[row][col]:
            return False

    return True


def is_visible_from_top(grid, row, col):
    if row == 0:
        return True

    for top_index in range(0, row):
        if grid[top_index][col] >= grid[row][col]:
            return False

    return True


def is_visible_from_bottom(grid, row, col):
    if row + 1 == len(grid):
        # at bottom
        return True

    for bottom_index in range(row + 1, len(grid)):
        if grid[bottom_index][col] >= grid[row][col]:
            return False

    return True


if __name__ == "__main__":
    main()
