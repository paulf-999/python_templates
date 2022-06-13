#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : boilerplate.py
* Description   : Boilerplate python script that reads ip from config file
* Created       : 26-02-2021
* Usage         : python3 boilerplate_w_ip.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os

# import sys
from datetime import datetime
from time import time
import logging
import json

# import custom modules

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)
# by default, turn off log outputs. But if desired, change this arg to True
# logger.propagate = False

current_dt_obj = datetime.now()
current_date_str = current_dt_obj.strftime("%d-%m-%Y")
current_time_str = current_dt_obj.strftime("%H:%M:%S")
# can use 'current_dt_obj' to get other date parts. E.g. 'current_dt_obj.year'


def main():
    """Main entry point of the app"""
    START_TIME = time()
    logger.debug("Function called: main()")
    # program logic here
    logger.debug(f"Function finished: main() finished in {round(time() - START_TIME, 2)} seconds")

    return


def read_ip():
    """Read input from config file"""
    START_TIME = time()
    logger.debug("Function called: read_ip()")

    with open("config.json", "r") as f:
        data = json.load(f)

    key1 = data["Parameters"]["Key1"]

    logger.info(f"config = {data}")
    logger.info(f"config = {key1}")

    logger.debug(f"Function finished: read_ip() finished in {round(time() - START_TIME, 2)} seconds")

    return


def function_template():
    """Description here"""
    START_TIME = time()
    logger.debug("Function called: function_template()")
    # program logic here
    logger.debug(f"Function finished: function_template() finished in {round(time() - START_TIME, 2)} seconds")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    read_ip()
