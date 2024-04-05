def read_files(file_path: str) -> str:
    """
    Read the contents of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str or None: The contents of the text file if it exists, None otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found.")
        return None

def write_to_file(lines, output_file):
    """
    Write lines to a text file.

    Args:
        lines (list of str): The list of lines to be written to the output file.
        output_file (str): The name of the output text file.

    Returns:
        None

    Raises:
        IOError: If an error occurs while writing to the output file.
    """
    try:
        with open(output_file, 'w') as f_out:
            f_out.writelines(lines)
    except IOError:
        print(f"Error writing to file '{output_file}'.")

