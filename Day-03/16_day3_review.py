# ============================================================
# REVIEWER — DAY 3: PYTHON ENGINEERING FUNDAMENTALS
# ============================================================
#
# DAY 3 GOAL:
# Move from simply writing Python code to writing Python code
# that is structured, testable, maintainable, and suitable for
# larger AI engineering projects.
#
# ============================================================
# 1. TYPE HINTS
# ============================================================
#
# Type hints describe expected input and output types.
#
# Example:
#
# def add(a: int, b: int) -> int:
#     return a + b
#
# Common types:
#     str
#     int
#     float
#     bool
#     list[str]
#     dict[str, int]
#
# Type hints improve readability and help tools detect mistakes.
#
# ============================================================
# 2. DATACLASSES
# ============================================================
#
# @dataclass provides a convenient way to create classes mainly
# used for storing structured data.
#
# Example:
#
# @dataclass
# class Document:
#     title: str
#     content: str
#     pages: int
#
# Useful for representing structured data such as:
#     documents
#     users
#     API data
#     configuration
#     model results
#
# ============================================================
# 3. GENERATORS
# ============================================================
#
# Generators use `yield` to produce values one at a time.
#
# Example:
#
# def process(items):
#     for item in items:
#         yield item
#
# `return` ends a function.
# `yield` pauses a generator and produces a value.
#
# Useful when processing large amounts of data incrementally.
#
# ============================================================
# 4. PYTEST / TESTING
# ============================================================
#
# pytest automatically discovers functions beginning with
# `test_`.
#
# Example:
#
# def test_add():
#     assert add(2, 3) == 5
#
# Test both:
#     - normal/happy paths
#     - edge cases
#     - invalid inputs
#     - expected exceptions
#
# Exception testing:
#
# with pytest.raises(ValueError):
#     function(...)
#
# ============================================================
# 5. LOGGING
# ============================================================
#
# Logging records events happening inside an application.
#
# Common levels:
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
#
# Example:
#
# logging.info("Processing document")
# logging.error("Document failed")
#
# Logging is more useful for production applications than
# relying entirely on print().
#
# ============================================================
# 6. EXCEPTIONS
# ============================================================
#
# try:
#     risky_operation()
# except SomeError:
#     handle_error()
#
# Other keywords:
#
# raise   -> manually trigger an exception
# else    -> runs when no exception occurred
# finally -> always runs
#
# Custom exception:
#
# class InvalidDocumentError(Exception):
#     pass
#
# Prefer catching specific exceptions instead of:
#
# except:
#     ...
#
# ============================================================
# 7. CLEAN CODE
# ============================================================
#
# Good code should be:
#     readable
#     understandable
#     maintainable
#     easy to modify
#
# Functions should have meaningful responsibilities.
#
# Avoid:
#     - huge functions
#     - unnecessary tiny functions
#     - duplicated logic
#     - unclear names
#     - excessive nesting
#
# ============================================================
# 8. PROGRAM STRUCTURE
# ============================================================
#
# A common Python application structure:
#
# def main():
#     ...
#
#
# if __name__ == "__main__":
#     main()
#
# This gives the program a clear entry point.
#
# ============================================================
# AI ENGINEERING CONNECTION
# ============================================================
#
# These concepts form the foundation for larger systems:
#
# Python
#   ↓
# APIs
#   ↓
# FastAPI
#   ↓
# LLM APIs
#   ↓
# RAG
#   ↓
# Agents
#   ↓
# Automation / n8n
#   ↓
# Cloud deployment
#
# The goal is not to memorize every Python feature.
#
# The goal is to become comfortable enough with Python that
# you can focus on solving AI engineering problems instead of
# fighting the language.
#
# ============================================================

def main():
    pass


# 1. What does -> str mean in this function?
#
# def greet(name: str) -> str:
#
# i think it means that the output would be a string type data

# 2. What problem does @dataclass solve?
#
# it's like a blueprint that helps you create an object based on that specific class with all the necessary content

# 3. What is the difference between `return` and `yield`?
#
# return waits for everything to get finished processing and stores in ram, while yield lets you process one data at a time

# 4. What is the difference between `raise` and `except`?
#
# raise is simply the error value or message while except is an exception wherein the code block that lives here gets executed when the try block fails

# 5. When would you use logging.error() instead of logging.info()?
#
# when you are catching a specific error message or type

# 6. What does assert do in pytest?
# this is to make an assertion or assumption on what value should appear correctly and is used for testing
# 7. What does pytest.raises() allow you to test?
# all the function that starts with "test_"

# 8. Why is this bad?
#
# def process():
#     # 100 lines of code doing everything
#     ...
#
# What would you do instead?
#
# takes too much memory. so i would just use yield

# 9. Imagine you have 10,000 PDF documents that need to be
# processed for a future RAG system.
#
# Which Day 3 concept would be useful for processing them
# one at a time without creating a giant list of results?
#
# Why?
#
# yield. this takes one information at a time instead of processing everything at once

if __name__ == "__main__":
    main()