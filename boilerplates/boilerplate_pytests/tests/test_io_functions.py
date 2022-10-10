import os

import io_functions


working_dir = os.getcwd()


def test_read_input_file():
    """
    Verify that the input file gets read correctly from the path specified.
    """
    expected_file_contents = ["a", "b", "c"]
    input_list_example_code = io_functions.read_input_file(os.path.join(working_dir, "ip"), "valid_file_test.txt")

    assert input_list_example_code == expected_file_contents, "Failed"
