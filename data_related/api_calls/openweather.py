#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : openweather.py
* Description   : Script to perform an API call to gain open weather data
* Created       : 26-02-2021
* Usage         : python3 openweather.py

see: https://knasmueller.net/using-the-open-weather-map-api-with-python
https://home.openweathermap.org/api_keys
"""

import os
from time import time
import logging
import requests
import json

# import custom modules

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)
# by default, turn off log outputs. But if desired, change this arg to True
# logger.propagate = False


def get_weather_data(lat, lon, api_key):
    """Main entry point of the app"""
    START_TIME = time()
    logger.debug("Function called: get_weather_data()")

    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

    response = requests.get(url)
    weather_data = json.loads(response.text)
    # logger.debug(weather_data)

    timezone = weather_data["timezone"]
    timezone_offset = weather_data["timezone_offset"]
    current = weather_data["current"]
    hourly = weather_data["hourly"]
    daily = weather_data["daily"]

    logger.debug(f"timezone = {timezone}")
    logger.debug(f"timezone_offset = {timezone_offset}")
    logger.debug(f"current = {current}")
    logger.debug(f"hourly = {hourly}")
    logger.debug(f"daily = {daily}")

    logger.debug(f"Function finished: get_weather_data() finished in {round(time() - START_TIME, 2)} seconds")

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""
    lat = "-37.811291"
    lon = "144.985916"
    api_key = ""

    get_weather_data(lat, lon, api_key)
