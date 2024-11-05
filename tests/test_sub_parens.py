# FILE: test_sub_parens.py

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sub_parens import max_length


def test_valid_parentheses():
    assert max_length("()") == 2
    assert max_length("()()") == 4
    assert max_length("(()())") == 6

def test_invalid_parentheses():
    assert max_length(")(") == 0
    assert max_length("(()") == 2
    assert max_length(")()())") == 4

def test_edge_cases():
    assert max_length("") == 0
    assert max_length("(") == 0
    assert max_length(")") == 0