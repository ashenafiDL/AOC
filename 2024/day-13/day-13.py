# https://adventofcode.com/2024/day/13

import re
from dataclasses import dataclass

from numpy import linalg

from utils.file import read_file_lines

CORRECTION_VALUE = 10_000_000_000_000


@dataclass
class ClawMachine:
    A: tuple[int, int]
    B: tuple[int, int]
    Prize: tuple[int, int]


def parse_machines(lines, use_correction=False):
    machines = []

    # remove blank lines
    blocks = [line for line in lines if line.strip()]

    for i in range(0, len(blocks), 3):
        a_line, b_line, prize_line = blocks[i : i + 3]

        ax, ay = map(int, re.findall(r"\d+", a_line))
        bx, by = map(int, re.findall(r"\d+", b_line))
        px, py = map(int, re.findall(r"\d+", prize_line))

        machines.append(
            ClawMachine(
                A=(ax, ay),
                B=(bx, by),
                Prize=(
                    px + CORRECTION_VALUE if use_correction else px,
                    py + CORRECTION_VALUE if use_correction else py,
                ),
            )
        )

    return machines


def calculate_number_of_token(machines, use_correction=False):
    total_tokens = 0
    for machine in machines:
        a, b = linalg.solve(
            [[machine.A[0], machine.B[0]], [machine.A[1], machine.B[1]]],
            list(machine.Prize),
        )

        # Check if a and b are integers, since a and b are number of moves they can't fractions
        if round(a, 2).is_integer() and round(b, 2).is_integer():
            # Also check if the number are greater than 0 (also number of moves cannot be negative)
            if a >= 0 and b >= 0:
                # when using correction value the moves can be more than 100
                if use_correction or (a <= 100 and b <= 100):
                    token_a = a * 3
                    token_b = b
                    total_tokens += token_a + token_b

    return total_tokens


def main():
    lines = read_file_lines("2024/day-13/day-13-input.txt")

    # Part 1
    machines = parse_machines(lines)
    tokens = calculate_number_of_token(machines)
    print(f"Number of token to spend: {tokens}")

    # Part 2: Apply correction value to prizes
    for m in machines:
        m.Prize = (m.Prize[0] + CORRECTION_VALUE, m.Prize[1] + CORRECTION_VALUE)

    tokens_with_correction = calculate_number_of_token(machines, use_correction=True)
    print(f"Number of token to spend (with correction): {tokens_with_correction}")


if __name__ == "__main__":
    main()
