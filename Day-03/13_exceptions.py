number = input("Enter a number: ")

try:
    result= 100 / int(number) 
    print(result)
except ValueError:
    print(f"{number} is not a number. It's a word!")
except ZeroDivisionError:
    print("You cannot divide by 0!")
else:
    print("Calculation was successful!")
finally:
    print("Calculation finished.")

class InvalidScoreError(Exception):
    pass


def calculate_score(score):
    try:
        if score > 100 or score < 0:
            raise InvalidScoreError("Score is not within the range!")

        return f"Score accepted: {score}"

    except InvalidScoreError as error:
        return f"Invalid score: {score} - {error}"

print(calculate_score(85))
print(calculate_score(-10))
print(calculate_score(150))






# ============================================================
# REVIEWER — DAY 3: EXCEPTIONS
# ============================================================
# KEY CONCEPTS:
# - An exception is an error/event that interrupts normal execution.
# - try = code that might cause an exception.
# - except = what to do when a specific exception occurs.
# - raise = manually create/trigger an exception.
# - else = runs when no exception occurred.
# - finally = runs whether an exception occurred or not.
#
# KEY SYNTAX:
#
# try:
#     risky_operation()
# except SomeError:
#     handle_error()
#
# IMPORTANT:
# Prefer catching specific exceptions instead of using:
#
# except:
#     ...
#
# This prevents unrelated bugs from being silently hidden.
#
# AI ENGINEERING RELEVANCE:
# AI applications frequently deal with API failures, invalid
# input, network errors, malformed JSON, missing files, and
# authentication problems. Proper exception handling prevents
# the entire application from crashing unexpectedly.
# ============================================================