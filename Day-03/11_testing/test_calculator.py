from calculator import multiply, divide
import pytest


def test_multiply_integers():
    assert multiply(10, 5) == 50

def test_multiply_decimals():
    assert multiply(2.5, 4) == 10

def test_multiply_by_zero():
    assert multiply(100, 0) == 0

def test_division_integer():
    assert divide(10, 2) == 5

def test_division_decimals():
    assert divide(7.5, 2.5) == 3

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)



# ============================================================
# REVIEWER — DAY 3: PYTEST
# ============================================================
# - pytest automatically discovers functions starting with test_
# - assert checks whether the actual result matches expectations.
# - Test normal inputs (happy paths).
# - Test edge cases such as zero, decimals, empty values, etc.
# - pytest.raises() verifies that code raises an expected exception.
#
# Key syntax:
#   assert function(...) == expected
#
#   with pytest.raises(ExpectedError):
#       function(...)
#
# AI ENGINEERING RELEVANCE:
# Automated tests help ensure AI/API/data-processing code keeps
# working when the application changes.
# ============================================================