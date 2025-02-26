#!/usr/bin/env python3
"""
Description: Tests for Jinja utility functions
Date created: 2025-02-26
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
from unittest.mock import MagicMock, patch

import pytest
from python_utils.classes.core.variable_utils import VariableUtils  # Import VariableUtils
from python_utils.classes.integrations.jinja_utils import JinjaTemplateRenderer


@pytest.fixture
def jinja_renderer():
    return JinjaTemplateRenderer()


@pytest.fixture
def jinja_templates_dir():
    variable_utils = VariableUtils()
    _, src_dir, _ = variable_utils.setup_directory_vars("python_templates")
    return os.path.join(src_dir, "templates/jinja_templates")


def test_setup_jinja_template_success(jinja_renderer, jinja_templates_dir):
    with patch("os.path.exists", return_value=True), patch("jinja2.Environment.get_template", return_value=MagicMock()):
        template = jinja_renderer.setup_jinja_template(jinja_templates_dir, "sql_query_template.sql.j2")
        assert template is not None


def test_setup_jinja_template_not_found(jinja_renderer, jinja_templates_dir):
    with patch("os.path.exists", return_value=False), patch("sys.exit") as mock_exit:
        with patch("jinja2.Environment") as mock_env:
            jinja_renderer.setup_jinja_template(jinja_templates_dir, "sql_query_template.sql.j2")
            mock_exit.assert_called_once_with(1)
            mock_env.assert_not_called()


def test_render_jinja_template(jinja_renderer, jinja_templates_dir):
    with patch.object(
        jinja_renderer,
        "setup_jinja_template",
        return_value=MagicMock(render=MagicMock(return_value="rendered content")),
    ):
        result = jinja_renderer.render_jinja_template(
            jinja_templates_dir,
            "sql_query_template.sql.j2",
            columns=["id", "name"],
            table_name="users",
            condition="id > 10",
        )
        assert result == "rendered content"
