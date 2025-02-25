#!/usr/bin/env python3
"""
Description: Boilerplate python script
"""
# flake8: noqa: E401

__author__ = ""
__version__ = "1.0"
__date_created__ = ""

import os  # noqa
import sys  # noqa
import logging

logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)


def main():
    """Main entry point of the script."""
    logger.debug("Function called 'main()'")


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
