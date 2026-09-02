def greet(name: str) -> str:
    return f"Hello, {name}! What's up?"


def multiply(a: float, b: float) -> float:
    return a * b


def get_skills() -> list[str]:
    return ["Python", "FastAPI", "AI"]


print(greet("Andrei"))
print(multiply(10.5, 5))
print(get_skills())



# ============================================================
# REVIEWER — DAY 3: TYPE HINTS
# ============================================================
#
# KEY CONCEPTS:
# - Type hints describe what type of data a function expects.
# - Type hints also describe what a function should return.
# - Type hints improve readability, autocomplete, and tooling.
# - Python normally does NOT enforce type hints at runtime.
#
# KEY SYNTAX:
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
# IMPORTANT:
# Type hints are guidance for developers and tools such as
# Pylance, Pyright, and mypy.
#
# AI ENGINEERING RELEVANCE:
# AI applications often contain many functions that pass
# structured data between APIs, models, databases, and
# processing pipelines. Type hints make these systems easier
# to understand and maintain.
# ============================================================