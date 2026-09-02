import json

profile = {
    "name": "Andrei",
    "age": 22,
    "skills": ["Python", "AI", "FastAPI"]
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r") as file:
    profile = json.load(file)


print(f"Name: {profile['name']}")
print(f"Age: {profile['age']}")
print(f"Skills: {', '.join(profile['skills'])}")



print(type(profile))
