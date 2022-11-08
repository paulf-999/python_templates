import os

import io_functions
import pytest

working_dir = os.getcwd()


def test_read_input_file():
    """
    Verify that the input file gets read correctly from the path specified.
    """
    valid_ip_file = "valid_file_test.txt"
    expected_file_contents = ["a", "b", "c"]
    input_list_example_code = io_functions.read_input_file(os.path.join(working_dir, "ip"), valid_ip_file)

    assert input_list_example_code == expected_file_contents, "Failed"


def test_read_input_file_exception():
    """
    Verify the FileNotFoundError exception is thrown when a file is not found
    """
    with pytest.raises(FileNotFoundError):
        io_functions.read_input_file("ip", "file_does_not_exist.txt")


def test_file_type():
    """
    Verify the input file is either .txt or .csv
    """
    valid_input_file = "valid_file_test.csv"
    valid_ip_file_exns = [".txt", ".csv"]
    file_type_check_passed = io_functions.check_input_file_extension(valid_input_file, valid_ip_file_exns)

    assert file_type_check_passed != 0, "Failed"
