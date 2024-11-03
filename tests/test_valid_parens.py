import pytest
from valid_parens import is_valid

# FILE: test_valid_parens.py


def test_valid_parentheses():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("{[]}") == True

def test_invalid_parentheses():
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[}") == False

def test_edge_cases():
    assert is_valid("") == True
    assert is_valid("(") == False
    assert is_valid(")") == False