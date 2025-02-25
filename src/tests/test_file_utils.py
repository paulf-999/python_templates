#!/usr/bin/env python3
"""
Description: Tests for File utility functions
Date created: 2025-02-25
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import logging
import os

import pytest
from python_utils.classes.core.file_utils import FileUtils
from python_utils.classes.core.logging_utils import LoggingUtils


@pytest.fixture
def file_utils():
    """Fixture to create an instance of FileUtils."""
    return FileUtils()


@pytest.fixture
def logging_utils():
    """Fixture to create an instance of LoggingUtils."""
    return LoggingUtils()


def test_create_directory_if_not_exists(file_utils, tmpdir, caplog):
    """Test the create_directory_if_not_exists method."""
    test_dir = tmpdir.mkdir("test_dir")
    new_dir = os.path.join(test_dir, "new_dir")

    with caplog.at_level(logging.DEBUG):
        file_utils.create_directory_if_not_exists(new_dir)

    assert os.path.exists(new_dir)
    assert "Directory created: " in caplog.text

    with caplog.at_level(logging.DEBUG):
        file_utils.create_directory_if_not_exists(new_dir)

    assert "Directory already exists: " in caplog.text


def test_prompt_for_file_overwrite(file_utils, tmpdir, caplog):
    """Test the prompt_for_file_overwrite method."""
    test_file = tmpdir.join("test.txt")
    test_file.write("dummy content")

    class Args:
        yes = False

    args = Args()

    # Simulate user input "yes"
    input_values = ["yes"]

    def mock_input(s):
        return input_values.pop(0)

    original_input = __builtins__["input"]
    __builtins__["input"] = mock_input

    with caplog.at_level(logging.DEBUG):
        result = file_utils.prompt_for_file_overwrite(str(test_file), args)

    assert result
    assert "Overwriting existing file." in caplog.text

    # Simulate user input "no"
    input_values = ["no"]
    __builtins__["input"] = mock_input

    with caplog.at_level(logging.INFO):
        result = file_utils.prompt_for_file_overwrite(str(test_file), args)

    assert not result
    assert "File not overwritten. Skipping..." in caplog.text

    # Restore the original input function
    __builtins__["input"] = original_input


def test_find_project_root(file_utils, tmpdir):
    """Test the find_project_root method."""
    project_dir = tmpdir.mkdir("project")
    sub_dir = project_dir.mkdir("subdir")

    os.chdir(sub_dir)  # Change the current working directory to sub_dir

    result = file_utils.find_project_root("project")
    assert result == str(project_dir)

    with pytest.raises(FileNotFoundError):
        file_utils.find_project_root("non_existent_project")
