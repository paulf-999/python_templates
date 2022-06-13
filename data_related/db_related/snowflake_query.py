#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : snowflake_query.py
* Description   : Boilerplate Snowflake query script.
* Created       : 04-06-2021
* Usage         : python3 snowflake_query.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os
import snowflake.connector
from time import time
import logging
import json

working_dir = os.getcwd()
# Set up a specific logger with our desired output level
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)
# by default, turn off log outputs. But if desired, change this arg to True
logger.propagate = True


def snowflake_query(snowflake_db, schema_name, sql_query):
    """Boilerplate Snowflake DB query

    Args:
        snowflake_db (str): Snowflake DB to use
        schema_name (str): Snowflake DB schema to use
        sql_query (str): SQL query string to execute
    """
    START_TIME = time()
    logger.debug("Function called: snowflake_query()")

    conn_params = get_conn_params()

    snowflake_account, username, password, snowflake_wh = [conn_params[i] for i in (0, 1, 2, 3)]

    conn = snowflake.connector.connect(user=f"{username}", password=f"{password}", account=f"{snowflake_account}", warehouse=f"{snowflake_wh}", database=f"{snowflake_db}", schema=f"{schema_name}")
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        query_result = cursor.fetchall()

        for result in query_result:
            print(result)

    finally:
        cursor.close()

    conn.close()

    logger.info(f"Function finished: snowflake_query() finished in {round(time() - START_TIME, 2)} seconds")

    return


def get_conn_params():
    """Function to retrieve connection parameters to be used to connect to Snowflake

    Returns:
        conn_params (array): Array containing connection parameters
    """
    START_TIME = time()
    logger.debug("Function called: get_conn_params()")

    with open(os.path.join(working_dir, "env/env.json"), "r") as ip_file:
        ip_dict_args = json.load(ip_file)

    snowflake_account = ip_dict_args["snowflake_account"]
    username = ip_dict_args["sf_username"]
    password = ip_dict_args["sf_password"]
    snowflake_wh = ip_dict_args["snowflake_wh"]

    conn_params = [snowflake_account, username, password, snowflake_wh]

    logger.debug(conn_params)

    logger.info(f"Function finished: snowflake_query() finished in {round(time() - START_TIME, 2)} seconds")

    return conn_params


if __name__ == "__main__":

    snowflake_db = "<SNOWFLAKE_DB>"  # e.g. "bikestores_raw_db"
    schema_name = "<SNOWFLAKE_DB_SCHEMA>"  # e.g. "production"
    # example Snowflake query
    sql_query = "<SQL_QUERY>"  # e.g. "SHOW TABLES"

    snowflake_query(snowflake_db, schema_name, sql_query)
