#!/usr/bin/env python3
"""
Description: Example usage of the LoggingUtils class
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

from python_utils.classes.core.logging_utils import LoggingUtils


def main():
    # Create an instance of LoggingUtils
    logging_utils = LoggingUtils()

    # Log a header
    logging_utils.log_header("# Example Header")

    # Log an error
    try:
        # Simulate an error
        1 / 0
    except ZeroDivisionError as e:
        logging_utils.log_error("Division by zero error", "example_logging_utils.py", "main", str(e))


if __name__ == "__main__":
    main()
