# https://adventofcode.com/2024/day/2

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
)
from file.utils import read_file_lines


def is_safe(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if all(1 <= abs(diff) <= 3 for diff in diffs):
        if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
            return True
    return False


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports(data, dampener=False):
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if dampener:
            if is_safe_with_dampener(report):
                safe_count += 1
        else:
            if is_safe(report):
                safe_count += 1
    return safe_count


def main():
    lines = read_file_lines("2024/day-02/day-02-input.txt")

    safe_count = count_safe_reports(lines)
    safe_count_with_dampener = count_safe_reports(lines, dampener=True)

    print(f"Safe Reports: {safe_count}")
    print(f"Safe Reports with Dampener: {safe_count_with_dampener}")


if __name__ == "__main__":
    main()
