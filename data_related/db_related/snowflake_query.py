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
    conn = snowflake.connector.connect(
        user=f'{username}',
        password=f'{password}',
        account=f'{snowflake_account}',
        warehouse=f'{snowflake_wh}',
        database=f'{snowflake_db}',
        schema=f'{schema_name}'
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"select table_name from {schema_name}.{ip_tbl}")
        query_result = cursor.fetchall()

        for result in query_result:
            print(result)

    finally:
        cursor.close()

    conn.close()

if __name__ == '__main__':
    #cmd line ip param
    ip_param = sys.argv[1]

    snowflake_query(schema_name, ip_tbl)
