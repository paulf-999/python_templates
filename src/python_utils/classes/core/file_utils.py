#!/usr/bin/env python3
"""
Description: File utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

from python_utils.classes.core.logging_utils import LoggingUtils

# Set up logging using custom shared module
logging_utils = LoggingUtils()
logger = logging_utils.logger

# Store the name of this py script as a var
py_script_name = os.path.basename(__file__)


class FileUtils:
    def create_directory_if_not_exists(self, directory):
        """Create a directory if it doesn't exist."""

        logger.debug("Function called 'FileUtils.create_directory_if_not_exists()'")

        # Convert the directory var to lowercase
        directory = os.path.abspath(directory.lower())

        logger.info("Check if directory already exists...\n")

        # Create the target directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Directory created: {directory}")
        else:
            logger.info(f"Directory already exists: {directory}")

        logger.debug(f"Checked and created directory if not exists: {directory}")

    def find_project_root(self, project_name):
        """
        Find the root directory of the Python project.
        :param project_name: The name of the Python project.
        :return: The root directory of the Python project.
        """

        logger.debug("Function called 'FileUtils.find_project_root()'")

        current_dir = os.path.abspath(os.getcwd())  # Get the current working directory

        while True:
            if os.path.basename(current_dir) == project_name:
                return current_dir  # Return if the project root is found

            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:
                raise FileNotFoundError(f"Project root '{project_name}' not found.")

            current_dir = parent_dir  # Move up one directory level

    def prompt_for_file_overwrite(self, output_file, args):
        """
        Prompt the user for file overwrite if necessary.
        :param output_file: The name to the output file.
        :param args: Command-line args passed to the function.
        :return: Boolean indicating whether the file should be overwritten.
        """

        logger.debug("Function called 'FileUtils.prompt_for_file_overwrite()'")

        # Check if a file already exists in the target directory
        if os.path.exists(output_file):
            overwrite_file = self._handle_existing_file(output_file, args)
        else:
            overwrite_file = True  # Allow overwrite if file does not exist

        return overwrite_file

    def _handle_existing_file(self, output_file, args):
        """Handle the logic for when the output file already exists."""

        # Flag to track whether any files are being overwritten
        overwrite_file = False

        # Prompt the user, asking if they want to override it
        if not args.yes:
            user_input = input(f"The file '{output_file}' already exists. Do you want to overwrite it? (yes/no): ")

            # If '-y' or '--yes', skip the overwrite prompt
            if user_input == "yes":
                overwrite_file = True
                logger.info("\nOverwriting existing file.")
            else:
                logger.info("\nFile not overwritten. Skipping...\n")

        elif not hasattr(args, "yes_logged") or not args.yes_logged:
            overwrite_file = True
            logger.info("\nOverwriting existing file.")

        return overwrite_file
