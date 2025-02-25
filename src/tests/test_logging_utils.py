#!/usr/bin/env python3
"""
Description: Tests for Logging utility functions
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

# cspell: ignore caplog
import logging

import pytest
from python_utils.classes.core.logging_utils import LoggingUtils


@pytest.fixture
def logging_utils():
    """PyTest Fixture to create an instance of LoggingUtils."""
    return LoggingUtils()


def test_configure_logging(logging_utils):
    """Test the configure_logging method to ensure it sets up the logger correctly."""
    logger = logging_utils.configure_logging()

    # Check that the logger is named correctly
    assert logger.name == "application_logger"
    # Check that the logger level is set to INFO
    assert logger.level == logging.INFO
    # Check that the logger has at least one handler
    assert len(logger.handlers) > 0
    # Check that the handler is a StreamHandler
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_log_error(logging_utils, caplog):
    """Test the log_error method to ensure it logs error messages correctly."""
    # Set the logger level to DEBUG to capture debug messages
    logging_utils.logger.setLevel(logging.DEBUG)

    with caplog.at_level(logging.DEBUG):
        # Call the log_error method
        logging_utils.log_error("Test message", "test_script.py", "test_function", "Test error")

    # Check that the debug message is in the log output
    assert "Function called 'LoggingUtils.log_error()'" in caplog.text
    # Check that the error message is in the log output
    assert "ERROR: An error occurred processing the script 'test_script.py'" in caplog.text
    assert "- Function name: test_function" in caplog.text
    assert "- Error details: Test message" in caplog.text
    assert "- Error: Test error" in caplog.text


def test_log_header(logging_utils, caplog):
    """Test the log_header method to ensure it logs headers correctly."""
    with caplog.at_level(logging.INFO):
        # Call the log_header method
        logging_utils.log_header("Test Header")

    # Check that the header border and message are in the log output
    assert "\n" + "-" * 77 in caplog.text
    assert "Test Header" in caplog.text
    assert "-" * 77 + "\n" in caplog.text
