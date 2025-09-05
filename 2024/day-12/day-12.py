# https://adventofcode.com/2024/day/12


from file.utils import read_file_lines

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant = grid[r][c]
                region = []
                stack = [(r, c)]
                visited[r][c] = True

                while stack:
                    x, y = stack.pop()
                    region.append((x, y))

                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and not visited[nx][ny]
                            and grid[nx][ny] == plant
                        ):
                            visited[nx][ny] = True
                            stack.append((nx, ny))

                regions.append((plant, region))
    return regions


def calculate_region_perimeter(region):
    perimeter = 0
    region_set = set(region)

    for x, y in region:
        for dx, dy in DIRECTIONS:
            if (x + dx, y + dy) not in region_set:
                perimeter += 1

    return perimeter


def count_region_sides(region):
    region_set = set(region)
    sides = 0

    for x, y in region:
        # check vertical sides
        for dx, dy in [(1, 0), (-1, 0)]:
            if (x + dx, y + dy) not in region_set:
                # only count if this is the *start* of a vertical edge
                if (x, y - 1) not in region_set or (x + dx, y - 1) in region_set:
                    sides += 1

        # check horizontal sides
        for dx, dy in [(0, 1), (0, -1)]:
            if (x + dx, y + dy) not in region_set:
                # only count if this is the *start* of a horizontal edge
                if (x - 1, y) not in region_set or (x - 1, y + dy) in region_set:
                    sides += 1

    return sides


def calculate_region_price(region, use_number_of_sides):
    if use_number_of_sides:
        return count_region_sides(region) * len(region)
    return calculate_region_perimeter(region) * len(region)


def main():
    lines = read_file_lines("2024/day-12/day-12-input.txt")
    grid = [line.strip() for line in lines]

    regions = find_regions(grid)

    for use_number_of_sides, label in [
        (False, "perimeter"),
        (True, "counting sides"),
    ]:
        total_price = sum(
            calculate_region_price(region, use_number_of_sides) for _, region in regions
        )
        print(f"The total price (by {label}): {total_price}")


if __name__ == "__main__":
    main()
