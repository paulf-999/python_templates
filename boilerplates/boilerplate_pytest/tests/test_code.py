#!/usr/bin/env python3
"""
Python Version  : 3.8
* Name          : test_code.py
* Description   : Example usage of calling the pytests
* Created       : 26-02-2021
* Usage         : pytest tests/test_code.py
"""

__author__ = "Paul Fry"
__version__ = "0.1"

from src.boilerplate import is_even


def test_valid_even():
    assert is_even(2)
