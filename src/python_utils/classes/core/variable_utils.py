#!/usr/bin/env python3
"""
Description: Variable setup utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

import yaml

# Custom modules
from python_utils.classes.core.logging_utils import LoggingUtils

logging_utils = LoggingUtils()
logger = logging_utils.logger

# Store the name of this py script as a var
py_script_name = os.path.basename(__file__)


class VariableUtils:
    def validate_env_vars(self, REQUIRED_ENV_VARS):
        """Verify whether the required environment variables exist."""

        # Check if any required environment variables are missing or empty
        missing_or_empty_env_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]

        # Log missing or empty environment variables as errors
        if missing_or_empty_env_vars:
            logger.error("\nError: The following environment variables are missing:\n")
            for var in missing_or_empty_env_vars:
                logger.error(var)

    def load_ip_params_from_config(self, config_file_path):
        """Load variables from a config.yaml into ip_params dictionary.
        Args:
            config_file_path (str): The path to the config.yaml file.
        Returns:
            ip_params: A dictionary containing the parameters loaded from the config.yaml file.
        """

        logger.debug("Function called 'VariableUtils.load_ip_params_from_config()'")

        ip_params = {}  # store the params in a dictionary

        try:
            with open(config_file_path) as config_file:
                ip_params = yaml.safe_load(config_file)

        except FileNotFoundError as e:
            logging_utils.log_error(
                message=f"Config file not found at {config_file_path}",
                script_name=py_script_name,
                function_name="load_ip_params_from_config()",
                error=e,
            )
        except yaml.YAMLError as e:
            logging_utils.log_error(
                message=f"Failed to load config file {config_file_path}",
                script_name=py_script_name,
                function_name="load_ip_params_from_config()",
                error=e,
            )

        return ip_params

    def setup_directory_vars(self, PROJECT_DIR):
        """Set up project directories.
        Args:
            PROJECT_DIR (str): The name of the project directory.
        Returns:
            SCRIPT_DIR (str): The path to the directory where the calling script is located.
            SRC_DIR (str): The path to the 'src' directory at the project root level.
            IP_DIR (str): The path to the 'inputs' directory at the project root level.
        """

        logger.debug("Function called 'VariableUtils.setup_directory_vars()'")

        # Get the directory name of where the calling script is located
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

        # Find the project root by searching for the project_root variable in the script path
        root_index = SCRIPT_DIR.find(PROJECT_DIR)

        if root_index != -1:
            # fmt: off
            # Construct paths for source directory and inputs directory at the project root level
            SRC_DIR = os.path.abspath(os.path.join(SCRIPT_DIR[: root_index + len(PROJECT_DIR)], "src"))
            IP_DIR = os.path.abspath(os.path.join(SCRIPT_DIR[: root_index + len(PROJECT_DIR)], "inputs"))

            # Log the directory path vars for debugging purposes
            list_dir_vars_str = ["SCRIPT_DIR", "SRC_DIR", "IP_DIR"]
            list_dir_vars = [SCRIPT_DIR, SRC_DIR, IP_DIR]

            for var_name, var_value in zip(list_dir_vars_str, list_dir_vars):
                logger.debug(f"{var_name} = {var_value}")
            # fmt: on

            return SCRIPT_DIR, SRC_DIR, IP_DIR
        else:
            logger.debug("Error: Project root not found in script path.")
            return None, None, None
