#!/usr/bin/env python3
"""
Description: File utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import pandas as pd
from logging_utils import LoggingUtils

logging_utils = LoggingUtils()

# Store the name of this py script as a var
py_script_name = os.path.basename(__file__)


class FileUtils:
    def __init__(self):
        self.logger = LoggingUtils.configure_logging(self)

    def create_directory_if_not_exists(self, directory):
        """Create a directory if it doesn't exist."""

        self.logger.debug("Function called 'FileUtils.create_directory_if_not_exists()'")

        # convert the directory var to lowercase
        directory = directory.lower()

        # create the target directory, if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
            self.logger.debug(f"Directory created: {directory}")

        else:
            self.logger.debug(f"Directory already exists: {directory}")

    def read_excel_file(self, excel_sheet, IP_EXCEL_FILE, header_row):
        """Read data from an Excel file and return a DataFrame."""

        self.logger.debug("Function called 'FileUtils.read_excel_file()'")

        try:
            if not os.path.exists(IP_EXCEL_FILE):
                raise FileNotFoundError(f"Excel file not found: {IP_EXCEL_FILE}")  # noqa

            # Note: the 'header' columns are in row 3
            df = (
                pd.read_excel(IP_EXCEL_FILE, sheet_name=excel_sheet, header=header_row).fillna("").reset_index()  # noqa
            )

            self.logger.debug(f"Read Excel file '{IP_EXCEL_FILE}' for sheet '{excel_sheet}'.")  # noqa

            return df

        except Exception as e:
            LoggingUtils.log_error(
                message="Error reading excel file",
                script_name=py_script_name,
                function_name="read_excel_file()",
                error=e,
            )
            raise

    def prompt_for_file_overwrite(self, OUTPUT_FILE_PATH, args):
        """
        Prompt the user for file overwrite if necessary.
        :param OUTPUT_FILE_PATH: The path to the output file.
        :param args: Command-line arguments passed to the function.
        :return: Boolean indicating whether the file should be overwritten.
        """

        self.logger.debug("Function called 'FileUtils.prompt_for_file_overwrite()'")  # noqa

        # Flag to track whether any files are being overwritten
        overwrite_file = False

        # temporarily turn off the black code formatter
        # fmt: off

        # Check if a file already exists in the target directory
        # Then prompt the user, asking if they want to override it
        if os.path.exists(OUTPUT_FILE_PATH):

            # store the name of the output file as a var
            output_file = os.path.abspath(OUTPUT_FILE_PATH.lower())

            # If the command line argument is '-y' or '--yes', skip the overwrite prompt
            if not args.yes:
                user_input = input(f"\n{output_file} already exists. Do you want to overwrite it? (yes/no): ")

                if user_input == "yes":
                    overwrite_file = True
                    self.logger.debug("\nOverwriting existing file.")

                else:
                    self.logger.info("\nFile not overwritten. Skipping...")
                    return False

            # If the '-y' argument is provided, mark the action as logged
            elif not hasattr(args, "yes_logged") or not args.yes_logged:

                overwrite_file = True
                self.logger.info("Overwriting existing files due to command-line '-y' argument.\n")
                args.yes_logged = True

        else:
            # File doesn't exist - no need to prompt asking to overwrite
            overwrite_file = True

        # fmt: on
        # turn the black code formatter back on

        return overwrite_file

    def find_project_root(self, PROJECT_DIR):
        """Find the project root directory."""

        self.logger.debug("Function called 'find_project_root()'")

        # Get the directory of the current script
        current_dir = os.path.abspath(os.path.dirname(__file__))

        # Traverse up the directory tree until the root directory ("/") is reached
        while current_dir != "/":
            # Check if PROJECT_DIR exists in the current directory
            if PROJECT_DIR in os.listdir(current_dir):
                # If found, return the path to the project root directory
                project_root = os.path.join(current_dir, PROJECT_DIR)

                return project_root

            # Move up one directory level
            current_dir = os.path.dirname(current_dir)

        # If the loop completes without finding the project root directory, raise an exception
        raise FileNotFoundError(f"Project root directory '{PROJECT_DIR}' not found.")
