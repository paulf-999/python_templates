import pytest
from boilerplate_basic_pytest import is_even


# use the below to provide test_cases
def test_valid_even():
    assert is_even(2)


@pytest.fixture()
def setup_fixture_example():
    """ Fixtures are used when we want to run some code before every test method.
    So instead of repeating the same code in every test we define fixtures."""

    filename = "example_input_file.txt"

    return filename


def test_fixture_example(filename):
    """ Simple example showing how input has been passed from the fixture"""

    return filename


# TODO
def test_pytestconfig_example(pytestconfig):
    # TODO
    pytest_config_eg = pytestconfig.getoption("example_arg")

    print(pytest_config_eg)

    assert ...
