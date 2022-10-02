import re

import pytest

# fmt: off
list_input = [
    "increase_count_by_one",
    "materials_procurement",
    "material_warehousing",
    "SnakeCaseRegexFailExample"
]
# fmt: on


# Valid filenames should only contain (lower-case) alphanumeric characters and underscores
# They shouldn't contain whitespace, dashes or dots
@pytest.mark.parametrize("filename", list_input)
def test_verify_dag_name_is_valid(filename):
    valid_filename = "^[^- .][a-z_1-9]*$"
    assert re.match(valid_filename, filename)  # nosec
