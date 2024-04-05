import pytest
from main import filter_lines


def test_filter_lines_returns_empty_list_when_file_is_empty(prepare_empty_file):
    keyword = 'test'
    result = filter_lines(prepare_empty_file, keyword)
    assert result == []
def test_filter_lines_returns_empty_list_when_keyword_is_not_present(prepare_input_file):
    keyword = 'test'
    result = filter_lines(prepare_input_file, keyword)
    assert result == []


@pytest.mark.parametrize("keyword, expected", [
    ('hello', ['hello\n', 'hello world\n', 'helloworld']),
    ('world', ['world\n', 'hello world\n', 'helloworld']),
])
def test_filter_lines_returns_filtered_lines(prepare_input_file, keyword, expected):
    result = filter_lines(prepare_input_file, keyword)
    assert result == expected
