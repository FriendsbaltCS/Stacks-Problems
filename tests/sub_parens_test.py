# FILE: test_sub_parens.py

import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sub_parens import max_length


def test_valid_sub_parentheses():
    assert max_length("()") == 2
    assert max_length("()()") == 4
    assert max_length("(()())") == 6

def test_invalid_sub_parentheses():
    assert max_length(")(") == 0
    assert max_length("(()") == 2
    assert max_length(")()())") == 4

def test_subparens_edge_cases():
    assert max_length("") == 0
    assert max_length("(") == 0
    assert max_length(")") == 0