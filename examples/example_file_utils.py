#!/usr/bin/env python3
"""
Description: Example usage of the FileUtils class
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

from python_utils.classes.core.file_utils import FileUtils
from python_utils.classes.core.logging_utils import LoggingUtils

logging_utils = LoggingUtils()
logger = logging_utils.configure_logging()


def create_example_directory(file_utils):
    """Create an example directory if it doesn't exist."""
    logging_utils.log_header("Example function 1: create_example_directory()")

    directory = "example_directory"
    file_utils.create_directory_if_not_exists(directory)
    logger.debug(f"Checked and created directory if not exists: {directory}")


def prompt_for_overwrite(file_utils):
    """Prompt for file overwrite if necessary."""

    logging_utils.log_header("Example function 2: prompt_for_overwrite()")

    class Args:
        yes = False

    args = Args()
    output_file_path = os.path.join("example_directory", "example_file.txt")

    # Create a dummy file to test overwrite prompt
    with open(output_file_path, "w") as f:
        f.write("Dummy content")

    overwrite = file_utils.prompt_for_file_overwrite(output_file_path, args)
    if overwrite:
        logger.debug(f"File will be overwritten: {output_file_path}")
    else:
        logger.debug(f"File will not be overwritten: {output_file_path}")


def find_project_root(file_utils):
    """Find the project root directory."""
    project_root = file_utils.find_project_root("python_templates")
    logger.info(f"Project root found: {project_root}\n")


def main():
    # Create an instance of FileUtils
    file_utils = FileUtils()

    # Perform example operations
    create_example_directory(file_utils)
    prompt_for_overwrite(file_utils)
    find_project_root(file_utils)


if __name__ == "__main__":
    main()
