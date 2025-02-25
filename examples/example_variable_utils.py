#!/usr/bin/env python3
"""
Description: Example usage of the VariableUtils class
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

from python_utils.classes.core.variable_utils import VariableUtils


def validate_env_vars_example(variable_utils):
    """Example: Validate environment variables."""
    required_env_vars = ["HOME", "USER", "SHELL"]
    variable_utils.validate_env_vars(required_env_vars)


def load_ip_params_from_config_example(variable_utils):
    """Example: Load IP parameters from config file."""
    config_file_path = "config.yaml"
    if not os.path.exists(config_file_path):
        # Create a sample config.yaml file if it doesn't exist
        with open(config_file_path, "w") as config_file:
            config_file.write("param1: value1\nparam2: value2\n")

    ip_params = variable_utils.load_ip_params_from_config(config_file_path)
    print("IP Parameters:", ip_params)


def setup_directory_vars_example(variable_utils):
    """Example: Setup directory variables."""
    project_dir = "python_templates"
    script_dir, src_dir, ip_dir = variable_utils.setup_directory_vars(project_dir)
    print("Script Directory:", script_dir)
    print("Source Directory:", src_dir)
    print("Inputs Directory:", ip_dir)


def main():
    variable_utils = VariableUtils()

    # Run examples
    validate_env_vars_example(variable_utils)
    load_ip_params_from_config_example(variable_utils)
    setup_directory_vars_example(variable_utils)


if __name__ == "__main__":
    main()
