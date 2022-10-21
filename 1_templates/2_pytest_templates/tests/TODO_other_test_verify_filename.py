import re


# Valid filenames should only contain (lower-case) alphanumeric characters and underscores
# They shouldn't contain whitespace, dashes or dots
def test_verify_dag_name_is_valid(filename):
    valid_filename = "^[^- .][a-z_1-9]*$"
    assert re.match(valid_filename, filename)  # nosec
