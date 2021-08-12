#!/usr/bin/env python3
"""
Python Version  : 3.7
* Name          : snowflake_query.py
* Description   : Boilerplate Snowflake query script.
* Created       : 04-06-2021
* Usage         : python3 snowflake_query.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import sys
import snowflake.connector


def snowflake_query(schema_name, ip_tbl):
    """[summary]

    Args:
        schema_name ([type]): [description]
        ip_tbl ([type]): [description]
    """
    conn_params = get_conn_params()

    snowflake_account, username, password, snowflake_wh, snowflake_db, schema_name = [conn_params[i] for i in (0, 1, 2, 3, 4, 5)]

    conn = snowflake.connector.connect(user=f"{username}", password=f"{password}", account=f"{snowflake_account}", warehouse=f"{snowflake_wh}", database=f"{snowflake_db}", schema=f"{schema_name}")
    cursor = conn.cursor()
    try:
        cursor.execute(f"select count(*) from {schema_name}.{ip_tbl}")
        query_result = cursor.fetchall()

        for result in query_result:
            print(result)

    finally:
        cursor.close()

    conn.close()


def get_conn_params():
    """Function to retrieve connection parameters used to connect to Snowflake

    Returns:
        conn_params (array): Array containing connection parameters
    """

    snowflake_account = "<snowflake_account>"
    username = "<username>"
    password = "<password>"
    snowflake_wh = "<wh_name>"
    snowflake_db = "<db_name>"
    schema_name = "<schema_name>"

    conn_params = [snowflake_account, username, password, snowflake_wh, snowflake_db, schema_name]

    return conn_params


if __name__ == "__main__":

    schema_name = sys.argv[1]
    ip_tbl = sys.argv[1]

    snowflake_query(schema_name, ip_tbl)
