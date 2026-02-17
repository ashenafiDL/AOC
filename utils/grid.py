from typing import Iterable, Tuple


DIRECTIONS = {
    "T": (-1, 0),
    "TR": (-1, 1),
    "R": (0, 1),
    "BR": (1, 1),
    "B": (1, 0),
    "BL": (1, -1),
    "L": (0, -1),
    "TL": (-1, -1),
}


def parse_grid(rows: list[str], ignore_chars: set[str] = ""):
    res = set()
    for row, line in enumerate(rows):
        for col, char in enumerate(line.strip()):
            if char in ignore_chars:
                continue
            res.add((row, col))

    return res


def get_adjacent_points(
    point: Tuple[int, int],
    grid,
    directions: Iterable[str] | None = None,
    ignore_dir: Iterable[str] | None = None,
):
    r, c = point
    rows, cols = len(grid), len(grid[0])

    if directions is None:
        directions = DIRECTIONS.keys()
    if ignore_dir:
        directions = [d for d in directions if d not in ignore_dir]

    results = []
    for d in directions:
        dr, dc = DIRECTIONS[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            results.append((nr, nc))

    return results


def replace_grid_items(rows: list[str], replace_pos, replace_with: str):
    replace_pos = set(replace_pos)

    res = []

    for row, line in enumerate(rows):
        new_row = []
        for col, char in enumerate(line):
            if (row, col) in replace_pos:
                new_row.append(replace_with)
            else:
                new_row.append(char)

        res.append("".join(new_row))

    return res
