#!/usr/bin/env python3
"""
Description: A script for interacting with Azure Key Vault, including operations for listing, retrieving, saving, and deleting secrets.
Date created: 2024-08-08
"""
# flake8: noqa: E402

__author__ = "Paul Fry"
__version__ = "1.0"

"""
* Note           : Requires Azure CLI authentication (i.e., the command `az login` must be run beforehand).
* Usage          : python3 azure_key_vault_client.py <command>
* Commands       :
*                 - list_secrets
*                 - get_secret_value <secret_name>
*                 - save_secret <secret_name> <secret_value>
*                 - delete_secret <secret_name>
"""

import os
import sys

import azure_key_vault_helpers as kv_helpers
from dotenv import load_dotenv

# custom modules
from python_utils.classes.core.logging_utils import LoggingUtils
from validate_inputs import InputValidator

validator_utils = InputValidator()

# Load environment variables from .env file
load_dotenv()

# Instantiate LoggingUtils and get the logger
logging_utils = LoggingUtils()
logger = logging_utils.logger

# Constants
PY_SCRIPT_NAME = os.path.basename(__file__)


def main(secret_client, key_vault_url, kev_vault_command):
    """Parse and execute the Azure Key Vault command provided by the user."""

    # store the function name as a constant
    FUNCTION_NAME = "handle_az_kv_command"

    if kev_vault_command == "list_secrets":
        kv_helpers.list_secrets(secret_client, key_vault_url)

    elif kev_vault_command == "get_secret_value":
        # Log an error if the secret name is missing
        if len(sys.argv) < 3:
            error_msg = "Missing 'secret_name' argument for 'get_secret_value'."
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "ArgumentError")
            sys.exit(1)

        # else, return the value for the secret
        kv_helpers.get_secret_value(secret_client, sys.argv[2])

    elif kev_vault_command == "save_secret":
        # Log an error if the secret name or value is missing
        if len(sys.argv) < 4:
            error_msg = "Missing 'secret_name' or 'secret_value' argument for 'save_secret'."
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "ArgumentError")
            sys.exit(1)

        # else, save the secret
        kv_helpers.save_secret(secret_client, sys.argv[2], sys.argv[3])

    elif kev_vault_command == "delete_secret":
        # Log an error if the secret name is missing
        if len(sys.argv) < 3:
            error_msg = "Missing 'secret_name' argument for 'delete_secret'."
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "ArgumentError")
            sys.exit(1)

        # else, delete the secret
        kv_helpers.delete_secret(secret_client, sys.argv[2])

    else:
        # Log an error if an invalid command is provided
        error_msg = "Invalid command. Use 'list_secrets', 'get_secret_value', 'save_secret', or 'delete_secret'."
        logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "CommandError")
        sys.exit(1)


if __name__ == "__main__":
    # Log message, re: addressing the az login prerequisite
    message = "Note: Remember to authenticate to Azure using the CLI command 'az login' before executing the script."
    logging_utils.log_header(message, char="-", length=102)

    # Validate command-line arguments
    validator_utils.validate_user_inputs()

    # Get Azure Key Vault client and URL
    secret_client, key_vault_url = kv_helpers.get_azure_constructors()

    # Orchestrate he script execution
    main(secret_client, key_vault_url, sys.argv[1])
