#!/usr/bin/env python3
"""
Description: Snowflake utility functions to be imported by other python scripts
Date created: 2025-01-13
"""
# cSpell:ignore sqlstate sfqid

__author__ = "Paul Fry"
__version__ = "1.0"

import argparse
import os
import sys

import snowflake.connector
from dotenv import load_dotenv

# Custom modules
from python_utils.classes.core.logging_utils import LoggingUtils
from python_utils.classes.core.variable_utils import VariableUtils

logging_utils = LoggingUtils()  # fetch logger functions
variable_utils = VariableUtils()  # fetch common variable util functions from variable_setup module

logger = logging_utils.configure_logging()  # Set up logging

# Load environment variables from .env file
load_dotenv()

# Constants
REQUIRED_ENV_VARS = [
    "SNOWFLAKE_ACCOUNT_NAME",
    "SNOWFLAKE_USERNAME",
    "SNOWFLAKE_PASSWORD",
    "SNOWFLAKE_WAREHOUSE",
    "SNOWFLAKE_DATABASE",
    "SNOWFLAKE_SCHEMA",
    "SNOWFLAKE_ROLE",
]


class SnowflakeClient:
    def __init__(self, args=None):
        self.args = args or self.parse_arguments()

    def parse_arguments(self):
        """Parse command-line arguments."""
        parser = argparse.ArgumentParser(description="Execute a Snowflake command.")
        parser.add_argument("--sql-query", help="Snowflake SQL command to execute")
        parser.add_argument("--sql-file", help="Path to a .sql file containing the SQL command")
        parser.add_argument("--args-json", help="JSON string containing input arguments for SQL placeholders")
        return parser.parse_args()

    def main(self):
        """Main entry point of the script."""
        try:
            # Verify whether the required environment variables exist
            variable_utils.validate_env_vars(REQUIRED_ENV_VARS)

            # Store the Snowflake connection parameters from environment variables
            conn_params = {
                "account": os.getenv("SNOWFLAKE_ACCOUNT_NAME"),
                "user": os.getenv("SNOWFLAKE_USERNAME"),
                "password": os.getenv("SNOWFLAKE_PASSWORD"),
                "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
                "database": os.getenv("SNOWFLAKE_DATABASE"),
                "schema": os.getenv("SNOWFLAKE_SCHEMA"),
                "role": os.getenv("SNOWFLAKE_ROLE"),
            }

            # Connect to Snowflake DB
            with self.create_snowflake_connection(conn_params) as conn:
                # Execute the Snowflake command
                with conn.cursor() as cursor:
                    self.query_results = self.execute_snowflake_command(cursor, self.args.sql_query)

        except Exception as e:
            logger.exception("An unexpected error occurred: %s", e)
            sys.exit(1)

    def execute_snowflake_command(self, cursor, sql_command):
        """Execute Snowflake command(s)"""
        query_results = []
        try:
            # Execute the SQL command
            cursor.execute(sql_command)

            # Fetch and store the results
            query_results = cursor.fetchall()

        except Exception as e:
            logger.exception("An error occurred while executing Snowflake command: %s", e)
            sys.exit(1)

        return query_results

    def create_snowflake_connection(self, conn_params):
        """Create a Snowflake connection instance."""
        try:
            # Connect to Snowflake
            conn = snowflake.connector.connect(**conn_params)
        except (
            snowflake.connector.errors.ProgrammingError,
            snowflake.connector.errors.DatabaseError,
        ) as e:
            if e.errno == 251005:
                message = f"Invalid username/password. Message: '{e.msg}'."
            elif e.errno == 250001:
                message = f"Invalid Snowflake account name provided. Message: '{e.msg}'."
            else:
                message = f"Error {e.errno} ({e.sqlstate}): ({e.sfqid})"
            logger.error(f"\nERROR: {message}\n")
            sys.exit(1)

        return conn


if __name__ == "__main__":
    """This is executed when run from the command line"""
