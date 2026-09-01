from greetings.messages import greet, farewell
from ai_utils.text import text_formatter


if __name__ == "__main__":
    print(greet("Andrei"))
    print(farewell("Andrei"))


result = text_formatter("Andrei will become an AI Engineer")
print(result)