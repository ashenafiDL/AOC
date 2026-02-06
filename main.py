from datetime import datetime
import sys
from importlib import import_module


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <year> <day>")
        sys.exit(1)

    year, day = sys.argv[1], sys.argv[2].zfill(2)  # pad day with 0
    module_path = f"{year}.day{day}"

    try:
        with open(f"{year}/inputs/day{day}.txt", "r") as f:
            input_data = f.readlines()
    except FileNotFoundError:
        print("Input file not found")
        sys.exit(1)

    try:
        module = import_module(module_path)
    except ModuleNotFoundError:
        print(f"Solution not found: {module_path}")
        sys.exit(1)

    if hasattr(module, "main"):
        start_time = datetime.now()
        module.main(input_data)
        end_time = datetime.now()

        duration = end_time - start_time
        print(f"\nTook {duration.total_seconds():.3f} seconds")
    else:
        print(f"Module {module_path} has no `main()` function.")


if __name__ == "__main__":
    main()
