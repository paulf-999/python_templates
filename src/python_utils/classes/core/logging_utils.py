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

# Define two new logging levels VERBOSE and TRACE
VERBOSE = 15
TRACE = 5
logging.addLevelName(VERBOSE, "VERBOSE")
logging.addLevelName(TRACE, "TRACE")


class LoggingUtils:
    def __init__(self):
        self.logger = self.configure_logging()
        self.set_log_level(logging.INFO)  # Set default log level to INFO

    def configure_logging(self):
        """Set up logging with coloured formatting"""

        logger = logging.getLogger("application_logger")

        # Add coloured formatting to the logger - if the handler is not already set
        if not logger.handlers:
            self._add_colored_handler(logger)

        return logger

    def _add_colored_handler(self, logger):
        """Add a colored handler to the logger."""

        # Required to apply colour formatting to the logger
        handler = colorlog.StreamHandler()

        # Add colour formatting to the logger
        handler.setFormatter(
            colorlog.ColoredFormatter(
                "%(log_color)s%(message)s",
                log_colors={
                    "TRACE": "blue",
                    "VERBOSE": "purple",
                    "DEBUG": "green",
                    "INFO": "cyan",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                },
            )
        )
        logger.addHandler(handler)

    def set_log_level(self, log_level=logging.INFO):
        """Set the log level for the logger and its handlers"""

        # Set the log level
        self.logger.setLevel(log_level)

        # Set the log level for each handler
        for handler in self.logger.handlers:
            handler.setLevel(log_level)

    def log_error(self, message, script_name, function_name, error):
        """Log an error message along with script name, function name, and error details."""

        # Get the line number where the method is called
        line_number = inspect.currentframe().f_back.f_lineno

        # Construct a structured error message
        error_message = (
            f"ERROR: An error occurred in '{script_name}'\n"
            f"- Script name: {script_name}\n"
            f"- Function name: {function_name}\n"
            f"- Line number: {line_number}\n"
            f"- Error details: {message}\n"
            f"- Exception: {error}\n"
        )

        # Log the error message along with the line number
        self.logger.error(error_message)

    def log_header(self, message, level=VERBOSE):
        """Not functional: generate a consistent logging header message"""

        # enable the headings to use a different colour
        self.set_log_level(level)

        border = "-" * 77  # Create a consistent border for the header
        log_method = self._get_log_method(level)  # Get the appropriate log method
        log_method(f"\n{border}")
        log_method(f"# {message}")  # Log the message
        log_method(f"{border}\n")

    def _get_log_method(self, level):
        """Get the appropriate log method based on the log level."""

        if level == logging.INFO:
            return self.logger.info
        elif level == logging.DEBUG:
            return self.logger.debug
        elif level == TRACE:
            return self.trace
        elif level == VERBOSE:
            return self.verbose
        else:
            return self.logger.info

    def verbose(self, message, *args, **kws):
        if self.logger.isEnabledFor(VERBOSE):
            self.logger._log(VERBOSE, message, args, **kws)

    def trace(self, message, *args, **kws):
        if self.logger.isEnabledFor(TRACE):
            self.logger._log(TRACE, message, args, **kws)
