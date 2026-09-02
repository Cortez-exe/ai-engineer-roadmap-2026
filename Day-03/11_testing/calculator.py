def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

# ============================================================
# REVIEWER — DAY 3: TESTING — APPLICATION CODE
# ============================================================
#
# PURPOSE:
# This file contains the functions that will be tested by
# test_calculator.py.
#
# KEY CONCEPTS:
# - Keep application logic separate from test code.
# - Functions should have predictable inputs and outputs.
# - Small, focused functions are easier to test.
#
# TESTING FLOW:
#
# calculator.py
#       ↓
# functions
#       ↓
# test_calculator.py
#       ↓
# pytest
#       ↓
# PASS / FAIL
#
# AI ENGINEERING RELEVANCE:
# AI systems contain many pieces of normal application logic
# around the actual model. Testing these functions helps prevent
# bugs when the application changes.
# ============================================================