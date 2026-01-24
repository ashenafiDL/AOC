# https://adventofcode.com/2024/day/8

from itertools import combinations

from utils.file import read_file_lines


def count_antinode(lines, has_resonance=False):
    cols, rows = len(lines[0].strip()), len(lines)

    frequencies = {}
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != ".":
                frequencies.setdefault(lines[r][c], set()).add((r, c))

    antinodes = set()

    for coords in frequencies.values():
        for (r1, c1), (r2, c2) in combinations(coords, 2):
            dr = r2 - r1
            dc = c2 - c1

            if has_resonance:
                # Add first tower as antinode
                antinodes.add((r1, c1))

                # Mark all points beyond the first point (in opposite direction)
                e1 = (r1 - dr, c1 - dc)
                while 0 <= e1[0] < rows and 0 <= e1[1] < cols:
                    antinodes.add(e1)
                    e1 = (e1[0] - dr, e1[1] - dc)
            else:
                # extend past first point (in opposite direction)
                e1 = (r1 - dr, c1 - dc)
                if 0 <= e1[0] < rows and 0 <= e1[1] < cols:
                    antinodes.add(e1)

            if has_resonance:
                # Add second tower as antinode
                antinodes.add((r2, c2))

                # Mark all points beyond the second point (in same direction)
                e2 = (r2 + dr, c2 + dc)
                while 0 <= e2[0] < rows and 0 <= e2[1] < cols:
                    antinodes.add(e2)
                    e2 = (e2[0] + dr, e2[1] + dc)
            else:
                # extend past second point (same direction)
                e2 = (r2 + dr, c2 + dc)
                if 0 <= e2[0] < rows and 0 <= e2[1] < cols:
                    antinodes.add(e2)

    return len(antinodes)


def main():
    lines = read_file_lines("2024/day-08/day-08-input.txt")

    antinodes = count_antinode(lines)
    antinodes_with_resonance = count_antinode(lines, has_resonance=True)

    print(f"Total antinodes: {antinodes}")
    print(f"Total antinodes with resonance: {antinodes_with_resonance}")


if __name__ == "__main__":
    main()
