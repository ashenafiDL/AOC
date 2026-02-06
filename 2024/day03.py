import re


def extract_multipliers(instruction):
    return map(int, re.findall(r"\d+", instruction))


def calculate_result(valid_instructions, condition_enabled=False):
    result = 0
    enabled = True

    for instruction in valid_instructions:
        if instruction.startswith("do()"):
            enabled = True
        elif instruction.startswith("don't()"):
            enabled = False
        elif instruction.startswith("mul") and (enabled or not condition_enabled):
            left, right = extract_multipliers(instruction)
            result += left * right

    return result


def main(lines):
    valid_instructions = []
    for line in lines:
        # Extract lines with the following format: mul(x, y) | do() | don't()
        instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        valid_instructions.extend(instructions)

    print(f"Result: {calculate_result(valid_instructions)}")
    print(
        f"Result (with condition enabled): {
            calculate_result(valid_instructions, condition_enabled=True)
        }"
    )
