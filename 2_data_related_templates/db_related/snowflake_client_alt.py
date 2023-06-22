#!/usr/bin/env python3
"""
Python Version  : 3.10
* Name          : functions.py
* Description   : Reusable Python functions to be used across Python scripts
* Created       : 12-04-2023
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys
import logging

import snowflake.connector
from snowflake.connector.errors import DatabaseError
from snowflake.connector.errors import ProgrammingError
import yaml

working_dir = os.getcwd()

# Set up a specific logger with our desired output level"""
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)


def get_sf_conn_params():
    """get snowflake db connections params from input config"""

    # store the credentials in a py dictionary
    sf_conn_details = {}

    with open(os.path.join(os.getcwd(), "ip", "config_mine.yaml")) as ip_yml:
        data = yaml.safe_load(ip_yml)

    sf_conn_details["sf_username"] = data["db_connection_params"]["snowflake_username"]
    sf_conn_details["sf_pass"] = data["db_connection_params"]["snowflake_pass"]
    # sf_conn_details["sf_p8_key_path"] = data['db_connection_params']['snowflake_p8_key']
    # sf_conn_details["sf_p8_key_passphrase"] = data['db_connection_params']['snowflake_p8_key_passphrase']
    sf_conn_details["sf_account"] = data["db_connection_params"]["snowflake_account"]
    sf_conn_details["sf_wh"] = data["db_connection_params"]["snowflake_wh"]
    sf_conn_details["sf_role"] = data["db_connection_params"]["snowflake_role"]
    sf_conn_details["sf_db"] = data["db_connection_params"]["snowflake_db"]
    sf_conn_details["sf_db_schema"] = data["db_connection_params"]["snowflake_db_schema"]

    return sf_conn_details


def create_snowflake_connection(conn="", sf_conn_details=get_sf_conn_params()):
    """create a sf connection instance"""
    try:
        conn = snowflake.connector.connect(
            user=sf_conn_details["sf_user_name"],
            password=sf_conn_details["sf_pass"],
            account=sf_conn_details["sf_account"],
            warehouse=sf_conn_details["sf_wh"],
            role=sf_conn_details["sf_role"],
            schema=sf_conn_details["sf_db_schema"],
        )

    except ProgrammingError as e:
        if e.errno == 251005:
            print(f"\nERROR: Invalid username/password.\n\nMessage: '{e.msg}'.")
            raise (SystemExit)
        else:
            print(f"Error {e.errno} ({e.sqlstate}): ({e.sfqid})")
            raise (SystemExit)

    except DatabaseError as db_e:
        if db_e.errno == 250001:
            print(f"\nERROR: Invaid Snowflake account name provided.\n\nMessage: '{db_e.msg}'.")
            raise (SystemExit)
        else:
            print(f"Error {db_e.errno} ({db_e.sqlstate}): ({db_e.sfqid})")
            raise (SystemExit)

    return conn


def snowflake_query(query, sf_query_op=""):
    """Connect to SF DB & run query"""

    # establish a SF connection
    conn = create_snowflake_connection()

    cursor = conn.cursor()

    try:
        cursor.execute(query)
        query_result = cursor.fetchall()
        logger.debug(f"query_result = {query_result}")
        for tuple_result in query_result:
            for column in tuple_result:
                sf_query_op += f"{column};"
            sf_query_op += "\n"
    finally:
        cursor.close()
    conn.close()

    return sf_query_op


if __name__ == "__main__":
    sql_query = sys.argv[1]

    snowflake_query(sql_query)
