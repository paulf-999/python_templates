#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : boilerplate.py
* Description   : Boilerplate XLS data ingestion script
* Created       : 13-06-2022
* Usage         : python3 xls_pandas.py
* Notes         : See: https://pythonbasics.org/read-excel/
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os

import sys
from datetime import datetime
from time import time
import logging
import pandas as pd

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)
# By default, turn off log outputs. But if desired, change this arg to True
# logger.propagate = False

current_dt_obj = datetime.now()
# can use 'current_dt_obj' to get other date parts. E.g. 'current_dt_obj.year'
current_date_str = current_dt_obj.strftime("%d-%m-%Y")
current_time_str = current_dt_obj.strftime("%H:%M:%S")


def read_xls_file(ip_xls_file):
    """TODO: description"""
    START_TIME = time()
    logger.debug("Function called: read_xls_file()")

    xls_file = pd.read_excel(ip_xls_file)  # read in the excel doc, build a dataframe...

    logger.info(xls_file)

    logger.debug(f"Function finished: read_xls_file() finished in {round(time() - START_TIME, 2)} seconds")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    # validate user input
    if len(sys.argv) < 2:
        print("\nError: No input arguments provided.\n")
        print("Usage:\npython3 xls_pandas.py <src xls file>\n")
    else:
        ip_xls_file = sys.argv[1]

        logger.info(f"ip_xls_file = {ip_xls_file}")

        read_xls_file(ip_xls_file)
