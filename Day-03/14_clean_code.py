def get_name() -> str:
    name = input("Enter your name: ").strip()

    if name == "":
        raise ValueError("Name cannot be empty!")

    return name

def get_age() -> int:
    age = int(input("How old are you: "))

    if age < 0:
        raise ValueError("Age cannot be less than 0!")

    return age

def greetings(name: str, age: int) -> str:
    return f"Hello {name}! Congratulations on turning {age} years old!"


def process():
    try:
        name = get_name()
        age = get_age()
        message = greetings(name, age)
        print(message)
    except ValueError as error:
        print(f"Error: {error}")






if __name__ == "__main__":
    process()










# ============================================================
# REVIEWER — DAY 3: CLEAN CODE
# ============================================================
# KEY CONCEPTS:
# - Functions should have a clear responsibility.
# - Use descriptive names.
# - Keep functions reasonably small.
# - Avoid unnecessary duplication.
# - Separate business logic from input/output.
# - Clean code should be easy to read and modify.
#
# IMPORTANT:

# "Clean code" does NOT mean making code as short as possible.
# It means making the code understandable and maintainable.
#
# AI ENGINEERING RELEVANCE:
# AI applications can quickly become complicated because they
# combine APIs, models, databases, prompts, documents, and
# external services. Clean separation of responsibilities makes
# these systems easier to debug, test, and extend.
# ============================================================
