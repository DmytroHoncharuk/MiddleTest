import pytest
from main import read_files
import os


@pytest.fixture
def create_test_file(tmpdir):
    test_file_path = os.path.join(tmpdir, 'test_file.txt')
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("Hello world!\n")
        f.write("This is a test file containing the word \"world\".\n")
        f.write("We want to filter out the lines containing the word \"world\".\n")
        f.write("Let's see if our script can do that.\n")
        f.write("Goodbye world!\n")
    return test_file_path


def test_read_files_existing_file(create_test_file):
    file_path = create_test_file
    expected_contents = "Hello world!\nThis is a test file containing the word \"world\".\nWe want to filter out the lines containing the word \"world\".\nLet's see if our script can do that.\nGoodbye world!\n"
    assert read_files(file_path) == expected_contents


def test_read_files_non_existing_file(tmpdir):
    assert read_files("non_existing_file.txt") is None
