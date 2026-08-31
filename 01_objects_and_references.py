# Shared reference
a = [1,2,3,4,5]
b = a
print(a)
print(b)

#Mutation
a.append(6)
print(a)

#Reassignment
a = a + [7]
print(a)

#Shallow copy
b = a.copy()
b.append(8)
print(b)

# Shallow copy with nested object
user = {
    "name": "Andrei",
    "skills": ["Python", "AI"]
}

user_copy = user.copy()

user_copy["skills"].append("FastAPI")

print(user)
print(user_copy)

#Breaking the shared nested reference
b = a.copy()
b = b + [9]
print(b)

# Deep copy
import copy

user_deep_copy = copy.deepcopy(user)

user_deep_copy["skills"].append("Docker")

print(user)
print(user_deep_copy)
