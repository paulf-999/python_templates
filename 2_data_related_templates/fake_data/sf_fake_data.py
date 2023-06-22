#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : fake_data.py
* Description   : Fake data generator script.
*                 See package doco for more details: https://faker.readthedocs.io/en/master/index.html
* Created       : 30-09-2022
* Usage         : python3 fake_data.py
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

# import sys
from datetime import datetime
from time import time
import logging
from faker import Faker
from faker.providers import credit_card

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


def simple_example(fake_generator):



    return


def generate_bulk_fake_data(fake_generator):
    """Generate fake data in bulk"""
    START_TIME = time()
    logger.debug("Function called: function_template()")

    logger.info("\nBulk fake names:\n")
    for _ in range(10):
        logger.info(fake_generator.name())

    FINISH_TIME = round(time() - START_TIME, 2)
    logger.debug(f"Function finished: function_template() in {FINISH_TIME} seconds")

    return


def provider_example(fake_generator):
    """Example of using a Faker provider"""
    START_TIME = time()
    logger.debug("Function called: function_template()")

    logger.info("\nFake provider example (credit card example):\n")
    # See this following for an exhaustive list of providers
    fake_generator.add_provider(credit_card)

    logger.info(fake_generator.credit_card_full())

    FINISH_TIME = round(time() - START_TIME, 2)
    logger.debug(f"Function finished: function_template() in {FINISH_TIME} seconds")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    # create and initialize a faker generator. Ireland localisation arg provided
    fake_generator = Faker("en_IE")

    simple_example(fake_generator)

    generate_bulk_fake_data(fake_generator)

    provider_example(fake_generator)
