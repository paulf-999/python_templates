#!/usr/bin/env python3
"""
Python Version  : 3.7
* Name          : slack.py
* Description   : Boilerplate slack API call script. Follows description given here: https://www.accadius.com/send-message-slack-python-program/#:~:text=Go%20to%20https%3A%2F%2Fmy,will%20appear%20in%20the%20channel
* Created       : 26-02-2021
* Usage         : python3 slack.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os
import sys
from datetime import datetime
from time import time
import logging
#import custom modules
from urllib import request, parse
import json
import ssl

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format='%(message)s')
logger = logging.getLogger('application_logger')
logger.setLevel(logging.INFO)
# by default, turn off log outputs. But if desired, change this arg to True
#logger.propagate = False

current_dt_obj = datetime.now()
current_date_str = current_dt_obj.strftime('%d-%m-%Y')
current_time_str = current_dt_obj.strftime('%H:%M:%S')
#can use 'current_dt_obj' to get other date parts. E.g. 'current_dt_obj.year'

#to use unverified ssl
ssl._create_default_https_context = ssl._create_unverified_context

webhook_url="services/T020PC8CWBD/B020LK2NCUV/9fYTa0bxEjaI8C6PhHzFnvJh"
#e.g. webhook_url="services/ABCDEFGHIJK/1aBCd0efG..."

def main():
    """ Main entry point of the app """
    START_TIME = time()
    logger.debug(f"Function called: main()")
    #program logic here
    send_message_to_slack("pf test")
    logger.debug(f"Function finished: main() finished in {round(time() - START_TIME, 2)} seconds")

    return

def send_message_to_slack(text):    
    """ Function to post a message to a Slack channel """
    START_TIME = time()
    logger.debug(f"Function called: send_message_to_slack()")
    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request(f"https://hooks.slack.com/{webhook_url}",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
    
    logger.debug(f"Function finished: send_message_to_slack() finished in {round(time() - START_TIME, 2)} seconds")

if __name__ == '__main__':
    """ This is executed when run from the command line """

    main()
    