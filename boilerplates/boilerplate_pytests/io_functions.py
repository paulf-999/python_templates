#!/usr/bin/env python3
"""
Python Version  : 3.8
# TODO: change these
* Name          : boilerplate_basic.py
* Description   : Boilerplate python script
* Created       : 26-02-2021
* Usage         : python3 boilerplate_basic.py
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys

from datetime import datetime
import logging

# import custom modules

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)
# By default, turn off log outputs. But if desired, change this arg to True
# logger.propagate = False

current_dt_obj = datetime.now()
# Can use 'current_dt_obj' to get other date parts. E.g. 'current_dt_obj.year'
current_date_str = current_dt_obj.strftime("%d-%m-%Y")
current_time_str = current_dt_obj.strftime("%H:%M:%S")


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
        logger.info("------------------------------------")
        with open(full_input_file_path) as f:
            try:
                if os.stat(full_input_file_path).st_size > 0:
                    logger.info("Valid file found")
                else:
                    logger.info("Input file is empty")
                    sys.exit(0)
            except OSError:
                logger.info("Input file not found")
            file_contents = [line.strip() for line in f]
            f.close()
            return file_contents
    except FileNotFoundError:
        raise FileNotFoundError(f"ERROR - file {full_input_file_path} does not exist")
    except Exception as error:
        logger.error(error)
        raise error


if __name__ == "__main__":
    """This is executed when run from the command line"""

    # read_input_file(os.getcwd(), "test1.txt")
