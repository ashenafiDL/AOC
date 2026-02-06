import math


def count_digits(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return int(math.log10(n)) + 1


def check_split_equal(num, parts):
    length = count_digits(num)

    s = str(num)

    # cannot split evenly
    if length % parts != 0:
        return False

    size = length // parts
    chunks = [s[i * size : (i + 1) * size] for i in range(parts)]

    # check if all chunks are identical
    return len(set(chunks)) == 1


def part_one(ids):
    sum = 0
    for i in ids:
        length = count_digits(i)
        if length % 2 != 0:
            continue

        if check_split_equal(i, 2):
            sum += i

    print(f"Part 1: {sum}")


def part_two(ids):
    sum = 0
    invalid_ids = []

    for id in ids:
        length = count_digits(id)

        for chunk in range(2, length + 1):
            if check_split_equal(id, chunk) and id not in invalid_ids:
                sum += id
                invalid_ids.append(id)

    print(f"Part 2: {sum}")


def main(lines):
    if not lines or not lines[0].strip():
        print("No input provided")
        return

    id_ranges = lines[0].split(",")

    ids = []
    for id_range in id_ranges:
        start, end = id_range.split("-")

        for i in range(int(start), (int(end) + 1)):
            ids.append(i)

    part_one(ids)
    part_two(ids)
