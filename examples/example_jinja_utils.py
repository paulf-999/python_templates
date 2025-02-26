#!/usr/bin/env python3
"""
Description: Example usage of the JinjaTemplateRenderer class
Date created: 2025-02-26
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os

from python_utils.classes.core.logging_utils import LoggingUtils
from python_utils.classes.core.variable_utils import VariableUtils
from python_utils.classes.integrations.jinja_utils import JinjaTemplateRenderer

variable_utils = VariableUtils()
logging_utils = LoggingUtils()
logger = logging_utils.configure_logging()


def setup_template(jinja_renderer, jinja_templates_dir, template_file):
    """Set up the Jinja template."""
    logging_utils.log_header("Example function: setup_template()")

    # Set up the Jinja template
    template = jinja_renderer.setup_jinja_template(jinja_templates_dir, template_file)
    logger.info(f"Jinja template set up: {template_file}")

    return template


def render_template(jinja_renderer, jinja_templates_dir, template_file, **kwargs):
    """Render the Jinja template."""
    logging_utils.log_header("Example function: render_template()")

    # Render the Jinja template
    rendered_content = jinja_renderer.render_jinja_template(jinja_templates_dir, template_file, **kwargs)
    logger.info(f"Rendered Jinja template:\n\n{rendered_content}\n")
    return rendered_content


def main():
    # Create an instance of JinjaTemplateRenderer
    jinja_renderer = JinjaTemplateRenderer()

    _, src_dir, _ = variable_utils.setup_directory_vars("python_templates")

    jinja_templates_dir = os.path.join(src_dir, "templates/jinja_templates")
    template_file = "sql_query_template.sql.j2"

    # Set up the Jinja template
    setup_template(jinja_renderer, jinja_templates_dir, template_file)

    # Render the Jinja template
    render_template(
        jinja_renderer,
        jinja_templates_dir,
        template_file,
        columns=["id", "name"],
        table_name="users",
        condition="id > 10",
    )


if __name__ == "__main__":
    main()
