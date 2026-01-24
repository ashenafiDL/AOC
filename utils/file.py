def read_file_lines(file_path):
    """
    Reads a file and returns its lines.

    :param file_path: Path to the file to be read.
    :return: List of lines from the file.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines
