#!/usr/bin/env python3
"""
Description: Jinja utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys

from jinja2 import Environment, FileSystemLoader

# Custom modules
from python_utils.classes.core.logging_utils import LoggingUtils
from python_utils.classes.core.variable_utils import VariableUtils

# fetch common variable util functions from variable_setup module
variable_utils = VariableUtils()

# Set up logging using custom shared module
logging_utils = LoggingUtils()
logger = logging_utils.logger


class JinjaTemplateRenderer:
    def setup_jinja_template(self, jinja_templates_dir, ip_jinja_template_file):
        """Set up/get the Jinja template"""

        logger.debug("Function called 'JinjaTemplateRenderer.setup_jinja_template()'")

        file_template = os.path.join(jinja_templates_dir, ip_jinja_template_file)

        # fmt: off
        # Validate the Jinja template
        if not os.path.exists(file_template):
            logger.error(f"Error: Jinja template not found. Path to Jinja template: {file_template}.")
            sys.exit(1)
        # fmt: on

        jinja_env = Environment(loader=FileSystemLoader(jinja_templates_dir), autoescape=True)
        return jinja_env.get_template(ip_jinja_template_file)

    def render_jinja_template(self, jinja_templates_dir, jinja_template, **kwargs):
        """Render an input jinja template"""

        logger.debug("Function called 'JinjaTemplateRenderer.render_jinja_template()'")

        # Set up the jinja template
        ip_jinja_template_file = self.setup_jinja_template(jinja_templates_dir, jinja_template)

        # Render the jinja template
        rendered_template = ip_jinja_template_file.render(**kwargs)

        return rendered_template
