#!/usr/bin/env python3
"""
Description: Tests for Logging utility functions
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import logging

import pytest
from python_utils.classes.core.logging_utils import TRACE_LEVEL_NUM, VERBOSE_LEVEL_NUM, LoggingUtils


@pytest.fixture
def logging_utils():
    """PyTest Fixture to create an instance of LoggingUtils."""
    return LoggingUtils()


def test_configure_logging(logging_utils):
    """Test the configure_logging method to ensure it sets up the logger correctly."""
    logger = logging_utils.logger

    # Check that the logger is named correctly
    assert logger.name == "application_logger"
    # Check that the logger level is set to INFO by default
    assert logger.level == logging.INFO
    # Check that the logger has at least one handler
    assert len(logger.handlers) > 0
    # Check that the handler is a StreamHandler
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_set_log_level(logging_utils):
    """Test the set_log_level method to ensure it sets the log level correctly."""
    logging_utils.set_log_level(logging.DEBUG)
    logger = logging_utils.logger

    # Check that the logger level is set to DEBUG
    assert logger.level == logging.DEBUG
    # Check that the handler level is set to DEBUG
    for handler in logger.handlers:
        assert handler.level == logging.DEBUG


def test_log_error(logging_utils, caplog):
    """Test the log_error method to ensure it logs error messages correctly."""
    # Set the logger level to DEBUG to capture debug messages
    logging_utils.set_log_level(logging.DEBUG)

    with caplog.at_level(logging.DEBUG):
        # Call the log_error method
        try:
            raise ValueError("Test error")
        except ValueError as e:
            logging_utils.log_error("Test message", "test_script.py", "test_function", str(e))

    # Check that the error message is in the log output
    assert "ERROR: An error occurred processing the script 'test_script.py'" in caplog.text
    assert "- Script name: test_script.py" in caplog.text
    assert "- Function name: test_function" in caplog.text
    assert "- Error details: Test message" in caplog.text
    assert "- Exception: Test error" in caplog.text

    # Dynamically check the line number
    log_output = caplog.text
    line_number = log_output.split("- Line number: ")[1].split("\n")[0]
    assert line_number.isdigit()


def test_log_header(logging_utils, caplog):
    """Test the log_header method to ensure it logs headers correctly."""
    with caplog.at_level(logging.INFO):
        # Call the log_header method
        logging_utils.log_header("Test Header")

    # Check that the header border and message are in the log output
    assert "\n" + "-" * 77 in caplog.text
    assert "Test Header" in caplog.text
    assert "-" * 77 + "\n" in caplog.text


def test_log_verbose(logging_utils, caplog):
    """Test logging with VERBOSE level."""
    logging_utils.set_log_level(VERBOSE_LEVEL_NUM)

    with caplog.at_level(VERBOSE_LEVEL_NUM):
        logging_utils.verbose("This is a VERBOSE level message")

    assert "This is a VERBOSE level message" in caplog.text


def test_log_trace(logging_utils, caplog):
    """Test logging with TRACE level."""
    logging_utils.set_log_level(TRACE_LEVEL_NUM)

    with caplog.at_level(TRACE_LEVEL_NUM):
        logging_utils.trace("This is a TRACE level message")

    assert "This is a TRACE level message" in caplog.text
