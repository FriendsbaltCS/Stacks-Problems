import pytest

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dijkstra import evaluate_expression

# FILE: test_dijkstra.py


def test_simple_expressions():
    assert evaluate_expression("3+2") == 5
    assert evaluate_expression("10-3") == 7
    assert evaluate_expression("4*5") == 20
    assert evaluate_expression("8/2") == 4

def test_expressions_with_negative_numbers():
    assert evaluate_expression("-3+2") == -1
    assert evaluate_expression("10--3") == 13
    assert evaluate_expression("4*-5") == -20
    assert evaluate_expression("8/-2") == -4

def test_order_of_operations():
    assert evaluate_expression("3+2*2") == 7
    assert evaluate_expression("10-3*2") == 4
    assert evaluate_expression("4*5+2") == 22
    assert evaluate_expression("8/2+2") == 6

def test_expressions_with_parentheses():
    assert evaluate_expression("(3+2)*2") == 10
    assert evaluate_expression("10/(5-3)") == 5
    assert evaluate_expression("2*(3+4)") == 14
    assert evaluate_expression("(2+3)*(4-1)") == 15

def test_expressions_with_spaces():
    assert evaluate_expression(" 3 + 2 ") == 5
    assert evaluate_expression(" 10 - 3 ") == 7
    assert evaluate_expression(" 4 * 5 ") == 20
    assert evaluate_expression(" 8 / 2 ") == 4

def test_equal_precedence_operations():
    assert evaluate_expression("3+3+3") == 9
    assert evaluate_expression("10-3+2") == 9
    assert evaluate_expression("4*5*2") == 40
    assert evaluate_expression("8/2/2") == 2

def test_dij_edge_cases():
    assert evaluate_expression("") == 0
    assert evaluate_expression("42") == 42
    assert evaluate_expression("-5") == -5