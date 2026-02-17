from utils.grid import parse_grid, get_adjacent_points, replace_grid_items


def is_accessible(grid, rolls, point):
    num_adjacent = 0
    for n in get_adjacent_points(point, grid):
        if n in rolls:
            num_adjacent += 1

    return num_adjacent < 4


def part_one(lines):
    rolls = parse_grid(lines, ignore_chars=".")
    accessible = [roll for roll in rolls if is_accessible(lines, rolls, roll)]
    print(f"Part one: {len(accessible)}")


def part_two(lines):
    rolls = parse_grid(lines, ignore_chars=".")

    total = 0

    while True:
        accessible = [roll for roll in rolls if is_accessible(lines, rolls, roll)]

        if len(accessible) == 0:
            break

        total += len(accessible)

        lines = replace_grid_items(lines, accessible, ".")
        rolls = parse_grid(lines, ignore_chars=".")

    print(f"Part two: {total}")


def main(lines):
    part_one(lines)
    part_two(lines)
