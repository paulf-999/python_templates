#!/usr/bin/env python3
"""
Python Version  : 3.8
# TODO: change these
* Name          : boilerplate.py
* Description   : Boilerplate python script
* Created       : 26-02-2021
* Usage         : python3 boilerplate.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os

# import sys
from datetime import datetime
from time import time
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


def main():
    """Main entry point of the app"""
    START_TIME = time()
    logger.debug("Function called: main()")

    # program logic here

    FINISH_TIME = round(time() - START_TIME, 2)
    logger.debug(f"Function finished: main() in {FINISH_TIME} seconds")
    return


def function_template():
    """Description here"""
    START_TIME = time()
    logger.debug("Function called: function_template()")

    # program logic here

    FINISH_TIME = round(time() - START_TIME, 2)
    logger.debug(f"Function finished: function_template() in {FINISH_TIME} seconds")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    main()
