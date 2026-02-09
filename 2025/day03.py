def find_max(bank: str, batteries: int) -> str:
    if batteries == 1:
        return max(bank)

    first_digit = max(bank[: -(batteries - 1)])
    i = bank.index(first_digit)

    return first_digit + find_max(bank[i + 1 :], batteries - 1)


def main(lines):
    part_one = sum(int(find_max(line.strip(), 2)) for line in lines)
    print(f"Part one: {part_one}")

    part_two = sum(int(find_max(line.strip(), 12)) for line in lines)
    print(f"Part two: {part_two}")
