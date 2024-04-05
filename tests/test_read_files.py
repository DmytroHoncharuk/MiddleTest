import pytest
from main import read_files
import os
@pytest.fixture
def create_test_file(tmpdir):
    # Create a temporary test file
    test_file_path = os.path.join(tmpdir, 'test_file.txt')
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("Hello world!\n")
        f.write("This is a test file containing the word \"world\".\n")
        f.write("We want to filter out the lines containing the word \"world\".\n")
        f.write("Let's see if our script can do that.\n")
        f.write("Goodbye world!\n")
    return test_file_path