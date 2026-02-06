def is_in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def search_word(grid, x, y, word):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0

    for dx, dy in directions:
        if all(
            is_in_bounds(grid, x + i * dx, y + i * dy)
            and grid[x + i * dx][y + i * dy] == word[i]
            for i in range(len(word))
        ):
            count += 1

    return count


def search_x_mas(grid, x, y):
    _set = {"M", "S"}
    if {grid[x - 1][y - 1], grid[x + 1][y + 1]} == _set and {
        grid[x - 1][y + 1],
        grid[x + 1][y - 1],
    } == _set:
        return True


def main(lines):
    grid = []
    for line in lines:
        row = [x for x in line.strip()]
        grid.append(row)

    word = "XMAS"
    count = sum(
        search_word(grid, row, col, word)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == word[0]
    )
    print(f"The word {word} appeared {count} times")

    second_count = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if grid[row][col] == "A":
                second_count += 1 if search_x_mas(grid, row, col) else 0

    print(f"The word X-MAS appeared {second_count} times")
