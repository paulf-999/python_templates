#!/usr/bin/env python3
"""
Python Version  : 3.7
* Name          : boilerplate_w_ip_validation.py
* Description   : Boilerplate python script, for basic ip validation
* Created       : 26-02-2021
* Usage         : python3 boilerplate_w_ip_validation.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os
import sys
from datetime import datetime
from time import time
import logging

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
    """ Main entry point of the app """
    START_TIME = time()
    logger.debug(f"Function called: main()")
    # program logic here
    logger.debug(f"Function finished: main() finished in {round(time() - START_TIME, 2)} seconds")


def function_template():
    """ Description here """
    START_TIME = time()
    logger.debug(f"Function called: function_template()")
    # program logic here
    logger.debug(f"Function finished: function_template() finished in {round(time() - START_TIME, 2)} seconds")

    return


if __name__ == "__main__":
    """ This is executed when run from the command line """

    # validate user input
    if len(sys.argv) < 2:
        print("\nError: No input arguments provided.\n")
        print("Usage:\npython3 boilerplate.py [numeric value here]\n")
    else:
        eg_arg = sys.argv[1]

        print(eg_arg)

        try:
            eg_arg = eg_arg / 2
        except TypeError:
            print("\nError: 'eg_arg' arg must be an even number.\n")
            print("Usage:\npython3 boilerplate_w_ip_validation.py '[eg_arg]'\n")
            raise (SystemExit)

    main()
