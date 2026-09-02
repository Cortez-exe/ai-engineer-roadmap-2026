from dataclasses import dataclass


@dataclass
class Developer:
    name: str
    experience_years: float
    skills: list[str]
    currently_hiring: bool

drei = Developer(
    "Andrei", 
    4.5, 
    ["Python", "HTML", "CSS", "JS"], 
    True)

print(drei)


# ============================================================
# REVIEWER — DAY 3: DATACLASSES
# ============================================================
#
# KEY CONCEPTS:
# - A dataclass is a convenient way to create classes used
#   primarily for storing structured data.
# - @dataclass automatically provides useful methods such as
#   __init__() and __repr__().
# - Fields can have type hints.
#
# KEY SYNTAX:
#
# from dataclasses import dataclass
#
# @dataclass
# class Developer:
#     name: str
#     experience_years: float
#     skills: list[str]
#
# OBJECT CREATION:
#
# developer = Developer(
#     "Andrei",
#     2.0,
#     ["Python", "AI"]
# )
#
# IMPORTANT:
# @dataclass is a decorator placed directly above the class.
#
# AI ENGINEERING RELEVANCE:
# Dataclasses are useful for representing structured information
# such as documents, users, API requests, model configurations,
# messages, and pipeline results.
# ============================================================