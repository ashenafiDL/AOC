# https://adventofcode.com/2024/day/9

import networkx as nx

from file.utils import read_file_lines


def generate_trails(map):
    rows, cols = len(map), len(map[0])

    graph = nx.DiGraph()

    trailheads = set()
    trailtails = set()

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 0:
                trailheads.add((r, c))
            elif map[r][c] == 9:
                trailtails.add((r, c))

            # Up
            if r - 1 >= 0:
                if map[r - 1][c] == map[r][c] + 1:
                    graph.add_edge((r, c), (r - 1, c))

            # Right
            if c + 1 < cols:
                if map[r][c + 1] == map[r][c] + 1:
                    graph.add_edge((r, c), (r, c + 1))

            # Down
            if r + 1 < rows:
                if map[r + 1][c] == map[r][c] + 1:
                    graph.add_edge((r, c), (r + 1, c))

            # Left
            if c - 1 >= 0:
                if map[r][c - 1] == map[r][c] + 1:
                    graph.add_edge((r, c), (r, c - 1))

    return graph, trailheads, trailtails


def calculate_trail_score(trail, trailheads, trailtails):
    trailscore = 0

    for head in trailheads:
        reachable_tails = set()
        for tail in trailtails:
            if nx.has_path(trail, head, tail):
                reachable_tails.add(tail)
        trailscore += len(reachable_tails)

    return trailscore


def calculate_trail_rating(trail, trailheads, trailtails):
    paths = []

    for head in trailheads:
        for tail in trailtails:
            paths.extend(nx.all_simple_paths(trail, head, tail))

    return len(paths)


def main():
    lines = read_file_lines("2024/day-10/day-10-input.txt")

    # Convert into list of numbers
    nums = [[int(ch) for ch in line.strip()] for line in lines]

    trail, trailheads, trailtails = generate_trails(nums)

    score = calculate_trail_score(trail, trailheads, trailtails)
    print(f"*Score* : {score}")

    rating = calculate_trail_rating(trail, trailheads, trailtails)
    print(f"*Rating*: {rating}")


if __name__ == "__main__":
    main()
