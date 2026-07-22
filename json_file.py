import json
data = {
    "student": {
        "name": "BORZ",
        "age": 18
    },
    "skills": [
        "Python",
        "AI",
        "Automation"
    ]
}
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)
with open("student.json", "r") as file:
    data = json.load(file)
print(data)
print(data["student"]["name"])
print(data["skills"][1])