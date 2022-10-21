#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : boilerplate_validate_ip.py
* Description   : Boilerplate python script, for basic ip validation
* Created       : 26-02-2021
* Usage         : python3 boilerplate_validate_ip.py
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys
from datetime import datetime
from time import time
import logging

working_dir = os.getcwd()
current_dt_obj = datetime.now()
# Can use 'current_dt_obj' to get other date parts. E.g. 'current_dt_obj.year'
current_date_str = current_dt_obj.strftime("%d-%m-%Y")
current_time_str = current_dt_obj.strftime("%H:%M:%S")


def get_logger():
    """Set up a specific logger with our desired output level"""
    logging.basicConfig(format="%(message)s")
    logger = logging.getLogger("application_logger")
    logger.setLevel(logging.INFO)

    return logger


def main():
    """Main entry point of the app"""
    START_TIME = time()
    logger = get_logger()
    logger.debug("Function called: main()")

    # program logic here
    function_template()

    FINISH_TIME = round(time() - START_TIME, 2)
    logger.debug(f"Function finished: main() in {FINISH_TIME} seconds")

    return


def function_template():
    """Description here"""
    START_TIME = time()
    logger = get_logger()
    logger.debug("Function called: function_template()")

    logger.info("Hello, world!")

    FINISH_TIME = round(time() - START_TIME, 2)
    logger.debug(f"Function finished: function_template() in {FINISH_TIME} seconds")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""
    logger = get_logger()

    # validate user input
    if len(sys.argv) < 2:
        print("\nError: No input arguments provided.\n")
        print("Usage:\npython3 boilerplate.py [numeric value here]\n")
    else:
        input_arg = sys.argv[1]

        # eg_arg = int(eg_arg) / 2
        is_even = int(input_arg) % 2
        if is_even != 0:
            logger.error("\nError: input_arg arg must be an even number.\n")
            logger.info("Usage:\npython3 boilerplate_w_ip_validation.py <input_arg>'\n")
            raise (SystemExit)

    main()
