import logging

import pytest
from boilerplate_basic_pytest import is_even

logging.basicConfig(format='%(message)s')
logger = logging.getLogger('application_logger')
logger.setLevel(logging.INFO)


####################################################################
# PyTest Fixtures
####################################################################
@pytest.fixture()
def input_filename():
    """ Fixtures are used when we want to run some code before every test method.
    So instead of repeating the same code in every test we define fixtures."""

    filename = "example_input_file.txt"

    return filename


@pytest.fixture()
def pytestconfig_fixture_eg(pytestconfig):
    """In this example a fixture is used to read the extra cmd line arg provided by pytestconfig"""
    pytest_config_eg = pytestconfig.getoption("pytest_example_arg")

    logger.info(pytest_config_eg)

    return pytest_config_eg


####################################################################
# PyTests
####################################################################
# use the below to provide test_cases
def test_valid_even():
    """ trivial example """
    assert is_even(2)


def test_fixture_example(input_filename):
    """ Simple example showing how input has been passed from the fixture"""

    assert len(input_filename) > 0


def test_pytestconfig_usage(pytestconfig_fixture_eg):
    """ Simple example showing how input has been passed from the fixture"""

    logger.info(f"pytestconfig_fixture_eg = {pytestconfig_fixture_eg}")

    assert len(pytestconfig_fixture_eg) > 0

# TODO - parameterisations
