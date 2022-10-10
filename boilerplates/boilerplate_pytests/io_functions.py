#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : io_functions.py
* Description   : Boilerplate pytest IO tests
* Created       : 10-10-2022

# Notes:
#TODO:
continue working through: https://medium.com/@paulfry999/list/pytest-9f047c74446a
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys

import logging

# import custom modules

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)


def read_input_file(file_path: str, input_file: str):
    """
    Function to read input file and save each line as a list of values
    :param file_path: (string): filepath to use to try to open input file
    :param input_file (string): input file to open
    :return: Returns a list where each element is a new line from the file read
    """
    try:
        full_input_file_path = f"{file_path}/{input_file}"
        logger.info("------------------------------------")
        logger.info(f"Reading contents from input file:\n{full_input_file_path}")
        logger.info("------------------------------------\n")
        with open(full_input_file_path) as f:
            try:
                if os.stat(full_input_file_path).st_size > 0:
                    logger.info("Valid input file found")
                else:
                    logger.error("Input file is empty")
                    sys.exit(0)
            except OSError:
                logger.error("Input file not found")
            file_contents = [line.strip() for line in f]
            f.close()
            return file_contents
    except FileNotFoundError:
        raise FileNotFoundError(f"ERROR - file '{full_input_file_path}' does not exist") from None
    except Exception as error:
        logger.error(error)
        raise error


def check_input_file_extension(input_file: str, valid_file_types: list):
    logger.info("------------------------------------")
    logger.info(f"Check filename extension of: {input_file}")
    logger.info(f"valid_file_types = {list(valid_file_types)}")
    logger.info("------------------------------------\n")

    input_file_ext = os.path.splitext(input_file)[1]
    logger.debug(f"Input file, file extension = {input_file_ext}")
    file_type_check_passed = 0

    for file_type in valid_file_types:
        logger.debug(f"Valid file type = {file_type}")
        if input_file_ext == file_type:
            logger.debug(f"added {input_file_ext}")
            file_type_check_passed += 1

    if file_type_check_passed != 0:
        logger.info("Valid input file type")
    else:
        logger.error("ERROR - wrong file type!")
        raise TypeError(f"ERROR - input file '{input_file}' is not in the list of valid file types: {valid_file_types}") from None

    return file_type_check_passed


def read_csv_file():

    # TODO

    return


def read_yaml_file():

    # TODO

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    # TODO - delete the below

    # working_dir = os.getcwd()

    # read_input_file(os.path.join(working_dir, "ip"), "valid_file_test.txt")
    # check_input_file_extension("valid_file_test.csv", [".txt", ".csv"])
