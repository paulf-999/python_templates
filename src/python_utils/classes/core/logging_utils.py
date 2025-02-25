#!/usr/bin/env python3
"""
Description: Logging utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import inspect
import logging

import colorlog


class LoggingUtils:
    def __init__(self):
        self.logger = self.configure_logging()

    def configure_logging(self, log_level=logging.DEBUG):
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

        # Get the line number where the method is called
        line_number = inspect.currentframe().f_back.f_lineno

        # Construct a structured error message
        error_message = (
            f"ERROR: An error occurred processing the script '{script_name}'\n"
            f"- Script name: {script_name}\n"
            f"- Function name: {function_name}\n"
            f"- Line number: {line_number}\n"
            f"- Error details: {message}\n"
            f"- Exception: {error}\n"
        )

        # Log the error message along with the line number
        self.logger.error(error_message)

    def log_header(self, message, char="-", length=77):
        """Log a formatted header with a specified character.

        Args:
            message (str): The header message to log.
            char (str): The character to use for the border.
            length (int): The length of the border.
        """

        border = char * length
        self.logger.info(f"\n{border}")
        self.logger.info(f"{message}")
        self.logger.info(f"{border}\n")
