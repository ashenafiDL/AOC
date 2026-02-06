def part_one(lines):
    pos = 50
    count = 0

    for line in lines:
        dir = line[0]
        step = int(line[1:])
        abs_dist = step % 100

        pos += abs_dist if dir == "R" else -abs_dist

        if pos % 100 == 0:
            count += 1

    print(f"Part 1 password: {count}")


def part_two(lines):
    pos = 50
    count = 0

    for line in lines:
        dir = line[0]
        step = int(line[1:])

        for _ in range(step):
            pos += 1 if dir == "R" else -1

            if pos % 100 == 0:
                count += 1

    print(f"Part 2 password: {count}")


def main(lines):
    part_one(lines)
    part_two(lines)
