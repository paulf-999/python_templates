#!/usr/bin/env python3
"""
Description: Executes a Snowflake command using the snowflake-connector-python library.
Date: 2023-08-30
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys
import argparse
import logging
import snowflake.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)

# Constants
REQUIRED_ENV_VARS = [
    "SNOWFLAKE_USER",
    "SNOWFLAKE_PASSWORD",
    "SNOWFLAKE_ACCOUNT",
    "SNOWFLAKE_WAREHOUSE",
    "SNOWFLAKE_DATABASE",
    "SNOWFLAKE_SCHEMA",
]


def execute_snowflake_command(conn, sql_command, query_result_str=""):
    """Execute Snowflake command(s)"""
    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL command
        cursor.execute(sql_command)

        # Fetch and print the results
        query_results = cursor.fetchall()

        # store query_results in a concatenated string

        if query_results:
            query_result_str = ", ".join(str(row) for row in query_results[0])
            logger.info(query_result_str)

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return query_result_str

    except Exception as e:
        logging.exception("An error occurred while executing Snowflake command: %s", e)
        sys.exit(1)


def create_snowflake_connection(conn_params):
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


def validate_env_vars(required_env_vars):
    """Verify whether the required environment variables exist."""

    missing_env_vars = [var for var in required_env_vars if os.getenv(var) is None]
    if missing_env_vars:
        logger.error("\nError: The following environment variables are missing:\n")
        for var in missing_env_vars:
            logger.error(var)
        exit(1)


def validate_input_args(args):
    """Validate that an input arg has been provided"""

    if not args.sql_command and not args.sql_file:
        logger.error("Error: You must provide either --sql-command or --sql-file.")
        sys.exit(1)


def main(args):
    """Main entry point of the script."""

    try:
        # Validate that an input arg has been provided
        validate_input_args(args)

        # Verify whether the required environment variables exist
        validate_env_vars(REQUIRED_ENV_VARS)

        # Store the Snowflake connection parameters from environment variables
        conn_params = {
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
            "database": os.getenv("SNOWFLAKE_DATABASE"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        }

        # If a SQL file has been passed in, assign it to the var sql_command
        if args.sql_file:
            with open(args.sql_file) as file:
                sql_command = file.read()
        else:
            # else assign the var sql_command the value of the input SQL statement
            sql_command = args.sql_command

        # Connect to Snowflake DB
        conn = create_snowflake_connection(conn_params)

        # Execute the Snowflake command
        query_result_str = execute_snowflake_command(conn, sql_command)

    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    """This is executed when run from the command line"""

    parser = argparse.ArgumentParser(description="Execute a Snowflake command.")
    parser.add_argument("--sql-command", help="Snowflake SQL command to execute")
    parser.add_argument("--sql-file", help="Path to a .sql file containing the SQL command")
    args = parser.parse_args()
    main(args)
