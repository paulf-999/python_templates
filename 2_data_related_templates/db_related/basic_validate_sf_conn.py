#!/usr/bin/env python
import logging
import os

import snowflake.connector
import yaml

logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)


def read_ip():
    """Read input from config file"""

    working_dir = os.getcwd()

    with open(os.path.join(working_dir, "ip", "config_mine.yaml")) as ip_yml:
        # with open(os.path.join(working_dir, "ip", "config.yaml")) as ip_yml:
        data = yaml.safe_load(ip_yml)

    snowflake_username = data["db_connection_params"]["snowflake_username"]
    snowflake_pass = data["db_connection_params"]["snowflake_pass"]
    snowflake_account = data["db_connection_params"]["snowflake_account"]

    return snowflake_username, snowflake_pass, snowflake_account


def main():
    """Main entry point of the app"""

    # get inputs
    snowflake_username, snowflake_pass, snowflake_account = read_ip()

    conn = snowflake.connector.connect(
        user=snowflake_username,
        password=snowflake_pass,
        account=snowflake_account
    )

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT current_version()")
        one_row = cursor.fetchone()
        logger.info(f"\nSnowflake version = {one_row[0]}\n")
    finally:
        cursor.close()

    conn.close()

    return


if __name__ == "__main__":
    """This is executed when run from the command line"""

    main()
