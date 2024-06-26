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


def filter_lines(input_file, keyword):
    """
    Filter lines containing a specified keyword from a text file and write them to a new file.

    Args:
        input_file (str): The name of the input text file (with .txt extension).
        keyword (str): The keyword used for filtering lines.
        output_file (str): The name of the output text file where filtered lines will be written.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified input file is not found.
    """
    try:
        with open(input_file, 'r') as f_in:
            lines = f_in.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    filtered_lines = [line for line in lines if keyword in line]
    return filtered_lines

def main():
    input_file = input("Enter the input file name (with .txt extension): ")
    keyword = input("Enter the keyword to filter lines: ")
    output_file = "filtered.txt"

    filtered_lines = filter_lines(input_file, keyword)
    if filtered_lines:
        write_to_file(filtered_lines, output_file)
        print(f"Filtered lines containing '{keyword}' have been written to '{output_file}'.")
    else:
        print(f"No lines containing '{keyword}' found in the file.")

if __name__ == "__main__":
    main()