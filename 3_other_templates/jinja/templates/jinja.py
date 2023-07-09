#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : jinja.py
* Description   : Demo jinja template script
* Created       : 14-07-2021
* Usage         : python3 jinja.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

import os
from jinja2 import Environment, FileSystemLoader

working_dir = os.getcwd()

if __name__ == "__main__":
    """This is executed when run from the command line"""

    template_dir = os.path.join(working_dir, "templates")
    jinja_env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)
    template = jinja_env.get_template("eg_template.sql.j2")

    data_src = "eg_src"
    src_db = "eg_src_db"
    src_db_schema = "eg_src_db_schema"
    src_tbl_name = "eg_src_tbl_name"

    rendered_op = template.render(data_src=data_src, src_db=src_db, src_db_schema=src_db_schema, src_tbl_name=src_tbl_name)

    with open(os.path.join(working_dir, "op", "eg_op.sql"), "w") as op:
        op.write(rendered_op)
