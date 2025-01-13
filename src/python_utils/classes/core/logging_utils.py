#!/usr/bin/env python3
"""
Description: Logging utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import logging
import colorlog
import inspect


class LoggingUtils:
    def __init__(self):
        self.logger = LoggingUtils.configure_logging(self)

    def configure_logging(self, log_level=logging.INFO):
        """Set up logging with set level & coloured formatting"""

        logger = logging.getLogger("application_logger")

        # Prevent adding duplicate handlers
        if not logger.handlers:
            logger.setLevel(log_level)
            handler = colorlog.StreamHandler()
            # add colour formatting to the logger
            handler.setFormatter(
                colorlog.ColoredFormatter(
                    "%(log_color)s%(message)s",
                    log_colors={
                        "DEBUG": "green",
                        "INFO": "cyan",
                        "WARNING": "yellow",
                        "ERROR": "red",
                        "CRITICAL": "bold_red",
                    },
                )
            )
            logger.addHandler(handler)

        return logger

    def log_error(self, message, script_name, function_name, error):
        """Log an error message along with script name, function name, and error details."""

        logger = self.configure_logging()  # Set up logging

        logger.debug("Function called 'LoggingUtils.log_error()'")

        # Get the line number where the method is called
        line_number = inspect.currentframe().f_back.f_lineno

        # Construct a structured error message
        error_message = (
            f"ERROR: An error occurred processing the script '{script_name}'\n"
            f"- Function name: {function_name}\n"
            f"- Line number: {line_number}\n"
            f"- Error details: {message}\n"
            f"- Error: {error}"
        )

        # Log the error message along with the line number
        logger.error(error_message)
