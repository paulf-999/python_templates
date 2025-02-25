#!/usr/bin/env python3
"""
Description: Example usage of the LoggingUtils class
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import logging

from python_utils.classes.core.logging_utils import LoggingUtils


def log_info_message(logging_utils):
    """Log a message with INFO level."""
    logging_utils.set_log_level(logging.INFO)
    logger_info = logging_utils.logger
    logger_info.info("\nThis is an INFO level message")
    logging_utils.log_header("Example Header with INFO level")


def log_debug_message(logging_utils):
    """Log a message with DEBUG level."""
    logging_utils.set_log_level(logging.DEBUG)
    logger_debug = logging_utils.logger
    logger_debug.debug("This is a DEBUG level message")
    logging_utils.log_header("Example Header with DEBUG level", level=logging.DEBUG)


def log_error_message(logging_utils):
    """Log an error with DEBUG level."""
    try:
        # Simulate an error
        1 / 0
    except ZeroDivisionError as e:
        logging_utils.log_error("Division by zero error", "example_logging_utils.py", "main", str(e))


def main():
    # Create an instance of LoggingUtils
    logging_utils = LoggingUtils()

    # Log messages with different levels
    log_info_message(logging_utils)
    log_debug_message(logging_utils)
    log_error_message(logging_utils)


if __name__ == "__main__":
    main()
