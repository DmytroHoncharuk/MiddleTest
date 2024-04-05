import os
import pytest

from main import write_to_file  # Replace 'your_module' with the actual module name


@pytest.fixture
def temp_output_file(tmpdir):
    return os.path.join(tmpdir, 'output.txt')


@pytest.mark.parametrize("lines, expected_content", [
    (["Line 1\n", "Line 2\n", "Line 3\n"], "Line 1\nLine 2\nLine 3\n"),
    ([], ""),
    (["Single line\n"], "Single line\n")
])
def test_write_to_file(temp_output_file, lines, expected_content):
    # Call the write_to_file function
    write_to_file(lines, temp_output_file)

    # Check if the file is created and contains the expected content
    assert os.path.exists(temp_output_file)
    with open(temp_output_file, 'r') as f:
        assert f.read() == expected_content


def test_write_to_file_error_handling(temp_output_file):

    invalid_file_path = os.path.join(temp_output_file, 'invalid_folder', 'output.txt')

    assert write_to_file(["Test line\n"], invalid_file_path) == None

