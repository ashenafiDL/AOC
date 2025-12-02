# https://adventofcode.com/2024/day/11

from collections import Counter

from utils.file import read_file_lines


def transform_stone(stone: int):
    if stone == 0:
        return [1]
    s = str(stone)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        return [int(s[:mid]), int(s[mid:])]
    else:
        return [stone * 2024]


def count_stones(initial: list[int], blinks: int) -> int:
    stones = Counter(initial)
    for _ in range(blinks):
        new_stones = Counter()
        for stone in stones:
            for new_stone in transform_stone(stone):
                new_stones[new_stone] += stones[stone]

        stones = new_stones

    return sum(stones.values())


def main():
    lines = read_file_lines("day-11/day-11-input.txt")
    initial_stones = list(map(int, lines[0].strip().split()))

    count_of_stones = count_stones(initial_stones, 25)
    print(f"After blinking 25 times: {count_of_stones}")

    count_of_stones = count_stones(initial_stones, 75)
    print(f"After blinking 75 times: {count_of_stones}")


if __name__ == "__main__":
    main()
