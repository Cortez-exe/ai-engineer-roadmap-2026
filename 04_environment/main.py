from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("MY_NAME")
role = os.getenv("TARGET_ROLE")
company = os.getenv("TARGET_COMPANY")
months = os.getenv("MONTHS_PRACTICING")

print(f"Name: {name}")
print(f"Target Role: {role}")
print(f"Target Company to work on: {company}")
print(f"How many months to practice: {months}")