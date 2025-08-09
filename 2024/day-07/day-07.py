# https://adventofcode.com/2024/day/7

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
)
from itertools import product

from file.utils import read_file_lines


def get_total_calibration_result(lines, operators):
    total_result = 0

    for line in lines:
        result, inputs = line.split(":")
        inputs = inputs.strip().split(" ")

        length = len(inputs) - 1

        for p in product(operators, repeat=length):
            current_operators = list(p)

            current_result = int(inputs[0])  # start with first number

            for i, op in enumerate(current_operators):
                if op == "+":
                    current_result = current_result + int(inputs[i + 1])
                elif op == "||":
                    current_result = int(f"{current_result}{inputs[i + 1]}")
                elif op == "*":
                    current_result = current_result * int(inputs[i + 1])

            if current_result == int(result):
                total_result += int(result)
                break

    return total_result


def main():
    lines = read_file_lines("2024/day-07/day-07-input.txt")

    without_concatination = get_total_calibration_result(lines, ["+", "*"])
    print(f"Total calibration result: {without_concatination}")

    with_concatination = get_total_calibration_result(lines, ["+", "*", "||"])
    print(f"Total calibration result with concatination: {with_concatination}")


if __name__ == "__main__":
    main()
