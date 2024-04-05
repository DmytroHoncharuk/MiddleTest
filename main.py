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

