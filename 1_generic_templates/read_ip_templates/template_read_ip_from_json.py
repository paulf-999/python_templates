#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : template_read_ip_from_config.py
* Description   : Boilerplate python script that reads ip from json file
* Created       : 26-02-2021
* Usage         : python3 template_read_ip_from_config.py
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import logging
import json


def get_logger():
    """Set up a specific logger with our desired output level"""
    logging.basicConfig(format="%(message)s")
    logger = logging.getLogger("application_logger")
    logger.setLevel(logging.INFO)

    return logger


def read_ip():
    """Read input from config file"""

    logger = get_logger()

    with open("config.json") as ip_json:
        data = json.load(ip_json)

    env = data["general_params"]["env"]
    logger.info(f"env = {env}")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    read_ip()
