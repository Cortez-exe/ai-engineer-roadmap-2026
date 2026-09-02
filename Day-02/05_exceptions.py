try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print(f"You entered: {number}")
finally:
    print("Program finished.")