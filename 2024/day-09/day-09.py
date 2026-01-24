# https://adventofcode.com/2024/day/9

from utils.file import read_file_lines


def calculate_checksum(filesystem):
    checksum = 0
    for i, j in enumerate(filesystem):
        if j != ".":
            checksum += i * int(filesystem[i])

    return checksum


def parse_filesystem(filesystem):
    new_filesystem = []
    file_id = 0

    # Create new filesystem with blocks of files and empty spaces
    for i, j in enumerate(filesystem):
        if i % 2 == 0:
            new_filesystem.extend([str(file_id)] * int(filesystem[i]))
            file_id += 1
        else:
            new_filesystem.extend("." * int(filesystem[i]))

    return new_filesystem


def move_block(filesystem):
    # Move file blocks to the left
    left, right = 0, len(filesystem) - 1
    while left < right:
        if filesystem[left] != ".":
            left += 1
            continue
        if filesystem[right] == ".":
            right -= 1
            continue

        # now temp[left] is "." and temp[right] is a file block
        filesystem[left] = filesystem[right]
        filesystem[right] = "."
        left += 1
        right -= 1

    return filesystem


def get_checksum(filesystem):
    new_filesystem = parse_filesystem(filesystem)
    new_filesystem = move_block(new_filesystem)

    return calculate_checksum(new_filesystem)


def part_two(filesystem):
    # Parse filesystem
    chunks = []
    file_id = 0
    for i, ch in enumerate(filesystem):
        length = int(ch)
        if i % 2 == 0:
            chunks.append((str(file_id), length))
            file_id += 1
        else:
            chunks.append((".", length))

    # Move files
    i = len(chunks) - 1
    while i >= 0:
        file_id, length = chunks[i]
        if file_id != ".":
            # Look for leftmost gap
            for j in range(i):
                gap_id, gap_length = chunks[j]
                if gap_id == "." and gap_length >= length:
                    # move file to gap
                    chunks[j] = (file_id, length)
                    remaining_gap = gap_length - length

                    # Remove the old file chunk
                    del chunks[i]

                    # Add the remaining gap
                    if remaining_gap > 0:
                        chunks.insert(j + 1, (".", remaining_gap))

                    # Add the new gap where the file was
                    chunks.insert(i, (".", length))

                    # Since we modified the list, we should increase the right most index by 1
                    i += 1

                    break
        i -= 1

    # Flatten chunks and calculate checksum
    new_filesystem = []
    for id_val, size in chunks:
        if id_val != ".":
            for _ in range(size):
                new_filesystem.append(int(id_val))
        else:
            for _ in range(size):
                new_filesystem.append(None)  # Using None for free space

    checksum = 0
    for idx, file_id in enumerate(new_filesystem):
        if file_id is not None:
            checksum += idx * file_id

    return checksum


def main():
    lines = read_file_lines("2024/day-09/day-09-input.txt")

    input = lines[0].strip()  # the input for this puzzle is a single, very long line

    checksum_block = get_checksum(input)
    print(f"The resulting filesystem checksum (block): {checksum_block}")

    checksum_file = part_two(input)
    print(f"The resulting filesystem checksum  (file): {checksum_file}")


if __name__ == "__main__":
    main()
