#!/usr/bin/env python3
"""
Description: Tests for VariableUtils class
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

import pytest
from python_utils.classes.core.variable_utils import VariableUtils


@pytest.fixture
def variable_utils():
    """PyTest Fixture to create an instance of VariableUtils."""
    return VariableUtils()


def test_validate_env_vars(variable_utils, caplog, REQUIRED_ENV_VARS=None):
    """Test the validate_env_vars method."""
    if REQUIRED_ENV_VARS is None:
        REQUIRED_ENV_VARS = ["HOME", "USER", "SHELL", "NON_EXISTENT_VAR"]
    variable_utils.validate_env_vars(REQUIRED_ENV_VARS)

    assert "Error: The following environment variables are missing:" in caplog.text
    for var in REQUIRED_ENV_VARS:
        if var not in os.environ:
            assert var in caplog.text


def test_load_ip_params_from_config(variable_utils, tmp_path, caplog):
    """Test the load_ip_params_from_config method."""
    config_file_path = tmp_path / "config.yaml"
    config_content = """
    param1: value1
    param2: value2
    """
    config_file_path.write_text(config_content)

    ip_params = variable_utils.load_ip_params_from_config(config_file_path)
    assert ip_params == {"param1": "value1", "param2": "value2"}

    # Test FileNotFoundError
    non_existent_path = tmp_path / "non_existent.yaml"
    variable_utils.load_ip_params_from_config(non_existent_path)
    assert "Config file not found at" in caplog.text

    # Test YAMLError
    invalid_config_content = """
    param1: value1
    param2: value2
    : invalid
    """
    config_file_path.write_text(invalid_config_content)
    variable_utils.load_ip_params_from_config(config_file_path)
    assert "Failed to load config file" in caplog.text


def test_setup_directory_vars(variable_utils, tmp_path, caplog):
    """Test the setup_directory_vars method."""
    project_dir = "python_templates"
    script_dir = tmp_path / project_dir / "src"

    script_dir.mkdir(parents=True)

    os.chdir(script_dir)
    script_dir, src_dir, ip_dir = variable_utils.setup_directory_vars(project_dir)

    # Adjust the assertions to match the actual directory structure
    assert src_dir.endswith("src")
    assert ip_dir.endswith("inputs")

    # Test project root not found
    script_dir, src_dir, ip_dir = variable_utils.setup_directory_vars("non_existent_project")
    assert script_dir is None
    assert src_dir is None
    assert ip_dir is None
    assert "Error: Project root not found in script path." in caplog.text
