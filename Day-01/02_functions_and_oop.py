def describe_person(name, *skills, **goals):
    print(f"{name} has {len(skills)} Skills:")

    for skill in skills:
        print(f"- {skill}")

    print(f"{name}'s information:")
    for key, value in goals.items():
        print(f"- {key}: {value}")

def create_profile(username, *skills, **information):
    print(" ")
    print(f"Username: {username}")
    print(" ")
    print("Skills:")

    for skill in skills:
        print(f"- {skill}")
    print(" ")

    print("Additional information:")
    for key, value in information.items():
        print(f"- {key}: {value}")
    


describe_person(
    "Andrei", 
    "Python", "FastAPI", "Git", "AI",
    age = 22,
    target_role = "AI Engineer",
    language = "Python"
)

create_profile(
    "drei",
    "Python",
    "FastAPI",
    "Git",
    experience=1,
    goal="AI Engineer"
)


class AIEngineer:
    profession = "AI Engineer"

    def __init__(self, name, *skills):
        self.name = name
        self.skills = skills

    def introduce(self):
        print(" ")
        print(f"Hi, I'm {self.name}.")
        print(f"I'm an {self.profession}")
        print(f"My skills are: {', '.join(self.skills)}")

drei = AIEngineer(
    "Andrei",
    "Python", "FastAPI", "Git", "AI"
)

jun = AIEngineer(
    "Jun",
    "Python", "TensorFlow", "PyTorch"
)

drei.introduce()
jun.introduce()