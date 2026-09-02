with open("notes.txt", "w") as file:
    file.write("Python\n")
    file.write("FastAPI\n")
    file.write("Git\n")
    file.write("AI Engineering\n")

with open("notes.txt", "a") as file:
    file.write("Machine Learning\n")

with open("notes.txt", "r") as file:
    content = file.read()


print(content)