from itertools import product


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


def main(lines):
    without_concatenation = get_total_calibration_result(lines, ["+", "*"])
    print(f"Total calibration result: {without_concatenation}")

    with_concatenation = get_total_calibration_result(lines, ["+", "*", "||"])
    print(f"Total calibration result with concatenation: {with_concatenation}")
