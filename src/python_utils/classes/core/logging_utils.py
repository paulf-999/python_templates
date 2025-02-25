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

# Define new log levels VERBOSE and TRACE
VERBOSE_LEVEL_NUM = 15
TRACE_LEVEL_NUM = 5
logging.addLevelName(VERBOSE_LEVEL_NUM, "VERBOSE")
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")


class LoggingUtils:
    def __init__(self):
        self.logger = self.configure_logging()
        self.set_log_level(logging.INFO)  # Set default log level to INFO

    def configure_logging(self):
        """Set up logging with set level & coloured formatting"""

        logger = logging.getLogger("application_logger")

        # Prevent adding duplicate handlers
        if not logger.handlers:
            handler = colorlog.StreamHandler()
            # add colour formatting to the logger
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

        return logger

    def set_log_level(self, log_level=logging.INFO):
        """Set the log level for the logger and its handlers"""

        self.logger.setLevel(log_level)
        for handler in self.logger.handlers:
            handler.setLevel(log_level)

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

    def log_header(self, message, char="-", length=77, level=logging.INFO):
        """Log a formatted header with a specified character.

        Args:
            message (str): The header message to log.
            char (str): The character to use for the border.
            length (int): The length of the border.
            level (int): The logging level to use for the header.
        """

        border = char * length
        if level == TRACE_LEVEL_NUM:
            self.trace(f"\n{border}")
            self.trace(f"# {message}")
            self.trace(f"{border}\n")
        elif level == VERBOSE_LEVEL_NUM:
            self.verbose(f"\n{border}")
            self.verbose(f"# {message}")
            self.verbose(f"{border}\n")
        elif level == logging.DEBUG:
            self.logger.debug(f"\n{border}")
            self.logger.debug(f"# {message}")
            self.logger.debug(f"{border}\n")
        else:
            self.logger.info(f"\n{border}")
            self.logger.info(f"# {message}")
            self.logger.info(f"{border}\n")

    def verbose(self, message, *args, **kws):
        if self.logger.isEnabledFor(VERBOSE_LEVEL_NUM):
            self.logger._log(VERBOSE_LEVEL_NUM, message, args, **kws)

    def trace(self, message, *args, **kws):
        if self.logger.isEnabledFor(TRACE_LEVEL_NUM):
            self.logger._log(TRACE_LEVEL_NUM, message, args, **kws)
