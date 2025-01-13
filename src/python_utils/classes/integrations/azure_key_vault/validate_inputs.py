#!/usr/bin/env python3
"""
Description: Provides functionality to validate command-line arguments for Azure Key Vault operations, including command and parameter checks.
Date created: 2024-08-08
"""
# flake8: noqa: E402

__author__ = "Paul Fry"
__version__ = "1.0"

import sys
import os

# Append src/py/shared/ to sys.path so that we can import its classes & functions
shared_py_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(shared_py_dir_path)

from shared.classes.logging_utils import LoggingUtils

# Initialize logging utilities
logging_utils = LoggingUtils()  # Create an instance of LoggingUtils for logging

# Constants
PY_SCRIPT_NAME = os.path.basename(__file__)  # Get the name of the current script


class InputValidator:
    """A class to validate command-line arguments for Azure Key Vault operations."""

    def __init__(self):
        """Initialize the InputValidator with logging utilities."""
        self.logger = logging_utils.logger  # Initialize the logger from LoggingUtils

    def validate_command(self, key_vault_command):
        """Validate the command-line command."""

        # Define valid Key Vault commands
        KEY_VAULT_COMMANDS = ["list_secrets", "get_secret_value", "save_secret", "delete_secret"]

        if key_vault_command not in KEY_VAULT_COMMANDS:
            # Log error if the command is not in the list of valid commands
            error_msg = (
                f"Invalid command '{key_vault_command}'. " f"Valid commands are: {', '.join(KEY_VAULT_COMMANDS)}."
            )
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, "validate_command", "ArgumentError")
            sys.exit(1)

    def validate_parameters(self, key_vault_command, args):
        """Validate command-line arguments based on the command."""

        FUNCTION_NAME = "validate_parameters"  # Name of the current function for logging purposes

        # Define commands that require additional parameters
        extra_param_reqd = ["get_secret_value", "save_secret", "delete_secret"]

        if key_vault_command in extra_param_reqd and len(args) < 3:
            # Log error if the command requires additional arguments and they are not provided
            error_msg = f"The function '{key_vault_command}' requires an extra input argument."
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "ArgumentError")
            sys.exit(1)

        elif key_vault_command == "save_secret" and len(args) < 4:
            # Log error if 'save_secret' requires an additional argument for the secret value and it's not provided
            error_msg = "The function 'save_secret' requires an extra input argument for 'secret_value'."
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "ArgumentError")
            sys.exit(1)

    def validate_user_inputs(self):
        """Validate command-line arguments."""

        # Log error if no command is provided
        if len(sys.argv) < 2:
            error_msg = "No command provided. Use one of the valid commands."
            logging_utils.log_error(error_msg, PY_SCRIPT_NAME, "validate_user_inputs", "ArgumentError")
            sys.exit(1)

        # Validate the command and its parameters
        self.validate_command(sys.argv[1])
        self.validate_parameters(sys.argv[1], sys.argv)
