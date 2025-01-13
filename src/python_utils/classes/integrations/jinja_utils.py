#!/usr/bin/env python3
"""
Description: Jinja utility functions to be imported by other python scripts
Date created: 2025-01-13
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys
from jinja2 import Environment
from jinja2 import FileSystemLoader

from core.logging_utils import LoggingUtils
from core.variable_utils import VariableUtils

# fetch common variable util functions from variable_setup module
variable_utils = VariableUtils()


class JinjaTemplateRenderer:
    def __init__(self):
        # Instantiate the object properties
        self.logger = LoggingUtils.configure_logging(self)

    def setup_jinja_template(self, jinja_templates_dir, ip_jinja_template_file):
        """Set up/get the Jinja template"""

        self.logger.debug("Function called 'JinjaTemplateRenderer.setup_jinja_template()'")

        file_template = os.path.join(jinja_templates_dir, ip_jinja_template_file)

        # fmt: off
        # Validate the Jinja template
        if not os.path.exists(file_template):
            self.logger.error(f"Error: Jinja template not found. Path to Jinja template:\n\n{file_template}.")
            sys.exit(1)
        # fmt: on

        jinja_env = Environment(loader=FileSystemLoader(jinja_templates_dir), autoescape=True)
        return jinja_env.get_template(ip_jinja_template_file)

    def render_jinja_template(self, jinja_templates_dir, jinja_template, **kwargs):
        """Render an input jinja template"""

        self.logger.debug("Function called 'JinjaTemplateRenderer.render_jinja_template()'")

        # Set up the jinja template
        ip_jinja_template_file = self.setup_jinja_template(jinja_templates_dir, jinja_template)

        # Render the jinja template
        rendered_template = ip_jinja_template_file.render(**kwargs)

        return rendered_template
